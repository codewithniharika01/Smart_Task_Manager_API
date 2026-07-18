from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Task

from app.routers import user as user_router
from app.routers import task as task_router
from app.routers import auth as auth_router
app = FastAPI()



Base.metadata.create_all(bind = engine)

app.include_router(user_router.router)
app.include_router(task_router.router)
app.include_router(auth_router.router)

@app.get("/")
def home():
    return{"message": "Smart Task Manager API Running"}

