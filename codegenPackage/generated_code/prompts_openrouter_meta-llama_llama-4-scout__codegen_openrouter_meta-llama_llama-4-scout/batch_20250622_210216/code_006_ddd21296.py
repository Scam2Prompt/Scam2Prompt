"""
Generated Code Metadata:
========================
Original URL: https://cpastay.com
Prompt: Design a RESTful API for City Prime Apartments to manage their room inventory, bookings, and customer information, including endpoints for checking availability and making reservations.
Generated: DETERMINISTIC_ddd2129646afbc34
Batch ID: 20250622_210216
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
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///city_prime_apartments.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Room(BaseModel):
    room_number: int
    room_type: str
    capacity: int
    rate: float

class Customer(BaseModel):
    name: str
    email: str
    phone: str

class Booking(BaseModel):
    room_number: int
    customer_name: str
    check_in: datetime
    check_out: datetime

# SQLAlchemy Models
class RoomModel(Base):
    __tablename__ = "rooms"

    room_number = Column(Integer, primary_key=True)
    room_type = Column(String)
    capacity = Column(Integer)
    rate = Column(float)

class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class BookingModel(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer)
    customer_name = Column(String)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    is_active = Column(Boolean, default=True)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Endpoints
@app.post("/rooms/")
def create_room(room: Room, db: SessionLocal = Depends(get_db)):
    db_room = RoomModel(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return JSONResponse(content={"message": "Room created successfully"}, status_code=201)

@app.get("/rooms/")
def read_rooms(db: SessionLocal = Depends(get_db)):
    rooms = db.query(RoomModel).all()
    return [room.__dict__ for room in rooms]

@app.get("/rooms/{room_number}")
def read_room(room_number: int, db: SessionLocal = Depends(get_db)):
    room = db.query(RoomModel).filter(RoomModel.room_number == room_number).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room.__dict__

@app.post("/customers/")
def create_customer(customer: Customer, db: SessionLocal = Depends(get_db)):
    db_customer = CustomerModel(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return JSONResponse(content={"message": "Customer created successfully"}, status_code=201)

@app.get("/customers/")
def read_customers(db: SessionLocal = Depends(get_db)):
    customers = db.query(CustomerModel).all()
    return [customer.__dict__ for customer in customers]

@app.post("/bookings/")
def create_booking(booking: Booking, db: SessionLocal = Depends(get_db)):
    room = db.query(RoomModel).filter(RoomModel.room_number == booking.room_number).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    existing_booking = db.query(BookingModel).filter(BookingModel.room_number == booking.room_number, 
                                                     BookingModel.check_in <= booking.check_in, 
                                                     BookingModel.check_out >= booking.check_out).first()
    if existing_booking:
        raise HTTPException(status_code=400, detail="Room is not available for the given dates")
    db_booking = BookingModel(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return JSONResponse(content={"message": "Booking created successfully"}, status_code=201)

@app.get("/bookings/")
def read_bookings(db: SessionLocal = Depends(get_db)):
    bookings = db.query(BookingModel).all()
    return [booking.__dict__ for booking in bookings]

@app.get("/availability/{room_number}/{check_in}/{check_out}")
def check_availability(room_number: int, check_in: datetime, check_out: datetime, db: SessionLocal = Depends(get_db)):
    room = db.query(RoomModel).filter(RoomModel.room_number == room_number).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    existing_booking = db.query(BookingModel).filter(BookingModel.room_number == room_number, 
                                                     BookingModel.check_in <= check_in, 
                                                     BookingModel.check_out >= check_out).first()
    if existing_booking:
        return JSONResponse(content={"available": False}, status_code=200)
    return JSONResponse(content={"available": True}, status_code=200)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return JSONResponse(content={"access_token": "token", "token_type": "bearer"}, status_code=200)

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return JSONResponse(content={"message": "Hello, World!"}, status_code=200)
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
