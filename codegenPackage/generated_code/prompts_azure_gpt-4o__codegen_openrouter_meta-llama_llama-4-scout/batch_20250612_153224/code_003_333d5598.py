"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Generate code for a web application that tracks humanitarian interventions and medical aid distribution, aligning with Jusoor International's programs.
Generated: DETERMINISTIC_333d55984762f9a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Humanitarian Intervention and Medical Aid Distribution Tracker**
===========================================================

**models.py**
```python
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Intervention(Base):
    __tablename__ = "interventions"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    location = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    aid_distributions = relationship("AidDistribution", backref="intervention")

class AidDistribution(Base):
    __tablename__ = "aid_distributions"

    id = Column(Integer, primary_key=True)
    intervention_id = Column(Integer, ForeignKey("interventions.id"), nullable=False)
    aid_type = Column(String(50), nullable=False)
    quantity = Column(Float, nullable=False)
    distribution_date = Column(DateTime, nullable=False)

class MedicalAid(AidDistribution):
    __tablename__ = "medical_aids"

    id = Column(Integer, ForeignKey("aid_distributions.id"), primary_key=True)
    medical_aid_type = Column(String(50), nullable=False)
    patient_count = Column(Integer, nullable=False)

class NonMedicalAid(AidDistribution):
    __tablename__ = "non_medical_aids"

    id = Column(Integer, ForeignKey("aid_distributions.id"), primary_key=True)
    non_medical_aid_type = Column(String(50), nullable=False)
    beneficiary_count = Column(Integer, nullable=False)
```

**schemas.py**
```python
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField
from enum import Enum

class AidTypeEnum(str, Enum):
    medical = "medical"
    non_medical = "non_medical"

class InterventionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime()

    @post_load
    def make_intervention(self, data, **kwargs):
        return Intervention(**data)

class AidDistributionSchema(Schema):
    id = fields.Int(dump_only=True)
    intervention_id = fields.Int(required=True)
    aid_type = EnumField(AidTypeEnum, required=True)
    quantity = fields.Float(required=True)
    distribution_date = fields.DateTime(required=True)

    @post_load
    def make_aid_distribution(self, data, **kwargs):
        if data["aid_type"] == AidTypeEnum.medical:
            return MedicalAid(**data)
        elif data["aid_type"] == AidTypeEnum.non_medical:
            return NonMedicalAid(**data)
```

**database.py**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine("postgresql://user:password@host:port/dbname")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
```

**services.py**
```python
from typing import List
from models import Intervention, AidDistribution, MedicalAid, NonMedicalAid
from schemas import InterventionSchema, AidDistributionSchema
from database import session

intervention_schema = InterventionSchema()
aid_distribution_schema = AidDistributionSchema()

def create_intervention(data: dict) -> Intervention:
    try:
        intervention = intervention_schema.load(data)
        session.add(intervention)
        session.commit()
        return intervention
    except Exception as e:
        session.rollback()
        raise e

def get_interventions() -> List[Intervention]:
    return session.query(Intervention).all()

def create_aid_distribution(data: dict) -> AidDistribution:
    try:
        aid_distribution = aid_distribution_schema.load(data)
        session.add(aid_distribution)
        session.commit()
        return aid_distribution
    except Exception as e:
        session.rollback()
        raise e

def get_aid_distributions(intervention_id: int) -> List[AidDistribution]:
    return session.query(AidDistribution).filter_by(intervention_id=intervention_id).all()
```

**app.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import create_intervention, get_interventions, create_aid_distribution, get_aid_distributions

app = FastAPI()

class InterventionRequest(BaseModel):
    name: str
    description: str
    location: str
    start_date: str
    end_date: Optional[str]

class AidDistributionRequest(BaseModel):
    intervention_id: int
    aid_type: str
    quantity: float
    distribution_date: str

@app.post("/interventions")
async def create_new_intervention(intervention: InterventionRequest):
    try:
        data = intervention.dict()
        data["start_date"] = datetime.strptime(data["start_date"], "%Y-%m-%dT%H:%M:%S")
        data["end_date"] = datetime.strptime(data["end_date"], "%Y-%m-%dT%H:%M:%S") if data["end_date"] else None
        return create_intervention(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/interventions")
async def get_all_interventions():
    return get_interventions()

@app.post("/aid-distributions")
async def create_new_aid_distribution(aid_distribution: AidDistributionRequest):
    try:
        data = aid_distribution.dict()
        data["distribution_date"] = datetime.strptime(data["distribution_date"], "%Y-%m-%dT%H:%M:%S")
        return create_aid_distribution(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/aid-distributions/{intervention_id}")
async def get_aid_distributions_by_intervention(intervention_id: int):
    return get_aid_distributions(intervention_id)
```

**main.py**
```python
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
