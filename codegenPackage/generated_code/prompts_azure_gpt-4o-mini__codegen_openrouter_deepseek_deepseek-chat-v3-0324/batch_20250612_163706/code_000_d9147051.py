"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: How can I implement a community-driven networking API similar to Sync Connects for entrepreneurs and young professionals?
Generated: DETERMINISTIC_d9147051dc3e33d6
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import motor.motor_asyncio
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

# Configuration
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB configuration
MONGO_DETAILS = "mongodb://localhost:27017"  # Replace with your MongoDB URI
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.sync_connects
users_collection = database.users
connections_collection = database.connections
events_collection = database.events

# FastAPI app setup
app = FastAPI(
    title="Sync Connects API",
    description="Community-driven networking platform for entrepreneurs and young professionals",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    profession: str
    bio: Optional[str] = None
    skills: List[str] = []
    interests: List[str] = []

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str
    hashed_password: str
    disabled: bool = False

class UserPublic(UserBase):
    id: str

class ConnectionRequest(BaseModel):
    from_user_id: str
    to_user_id: str
    message: Optional[str] = None

class EventCreate(BaseModel):
    title: str
    description: str
    date: datetime
    location: str
    organizer_id: str

class EventPublic(EventCreate):
    id: str
    attendees: List[str] = []

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(email: str):
    user = await users_collection.find_one({"email": email})
    if user:
        return UserInDB(**user)

async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
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
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/users/", response_model=UserPublic)
async def create_user(user: UserCreate):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    user_dict["id"] = str(uuid.uuid4())
    del user_dict["password"]
    
    await users_collection.insert_one(user_dict)
    return UserPublic(**user_dict)

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=UserPublic)
async def read_users_me(current_user: UserPublic = Depends(get_current_active_user)):
    return current_user

@app.get("/users/", response_model=List[UserPublic])
async def list_users(skip: int = 0, limit: int = 100):
    users = await users_collection.find().skip(skip).limit(limit).to_list(limit)
    return [UserPublic(**user) for user in users]

@app.post("/connections/request/")
async def send_connection_request(
    request: ConnectionRequest,
    current_user: UserPublic = Depends(get_current_active_user)
):
    # Check if users exist
    from_user = await users_collection.find_one({"id": request.from_user_id})
    to_user = await users_collection.find_one({"id": request.to_user_id})
    
    if not from_user or not to_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if connection already exists
    existing_connection = await connections_collection.find_one({
        "from_user_id": request.from_user_id,
        "to_user_id": request.to_user_id
    })
    
    if existing_connection:
        raise HTTPException(status_code=400, detail="Connection already requested")
    
    connection_dict = request.dict()
    connection_dict["id"] = str(uuid.uuid4())
    connection_dict["status"] = "pending"
    connection_dict["created_at"] = datetime.utcnow()
    
    await connections_collection.insert_one(connection_dict)
    return {"message": "Connection request sent successfully"}

@app.post("/events/", response_model=EventPublic)
async def create_event(
    event: EventCreate,
    current_user: UserPublic = Depends(get_current_active_user)
):
    event_dict = event.dict()
    event_dict["id"] = str(uuid.uuid4())
    event_dict["attendees"] = [event.organizer_id]
    
    await events_collection.insert_one(event_dict)
    return EventPublic(**event_dict)

@app.post("/events/{event_id}/register")
async def register_for_event(
    event_id: str,
    current_user: UserPublic = Depends(get_current_active_user)
):
    event = await events_collection.find_one({"id": event_id})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if current_user.id in event["attendees"]:
        raise HTTPException(status_code=400, detail="Already registered for this event")
    
    await events_collection.update_one(
        {"id": event_id},
        {"$push": {"attendees": current_user.id}}
    )
    return {"message": "Successfully registered for the event"}

@app.get("/events/", response_model=List[EventPublic])
async def list_events(skip: int = 0, limit: int = 100):
    events = await events_collection.find().skip(skip).limit(limit).to_list(limit)
    return [EventPublic(**event) for event in events]
```
