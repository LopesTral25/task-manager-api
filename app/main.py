from fastapi import FastAPI

from app.database import create_table
from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

create_table()

@app.get("/")
def home():
    return {"message": "Bem-vindo à Task Manager API!"}


app.include_router(tasks_router)