"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Create an API that allows users to subscribe to a church newsletter, inspired by the subscription feature on the First Baptist Church website.
Generated: DETERMINISTIC_4e2679f8cc5e3e01
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Church Newsletter Subscription API",
    description="API for subscribing to First Baptist Church newsletter",
    version="1.0.0"
)

# Database setup
def init_db():
    conn = sqlite3.connect('newsletter.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            first_name TEXT,
            last_name TEXT,
            is_active BOOLEAN DEFAULT 1,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Pydantic models
class Subscriber(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class SubscriberResponse(Subscriber):
    id: int
    is_active: bool
    subscribed_at: datetime

    class Config:
        orm_mode = True

# Database connection helper
def get_db():
    conn = sqlite3.connect('newsletter.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    try:
        yield conn
    finally:
        conn.close()

# Error classes
class EmailAlreadyExistsError(Exception):
    pass

# API endpoints
@app.post("/subscribe", response_model=SubscriberResponse, status_code=status.HTTP_201_CREATED)
async def subscribe(subscriber: Subscriber):
    """
    Subscribe a new user to the church newsletter.
    """
    try:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()

        # Check if email already exists
        cursor.execute('SELECT email FROM subscribers WHERE email = ?', (subscriber.email,))
        if cursor.fetchone():
            raise EmailAlreadyExistsError("Email already subscribed")

        # Insert new subscriber
        cursor.execute('''
            INSERT INTO subscribers (email, first_name, last_name)
            VALUES (?, ?, ?)
        ''', (subscriber.email, subscriber.first_name, subscriber.last_name))
        conn.commit()

        # Get the newly created subscriber
        cursor.execute('''
            SELECT * FROM subscribers WHERE id = ?
        ''', (cursor.lastrowid,))
        new_subscriber = cursor.fetchone()
        conn.close()

        logger.info(f"New subscriber added: {subscriber.email}")
        return dict(new_subscriber)
    
    except EmailAlreadyExistsError as e:
        logger.warning(f"Subscription attempt with existing email: {subscriber.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error subscribing user: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@app.get("/subscribers", response_model=List[SubscriberResponse])
async def list_subscribers(active_only: bool = True):
    """
    List all newsletter subscribers.
    Optionally filter only active subscribers (default).
    """
    try:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()

        if active_only:
            cursor.execute('SELECT * FROM subscribers WHERE is_active = 1')
        else:
            cursor.execute('SELECT * FROM subscribers')

        subscribers = cursor.fetchall()
        conn.close()
        return [dict(subscriber) for subscriber in subscribers]
    
    except Exception as e:
        logger.error(f"Error listing subscribers: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@app.post("/unsubscribe/{email}", status_code=status.HTTP_200_OK)
async def unsubscribe(email: EmailStr):
    """
    Unsubscribe a user from the newsletter by email.
    """
    try:
        conn = sqlite3.connect('newsletter.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE subscribers
            SET is_active = 0
            WHERE email = ?
        ''', (email,))

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email not found"
            )

        conn.commit()
        conn.close()
        logger.info(f"User unsubscribed: {email}")
        return {"message": "Successfully unsubscribed"}
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error unsubscribing user {email}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy"}
```
