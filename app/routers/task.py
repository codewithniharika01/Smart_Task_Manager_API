from fastapi import  APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import crud
from app.schemas.task import TaskCreate, TaskResponse
from fastapi import HTTPException
from app.dependencies import get_current_user

router = APIRouter(
prefix = "/tasks",
tags=["Tasks"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.post("/", response_model = TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
    ):

      return crud.create_task(db, task)

@router.get("/", response_model=list[TaskResponse])
def read_tasks(
    db: Session = Depends(get_db)
):
    return crud.get_tasks(db)


@router.put("/{task_id}",response_model=TaskResponse)
def update_task(
    task_id:int,
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    
    updated_task = crud.update_task(db, task_id, task)

    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )
    
    return updated_task

@router.delete("/{task_id}")
def delete_task(
    task_id:int,
    db: Session = Depends(get_db)
):
    
    deleted_task = crud.deleted_task(db, task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )
    
    return {
        "Message": "Task deleted successfully"
    }
