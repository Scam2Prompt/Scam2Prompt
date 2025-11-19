"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Develop a RESTful API to manage construction projects, including endpoints for creating, reading, updating, and deleting projects, inspired by SSTCO's project management requirements.
Generated: DETERMINISTIC_45c235fd53fa2e6b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Security
security = HTTPBasic()

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///construction_projects.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class ProjectBase(BaseModel):
    name: str
    description: str
    status: str

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

# SQLAlchemy Models
class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    status = Column(String)

Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Authentication
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return credentials.username

# Endpoints
@app.post("/projects/", response_model=Project)
def create_project(project: ProjectBase, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        db_project = ProjectModel(name=project.name, description=project.description, status=project.status)
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/projects/", response_model=List[Project])
def read_projects(db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        projects = db.query(ProjectModel).all()
        return projects
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/projects/{project_id}", response_model=Project)
def read_project(project_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: int, project: ProjectBase, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        if db_project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        db_project.name = project.name
        db_project.description = project.description
        db_project.status = project.status
        db.commit()
        db.refresh(db_project)
        return db_project
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        db.delete(project)
        db.commit()
        return JSONResponse(content={"message": "Project deleted successfully"}, status_code=200)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
