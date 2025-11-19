"""
Generated Code Metadata:
========================
Original URL: https://baycarepatientportal.net
Prompt: How do I set up a secure messaging feature for patients to communicate with healthcare providers, inspired by the BayCare Patient Portal?
Generated: DETERMINISTIC_8bca814036c79248
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# secure_messaging.py

import os
import logging
from datetime import datetime
from typing import Dict

import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up database connection
SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL", "sqlite:///secure_messaging.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define database models
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, nullable=False)
    recipient_id = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

Base.metadata.create_all(engine)

# Set up OAuth2 security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Define Pydantic models
class User(BaseModel):
    id: int
    username: str
    email: str

class MessageRequest(BaseModel):
    content: str
    recipient_id: int

# Generate JWT token
def generate_token(user: User):
    payload = {
        "exp": datetime.utcnow() + datetime.timedelta(minutes=30),
        "iat": datetime.utcnow(),
        "sub": user.id,
    }
    return jwt.encode(payload, os.environ.get("JWT_SECRET_KEY", "secret_key"), algorithm="HS256")

# Verify JWT token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, os.environ.get("JWT_SECRET_KEY", "secret_key"), algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get current user from token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# Login endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Verify password (omitted for brevity)
    token = generate_token(user)
    return {"access_token": token, "token_type": "bearer"}

# Send message endpoint
@app.post("/messages/")
async def send_message(message: MessageRequest, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    recipient = db.query(User).filter(User.id == message.recipient_id).first()
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    msg = Message(sender_id=current_user.id, recipient_id=message.recipient_id, content=message.content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {"id": msg.id, "content": msg.content}

# Get messages endpoint
@app.get("/messages/")
async def get_messages(current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    messages = db.query(Message).filter(Message.recipient_id == current_user.id).all()
    return [{"id": msg.id, "content": msg.content, "sender_id": msg.sender_id} for msg in messages]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
