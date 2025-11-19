"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Create an API integration to allow users to sign up for updates and receive notifications about the VEMP Hunt campaign.
Generated: DETERMINISTIC_6f06708e1378c1c4
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional
import logging
import os
import uvicorn
from email.message import EmailMessage
import smtplib

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up database connection
SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL", "sqlite:///vemp_hunt.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define database model
class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    subscribed = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

# Set up FastAPI app
app = FastAPI()

# Set up email configuration
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
FROM_EMAIL = os.environ.get("FROM_EMAIL", "your-email@gmail.com")
PASSWORD = os.environ.get("PASSWORD", "your-password")

# Define Pydantic model for user sign up
class UserSignUp(BaseModel):
    email: str

# Define Pydantic model for user subscription
class UserSubscription(BaseModel):
    subscribed: bool

# Create a new user or update existing user's subscription
@app.post("/sign_up", response_model=JSONResponse)
async def sign_up(user_sign_up: UserSignUp):
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.email == user_sign_up.email).first()
        if user:
            user.subscribed = True
            db.commit()
            db.refresh(user)
        else:
            new_user = User(email=user_sign_up.email)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        return JSONResponse(content={"message": "Signed up successfully"}, status_code=201)
    except Exception as e:
        logger.error(f"Error signing up user: {e}")
        raise HTTPException(status_code=500, detail="Failed to sign up user")

# Update user's subscription
@app.patch("/subscription", response_model=JSONResponse)
async def update_subscription(user_subscription: UserSubscription, user_email: str):
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.email == user_email).first()
        if user:
            user.subscribed = user_subscription.subscribed
            db.commit()
            db.refresh(user)
            return JSONResponse(content={"message": "Subscription updated successfully"}, status_code=200)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        logger.error(f"Error updating subscription: {e}")
        raise HTTPException(status_code=500, detail="Failed to update subscription")

# Send notifications to subscribed users
@app.post("/send_notifications", response_model=JSONResponse)
async def send_notifications(request: Request):
    try:
        db = SessionLocal()
        users = db.query(User).filter(User.subscribed == True).all()
        msg = EmailMessage()
        msg.set_content("This is a notification about the VEMP Hunt campaign")
        msg["Subject"] = "VEMP Hunt Campaign Notification"
        msg["From"] = FROM_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(FROM_EMAIL, PASSWORD)
            for user in users:
                msg["To"] = user.email
                smtp.send_message(msg)
        return JSONResponse(content={"message": "Notifications sent successfully"}, status_code=200)
    except Exception as e:
        logger.error(f"Error sending notifications: {e}")
        raise HTTPException(status_code=500, detail="Failed to send notifications")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
