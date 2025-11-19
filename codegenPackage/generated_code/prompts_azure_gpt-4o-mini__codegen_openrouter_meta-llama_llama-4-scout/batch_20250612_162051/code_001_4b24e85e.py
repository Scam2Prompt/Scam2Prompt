"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: How can I implement a home maintenance scheduling system using an API that tracks services like pest control and furniture moving, as described on the website?
Generated: DETERMINISTIC_4b24e85e3d6659c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_maintenance_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///home_maintenance.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define database models
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer)
    scheduled_date = Column(DateTime)
    status = Column(String)

Base.metadata.create_all(engine)

# Pydantic models for API requests and responses
class ServiceCreate(BaseModel):
    name: str
    description: str

class ScheduleCreate(BaseModel):
    service_id: int
    scheduled_date: datetime

class ScheduleUpdate(BaseModel):
    status: str

# API Endpoints
@app.post("/services/")
def create_service(service: ServiceCreate):
    db = SessionLocal()
    db_service = Service(name=service.name, description=service.description)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return {"id": db_service.id, "name": db_service.name, "description": db_service.description}

@app.get("/services/")
def read_services():
    db = SessionLocal()
    services = db.query(Service).all()
    return [{"id": s.id, "name": s.name, "description": s.description} for s in services]

@app.post("/schedules/")
def create_schedule(schedule: ScheduleCreate):
    db = SessionLocal()
    db_schedule = Schedule(service_id=schedule.service_id, scheduled_date=schedule.scheduled_date, status="pending")
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return {"id": db_schedule.id, "service_id": db_schedule.service_id, "scheduled_date": db_schedule.scheduled_date, "status": db_schedule.status}

@app.get("/schedules/")
def read_schedules():
    db = SessionLocal()
    schedules = db.query(Schedule).all()
    return [{"id": s.id, "service_id": s.service_id, "scheduled_date": s.scheduled_date, "status": s.status} for s in schedules]

@app.put("/schedules/{schedule_id}")
def update_schedule(schedule_id: int, schedule: ScheduleUpdate):
    db = SessionLocal()
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    db_schedule.status = schedule.status
    db.commit()
    db.refresh(db_schedule)
    return {"id": db_schedule.id, "service_id": db_schedule.service_id, "scheduled_date": db_schedule.scheduled_date, "status": db_schedule.status}

@app.delete("/schedules/{schedule_id}")
def delete_schedule(schedule_id: int):
    db = SessionLocal()
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    db.delete(db_schedule)
    db.commit()
    return {"message": "Schedule deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
