"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Create a REST API design for an NGO like Child Nepal to manage their projects, beneficiaries, and partnerships. Include endpoints for tracking project milestones and reporting impact metrics.
Generated: DETERMINISTIC_74e76391c761d58f
Batch ID: 20250612_153517
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
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from typing import Optional

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///ngo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Project(BaseModel):
    id: Optional[int]
    name: str
    description: str
    start_date: datetime
    end_date: Optional[datetime]

class Beneficiary(BaseModel):
    id: Optional[int]
    name: str
    age: int
    project_id: int

class Partnership(BaseModel):
    id: Optional[int]
    name: str
    description: str

class Milestone(BaseModel):
    id: Optional[int]
    project_id: int
    description: str
    achieved_date: datetime

class ImpactMetric(BaseModel):
    id: Optional[int]
    project_id: int
    metric_name: str
    value: float
    date: datetime

# SQLAlchemy Models
class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

class BeneficiaryDB(Base):
    __tablename__ = "beneficiaries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    project_id = Column(Integer)

class PartnershipDB(Base):
    __tablename__ = "partnerships"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class MilestoneDB(Base):
    __tablename__ = "milestones"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    description = Column(String)
    achieved_date = Column(DateTime)

class ImpactMetricDB(Base):
    __tablename__ = "impact_metrics"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    metric_name = Column(String)
    value = Column(Float)
    date = Column(DateTime)

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

# Endpoints
@app.post("/projects/")
async def create_project(project: Project, db: SessionLocal = Depends(get_db)):
    db_project = ProjectDB(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects/")
async def read_projects(db: SessionLocal = Depends(get_db)):
    return db.query(ProjectDB).all()

@app.get("/projects/{project_id}")
async def read_project(project_id: int, db: SessionLocal = Depends(get_db)):
    project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/beneficiaries/")
async def create_beneficiary(beneficiary: Beneficiary, db: SessionLocal = Depends(get_db)):
    db_beneficiary = BeneficiaryDB(**beneficiary.dict())
    db.add(db_beneficiary)
    db.commit()
    db.refresh(db_beneficiary)
    return db_beneficiary

@app.get("/beneficiaries/")
async def read_beneficiaries(db: SessionLocal = Depends(get_db)):
    return db.query(BeneficiaryDB).all()

@app.post("/partnerships/")
async def create_partnership(partnership: Partnership, db: SessionLocal = Depends(get_db)):
    db_partnership = PartnershipDB(**partnership.dict())
    db.add(db_partnership)
    db.commit()
    db.refresh(db_partnership)
    return db_partnership

@app.get("/partnerships/")
async def read_partnerships(db: SessionLocal = Depends(get_db)):
    return db.query(PartnershipDB).all()

@app.post("/projects/{project_id}/milestones/")
async def create_milestone(milestone: Milestone, project_id: int, db: SessionLocal = Depends(get_db)):
    project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_milestone = MilestoneDB(**milestone.dict())
    db.add(db_milestone)
    db.commit()
    db.refresh(db_milestone)
    return db_milestone

@app.get("/projects/{project_id}/milestones/")
async def read_milestones(project_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(MilestoneDB).filter(MilestoneDB.project_id == project_id).all()

@app.post("/projects/{project_id}/impact-metrics/")
async def create_impact_metric(impact_metric: ImpactMetric, project_id: int, db: SessionLocal = Depends(get_db)):
    project = db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db_impact_metric = ImpactMetricDB(**impact_metric.dict())
    db.add(db_impact_metric)
    db.commit()
    db.refresh(db_impact_metric)
    return db_impact_metric

@app.get("/projects/{project_id}/impact-metrics/")
async def read_impact_metrics(project_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(ImpactMetricDB).filter(ImpactMetricDB.project_id == project_id).all()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "token", "token_type": "bearer"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
