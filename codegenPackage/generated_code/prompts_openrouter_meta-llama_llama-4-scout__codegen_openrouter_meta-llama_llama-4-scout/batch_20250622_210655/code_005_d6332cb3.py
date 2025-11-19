"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Create a RESTful API to manage construction project documentation, including client information, project plans, and progress reports, for a company like ILMAM Construction."
Generated: DETERMINISTIC_d6332cb3031d5ce4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**construction_api.py**
```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from jose import jwt, JWTError

# Database Connection
SQLALCHEMY_DATABASE_URL = "sqlite:///construction.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class ProjectPlan(BaseModel):
    id: int
    project_id: int
    plan_name: str
    plan_description: str

class ProgressReport(BaseModel):
    id: int
    project_id: int
    report_date: datetime
    report_description: str

# SQLAlchemy Models
class ClientORM(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class ProjectORM(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("ClientORM", backref="projects")

class ProjectPlanORM(Base):
    __tablename__ = "project_plans"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    plan_name = Column(String)
    plan_description = Column(String)

class ProgressReportORM(Base):
    __tablename__ = "progress_reports"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    report_date = Column(DateTime)
    report_description = Column(String)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

# Authentication
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = jwt.encode({"sub": user}, "secret_key", algorithm="HS256")
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(username: str, password: str):
    # Replace with actual authentication logic
    return username

# Clients
@app.get("/clients/")
async def read_clients(db: SessionLocal = Depends(get_db)):
    return db.query(ClientORM).all()

@app.post("/clients/")
async def create_client(client: Client, db: SessionLocal = Depends(get_db)):
    db_client = ClientORM(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Projects
@app.get("/projects/")
async def read_projects(db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    return db.query(ProjectORM).all()

@app.post("/projects/")
async def create_project(project: ProjectPlan, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_project = ProjectORM(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Project Plans
@app.get("/project_plans/")
async def read_project_plans(db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    return db.query(ProjectPlanORM).all()

@app.post("/project_plans/")
async def create_project_plan(project_plan: ProjectPlan, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_project_plan = ProjectPlanORM(**project_plan.dict())
    db.add(db_project_plan)
    db.commit()
    db.refresh(db_project_plan)
    return db_project_plan

# Progress Reports
@app.get("/progress_reports/")
async def read_progress_reports(db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    return db.query(ProgressReportORM).all()

@app.post("/progress_reports/")
async def create_progress_report(progress_report: ProgressReport, db: SessionLocal = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_progress_report = ProgressReportORM(**progress_report.dict())
    db.add(db_progress_report)
    db.commit()
    db.refresh(db_progress_report)
    return db_progress_report
```

**main.py**
```python
import uvicorn
from construction_api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
python-jose
```
