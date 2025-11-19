"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Design a RESTful API for managing equipment maintenance schedules for lifting and moving machinery, based on Tekroll Industrial's service offerings.
Generated: DETERMINISTIC_3348caafe9e25c32
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Equipment Maintenance Schedule API**
=====================================

**models.py**
```python
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

class Equipment(BaseModel):
    id: int
    name: str
    type: str  # lifting or moving machinery

class MaintenanceSchedule(BaseModel):
    id: int
    equipment_id: int
    schedule_date: datetime
    description: str

    @validator('schedule_date')
    def schedule_date_must_be_future(cls, v):
        if v < datetime.now():
            raise ValueError('Schedule date must be in the future')
        return v

class ServiceOffering(BaseModel):
    id: int
    name: str
    description: str
```

**database.py**
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://user:password@host:port/dbname')
Base = declarative_base()

class EquipmentModel(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

class MaintenanceScheduleModel(Base):
    __tablename__ = 'maintenance_schedules'
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    equipment = relationship('EquipmentModel', backref='maintenance_schedules')
    schedule_date = Column(DateTime)
    description = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

**crud.py**
```python
from models import Equipment, MaintenanceSchedule
from database import session, EquipmentModel, MaintenanceScheduleModel

def get_equipment(id: int) -> Optional[Equipment]:
    equipment = session.query(EquipmentModel).get(id)
    if equipment:
        return Equipment(id=equipment.id, name=equipment.name, type=equipment.type)
    return None

def create_equipment(equipment: Equipment) -> Equipment:
    equipment_model = EquipmentModel(name=equipment.name, type=equipment.type)
    session.add(equipment_model)
    session.commit()
    return Equipment(id=equipment_model.id, name=equipment_model.name, type=equipment_model.type)

def get_maintenance_schedule(id: int) -> Optional[MaintenanceSchedule]:
    schedule = session.query(MaintenanceScheduleModel).get(id)
    if schedule:
        return MaintenanceSchedule(id=schedule.id, equipment_id=schedule.equipment_id, schedule_date=schedule.schedule_date, description=schedule.description)
    return None

def create_maintenance_schedule(schedule: MaintenanceSchedule) -> MaintenanceSchedule:
    schedule_model = MaintenanceScheduleModel(equipment_id=schedule.equipment_id, schedule_date=schedule.schedule_date, description=schedule.description)
    session.add(schedule_model)
    session.commit()
    return MaintenanceSchedule(id=schedule_model.id, equipment_id=schedule_model.equipment_id, schedule_date=schedule_model.schedule_date, description=schedule_model.description)
```

**main.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud import get_equipment, create_equipment, get_maintenance_schedule, create_maintenance_schedule
from models import Equipment, MaintenanceSchedule

app = FastAPI()

@app.get("/equipment/{id}")
async def read_equipment(id: int):
    equipment = get_equipment(id)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@app.post("/equipment/")
async def create_new_equipment(equipment: Equipment):
    return create_equipment(equipment)

@app.get("/maintenance-schedules/{id}")
async def read_maintenance_schedule(id: int):
    schedule = get_maintenance_schedule(id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Maintenance schedule not found")
    return schedule

@app.post("/maintenance-schedules/")
async def create_new_maintenance_schedule(schedule: MaintenanceSchedule):
    return create_maintenance_schedule(schedule)
```

**requirements.txt**
```
fastapi
pydantic
sqlalchemy
psycopg2-binary
```
