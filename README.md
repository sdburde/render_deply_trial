# Simple FastAPI Todo App

A basic FastAPI application with CRUD operations for a todo list, designed for deployment on Render.

## Project Structure
- `main.py`: FastAPI application with todo list endpoints
- `requirements.txt`: Project dependencies

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
3. Access the API at `http://localhost:8000` and API docs at `http://localhost:8000/docs`

## Deploying to Render
1. Create a new Web Service on Render
2. Connect your GitHub repository containing this code
3. Configure the service:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Set environment variables:
   - `PORT`: 8000 (or any port assigned by Render)
5. Deploy the service

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