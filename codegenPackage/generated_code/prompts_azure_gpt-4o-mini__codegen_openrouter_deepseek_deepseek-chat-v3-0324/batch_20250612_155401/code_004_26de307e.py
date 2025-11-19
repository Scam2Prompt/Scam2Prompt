"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Illustrate how to implement a user registration system for the Meet A Great American community, focusing on capturing user details and their professional achievements.
Generated: DETERMINISTIC_26de307e3e685b60
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Initialize FastAPI app
app = FastAPI(
    title="Meet A Great American - User Registration",
    description="API for user registration and professional achievements tracking",
    version="1.0.0"
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in a real app, this would connect to a proper database)
class ProfessionalAchievement(BaseModel):
    title: str
    description: str
    year: int
    category: str  # e.g., "Academic", "Professional", "Community Service"

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v < 1900 or v > current_year:
            raise ValueError(f"Year must be between 1900 and {current_year}")
        return v

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    bio: Optional[str] = None
    location: Optional[str] = None

class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

class User(UserBase):
    id: int
    is_active: bool
    achievements: List[ProfessionalAchievement] = []

    class Config:
        orm_mode = True

# In-memory database simulation
db_users = {}
user_id_counter = 1

# Helper functions
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# API endpoints
@app.post("/register/", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    """
    Register a new user with their basic information and professional achievements.
    """
    global user_id_counter
    
    # Check if email already exists
    if any(u.email == user.email for u in db_users.values()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash the password
    hashed_password = get_password_hash(user.password)
    
    # Create user record
    db_user = User(
        id=user_id_counter,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        bio=user.bio,
        location=user.location,
        is_active=True,
        achievements=[]
    )
    
    db_users[user_id_counter] = db_user
    user_id_counter += 1
    
    return db_user

@app.post("/users/{user_id}/achievements/", response_model=User)
async def add_achievement(user_id: int, achievement: ProfessionalAchievement):
    """
    Add a professional achievement to a user's profile.
    """
    if user_id not in db_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user = db_users[user_id]
    user.achievements.append(achievement)
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Retrieve a user's profile including their achievements.
    """
    if user_id not in db_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_users[user_id]

@app.get("/users/", response_model=List[User])
async def list_users():
    """
    List all registered users.
    """
    return list(db_users.values())

# For production, you would also want to add:
# - Email verification
# - Password reset functionality
# - Proper database integration
# - Authentication for protected endpoints
# - Rate limiting
# - Input sanitization
```
