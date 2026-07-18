from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import user as user_schema
from app.models.task import Task
from app.schemas import task as task_schema
from app.auth import hash_password
from app.auth import verify_password

def create_user(db: Session, user_data: user_schema.UserCreate):

    hashed_password = hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_users(db: Session):
    return db.query(User).all()

def create_task(db: Session, task_data: task_schema.TaskCreate):

    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        owner_id=task_data.owner_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db: Session):

    return db.query(Task).all()

def update_task(db:Session, 
                task_id:int,
                task_data: task_schema.TaskCreate
                ):

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        task.title = task_data.title
        task.description = task_data.description
        task.owner_id = task_data.owner_id

        db.commit()
        db.refresh(task)
        
    return task


def delete_task(db: Session, task_id: int):

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return task  

def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None
    
    return user