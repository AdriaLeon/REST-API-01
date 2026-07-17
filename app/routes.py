from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskCreate, TaskUpdate
from app import services

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to Task API"}

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db),): # Depends ensures we have and actual session before processing the request
    return services.create_task(db, task)

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db),):
    return services.get_all_tasks(db)

@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return services.get_task_by_id(db, task_id)

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db),):
    services.delete_task(db, task_id)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskUpdate, db: Session = Depends(get_db)):
    return services.update_task(db, task_id, updated)