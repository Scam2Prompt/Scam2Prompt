"""
Generated Code Metadata:
========================
Original URL: https://pokemoney.info
Prompt: Explain how to implement a secure user authentication system for the UW99 online casino application.
Generated: DETERMINISTIC_55007f0a4c0d1762
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# UW99 Online Casino - Secure Authentication System

```python
import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="UW99 Casino Authentication API",
    description="Secure authentication system for UW99 Online Casino",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

# Database configuration
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client.uw99_casino
users_collection = db.users
users_collection.create_index("email", unique=True)

# Security configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password complexity requirements
MIN_PASSWORD_LENGTH = 8
REQUIRE_SPECIAL_CHAR = True
REQUIRE_UPPERCASE = True
REQUIRE_NUMBER = True

# Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
        if REQUIRE_UPPERCASE and not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if REQUIRE_NUMBER and not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one number")
        if REQUIRE_SPECIAL_CHAR and not any(not c.isalnum() for c in v):
            raise ValueError("Password must contain at least one special character")
        return v

class UserInDB(UserBase):
    hashed_password: str
    disabled: bool = False
    last_login: Optional[datetime] = None
    failed_login_attempts: int = 0
    account_locked: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hashed version"""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_password_hash(password: str) -> str:
    """Generate a bcrypt hash for the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current authenticated user from JWT token"""
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
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = users_collection.find_one({"email": token_data.email})
    if user is None:
        raise credentials_exception
    return UserInDB(**user)

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    """Check if current user is active"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    if current_user.account_locked:
        raise HTTPException(status_code=400, detail="Account locked due to too many failed attempts")
    return current_user

# API Endpoints
@app.post("/register", response_model=UserBase)
async def register_user(user: UserCreate):
    """Register a new user"""
    try:
        hashed_password = get_password_hash(user.password)
        db_user = {
            "email": user.email,
            "full_name": user.full_name,
            "hashed_password": hashed_password,
            "disabled": False,
            "failed_login_attempts": 0,
            "account_locked": False
        }
        
        result = users_collection.insert_one(db_user)
        if result.inserted_id:
            return UserBase(**user.dict())
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate user and return access token"""
    user = users_collection.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = UserInDB(**user)
    
    # Check if account is locked
    if user.account_locked:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account locked due to too many failed attempts"
        )
    
    # Verify password
    if not verify_password(form_data.password, user.hashed_password):
        # Increment failed attempts
        users_collection.update_one(
            {"email": form_data.username},
            {"$inc": {"failed_login_attempts": 1}}
        )
        
        # Lock account after 5 failed attempts
        if user.failed_login_attempts + 1 >= 5:
            users_collection.update_one(
                {"email": form_data.username},
                {"$set": {"account_locked": True}}
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account locked due to too many failed attempts"
            )
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Reset failed attempts on successful login
    users_collection.update_one(
        {"email": form_data.username},
        {
            "$set": {
                "failed_login_attempts": 0,
                "last_login": datetime.utcnow()
            }
        }
    )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: UserBase = Depends(get_current_active_user)):
    """Get current user details"""
    return current_user

# Security middleware (example - implement according to your infrastructure)
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response
```

This implementation includes:

1. Secure password storage with bcrypt hashing
2. JWT token-based authentication
3. Password complexity requirements
4. Account lockout after multiple failed attempts
5. Secure HTTP headers
6
