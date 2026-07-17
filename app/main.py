from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.routes import router
from app.database import engine
from app.models import Base

app = FastAPI(
    title="Task API",
    version="0.1.0",
)

app.include_router(router)

@app.on_event("startup")
def startup():
    for _ in range(10): # Tries during 20 seconds in case it is called before the service of the database is up and running
        try:
            Base.metadata.create_all(bind=engine) # Creates all the tables that are childs of Base (in this case, TaskModel)
            print("Database connected.")
            break
        except OperationalError:
            print("Waiting for database...")
            time.sleep(2)