"""
Generated Code Metadata:
========================
Original URL: https://member.bmtours.id
Prompt: Suggest an API for managing travel itineraries and integrating it with a member portal for Umrah services like BM Tours.
Generated: DETERMINISTIC_28aab6058b24342c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Travel Itinerary API**
=======================

### models.py
```python
from datetime import datetime
from typing import List
from pydantic import BaseModel, validator

class TravelItinerary(BaseModel):
    id: int
    member_id: int
    trip_name: str
    start_date: datetime
    end_date: datetime
    destinations: List[str]

    @validator('start_date')
    def start_date_must_be_before_end_date(cls, v, values, **kwargs):
        if 'end_date' in values and v > values['end_date']:
            raise ValueError('Start date must be before end date')
        return v

class UmrahService(BaseModel):
    id: int
    name: str
    description: str
```

### database.py
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://user:password@host:port/dbname')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class TravelItineraryDB(Base):
    __tablename__ = 'travel_itineraries'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    trip_name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    destinations = Column(String)

class UmrahServiceDB(Base):
    __tablename__ = 'umrah_services'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

Base.metadata.create_all(engine)
```

### crud.py
```python
from models import TravelItinerary, UmrahService
from database import session, TravelItineraryDB, UmrahServiceDB

def create_travel_itinerary(itinerary: TravelItinerary):
    try:
        db_itinerary = TravelItineraryDB(**itinerary.dict())
        session.add(db_itinerary)
        session.commit()
        return db_itinerary
    except Exception as e:
        session.rollback()
        raise e

def get_travel_itinerary(id: int):
    try:
        return session.query(TravelItineraryDB).filter_by(id=id).first()
    except Exception as e:
        raise e

def update_travel_itinerary(id: int, itinerary: TravelItinerary):
    try:
        db_itinerary = session.query(TravelItineraryDB).filter_by(id=id).first()
        if db_itinerary:
            db_itinerary.trip_name = itinerary.trip_name
            db_itinerary.start_date = itinerary.start_date
            db_itinerary.end_date = itinerary.end_date
            db_itinerary.destinations = itinerary.destinations
            session.commit()
            return db_itinerary
    except Exception as e:
        session.rollback()
        raise e

def delete_travel_itinerary(id: int):
    try:
        db_itinerary = session.query(TravelItineraryDB).filter_by(id=id).first()
        if db_itinerary:
            session.delete(db_itinerary)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e

def create_umrah_service(service: UmrahService):
    try:
        db_service = UmrahServiceDB(**service.dict())
        session.add(db_service)
        session.commit()
        return db_service
    except Exception as e:
        session.rollback()
        raise e
```

### api.py
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud import create_travel_itinerary, get_travel_itinerary, update_travel_itinerary, delete_travel_itinerary, create_umrah_service
from models import TravelItinerary, UmrahService

app = FastAPI()

@app.post("/travel-itineraries/")
async def create_itinerary(itinerary: TravelItinerary):
    try:
        return create_travel_itinerary(itinerary)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/travel-itineraries/{id}")
async def get_itinerary(id: int):
    try:
        itinerary = get_travel_itinerary(id)
        if not itinerary:
            raise HTTPException(status_code=404, detail="Itinerary not found")
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/travel-itineraries/{id}")
async def update_itinerary(id: int, itinerary: TravelItinerary):
    try:
        updated_itinerary = update_travel_itinerary(id, itinerary)
        if not updated_itinerary:
            raise HTTPException(status_code=404, detail="Itinerary not found")
        return updated_itinerary
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/travel-itineraries/{id}")
async def delete_itinerary(id: int):
    try:
        delete_travel_itinerary(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/umrah-services/")
async def create_service(service: UmrahService):
    try:
        return create_umrah_service(service)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### main.py
```python
from api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
