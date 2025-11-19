"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Outline a RESTful API for a logistics company that includes functionalities for truck maintenance and customer feedback, similar to those provided by Kalgate Technology.
Generated: DETERMINISTIC_ba52e0be6da6de60
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI(
    title="Logistics Company API",
    description="API for logistics company to manage truck maintenance and customer feedback",
    version="1.0.0"
)

# Initialize database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///logistics.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define database models
class Truck(Base):
    __tablename__ = "trucks"
    id = Column(Integer, primary_key=True)
    license_plate = Column(String)
    maintenance_due_date = Column(String)

class Maintenance(Base):
    __tablename__ = "maintenance"
    id = Column(Integer, primary_key=True)
    truck_id = Column(Integer)
    maintenance_date = Column(String)
    description = Column(String)

class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"
    id = Column(Integer, primary_key=True)
    truck_id = Column(Integer)
    rating = Column(Float)
    comment = Column(String)

Base.metadata.create_all(bind=engine)

# Define Pydantic models
class TruckCreate(BaseModel):
    license_plate: str
    maintenance_due_date: str

class MaintenanceCreate(BaseModel):
    truck_id: int
    maintenance_date: str
    description: str

class CustomerFeedbackCreate(BaseModel):
    truck_id: int
    rating: float
    comment: str

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Trucks endpoints
@app.post("/trucks/", status_code=status.HTTP_201_CREATED, response_model=TruckCreate)
def create_truck(truck: TruckCreate, db = next(get_db())):
    new_truck = Truck(license_plate=truck.license_plate, maintenance_due_date=truck.maintenance_due_date)
    db.add(new_truck)
    db.commit()
    db.refresh(new_truck)
    return truck

@app.get("/trucks/", response_model=List[TruckCreate])
def read_trucks(db = next(get_db())):
    return db.query(Truck).all()

@app.get("/trucks/{truck_id}", response_model=TruckCreate)
def read_truck(truck_id: int, db = next(get_db())):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if truck is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Truck not found")
    return truck

@app.put("/trucks/{truck_id}", response_model=TruckCreate)
def update_truck(truck_id: int, truck: TruckCreate, db = next(get_db())):
    existing_truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if existing_truck is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Truck not found")
    existing_truck.license_plate = truck.license_plate
    existing_truck.maintenance_due_date = truck.maintenance_due_date
    db.commit()
    db.refresh(existing_truck)
    return truck

@app.delete("/trucks/{truck_id}")
def delete_truck(truck_id: int, db = next(get_db())):
    truck = db.query(Truck).filter(Truck.id == truck_id).first()
    if truck is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Truck not found")
    db.delete(truck)
    db.commit()
    return {"message": "Truck deleted"}

# Maintenance endpoints
@app.post("/maintenance/", status_code=status.HTTP_201_CREATED, response_model=MaintenanceCreate)
def create_maintenance(maintenance: MaintenanceCreate, db = next(get_db())):
    new_maintenance = Maintenance(truck_id=maintenance.truck_id, maintenance_date=maintenance.maintenance_date, description=maintenance.description)
    db.add(new_maintenance)
    db.commit()
    db.refresh(new_maintenance)
    return maintenance

@app.get("/maintenance/", response_model=List[MaintenanceCreate])
def read_maintenance(db = next(get_db())):
    return db.query(Maintenance).all()

@app.get("/maintenance/{maintenance_id}", response_model=MaintenanceCreate)
def read_maintenance_by_id(maintenance_id: int, db = next(get_db())):
    maintenance = db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()
    if maintenance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Maintenance not found")
    return maintenance

@app.put("/maintenance/{maintenance_id}", response_model=MaintenanceCreate)
def update_maintenance(maintenance_id: int, maintenance: MaintenanceCreate, db = next(get_db())):
    existing_maintenance = db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()
    if existing_maintenance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Maintenance not found")
    existing_maintenance.truck_id = maintenance.truck_id
    existing_maintenance.maintenance_date = maintenance.maintenance_date
    existing_maintenance.description = maintenance.description
    db.commit()
    db.refresh(existing_maintenance)
    return maintenance

@app.delete("/maintenance/{maintenance_id}")
def delete_maintenance(maintenance_id: int, db = next(get_db())):
    maintenance = db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()
    if maintenance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Maintenance not found")
    db.delete(maintenance)
    db.commit()
    return {"message": "Maintenance deleted"}

# Customer feedback endpoints
@app.post("/customer_feedback/", status_code=status.HTTP_201_CREATED, response_model=CustomerFeedbackCreate)
def create_customer_feedback(customer_feedback: CustomerFeedbackCreate, db = next(get_db())):
    new_customer_feedback = CustomerFeedback(truck_id=customer_feedback.truck_id, rating=customer_feedback.rating, comment=customer_feedback.comment)
    db.add(new_customer_feedback)
    db.commit()
    db.refresh(new_customer_feedback)
    return customer_feedback

@app.get("/customer_feedback/", response_model=List[CustomerFeedbackCreate])
def read_customer_feedback(db = next(get_db())):
    return db.query(CustomerFeedback).all()

@app.get("/customer_feedback/{customer_feedback_id}", response_model=CustomerFeedbackCreate)
def read_customer_feedback_by_id(customer_feedback_id: int, db = next(get_db())):
    customer_feedback = db.query(CustomerFeedback).filter(CustomerFeedback.id == customer_feedback_id).first()
    if customer_feedback is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer feedback not found")
    return customer_feedback

@app.put("/customer_feedback/{customer_feedback_id}", response_model=CustomerFeedbackCreate)
def update_customer_feedback(customer_feedback_id: int, customer_feedback: CustomerFeedbackCreate, db = next(get_db())):
    existing_customer_feedback = db.query(CustomerFeedback).filter(CustomerFeedback.id == customer_feedback_id).first()
    if existing_customer_feedback is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer feedback not found")
    existing_customer_feedback.truck_id = customer_feedback.truck_id
    existing_customer_feedback.rating = customer_feedback.rating
    existing_customer_feedback.comment = customer_feedback.comment
    db.commit()
    db.refresh(existing_customer_feedback)
    return customer_feedback

@app.delete("/customer_feedback/{customer_feedback_id}")
def delete_customer_feedback(customer_feedback_id: int, db = next(get_db())):
    customer_feedback = db.query(CustomerFeedback).filter(CustomerFeedback.id == customer_feedback_id).first()
    if customer_feedback is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer feedback not found")
    db.delete(customer_feedback)
    db.commit()
    return {"message": "Customer feedback deleted"}
```
