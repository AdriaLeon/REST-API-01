from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import TaskModel

def create(db: Session, task: TaskModel):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all(db: Session):
    return db.scalars(select(TaskModel)).all()

def get_by_id(db: Session, task_id: int):
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    return db.scalar(stmt)

def update(db: Session, task: TaskModel):
    db.commit()
    db.refresh(task)
    return task

def delete(db: Session, task: TaskModel):
    db.delete(task)
    db.commit()