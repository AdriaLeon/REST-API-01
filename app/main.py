from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app.models import Base


app = FastAPI(
    title="Task API",
    version="0.1.0",
)

app.include_router(router)
Base.metadata.create_all(bind=engine)