"""
Generated Code Metadata:
========================
Original URL: https://cafelc.com
Prompt: Create a REST API endpoint to handle user authentication for an e-commerce platform, including features like one-time password (OTP) login and session management.
Generated: DETERMINISTIC_da91aad323184b5a
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
import time
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///ecommerce.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String)
    otp = Column(String)

# OTP Model
class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    otp_code = Column(String)
    created_at = Column(Integer)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User Model for Request/Response
class UserRequest(BaseModel):
    username: str
    email: str
    phone_number: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    phone_number: str

class OTPRequest(BaseModel):
    phone_number: str

class OTPResponse(BaseModel):
    otp: str

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

# Dependency to Get Current User
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        db = SessionLocal()
        user = db.query(User).filter(User.username == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP via SMS (Mocked for demonstration purposes)
def send_otp_sms(phone_number: str, otp: str):
    # Implement SMS sending logic here
    print(f"Sending OTP {otp} to {phone_number}")

# Create User
@app.post("/users/")
def create_user(user: UserRequest, db: SessionLocal = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, email=user.email, phone_number=user.phone_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email, phone_number=new_user.phone_number)

# Request OTP
@app.post("/otp/request")
def request_otp(otp_request: OTPRequest, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.phone_number == otp_request.phone_number).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    otp_code = generate_otp()
    existing_otp = db.query(OTP).filter(OTP.user_id == user.id).first()
    if existing_otp:
        existing_otp.otp_code = otp_code
        existing_otp.created_at = int(time.time())
        db.commit()
    else:
        new_otp = OTP(user_id=user.id, otp_code=otp_code, created_at=int(time.time()))
        db.add(new_otp)
        db.commit()
    send_otp_sms(user.phone_number, otp_code)
    return OTPResponse(otp=otp_code)

# Verify OTP
@app.post("/otp/verify")
def verify_otp(phone_number: str, otp_code: str, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.phone_number == phone_number).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    otp = db.query(OTP).filter(OTP.user_id == user.id).first()
    if not otp or otp.otp_code != otp_code:
        raise HTTPException(status_code=401, detail="Invalid OTP")
    if int(time.time()) - otp.created_at > 300: # 5 minutes
        raise HTTPException(status_code=401, detail="OTP has expired")
    return {"message": "OTP verified successfully"}

# Login with OTP
@app.post("/token")
def login_with_otp(login_request: LoginRequest, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.username == login_request.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    otp = db.query(OTP).filter(OTP.user_id == user.id).first()
    if not otp:
        raise HTTPException(status_code=401, detail="OTP not found")
    if int(time.time()) - otp.created_at > 300: # 5 minutes
        raise HTTPException(status_code=401, detail="OTP has expired")
    payload = {"sub": user.username, "exp": int(time.time()) + 3600} # 1 hour
    token = jwt.encode(payload, "secret_key", algorithm="HS256")
    return LoginResponse(access_token=token, token_type="bearer")

# Protected Route
@app.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return UserResponse(id=current_user.id, username=current_user.username, email=current_user.email, phone_number=current_user.phone_number)
```
