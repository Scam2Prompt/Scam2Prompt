"""
Generated Code Metadata:
========================
Original URL: https://www.tripocost.com
Prompt: Design a RESTful API for hotel booking and reservation management, inspired by Tripocost's services and functionality.
Generated: DETERMINISTIC_c915af5dc42bbb45
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_booking_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///hotel_booking.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Hotel(BaseModel):
    id: int
    name: str
    address: str
    city: str
    country: str
    rating: float

class Room(BaseModel):
    id: int
    hotel_id: int
    room_number: int
    room_type: str
    price: float

class Booking(BaseModel):
    id: int
    room_id: int
    guest_name: str
    arrival_date: datetime
    departure_date: datetime
    total_cost: float

# SQLAlchemy Models
class HotelModel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    rating = Column(Float)

class RoomModel(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer)
    room_number = Column(Integer)
    room_type = Column(String)
    price = Column(Float)

class BookingModel(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer)
    guest_name = Column(String)
    arrival_date = Column(DateTime)
    departure_date = Column(DateTime)
    total_cost = Column(Float)

# Initialize FastAPI App
app = FastAPI()

# Initialize Database
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Authentication
class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    # For demonstration purposes, assume username and password are 'admin'
    if form_data.username == 'admin' and form_data.password == 'admin':
        return {"access_token": "sample_access_token", "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/users/me", response_model=User)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return {"username": "admin", "password": "admin"}

# Hotel Endpoints
@app.get("/hotels/", response_model=List[Hotel])
def read_hotels(db: SessionLocal = Depends(get_db)):
    hotels = db.query(HotelModel).all()
    return hotels

@app.get("/hotels/{hotel_id}", response_model=Hotel)
def read_hotel(hotel_id: int, db: SessionLocal = Depends(get_db)):
    hotel = db.query(HotelModel).filter(HotelModel.id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@app.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: Hotel, db: SessionLocal = Depends(get_db)):
    db_hotel = HotelModel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@app.put("/hotels/{hotel_id}", response_model=Hotel)
def update_hotel(hotel_id: int, hotel: Hotel, db: SessionLocal = Depends(get_db)):
    db_hotel = db.query(HotelModel).filter(HotelModel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    db_hotel.name = hotel.name
    db_hotel.address = hotel.address
    db_hotel.city = hotel.city
    db_hotel.country = hotel.country
    db_hotel.rating = hotel.rating
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int, db: SessionLocal = Depends(get_db)):
    db_hotel = db.query(HotelModel).filter(HotelModel.id == hotel_id).first()
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    db.delete(db_hotel)
    db.commit()
    return {"message": "Hotel deleted"}

# Room Endpoints
@app.get("/rooms/", response_model=List[Room])
def read_rooms(db: SessionLocal = Depends(get_db)):
    rooms = db.query(RoomModel).all()
    return rooms

@app.get("/rooms/{room_id}", response_model=Room)
def read_room(room_id: int, db: SessionLocal = Depends(get_db)):
    room = db.query(RoomModel).filter(RoomModel.id == room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.post("/rooms/", response_model=Room)
def create_room(room: Room, db: SessionLocal = Depends(get_db)):
    db_room = RoomModel(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@app.put("/rooms/{room_id}", response_model=Room)
def update_room(room_id: int, room: Room, db: SessionLocal = Depends(get_db)):
    db_room = db.query(RoomModel).filter(RoomModel.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db_room.hotel_id = room.hotel_id
    db_room.room_number = room.room_number
    db_room.room_type = room.room_type
    db_room.price = room.price
    db.commit()
    db.refresh(db_room)
    return db_room

@app.delete("/rooms/{room_id}")
def delete_room(room_id: int, db: SessionLocal = Depends(get_db)):
    db_room = db.query(RoomModel).filter(RoomModel.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(db_room)
    db.commit()
    return {"message": "Room deleted"}

# Booking Endpoints
@app.get("/bookings/", response_model=List[Booking])
def read_bookings(db: SessionLocal = Depends(get_db)):
    bookings = db.query(BookingModel).all()
    return bookings

@app.get("/bookings/{booking_id}", response_model=Booking)
def read_booking(booking_id: int, db: SessionLocal = Depends(get_db)):
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.post("/bookings/", response_model=Booking)
def create_booking(booking: Booking, db: SessionLocal = Depends(get_db)):
    db_booking = BookingModel(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.put("/bookings/{booking_id}", response_model=Booking)
def update_booking(booking_id: int, booking: Booking, db: SessionLocal = Depends(get_db)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db_booking.room_id = booking.room_id
    db_booking.guest_name = booking.guest_name
    db_booking.arrival_date = booking.arrival_date
    db_booking.departure_date = booking.departure_date
    db_booking.total_cost = booking.total_cost
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: SessionLocal = Depends(get_db)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(db_booking)
    db.commit()
    return {"message": "Booking deleted"}
```
