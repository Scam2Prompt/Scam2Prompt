"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Suggest a code snippet for implementing a subscription model for a newsletter like The Infinite Game, aimed at self-improvement and entrepreneurship.
Generated: DETERMINISTIC_6e9495f3cbe3c5b4
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
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
    title="The Infinite Game Newsletter Subscription API",
    description="API for managing subscriptions to The Infinite Game newsletter",
    version="1.0.0"
)

# Database setup
def get_db():
    conn = sqlite3.connect('newsletter.db')
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
                subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT TRUE,
                subscription_type TEXT DEFAULT 'free'
            )
        ''')
        conn.commit()

# Models
class Subscriber(BaseModel):
    email: EmailStr
    name: str = None
    subscription_type: str = 'free'

class SubscriptionResponse(BaseModel):
    message: str
    subscriber: Subscriber

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()
    logger.info("Database initialized")

# Endpoints
@app.post("/subscribe", response_model=SubscriptionResponse)
async def subscribe(subscriber: Subscriber, conn: sqlite3.Connection = Depends(get_db)):
    """
    Subscribe a new user to the newsletter.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO subscribers (email, name, subscription_type)
            VALUES (?, ?, ?)
        ''', (subscriber.email, subscriber.name, subscriber.subscription_type))
        conn.commit()
        
        logger.info(f"New subscriber added: {subscriber.email}")
        return {
            "message": "Successfully subscribed to The Infinite Game newsletter!",
            "subscriber": subscriber
        }
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="This email is already subscribed."
        )
    except Exception as e:
        logger.error(f"Error subscribing user: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your subscription."
        )

@app.get("/subscribers", response_model=List[Subscriber])
async def get_subscribers(active: bool = True, conn: sqlite3.Connection = Depends(get_db)):
    """
    Get list of all active subscribers.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT email, name, subscription_type 
            FROM subscribers 
            WHERE is_active = ?
        ''', (active,))
        subscribers = [
            Subscriber(email=row[0], name=row[1], subscription_type=row[2])
            for row in cursor.fetchall()
        ]
        return subscribers
    except Exception as e:
        logger.error(f"Error fetching subscribers: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching subscribers."
        )

@app.post("/unsubscribe/{email}")
async def unsubscribe(email: EmailStr, conn: sqlite3.Connection = Depends(get_db)):
    """
    Unsubscribe a user from the newsletter.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE subscribers 
            SET is_active = FALSE 
            WHERE email = ?
        ''', (email,))
        
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Email not found in our subscription list."
            )
            
        conn.commit()
        logger.info(f"User unsubscribed: {email}")
        return {"message": "You have been successfully unsubscribed."}
    except Exception as e:
        logger.error(f"Error unsubscribing user: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your unsubscribe request."
        )

# Run with: uvicorn main:app --reload
```
