"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Illustrate how to implement a user authentication system for a cleaning service platform, ensuring trust and security like Maid in Heaven's vetted cleaning staff.
Generated: DETERMINISTIC_9e5c9b5340416b48
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from passlib.context import CryptContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Security configurations
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in-memory for illustration)
fake_users_db = {}

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str
    ssn_last_four: str  # For background checks
    phone_number: str
    
    @validator('ssn_last_four')
    def validate_ssn(cls, v):
        if not v.isdigit() or len(v) != 4:
            raise ValueError("SSN last four must be 4 digits")
        return v
    
    @validator('phone_number')
    def validate_phone(cls, v):
        if not v.replace('-', '').isdigit() or len(v.replace('-', '')) != 10:
            raise ValueError("Phone number must be 10 digits")
        return v

class User(UserBase):
    id: str
    is_verified: bool = False
    is_active: bool = True

class UserInDB(User):
    hashed_password: str
    ssn_last_four: str
    phone_number: str

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

def get_user(db, email: str):
    if email in db:
        user_dict = db[email]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, email: str, password: str):
    user = get_user(fake_db, email)
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
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API endpoints
@app.post("/register", response_model=User)
async def register(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # In a real system, we would perform background checks here
    # For demo, we just mark as verified
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        id=str(len(fake_users_db) + 1),
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        ssn_last_four=user.ssn_last_four,
        phone_number=user.phone_number,
        is_verified=True
    )
    fake_users_db[user.email] = db_user.dict()
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account not verified",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Background check verification endpoint (admin-only in real system)
@app.post("/verify/{user_email}")
async def verify_user(user_email: str, current_user: User = Depends(get_current_active_user)):
    if user_email not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # In a real system, this would require admin privileges
    fake_users_db[user_email]["is_verified"] = True
    return {"message": f"User {user_email} verified successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
