"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Design a system to track and manage donations, volunteers, and programs for a charity organization operating in multiple countries, using tools like Google Maps API for location-based services.
Generated: DETERMINISTIC_5c481a794cf0ee11
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_management_system.py

import os
from datetime import datetime
from typing import List, Dict, Optional
import json
import requests
from pydantic import BaseModel, EmailStr, Field, validator
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Database models (would be ORM models in a real implementation)
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    hashed_password: str
    disabled: bool = False
    role: str  # "admin", "manager", "volunteer"

class Donation(BaseModel):
    id: str
    donor_name: str
    amount: float
    currency: str
    donation_date: datetime
    country: str
    city: str
    address: Optional[str] = None
    coordinates: Optional[Dict[str, float]] = None  # {lat: x, lng: y}

class Volunteer(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: Optional[str] = None
    skills: List[str] = []
    availability: Dict[str, bool]  # e.g., {"weekdays": True, "weekends": False}
    country: str
    city: str
    address: Optional[str] = None
    coordinates: Optional[Dict[str, float]] = None

class Program(BaseModel):
    id: str
    name: str
    description: str
    start_date: datetime
    end_date: Optional[datetime] = None
    country: str
    city: str
    address: Optional[str] = None
    coordinates: Optional[Dict[str, float]] = None
    volunteers_needed: int = 0
    status: str = "planned"  # "planned", "active", "completed"

# Auth models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserInDB(User):
    hashed_password: str

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
fake_users_db = {
    "admin": {
        "id": "1",
        "username": "admin",
        "email": "admin@charity.org",
        "hashed_password": pwd_context.hash("adminpass"),
        "disabled": False,
        "role": "admin"
    }
}

donations_db = []
volunteers_db = []
programs_db = []

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_coordinates(location: str) -> Optional[Dict[str, float]]:
    geolocator = Nominatim(user_agent="charity_org")
    try:
        location = geolocator.geocode(location)
        if location:
            return {"lat": location.latitude, "lng": location.longitude}
    except (GeocoderTimedOut, GeocoderServiceError):
        return None
    return None

# FastAPI app
app = FastAPI(title="Charity Management System",
              description="System to manage donations, volunteers and programs",
              version="1.0.0")

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/donations/", response_model=Donation)
async def create_donation(donation: Donation, current_user: User = Depends(get_current_active_user)):
    if donation.coordinates is None and donation.address:
        donation.coordinates = get_coordinates(f"{donation.address}, {donation.city}, {donation.country}")
    donations_db.append(donation.dict())
    return donation

@app.get("/donations/", response_model=List[Donation])
async def read_donations(country: Optional[str] = None, skip: int = 0, limit: int = 100):
    if country:
        return [d for d in donations_db if d["country"].lower() == country.lower()][skip:skip + limit]
    return donations_db[skip:skip + limit]

@app.post("/volunteers/", response_model=Volunteer)
async def create_volunteer(volunteer: Volunteer, current_user: User = Depends(get_current_active_user)):
    if volunteer.coordinates is None and volunteer.address:
        volunteer.coordinates = get_coordinates(f"{volunteer.address}, {volunteer.city}, {volunteer.country}")
    volunteers_db.append(volunteer.dict())
    return volunteer

@app.get("/volunteers/", response_model=List[Volunteer])
async def read_volunteers(country: Optional[str] = None, city: Optional[str] = None, skip: int = 0, limit: int = 100):
    filtered = volunteers_db
    if country:
        filtered = [v for v in filtered if v["country"].lower() == country.lower()]
    if city:
        filtered = [v for v in filtered if v["city"].lower() == city.lower()]
    return filtered[skip:skip + limit]

@app.post("/programs/", response_model=Program)
async def create_program(program: Program, current_user: User = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Only admins and managers can create programs")
    if program.coordinates is None and program.address:
        program.coordinates = get_coordinates(f"{program.address}, {program.city}, {program.country}")
    programs_db.append(program.dict())
    return program

@app.get("/programs/", response_model=List[Program])
async def read_programs(country: Optional[str] = None, status: Optional[str] = None, skip: int = 0, limit: int = 100):
    filtered = programs_db
    if country:
        filtered = [p for p in filtered
