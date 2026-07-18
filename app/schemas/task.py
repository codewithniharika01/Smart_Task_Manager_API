from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    owner_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

    class Config:
        from_attributes = True