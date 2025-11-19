"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
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
from datetime import datetime

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///construction_management.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Project(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime

class Equipment(BaseModel):
    id: int
    name: str
    type: str
    maintenance_due: datetime

class Maintenance(BaseModel):
    id: int
    equipment_id: int
    date: datetime
    description: str

# SQLAlchemy Models
class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(datetime)
    end_date = Column(datetime)

class EquipmentDB(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    maintenance_due = Column(datetime)

class MaintenanceDB(Base):
    __tablename__ = "maintenance"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    date = Column(datetime)
    description = Column(String)

Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return token

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/projects/")
async def read_projects(db: SessionLocal = Depends(get_db)):
    projects = db.query(ProjectDB).all()
    return [{"id": p.id, "name": p.name, "description": p.description, "start_date": p.start_date, "end_date": p.end_date} for p in projects]

@app.post("/projects/")
async def create_project(project: Project, db: SessionLocal = Depends(get_db)):
    db_project = ProjectDB(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return {"id": db_project.id, "name": db_project.name, "description": db_project.description, "start_date": db_project.start_date, "end_date": db_project.end_date}

@app.get("/equipment/")
async def read_equipment(db: SessionLocal = Depends(get_db)):
    equipment = db.query(EquipmentDB).all()
    return [{"id": e.id, "name": e.name, "type": e.type, "maintenance_due": e.maintenance_due} for e in equipment]

@app.post("/equipment/")
async def create_equipment(equipment: Equipment, db: SessionLocal = Depends(get_db)):
    db_equipment = EquipmentDB(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return {"id": db_equipment.id, "name": db_equipment.name, "type": db_equipment.type, "maintenance_due": db_equipment.maintenance_due}

@app.get("/maintenance/")
async def read_maintenance(db: SessionLocal = Depends(get_db)):
    maintenance = db.query(MaintenanceDB).all()
    return [{"id": m.id, "equipment_id": m.equipment_id, "date": m.date, "description": m.description} for m in maintenance]

@app.post("/maintenance/")
async def create_maintenance(maintenance: Maintenance, db: SessionLocal = Depends(get_db)):
    db_maintenance = MaintenanceDB(**maintenance.dict())
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return {"id": db_maintenance.id, "equipment_id": db_maintenance.equipment_id, "date": db_maintenance.date, "description": db_maintenance.description}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return {"error": "Internal Server Error"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
