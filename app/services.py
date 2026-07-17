from sqlalchemy.orm import Session

from app import repositories
from app.models import TaskModel
from app.schemas import TaskCreate, TaskUpdate
from fastapi import HTTPException
from app import repositories

next_id = 1

# Translates the task schema into a task model and saves it to the database
def create_task(db: Session, task: TaskCreate):

    new_task = TaskModel(
        title=task.title,
        description=task.description,
        completed=False,
    )

    return repositories.create(db, new_task)

def get_all_tasks(db: Session):
    return repositories.get_all(db)

def get_task_by_id(db: Session, task_id: int):

    task = repositories.get_by_id(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task

def update_task(db: Session, task_id: int, updated: TaskUpdate,):

    task = repositories.get_by_id(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    task.title = updated.title
    task.description = updated.description
    task.completed = updated.completed

    return repositories.update(db, task)

def delete_task(db: Session, task_id: int,):

    task = repositories.get_by_id(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    repositories.delete(db, task)