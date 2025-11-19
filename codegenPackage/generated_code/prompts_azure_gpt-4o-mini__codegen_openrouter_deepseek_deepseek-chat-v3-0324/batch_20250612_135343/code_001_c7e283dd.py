"""
Generated Code Metadata:
========================
Original URL: https://nissta.org
Prompt: Write a code snippet that implements a consultation scheduling system for industry experts and farmers, inspired by the consultative processes highlighted by NISSTA.
Generated: DETERMINISTIC_c7e283dda6dee067
Batch ID: 20250612_135343
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
from typing import List, Dict, Optional
from pydantic import BaseModel, validator, ValidationError
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import timedelta

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Models
class UserType(str, Enum):
    FARMER = "farmer"
    EXPERT = "expert"

class User(BaseModel):
    username: str
    email: str
    full_name: str
    user_type: UserType
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ConsultationRequest(BaseModel):
    farmer_username: str
    expert_username: str
    topic: str
    preferred_date: datetime.date
    preferred_time: str
    duration_minutes: int = 30
    description: Optional[str] = None

    @validator('preferred_time')
    def validate_time_format(cls, v):
        try:
            datetime.datetime.strptime(v, "%H:%M")
            return v
        except ValueError:
            raise ValueError("Time must be in HH:MM format")

class Consultation(BaseModel):
    id: str
    farmer_username: str
    expert_username: str
    topic: str
    scheduled_date: datetime.date
    scheduled_time: str
    duration_minutes: int
    status: str = "pending"
    description: Optional[str] = None

# Database (simulated)
fake_users_db = {
    "farmer1": {
        "username": "farmer1",
        "email": "farmer1@example.com",
        "full_name": "John Farmer",
        "user_type": UserType.FARMER,
        "disabled": False,
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # "secret"
    },
    "expert1": {
        "username": "expert1",
        "email": "expert1@example.com",
        "full_name": "Dr. Agriculture",
        "user_type": UserType.EXPERT,
        "disabled": False,
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # "secret"
    }
}

consultations_db: Dict[str, Consultation] = {}

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

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

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = authenticate_user(fake_users_db, username, password)
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

@app.post("/consultations/request", response_model=Consultation)
async def request_consultation(
    consultation_request: ConsultationRequest,
    current_user: User = Depends(get_current_active_user)
):
    if current_user.user_type != UserType.FARMER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only farmers can request consultations"
        )
    
    if consultation_request.farmer_username != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot request consultation for another farmer"
        )
    
    expert = get_user(fake_users_db, consultation_request.expert_username)
    if not expert or expert.user_type != UserType.EXPERT:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expert not found"
        )
    
    consultation_id = f"cons_{len(consultations_db) + 1}"
    consultation = Consultation(
        id=consultation_id,
        farmer_username=consultation_request.farmer_username,
        expert_username=consultation_request.expert_username,
        topic=consultation_request.topic,
        scheduled_date=consultation_request.preferred_date,
        scheduled_time=consultation_request.preferred_time,
        duration_minutes=consultation_request.duration_minutes,
        description=consultation_request.description
    )
    
    consultations_db[consultation_id] = consultation
    return consultation

@app.get("/consultations", response_model=List[Consultation])
async def get_consultations(
    current_user: User = Depends(get_current_active_user),
    status_filter: Optional[str] = None
):
    if current_user.user_type == UserType.FARMER:
        consultations = [
            c for c in consultations_db.values() 
            if c.farmer_username == current_user.username
        ]
    else:
        consultations = [
            c for c in consultations_db.values() 
            if c.expert_username == current_user.username
        ]
    
    if status_filter:
        consultations = [c for c in consultations if c.status == status_filter]
    
    return consultations

@app.put("/consultations/{consultation_id}/status")
async def update_consultation_status(
    consultation_id: str,
    new_status: str,
    current_user: User = Depends(get_current_active_user)
):
    if current_user.user_type != UserType.EXPERT:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only experts can update consultation status"
        )
    
    if consultation_id not in consultations_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consultation not found"
        )
    
    consultation = consultations_db[consultation_id]
    if consultation.expert_username != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot update consultation for another expert"
        )
    
    consultation.status = new_status
    consultations_db[consultation_id] = consultation
    return {"message": "Consultation status updated successfully"}

@app.get("/users/experts", response_model
