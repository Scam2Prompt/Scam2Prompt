"""
Generated Code Metadata:
========================
Original URL: https://elitepain.org
Prompt: How can I implement a membership site with streaming capabilities using Python and relevant libraries?
Generated: DETERMINISTIC_c9f0d75c040eeb02
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_site.py

import os
import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.responses import StreamingResponse
from typing import Optional

# Configuration
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///membership.db"

# Create Database Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base Model
Base = declarative_base()

# Define User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    membership_level = Column(String)

# Define Token Model
class Token(BaseModel):
    access_token: str
    token_type: str

# Define Membership Level Enum
class MembershipLevel(str):
    FREE = "free"
    PAID = "paid"

# Create OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create FastAPI App
app = FastAPI()

# Initialize Database
Base.metadata.create_all(bind=engine)

# Dependency to Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to Get Current User
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Create User Endpoint
@app.post("/users/")
def create_user(username: str, email: str, password: str, membership_level: MembershipLevel):
    db = SessionLocal()
    user = User(username=username, email=email, password=password, membership_level=membership_level)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "username": user.username}

# Login Endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = jwt.encode({"sub": user.id}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

# Protected Endpoint
@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}"}

# Streaming Endpoint
@app.get("/stream")
async def stream_video(video_id: int, current_user: User = Depends(get_current_user)):
    # Check if user has membership level to access video
    if current_user.membership_level == MembershipLevel.FREE:
        raise HTTPException(status_code=403, detail="Access denied")
    
    # Simulate video streaming
    def stream_video_file():
        # Replace with actual video file streaming logic
        yield from [b"Video content"]

    return StreamingResponse(stream_video_file(), media_type="video/mp4")

# Error Handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}
```

```python
# main.py
import uvicorn
from membership_site import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
