from fastapi import FastAPI, HTTPException
from typing import List

from schemas import Task, TaskCreate, TaskUpdate
from database import task_db

app = FastAPI(title="To-Do List App")


@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    return task_db.add(task)


@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return task_db.get_all()


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = task_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate):
    updated = task_db.update(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = task_db.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
