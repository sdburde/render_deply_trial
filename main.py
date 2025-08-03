from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Simple Todo API")

# In-memory storage for todos
todos = []
todo_id_counter = 1

# Pydantic model for Todo item
class Todo(BaseModel):
    id: int | None = None
    title: str
    completed: bool = False


# Redirect root to /docs
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Endpoints
@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    global todo_id_counter
    new_todo = Todo(id=todo_id_counter, title=todo.title, completed=todo.completed)
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.completed = updated_todo.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)