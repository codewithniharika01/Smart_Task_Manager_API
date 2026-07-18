from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import SessionLocal
from app.schemas import user as user_schema

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(
    user: user_schema.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db=db, user_data=user)

@router.get("/")
def get_all_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db=db)