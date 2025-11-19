"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Design a RESTful API for a chiller van rental company in Dubai, including endpoints for booking, tracking, and managing deliveries with temperature monitoring.
Generated: DETERMINISTIC_1cfea8a800101791
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chiller_van_rental_api.py
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# App setup
app = FastAPI(
    title="Chiller Van Rental API",
    description="API for managing chiller van rentals in Dubai",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "email": "support@chillervanrental.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Security setup
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in-memory for demo purposes)
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    hashed_password: str
    disabled: bool = False
    is_admin: bool = False

class ChillerVan(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    license_plate: str
    capacity: float  # in cubic meters
    temperature_range: str  # e.g., "2°C to 8°C"
    status: str = "available"  # available, booked, maintenance
    current_location: Optional[str] = None

class Booking(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    van_id: str
    start_time: datetime
    end_time: datetime
    pickup_location: str
    delivery_location: str
    temperature_requirement: str
    status: str = "pending"  # pending, confirmed, completed, cancelled
    created_at: datetime = Field(default_factory=datetime.now)

class TemperatureLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    van_id: str
    temperature: float
    timestamp: datetime = Field(default_factory=datetime.now)
    location: Optional[str] = None

# In-memory databases
users_db = {}
vans_db = {}
bookings_db = {}
temperature_logs_db = {}

# Helper functions
def get_user(username: str):
    if username in users_db:
        user_dict = users_db[username]
        return User(**user_dict)
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
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
    except JWTError:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def get_admin_user(current_user: User = Depends(get_current_active_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

# Pydantic models for requests/responses
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool = False

class UserOut(BaseModel):
    id: str
    username: str
    email: str
    is_admin: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class BookingCreate(BaseModel):
    van_id: str
    start_time: datetime
    end_time: datetime
    pickup_location: str
    delivery_location: str
    temperature_requirement: str

    @validator('end_time')
    def end_time_must_be_after_start_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError('End time must be after start time')
        return v

class BookingOut(BaseModel):
    id: str
    user_id: str
    van_id: str
    start_time: datetime
    end_time: datetime
    pickup_location: str
    delivery_location: str
    temperature_requirement: str
    status: str
    created_at: datetime

class TemperatureLogCreate(BaseModel):
    van_id: str
    temperature: float
    location: Optional[str] = None

class TemperatureLogOut(BaseModel):
    id: str
    van_id: str
    temperature: float
    timestamp: datetime
    location: Optional[str] = None

class ChillerVanCreate(BaseModel):
    license_plate: str
    capacity: float
    temperature_range: str

class ChillerVanOut(BaseModel):
    id: str
    license_plate: str
    capacity: float
    temperature_range: str
    status: str
    current_location: Optional[str] = None

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate, current_user: User = Depends(get_admin_user)):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin
    )
    users_db[user.username] = db_user.dict()
    return db_user

@app.get("/users/me/", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Chiller Van endpoints
@app.post("/vans/", response_model=ChillerVanOut)
async def create_van(van: ChillerVanCreate, current_user: User = Depends(get_admin_user)):
    new_van = ChillerVan(**van.dict())
    vans_db[new_van.id] = new_van.dict()
    return new_van

@app.get("/vans/", response_model=List[ChillerVanOut])
async def list_vans(status: Optional[str] = None, current_user: User = Depends(get_current_active_user)):
    if status:
        return [van for van in vans_db.values() if van["status"] == status]
    return list(vans_db.values())

@app.get("/vans/{van_id}", response_model=ChillerVanOut)
async def get_van(van_id: str, current_user: User = Depends(get_current_active_user)):
    if van_id not in vans_db:
        raise HTTPException(status_code=404, detail="Van not found")
    return vans_db[van_id]

@app.put("/vans/{van_id}", response_model=ChillerVanOut)
async def update_van(van_id: str, van_update: ChillerVanCreate, current_user: User = Depends(get_admin_user)):
    if van_id not in vans_db:
        raise HTTPException(status_code=404, detail="Van not found")
    
    van_data
