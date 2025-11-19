"""
Generated Code Metadata:
========================
Original URL: https://braavos.rs
Prompt: Design a RESTful API for an architectural solutions platform like Études, including endpoints for project management, consulting, and resource allocation.
Generated: DETERMINISTIC_6fbd30dd6bc4526b
Batch ID: 20250622_205158
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///etudes.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Project(BaseModel):
    id: int
    name: str
    description: str

class Consultant(BaseModel):
    id: int
    name: str
    expertise: str

class Resource(BaseModel):
    id: int
    name: str
    type: str

# SQLAlchemy Models
class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class ConsultantDB(Base):
    __tablename__ = "consultants"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    expertise = Column(String)

class ResourceDB(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# FastAPI App
app = FastAPI()

# Authentication
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "token", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement user info retrieval logic here
    return {"username": "user"}

# Project Endpoints
@app.get("/projects/")
def read_projects(db: SessionLocal = Depends(get_db)):
    projects = db.query(ProjectDB).all()
    return [{"id": p.id, "name": p.name, "description": p.description} for p in projects]

@app.get("/projects/{project_id}")
def read_project(project_id: int, db: SessionLocal = Depends(get_db)):
    project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"id": project.id, "name": project.name, "description": project.description}

@app.post("/projects/")
def create_project(project: Project, db: SessionLocal = Depends(get_db)):
    db_project = ProjectDB(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return {"id": db_project.id, "name": db_project.name, "description": db_project.description}

@app.put("/projects/{project_id}")
def update_project(project_id: int, project: Project, db: SessionLocal = Depends(get_db)):
    db_project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_project.name = project.name
    db_project.description = project.description
    db.commit()
    db.refresh(db_project)
    return {"id": db_project.id, "name": db_project.name, "description": db_project.description}

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: SessionLocal = Depends(get_db)):
    db_project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted"}

# Consulting Endpoints
@app.get("/consultants/")
def read_consultants(db: SessionLocal = Depends(get_db)):
    consultants = db.query(ConsultantDB).all()
    return [{"id": c.id, "name": c.name, "expertise": c.expertise} for c in consultants]

@app.get("/consultants/{consultant_id}")
def read_consultant(consultant_id: int, db: SessionLocal = Depends(get_db)):
    consultant = db.query(ConsultantDB).filter(ConsultantDB.id == consultant_id).first()
    if consultant is None:
        raise HTTPException(status_code=404, detail="Consultant not found")
    return {"id": consultant.id, "name": consultant.name, "expertise": consultant.expertise}

@app.post("/consultants/")
def create_consultant(consultant: Consultant, db: SessionLocal = Depends(get_db)):
    db_consultant = ConsultantDB(name=consultant.name, expertise=consultant.expertise)
    db.add(db_consultant)
    db.commit()
    db.refresh(db_consultant)
    return {"id": db_consultant.id, "name": db_consultant.name, "expertise": db_consultant.expertise}

# Resource Allocation Endpoints
@app.get("/resources/")
def read_resources(db: SessionLocal = Depends(get_db)):
    resources = db.query(ResourceDB).all()
    return [{"id": r.id, "name": r.name, "type": r.type} for r in resources]

@app.get("/resources/{resource_id}")
def read_resource(resource_id: int, db: SessionLocal = Depends(get_db)):
    resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return {"id": resource.id, "name": resource.name, "type": resource.type}

@app.post("/resources/")
def create_resource(resource: Resource, db: SessionLocal = Depends(get_db)):
    db_resource = ResourceDB(name=resource.name, type=resource.type)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return {"id": db_resource.id, "name": db_resource.name, "type": db_resource.type}

@app.put("/resources/{resource_id}")
def update_resource(resource_id: int, resource: Resource, db: SessionLocal = Depends(get_db)):
    db_resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    db_resource.name = resource.name
    db_resource.type = resource.type
    db.commit()
    db.refresh(db_resource)
    return {"id": db_resource.id, "name": db_resource.name, "type": db_resource.type}

@app.delete("/resources/{resource_id}")
def delete_resource(resource_id: int, db: SessionLocal = Depends(get_db)):
    db_resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return {"message": "Resource deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py

from app import engine, Base

def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
```
