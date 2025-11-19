"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Develop a RESTful API that manages travel packages and itineraries, ensuring it includes features for group travel and local community engagement, as emphasized by Rehiletes.
Generated: DETERMINISTIC_ae1760cf5022d42c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Travel Package API**
======================

### **models.py**
```python
from typing import List
from pydantic import BaseModel, validator
from datetime import date

class Location(BaseModel):
    """Represents a location."""
    city: str
    country: str

class Itinerary(BaseModel):
    """Represents an itinerary."""
    location: Location
    start_date: date
    end_date: date

class TravelPackage(BaseModel):
    """Represents a travel package."""
    name: str
    description: str
    itineraries: List[Itinerary]
    price: float
    capacity: int

    @validator('itineraries')
    def validate_itineraries(cls, v):
        if not v:
            raise ValueError('At least one itinerary is required')
        return v

class GroupTravel(BaseModel):
    """Represents a group travel."""
    travel_package_id: int
    group_name: str
    group_size: int

class CommunityEngagement(BaseModel):
    """Represents a community engagement."""
    travel_package_id: int
    engagement_type: str
    description: str
```

### **database.py**
```python
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from models import TravelPackage, Itinerary, Location, GroupTravel, CommunityEngagement

engine = create_engine('sqlite:///travel.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class LocationModel(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)

    itineraries = relationship('ItineraryModel', backref='location')

class ItineraryModel(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    start_date = Column(Date)
    end_date = Column(Date)

    travel_packages = relationship('TravelPackageModel', secondary='itinerary_travel_packages')

class TravelPackageModel(Base):
    __tablename__ = 'travel_packages'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    capacity = Column(Integer)

    itineraries = relationship('ItineraryModel', secondary='itinerary_travel_packages', backref='travel_packages')
    group_travels = relationship('GroupTravelModel', backref='travel_package')
    community_engagements = relationship('CommunityEngagementModel', backref='travel_package')

class GroupTravelModel(Base):
    __tablename__ = 'group_travels'
    id = Column(Integer, primary_key=True)
    travel_package_id = Column(Integer, ForeignKey('travel_packages.id'))
    group_name = Column(String)
    group_size = Column(Integer)

class CommunityEngagementModel(Base):
    __tablename__ = 'community_engagements'
    id = Column(Integer, primary_key=True)
    travel_package_id = Column(Integer, ForeignKey('travel_packages.id'))
    engagement_type = Column(String)
    description = Column(String)

itinerary_travel_packages = Table('itinerary_travel_packages', Base.metadata,
    Column('itinerary_id', Integer, ForeignKey('itineraries.id')),
    Column('travel_package_id', Integer, ForeignKey('travel_packages.id'))
)

Base.metadata.create_all(engine)
```

### **main.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import Session, TravelPackageModel, ItineraryModel, LocationModel, GroupTravelModel, CommunityEngagementModel
from models import TravelPackage, Itinerary, Location, GroupTravel, CommunityEngagement

app = FastAPI()

# Create a new session
session = Session()

# Travel Packages
@app.post('/travel-packages/', response_model=TravelPackage)
async def create_travel_package(travel_package: TravelPackage):
    db_travel_package = TravelPackageModel(
        name=travel_package.name,
        description=travel_package.description,
        price=travel_package.price,
        capacity=travel_package.capacity
    )
    session.add(db_travel_package)
    session.commit()
    session.refresh(db_travel_package)
    return db_travel_package

@app.get('/travel-packages/', response_model=List[TravelPackage])
async def read_travel_packages():
    return session.query(TravelPackageModel).all()

@app.get('/travel-packages/{travel_package_id}', response_model=TravelPackage)
async def read_travel_package(travel_package_id: int):
    db_travel_package = session.query(TravelPackageModel).filter_by(id=travel_package_id).first()
    if db_travel_package is None:
        raise HTTPException(status_code=404, detail='Travel package not found')
    return db_travel_package

@app.put('/travel-packages/{travel_package_id}', response_model=TravelPackage)
async def update_travel_package(travel_package_id: int, travel_package: TravelPackage):
    db_travel_package = session.query(TravelPackageModel).filter_by(id=travel_package_id).first()
    if db_travel_package is None:
        raise HTTPException(status_code=404, detail='Travel package not found')
    db_travel_package.name = travel_package.name
    db_travel_package.description = travel_package.description
    db_travel_package.price = travel_package.price
    db_travel_package.capacity = travel_package.capacity
    session.commit()
    session.refresh(db_travel_package)
    return db_travel_package

@app.delete('/travel-packages/{travel_package_id}')
async def delete_travel_package(travel_package_id: int):
    db_travel_package = session.query(TravelPackageModel).filter_by(id=travel_package_id).first()
    if db_travel_package is None:
        raise HTTPException(status_code=404, detail='Travel package not found')
    session.delete(db_travel_package)
    session.commit()
    return {'message': 'Travel package deleted'}

# Itineraries
@app.post('/itineraries/', response_model=Itinerary)
async def create_itinerary(itinerary: Itinerary):
    db_location = LocationModel(city=itinerary.location.city, country=itinerary.location.country)
    session.add(db_location)
    session.commit()
    session.refresh(db_location)
    db_itinerary = ItineraryModel(
        location_id=db_location.id,
        start_date=itinerary.start_date,
        end_date=itinerary.end_date
    )
    session.add(db_itinerary)
    session.commit()
    session.refresh(db_itinerary)
    return db_itinerary

# Group Travels
@app.post('/group-travels/', response_model=GroupTravel)
async def create_group_travel(group_travel: GroupTravel):
    db_group_travel = GroupTravelModel(
        travel_package_id=group_travel.travel_package_id,
        group_name=group_travel.group_name,
        group_size=group_travel.group_size
    )
    session.add(db_group_travel)
    session.commit()
    session.refresh(db_group_travel)
    return db_group_travel

# Community Engagements
@app.post('/community-engagements/', response_model=CommunityEngagement)
async def create_community_engagement(community_engagement: CommunityEngagement):
    db_community_engagement = CommunityEngagementModel(
        travel_package_id=community_engagement.travel_package_id,
        engagement_type=community_engagement.engagement_type,
        description=community_engagement.description
    )
    session.add(db_community_engagement)
    session.commit()
    session.refresh(db_community_engagement)
    return db_community_engagement
```

### **requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```

### **run.sh**
```bash
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
