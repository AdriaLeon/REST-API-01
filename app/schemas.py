from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    # This model is for incoming data (when a user CREATES a task)
    title: str
    description: str | None = None

class Task(TaskCreate):
    # This model is for outgoing data (when the system SAVES or RETURNS a task)
    id: int
    completed: bool
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title: str # Adding | None = None allows partial updates
    description: str | None = None
    completed: bool