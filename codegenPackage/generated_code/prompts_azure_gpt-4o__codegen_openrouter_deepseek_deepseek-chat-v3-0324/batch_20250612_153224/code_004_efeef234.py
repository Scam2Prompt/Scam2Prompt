"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Write code to automate the signup process for a newsletter similar to the Études Newsletter, ensuring users can easily subscribe and access thought-provoking articles and design insights.
Generated: DETERMINISTIC_efeef23493790f9d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Dict
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, validator
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Études Newsletter Signup API",
    description="API for subscribing to the Études Newsletter",
    version="1.0.0"
)

# Database setup
DATABASE_NAME = "newsletter.db"

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Pydantic models
class Subscriber(BaseModel):
    email: EmailStr
    name: Optional[str] = None

    @validator('name')
    def name_validator(cls, v):
        if v and len(v) > 100:
            raise ValueError("Name must be less than 100 characters")
        return v

class SubscriptionResponse(BaseModel):
    message: str
    subscriber: Subscriber

# Email configuration
class EmailConfig:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    FROM_EMAIL = os.getenv("FROM_EMAIL", "newsletter@etudes.com")
    WELCOME_SUBJECT = "Welcome to Études Newsletter"

# Helper functions
def send_welcome_email(subscriber: Subscriber):
    """Send welcome email to new subscriber."""
    if not all([EmailConfig.SMTP_SERVER, EmailConfig.SMTP_USERNAME, EmailConfig.SMTP_PASSWORD]):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email configuration incomplete"
        )

    message = MIMEMultipart()
    message["From"] = EmailConfig.FROM_EMAIL
    message["To"] = subscriber.email
    message["Subject"] = EmailConfig.WELCOME_SUBJECT

    body = f"""
    <html>
        <body>
            <h1>Welcome to Études Newsletter, {subscriber.name or 'Subscriber'}!</h1>
            <p>Thank you for subscribing to our newsletter. You'll now receive thought-provoking articles and design insights directly to your inbox.</p>
            <p>We're excited to have you as part of our community!</p>
            <p>Best regards,<br>The Études Team</p>
        </body>
    </html>
    """
    message.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT) as server:
            server.starttls()
            server.login(EmailConfig.SMTP_USERNAME, EmailConfig.SMTP_PASSWORD)
            server.send_message(message)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send welcome email: {str(e)}"
        )

def is_email_registered(email: str) -> bool:
    """Check if email is already registered."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM subscribers WHERE email = ? AND is_active = 1", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def add_subscriber(subscriber: Subscriber) -> Dict:
    """Add new subscriber to database."""
    if is_email_registered(subscriber.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already subscribed"
        )

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO subscribers (email, name) VALUES (?, ?)",
            (subscriber.email, subscriber.name)
        )
        conn.commit()
        return {"email": subscriber.email, "name": subscriber.name}
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    finally:
        conn.close()

# API endpoints
@app.post("/subscribe", response_model=SubscriptionResponse, status_code=status.HTTP_201_CREATED)
async def subscribe(subscriber: Subscriber):
    """Subscribe to the Études Newsletter."""
    try:
        subscriber_data = add_subscriber(subscriber)
        send_welcome_email(subscriber)
        return {
            "message": "Successfully subscribed to Études Newsletter",
            "subscriber": subscriber_data
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )

@app.get("/subscribers", status_code=status.HTTP_200_OK)
async def get_subscribers():
    """Get list of all active subscribers (for admin purposes)."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT email, name, subscribed_at FROM subscribers WHERE is_active = 1")
        subscribers = cursor.fetchall()
        return {
            "subscribers": [
                {"email": row[0], "name": row[1], "subscribed_at": row[2]}
                for row in subscribers
            ]
        }
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )
    finally:
        conn.close()

# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred"},
    )

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
