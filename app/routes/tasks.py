from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.database import get_connection

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=300)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=300)
    completed: bool = False

@router.post("/")
def create_task(task: TaskCreate):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (task.title, task.description)
    )

    connection.commit()
    task_id = cursor.lastrowid
    connection.close()

    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }


@router.get("/")
def list_tasks():
    connection = get_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()

    connection.close()

    return [dict(task) for task in tasks]


@router.get("/{task_id}")
def get_task(task_id: int):
    connection = get_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return dict(task)


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
        """,
        (task.title, task.description, task.completed, task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    updated_task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return dict(updated_task)


@router.delete("/{task_id}")
def delete_task(task_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return {"message": "Tarefa excluída com sucesso!"}