"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Implement a feature to manage school events and cultural activities, inspired by the Event Planning module in Him Saral's school management system.
Generated: DETERMINISTIC_e45b2aad45e57ffc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
from datetime import timedelta

# Constants
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (simulated with in-memory storage)
class EventType(str, Enum):
    ACADEMIC = "academic"
    CULTURAL = "cultural"
    SPORTS = "sports"
    OTHER = "other"

class EventStatus(str, Enum):
    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Event(BaseModel):
    id: str
    title: str
    description: str
    event_type: EventType
    start_date: datetime.datetime
    end_date: datetime.datetime
    location: str
    organizer: str
    status: EventStatus = EventStatus.PLANNED
    participants: List[str] = []
    budget: Optional[float] = None
    created_by: str
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

# In-memory database
db_users = {
    "admin": UserInDB(
        username="admin",
        email="admin@school.edu",
        full_name="Admin User",
        hashed_password=pwd_context.hash("adminpass"),
        disabled=False
    )
}

db_events: Dict[str, Event] = {}

# Authentication functions
def authenticate_user(username: str, password: str):
    user = db_users.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + timedelta(minutes=15)
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
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = db_users.get(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# FastAPI app
app = FastAPI(title="School Events Management System")

# Authentication endpoints
@app.post("/token")
async def login_for_access_token(form_data: dict):
    user = authenticate_user(form_data["username"], form_data["password"])
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

# Event endpoints
@app.post("/events/", response_model=Event)
async def create_event(event: Event, current_user: User = Depends(get_current_active_user)):
    if event.id in db_events:
        raise HTTPException(status_code=400, detail="Event ID already exists")
    event.created_by = current_user.username
    db_events[event.id] = event
    return event

@app.get("/events/", response_model=List[Event])
async def list_events(
    event_type: Optional[EventType] = None,
    status: Optional[EventStatus] = None,
    limit: int = 100,
    skip: int = 0
):
    events = list(db_events.values())
    if event_type:
        events = [e for e in events if e.event_type == event_type]
    if status:
        events = [e for e in events if e.status == status]
    return events[skip : skip + limit]

@app.get("/events/{event_id}", response_model=Event)
async def get_event(event_id: str):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_events[event_id]

@app.put("/events/{event_id}", response_model=Event)
async def update_event(
    event_id: str,
    event_update: Event,
    current_user: User = Depends(get_current_active_user)
):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    existing_event = db_events[event_id]
    if existing_event.created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this event")
    
    # Preserve some fields
    event_update.id = event_id
    event_update.created_by = existing_event.created_by
    event_update.created_at = existing_event.created_at
    event_update.updated_at = datetime.datetime.now()
    
    db_events[event_id] = event_update
    return event_update

@app.delete("/events/{event_id}")
async def delete_event(
    event_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if db_events[event_id].created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to delete this event")
    
    del db_events[event_id]
    return {"message": "Event deleted successfully"}

@app.post("/events/{event_id}/participants/{username}")
async def add_participant(
    event_id: str,
    username: str,
    current_user: User = Depends(get_current_active_user)
):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if username not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    
    if username in db_events[event_id].participants:
        raise HTTPException(status_code=400, detail="User already a participant")
    
    db_events[event_id].participants.append(username)
    return {"message": "Participant added successfully"}

@app.delete("/events/{event_id}/participants/{username}")
async def remove_participant(
    event_id: str,
    username: str,
    current_user: User = Depends(get_current_active_user)
):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if username not in db_events[event_id].participants:
        raise HTTPException(status_code=404, detail="User is not a participant")
    
    db_events[event_id].participants.remove(username)
    return {"message": "Participant removed successfully"}

@app.put("/events/{event_id}/status/{status}")
async def update_event_status(
    event_id: str,
    status: EventStatus,
    current_user: User = Depends(get_current_active_user)
):
    if event_id not in db_events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if db_events[event_id].created_by != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this event")
    
    db_events[event_id].status = status
    db_events[event_id].updated_at = datetime.datetime.now()
    return {"message": "Event status updated
