# Smart Task Manager API

A backend Task Management API built using FastAPI and SQLAlchemy.

## Features

- User Management
- Task Management
- CRUD Operations
- API Documentation with Swagger

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Git & GitHub

## Project Structure

```text
app/
│
├── models/
│   ├── user.py
│   └── task.py
│
├── routers/
│   ├── user.py
│   ├── task.py
│   └── auth.py
│
├── schemas/
│   ├── user.py
│   ├── task.py
│   └── auth.py
│
├── auth.py
├── crud.py
├── database.py
├── dependencies.py
└── main.py

requirements.txt
README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/codewithniharika01/Smart_Task_Manager_API.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## Database

Currently using SQLite database with SQLAlchemy ORM.

## Author

Niharika