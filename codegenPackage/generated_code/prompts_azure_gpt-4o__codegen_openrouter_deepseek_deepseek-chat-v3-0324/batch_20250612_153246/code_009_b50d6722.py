"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Create a REST API that allows users to subscribe to newsletters like the one offered by Eye Magazine, ensuring compliance with privacy regulations.
Generated: DETERMINISTIC_b50d6722c3d06fae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional
import sqlite3
import logging
from datetime import datetime
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Newsletter Subscription API",
    description="API for managing newsletter subscriptions with privacy compliance",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database setup
def get_db():
    conn = sqlite3.connect('newsletter.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with sqlite3.connect('newsletter.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT,
                is_active BOOLEAN DEFAULT 1,
                subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                unsubscribed_at TIMESTAMP,
                consent_given_at TIMESTAMP,
                ip_address TEXT,
                source TEXT
            )
        ''')
        conn.commit()

# Models
class SubscriberCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    consent_given: bool
    ip_address: Optional[str] = None
    source: Optional[str] = None

class SubscriberResponse(BaseModel):
    email: EmailStr
    name: Optional[str]
    is_active: bool
    subscribed_at: datetime
    consent_given_at: datetime

class UnsubscribeRequest(BaseModel):
    email: EmailStr

# Helper functions
def validate_email_domain(email: str) -> bool:
    """Check if email domain is valid and not disposable"""
    domain = email.split('@')[-1]
    disposable_domains = ["mailinator.com", "temp-mail.org", "guerrillamail.com"]
    return domain not in disposable_domains

def log_subscription_attempt(email: str, ip: str, success: bool):
    """Log subscription attempts for security and auditing"""
    logger.info(f"Subscription attempt - Email: {email}, IP: {ip}, Success: {success}")

# API Endpoints
@app.on_event("startup")
async def startup_event():
    init_db()

@app.post("/subscribe", response_model=SubscriberResponse, status_code=status.HTTP_201_CREATED)
async def subscribe(subscriber: SubscriberCreate, db: sqlite3.Connection = Depends(get_db)):
    """Subscribe a new user to the newsletter"""
    if not subscriber.consent_given:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Consent must be given to subscribe"
        )

    if not validate_email_domain(subscriber.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Disposable email addresses are not allowed"
        )

    try:
        cursor = db.cursor()
        current_time = datetime.utcnow().isoformat()
        
        cursor.execute('''
            INSERT INTO subscribers (email, name, consent_given_at, ip_address, source)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
                name = excluded.name,
                is_active = 1,
                unsubscribed_at = NULL,
                consent_given_at = excluded.consent_given_at,
                ip_address = excluded.ip_address,
                source = excluded.source
        ''', (
            subscriber.email,
            subscriber.name,
            current_time,
            subscriber.ip_address,
            subscriber.source
        ))
        
        db.commit()
        
        # Get the newly created/updated subscriber
        subscriber_data = cursor.execute(
            'SELECT email, name, is_active, subscribed_at, consent_given_at FROM subscribers WHERE email = ?',
            (subscriber.email,)
        ).fetchone()
        
        log_subscription_attempt(subscriber.email, subscriber.ip_address, True)
        return dict(subscriber_data)
    
    except sqlite3.Error as e:
        logger.error(f"Database error during subscription: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process subscription"
        )

@app.post("/unsubscribe", status_code=status.HTTP_200_OK)
async def unsubscribe(request: UnsubscribeRequest, db: sqlite3.Connection = Depends(get_db)):
    """Unsubscribe a user from the newsletter"""
    try:
        cursor = db.cursor()
        current_time = datetime.utcnow().isoformat()
        
        result = cursor.execute(
            'UPDATE subscribers SET is_active = 0, unsubscribed_at = ? WHERE email = ? AND is_active = 1',
            (current_time, request.email)
        )
        
        if result.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscriber not found or already unsubscribed"
            )
        
        db.commit()
        return {"message": "Successfully unsubscribed"}
    
    except sqlite3.Error as e:
        logger.error(f"Database error during unsubscription: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process unsubscription"
        )

@app.get("/subscribers/{email}", response_model=SubscriberResponse)
async def get_subscriber(email: EmailStr, db: sqlite3.Connection = Depends(get_db)):
    """Get subscriber details"""
    try:
        subscriber = db.execute(
            'SELECT email, name, is_active, subscribed_at, consent_given_at FROM subscribers WHERE email = ?',
            (email,)
        ).fetchone()
        
        if not subscriber:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscriber not found"
            )
            
        return dict(subscriber)
    
    except sqlite3.Error as e:
        logger.error(f"Database error fetching subscriber: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch subscriber"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
