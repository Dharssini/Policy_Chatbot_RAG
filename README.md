# Chatbot for Policy Document using RAG
<img src="https://raw.githubusercontent.com/Dharssini/Policy_Chatbot_RAG/main/demoproj.gif" width="800">
## Overview
This project involves creating a chatbot for querying policy documents using Retrieval-Augmented Generation (RAG). The system utilizes Flask as the backend framework and LM Studio, which runs the DeepSeek model for inference. The language model is exposed via an ngrok tunnel, and the Flask application is deployed on Render. Additionally, Docker is used for containerization, and MLOps is integrated to streamline model deployment, monitoring, and maintenance. The Flask API interacts with the locally running LLM endpoint for answering user queries.

## Components

### 1. LM Studio and DeepSeek Model
- LM Studio is used to host the DeepSeek language model locally.
- The model serves responses based on retrieved policy document data.
- The endpoint is exposed to the internet via ngrok.

### 2. Flask Application
- A Flask server is developed to process user queries.
- It retrieves relevant policy documents and sends them to the LLM for context-aware responses.
- Hosted on Render for deployment and accessibility.

### 3. Ngrok for Secure Tunneling
- Ngrok is used to expose the LM Studio model running locally to the internet.
- This allows the Flask application deployed on Render to communicate with the local LLM endpoint.

### 4. Docker for Containerization
- Docker is used to containerize the Flask application, ensuring consistent deployment across different environments.
- Provides an easy way to package dependencies and scale the application.

### 5. MLOps for Model Deployment and Monitoring
- MLOps is integrated to manage the lifecycle of the DeepSeek model.
- Enables version control, automated deployments, monitoring, and performance tracking.
- Ensures continuous improvements and updates to the chatbot.

## Workflow
1. The user sends a query to the Flask application deployed on Render.
2. The Flask app retrieves relevant policy documents using a RAG-based retrieval mechanism.
3. The extracted content is forwarded to the DeepSeek model via the ngrok-exposed endpoint.
4. The LLM generates a response based on the retrieved context.
5. The response is sent back to the user.
6. Docker ensures seamless deployment, while MLOps monitors the performance and updates the model as needed.

## Technologies Used
- **LM Studio** (for running the DeepSeek LLM locally)
- **Flask** (as the backend API server)
- **Ngrok** (to expose the local model to the internet)
- **Render** (for Flask app deployment)
- **Docker** (for containerization)
- **MLOps** (for model lifecycle management)
- **RAG** (Retrieval-Augmented Generation for policy document processing)

## Flowchart
![Flowchart](https://raw.githubusercontent.com/Dharssini/Policy_Chatbot_RAG/main/flowchart.png)

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask
- Docker
- Ngrok
- LM Studio with DeepSeek Model

### Steps to Run Locally
```bash
# Clone the repository
git clone https://github.com/yourusername/rag-chatbot.git
cd rag-chatbot

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the LM Studio DeepSeek Model locally
# Start LM Studio and load the DeepSeek model.
# Ensure it runs on a local endpoint (e.g., `http://localhost:5001`).

# Expose the model using Ngrok
ngrok http 5001

# Copy the public URL from ngrok and update the Flask application to use this endpoint.

# Run the Flask application
python app.py

# Deploy using Docker (optional)
docker build -t rag-chatbot .
docker run -p 5000:5000 rag-chatbot
```

## Deployment

### Deploy on Render
- Upload the Flask application to a GitHub repository.
- Connect the repository to Render and set up an automatic deployment.
- Ensure the environment variables match your local setup.

## Contributing
Feel free to open an issue or submit a pull request if you would like to contribute.

## License
This project is licensed under the MIT License.

