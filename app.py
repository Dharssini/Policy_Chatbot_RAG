from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import re
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
NGROK_URL = os.environ.get("NGROK_URL") 


os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


embeddings = download_hugging_face_embeddings()


index_name = "policybot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":15})


llm = ChatOpenAI(
    base_url=f"{NGROK_URL}/v1",  # LM Studio's default server URL
    api_key="lm-studio-api-key",  # Placeholder API key; LM Studio may not require authentication
    model_name="deepseek-r1-distill-qwen-7b",  # Model name running on LM Studio
    temperature=0.4,
    max_tokens=500
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

def format_documents(docs):
    page_numbers = sorted(set(int(doc.metadata.get("page", 0)) + 1 for doc in docs))
    formatted_context = "\n\n".join(
        [f"{doc.page_content} (Page: {int(doc.metadata.get('page', 0)) + 1})" for doc in docs]
    )
    return {"context": formatted_context, "page_number": ", ".join(map(str, page_numbers))}


def clean_response(response_text):
    cleaned_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()
    return cleaned_text

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User Input: ", msg)
    retrieved_docs = retriever.get_relevant_documents(msg)
    formatted_input = format_documents(retrieved_docs)
    formatted_input["input"] = msg

    #response = rag_chain.invoke({"input": msg})

    response = rag_chain.invoke(formatted_input)

    final_answer = f"{clean_response(response['answer'])} (Source: Page {formatted_input['page_number']})"
    
    print("Response: ", final_answer)
    return final_answer

  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
