"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Provide code examples for implementing a subscription system for publications, similar to the "Subscribe to our publications" feature on the Innodapter ApS website.
Generated: DETERMINISTIC_21685822281fa783
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_system.py
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, status
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('subscriptions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT,
            publication_types TEXT NOT NULL,
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Models
class SubscriptionRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    publication_types: List[str]

    @validator('publication_types')
    def validate_publication_types(cls, v):
        if not v:
            raise ValueError('At least one publication type must be selected')
        valid_types = ['newsletter', 'whitepapers', 'case_studies', 'blog_updates']
        for pub_type in v:
            if pub_type not in valid_types:
                raise ValueError(f'Invalid publication type: {pub_type}')
        return v

class SubscriptionResponse(BaseModel):
    id: int
    email: str
    name: Optional[str]
    publication_types: List[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

# FastAPI app
app = FastAPI(
    title="Publication Subscription System",
    description="API for managing publication subscriptions",
    version="1.0.0"
)

@app.post("/subscriptions/", response_model=SubscriptionResponse, status_code=status.HTTP_201_CREATED)
async def create_subscription(subscription: SubscriptionRequest):
    """
    Create a new subscription for publications.
    """
    try:
        conn = sqlite3.connect('subscriptions.db')
        cursor = conn.cursor()
        
        # Check if email already exists
        cursor.execute('SELECT id FROM subscriptions WHERE email = ?', (subscription.email,))
        if cursor.fetchone():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already subscribed"
            )
        
        # Insert new subscription
        publication_types_str = ','.join(subscription.publication_types)
        cursor.execute('''
            INSERT INTO subscriptions (email, name, publication_types)
            VALUES (?, ?, ?)
        ''', (subscription.email, subscription.name, publication_types_str))
        
        # Get the created subscription
        subscription_id = cursor.lastrowid
        cursor.execute('SELECT * FROM subscriptions WHERE id = ?', (subscription_id,))
        sub_data = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        if not sub_data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create subscription"
            )
            
        return {
            "id": sub_data[0],
            "email": sub_data[1],
            "name": sub_data[2],
            "publication_types": sub_data[3].split(','),
            "is_active": bool(sub_data[4]),
            "created_at": sub_data[5],
            "updated_at": sub_data[6]
        }
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

@app.get("/subscriptions/{email}", response_model=SubscriptionResponse)
async def get_subscription(email: EmailStr):
    """
    Get subscription details by email.
    """
    try:
        conn = sqlite3.connect('subscriptions.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM subscriptions WHERE email = ?', (email,))
        sub_data = cursor.fetchone()
        conn.close()
        
        if not sub_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscription not found"
            )
            
        return {
            "id": sub_data[0],
            "email": sub_data[1],
            "name": sub_data[2],
            "publication_types": sub_data[3].split(','),
            "is_active": bool(sub_data[4]),
            "created_at": sub_data[5],
            "updated_at": sub_data[6]
        }
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed"
        )

@app.patch("/subscriptions/{email}/unsubscribe", response_model=SubscriptionResponse)
async def unsubscribe(email: EmailStr):
    """
    Unsubscribe from publications (mark as inactive).
    """
    try:
        conn = sqlite3.connect('subscriptions.db')
        cursor = conn.cursor()
        
        # Check if subscription exists
        cursor.execute('SELECT id FROM subscriptions WHERE email = ?', (email,))
        if not cursor.fetchone():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscription not found"
            )
        
        # Update subscription
        cursor.execute('''
            UPDATE subscriptions 
            SET is_active = 0, updated_at = CURRENT_TIMESTAMP
            WHERE email = ?
        ''', (email,))
        
        # Get the updated subscription
        cursor.execute('SELECT * FROM subscriptions WHERE email = ?', (email,))
        sub_data = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        return {
            "id": sub_data[0],
            "email": sub_data[1],
            "name": sub_data[2],
            "publication_types": sub_data[3].split(','),
            "is_active": bool(sub_data[4]),
            "created_at": sub_data[5],
            "updated_at": sub_data[6]
        }
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
