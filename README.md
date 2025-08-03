## Network Security ML Project
### About The Project
This is a comprehensive machine learning project designed to detect network security threats. The project is built as a complete MLOps pipeline, encompassing data ingestion from a MongoDB database, data validation, data transformation, model training, and a FastAPI-based web application for making real-time predictions. The system is designed to be scalable and modular, allowing for easy integration and maintenance of different components of the ML pipeline.

## Key Features
Data Ingestion: Reads data from a MongoDB database.

## ML Pipeline: 
A structured pipeline that includes data ingestion, validation, and transformation.

## Model Training: 
Trains a machine learning model on the processed data and stores it for later use.

## Prediction Service: 
A FastAPI application with a /predict endpoint that accepts a CSV file, processes it, makes predictions using the trained model, and returns the results in an HTML table.

## Dependencies: 
All dependencies are managed via requirements.txt.

## Configuration: 
Uses schema.yaml to define the data schema for validation.

## Technologies
The project leverages the following technologies and libraries:

Backend Framework: FastAPI, Uvicorn

Machine Learning: Scikit-learn

Data Handling: Pandas, NumPy

Database: MongoDB

Configuration: PyYAML

Logging: Python's built-in logging module

MLOps: DVC, MLflow (as implied by requirements)

Other: python-dotenv, certifi, dill (for object serialization)

## Getting Started
Prerequisites
To set up and run this project, you will need:

Python 3.10 or higher

A MongoDB instance (local or remote)

A .env file with your MongoDB connection URL, e.g., MONGODB_URL_KEY="mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority"

## Installation
Clone the repository:

git clone https://github.com/himanshub0810/networksecurity.git
cd networksecurity

## Install the dependencies:

pip install -r requirements.txt

## Project Structure
app.py: The FastAPI application that handles prediction requests and model training.

main.py: The entry point for the training pipeline.

networksecurity/:

components/: Contains the modular components of the ML pipeline (data ingestion, data validation, data transformation, model training).

constant/: Defines constants used throughout the project.

entity/: Contains data classes for configuration and artifacts.

exception/: Custom exception handling.

logging/: Logging configuration.

pipeline/: Manages the overall training pipeline flow.

utils/: Utility functions, including for loading/saving objects.

data_schema/schema.yaml: Defines the schema for data validation.

final_model/: Directory to store the trained model and preprocessor.

requirements.txt: Lists all project dependencies.

templates/table.html: HTML template for displaying prediction results.

test_mongodb.py: A utility script for testing the MongoDB connection.

## Usage
Training the Model
To initiate the full machine learning training pipeline, run the main.py script. This will perform all pipeline steps from data ingestion to model training.

python main.py

## Running the Web Server
To start the FastAPI web server, run the app.py file. The server will be accessible at http://localhost:8000.


uvicorn app:app --host 0.0.0.0 --port 8000 --reload  

## Making Predictions
Once the server is running, you can submit a CSV file to the /predict endpoint to get predictions. The application will process the data using the preprocessor and model, and return an HTML page with the results.

You can use a tool like curl or Postman to send a file to the endpoint.





## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
3. Access the API at `http://localhost:8000` and API docs at `http://localhost:8000/docs`

## Deploying to Render
1. Create a new Web Service on Render
2. Connect your GitHub repository containing this code
3. Configure the service:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port 8000 --reload  `
4. Deploy the service

## API Endpoints
- GET `/todos`: List all todos
- POST `/todos`: Create a new todo
- PUT `/todos/{id}`: Update a todo
- DELETE `/todos/{id}`: Delete a todo

## Testing the API
Use the interactive API documentation at `/docs` or tools like curl/Postman:
```bash
curl -X POST "http://your-render-url/todos" -H "Content-Type: application/json" -d '{"title":"Sample Todo","completed":false}'
```