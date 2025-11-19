"""
Generated Code Metadata:
========================
Original URL: https://omninetwork.org
Prompt: Create a Python script that handles user subscription to a newsletter, including validation for already subscribed users, inspired by the subscription functionality on Omni Network.
Generated: DETERMINISTIC_bc3f77e962d5b9b3
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, validator

app = FastAPI()

# In-memory database simulation
subscriptions_db = set()

class SubscriptionRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    preferences: Optional[Dict[str, Any]] = None

    @validator('name')
    def validate_name(cls, v):
        if v is not None and len(v.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return v

@app.post("/subscribe", status_code=status.HTTP_201_CREATED)
async def subscribe_user(subscription: SubscriptionRequest):
    """
    Subscribe a user to the newsletter.
    
    Args:
        subscription: SubscriptionRequest containing user details
        
    Returns:
        dict: Success message
        
    Raises:
        HTTPException: If user is already subscribed or validation fails
    """
    email = subscription.email.lower().strip()
    
    if email in subscriptions_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already subscribed"
        )
    
    subscriptions_db.add(email)
    
    return {
        "message": "Subscription successful",
        "email": email,
        "name": subscription.name,
        "preferences": subscription.preferences
    }

@app.get("/subscriptions")
async def list_subscriptions():
    """
    List all current subscriptions (for admin purposes)
    
    Returns:
        list: All subscribed emails
    """
    return list(subscriptions_db)

@app.delete("/unsubscribe/{email}")
async def unsubscribe_user(email: str):
    """
    Unsubscribe a user from the newsletter
    
    Args:
        email: Email to unsubscribe
        
    Returns:
        dict: Success message
        
    Raises:
        HTTPException: If email is not found in subscriptions
    """
    email = email.lower().strip()
    
    if email not in subscriptions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found in subscriptions"
        )
    
    subscriptions_db.remove(email)
    
    return {"message": "Successfully unsubscribed", "email": email}
```
