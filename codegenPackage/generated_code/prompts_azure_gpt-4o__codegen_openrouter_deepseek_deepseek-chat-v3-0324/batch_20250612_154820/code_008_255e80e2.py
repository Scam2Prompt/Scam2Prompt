"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement a virtual healthcare service booking system, inspired by the "MyClinic" feature mentioned for Irish Life Health members on the Health Insurance Shop website.
Generated: DETERMINISTIC_255e80e26482413f
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError

# Initialize FastAPI app
app = FastAPI(
    title="MyClinic Virtual Healthcare Booking System",
    description="A virtual healthcare service booking system for Irish Life Health members",
    version="1.0.0"
)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in a real app, this would connect to a database)
class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    hashed_password: str
    is_active: bool = True
    is_health_member: bool = False
    member_id: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    is_health_member: bool = False
    member_id: Optional[str] = None

    @validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v

class UserInDB(User):
    class Config:
        orm_mode = True

class ServiceType(str, Enum):
    general_practitioner = "General Practitioner"
    dermatologist = "Dermatologist"
    pediatrician = "Pediatrician"
    psychiatrist = "Psychiatrist"
    nutritionist = "Nutritionist"

class AppointmentStatus(str, Enum):
    booked = "Booked"
    completed = "Completed"
    cancelled = "Cancelled"
    rescheduled = "Rescheduled"

class Appointment(BaseModel):
    id: int
    user_id: int
    service_type: ServiceType
    appointment_time: datetime.datetime
    status: AppointmentStatus = AppointmentStatus.booked
    notes: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime.now()

class AppointmentCreate(BaseModel):
    service_type: ServiceType
    appointment_time: datetime.datetime
    notes: Optional[str] = None

    @validator('appointment_time')
    def appointment_time_must_be_future(cls, v):
        if v < datetime.datetime.now():
            raise ValueError("Appointment time must be in the future")
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database
fake_users_db: Dict[str, User] = {}
fake_appointments_db: Dict[int, Appointment] = {}
current_appointment_id = 1

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
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
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API endpoints
@app.post("/register", response_model=User)
async def register_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        id=len(fake_users_db) + 1,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        is_health_member=user.is_health_member,
        member_id=user.member_id
    )
    fake_users_db[user.username] = db_user
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = authenticate_user(fake_users_db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/services", response_model=List[ServiceType])
async def get_available_services():
    return list(ServiceType)

@app.post("/appointments", response_model=Appointment)
async def create_appointment(
    appointment: AppointmentCreate,
    current_user: User = Depends(get_current_active_user)
):
    global current_appointment_id
    
    # Check if user is a health member
    if not current_user.is_health_member:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only health members can book appointments"
        )
    
    # Check for conflicting appointments
    for existing_appointment in fake_appointments_db.values():
        if existing_appointment.user_id == current_user.id and existing_appointment.status == AppointmentStatus.booked:
            time_diff = abs((existing_appointment.appointment_time - appointment.appointment_time).total_seconds())
            if time_diff < 3600:  # 1 hour buffer between appointments
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="You already have an appointment within this time frame"
                )
    
    new_appointment = Appointment(
        id=current_appointment_id,
        user_id=current_user.id,
        service_type=appointment.service_type,
        appointment_time=appointment.appointment_time,
        notes=appointment.notes
    )
    
    fake_appointments_db[current_appointment_id] = new_appointment
    current_appointment_id += 1
    return new_appointment

@app.get("/appointments", response_model=List[Appointment])
async def get_user_appointments(
    current_user: User = Depends(get_current_active_user),
    status_filter: Optional[AppointmentStatus] = None
):
    user_appointments = [
        appt for appt in fake_appointments_db.values() 
        if appt.user_id == current_user.id and 
        (status_filter is None or appt.status == status_filter)
    ]
    return sorted(user_appointments, key=lambda x: x.appointment_time)

@app.put("/appointments/{appointment_id}", response_model=Appointment)
async def update_appointment(
    appointment_id: int,
    new_time: Optional[datetime.datetime] = None,
    new_status: Optional[AppointmentStatus] = None,
    new_notes: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    if appointment_id not in fake_appointments
