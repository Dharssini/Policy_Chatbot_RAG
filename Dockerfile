# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install virtualenv to create isolated environments
RUN pip install virtualenv

# Create and activate a virtual environment inside the container
RUN python3 -m venv /venv

# Ensure the virtual environment is activated
ENV PATH="/venv/bin:$PATH"

# Install the required Python packages inside the virtual environment
RUN pip install -r requirements.txt

# Define the command to run the application
CMD ["python3", "app.py"]
