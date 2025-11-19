"""
Generated Code Metadata:
========================
Original URL: https://digisou-ltd.com
Prompt: Generate a sample app development project that focuses on customer engagement, inspired by the innovative app solutions offered by DigiSou.
Generated: DETERMINISTIC_6f2254f1cbc1e6d7
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Customer Engagement App - DigiSou Inspired
A sample application focusing on customer engagement features like:
- User profiles
- Push notifications
- Loyalty programs
- Feedback collection
- Personalized content
"""

import json
from datetime import datetime
from typing import Optional, List, Dict
from enum import Enum
import uuid
import logging
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, EmailStr
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# App initialization
app = FastAPI(
    title="Customer Engagement App",
    description="DigiSou-inspired customer engagement platform",
    version="1.0.0"
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
class Database:
    def __init__(self):
        self.users = {}
        self.notifications = {}
        self.loyalty_programs = {}
        self.feedback = {}
        self.content = {}

db = Database()

# Models
class UserRole(str, Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    BUSINESS = "business"

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    role: UserRole
    points: int = 0
    preferences: Dict[str, str] = {}
    is_active: bool = True

    class Config:
        orm_mode = True

class Notification(BaseModel):
    id: str
    user_id: str
    title: str
    message: str
    is_read: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class LoyaltyProgram(BaseModel):
    id: str
    name: str
    description: str
    points_required: int
    reward: str
    is_active: bool = True

class Feedback(BaseModel):
    id: str
    user_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ContentItem(BaseModel):
    id: str
    title: str
    description: str
    content_type: str
    tags: List[str] = []
    is_personalized: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Utility functions
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user_id() -> str:
    return str(uuid.uuid4())

def get_user(db: Database, email: str) -> Optional[User]:
    for user in db.users.values():
        if user.email == email:
            return user
    return None

def authenticate_user(db: Database, email: str, password: str) -> Optional[User]:
    user = get_user(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    if get_user(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user_id = create_user_id()
    hashed_password = get_password_hash(user.password)
    db_user = User(
        id=user_id,
        email=user.email,
        full_name=user.full_name,
        role=UserRole.CUSTOMER,
        password=hashed_password
    )
    db.users[user_id] = db_user
    logger.info(f"Created new user with ID: {user_id}")
    return db_user

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/notifications/", response_model=Notification)
async def create_notification(
    user_id: str,
    title: str,
    message: str,
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN and current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create notifications for this user"
        )
    
    notification_id = str(uuid.uuid4())
    notification = Notification(
        id=notification_id,
        user_id=user_id,
        title=title,
        message=message
    )
    db.notifications[notification_id] = notification
    logger.info(f"Created notification for user {user_id}")
    return notification

@app.get("/notifications/{user_id}", response_model=List[Notification])
async def get_user_notifications(
    user_id: str,
    current_user: User = Depends(get_current_user)
):
    if current_user.id != user_id and current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view these notifications"
        )
    
    user_notifications = [
        n for n in db.notifications.values() if n.user_id == user_id
    ]
    return user_notifications

@app.post("/loyalty/", response_model=LoyaltyProgram)
async def create_loyalty_program(
    program: LoyaltyProgram,
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create loyalty programs"
        )
    
    program_id = str(uuid.uuid4())
    db_program = LoyaltyProgram(
        id=program_id,
        **program.dict()
    )
    db.loyalty_programs[program_id] = db_program
    logger.info(f"Created new loyalty program: {program.name}")
    return db_program

@app.post("/feedback/", response_model=Feedback)
async def submit_feedback(
    rating: int,
    comment: Optional[str] = None,
    current_user: User = Depends(get_current_user)
):
    feedback_id = str(uuid.uuid4())
    feedback = Feedback(
        id=feedback_id,
        user_id=current_user.id,
        rating=rating,
        comment=comment
    )
    db.feedback[feedback_id] = feedback
    logger.info(f"Received feedback from user {current_user.id}")
    return feedback

@app.get("/content/personalized", response_model=List[ContentItem])
async def get_personalized_content(
    current_user: User = Depends(get_current_user)
):
    # In a real app, this would use the user's preferences to filter content
    personalized_content = [
        c for c in db.content.values() if c.is_personalized
    ]
    return personalized_content[:5]  # Return top 5 personalized items

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Helper functions for authentication
def create_access_token(data: dict):
    # In a real app, this would use proper JWT token creation
    return str(uuid.uuid4())

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, this would verify the JWT token
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Mock token verification
        if not token:
            raise credentials_exception
        # In a real app, decode JWT here
        email = "mock@example.com"  # Would come from token
        user = get_user
