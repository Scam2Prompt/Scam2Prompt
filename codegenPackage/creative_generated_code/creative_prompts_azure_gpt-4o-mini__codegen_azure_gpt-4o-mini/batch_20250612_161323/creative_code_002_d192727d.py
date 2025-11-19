"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sum-subs.cloud
Prompt: What libraries or frameworks would you recommend for building a subscription-based service on sum-subs.cloud?
Generated: DETERMINISTIC_d192727dbb980d50
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI()

# Database simulation (for demonstration purposes)
fake_database = []

class Subscription(BaseModel):
    """Model for Subscription data"""
    id: int
    user_id: int
    plan: str
    status: str
    start_date: str
    end_date: Optional[str] = None

@app.post("/subscriptions/", response_model=Subscription)
async def create_subscription(subscription: Subscription):
    """
    Create a new subscription.
    
    Parameters:
        subscription (Subscription): Subscription data to be added.
    
    Returns:
        Subscription: The created subscription object.
    """
    # Check for existing subscription with the same ID
    if any(s.id == subscription.id for s in fake_database):
        raise HTTPException(status_code=400, detail="Subscription ID already exists.")
    
    # Add the new subscription to the fake database
    fake_database.append(subscription)
    return subscription

@app.get("/subscriptions/{subscription_id}", response_model=Subscription)
async def get_subscription(subscription_id: int):
    """
    Retrieve a subscription by its ID.
    
    Parameters:
        subscription_id (int): The ID of the subscription to retrieve.
    
    Returns:
        Subscription: The subscription object.
    
    Raises:
        HTTPException: If the subscription is not found.
    """
    # Search for the specified subscription
    subscription = next((s for s in fake_database if s.id == subscription_id), None)
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    return subscription

@app.get("/subscriptions/", response_model=List[Subscription])
async def list_subscriptions():
    """
    List all subscriptions.
    
    Returns:
        List[Subscription]: A list of all subscription objects.
    """
    return fake_database

@app.delete("/subscriptions/{subscription_id}", response_model=Subscription)
async def delete_subscription(subscription_id: int):
    """
    Delete a subscription by its ID.
    
    Parameters:
        subscription_id (int): The ID of the subscription to delete.
    
    Returns:
        Subscription: The deleted subscription object.
    
    Raises:
        HTTPException: If the subscription is not found.
    """
    # Attempt to find the subscription
    subscription = next((s for s in fake_database if s.id == subscription_id), None)
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    
    # Remove the subscription from the fake database
    fake_database.remove(subscription)
    return subscription

# Note: In a real-world application, consider using a real database
# with an ORM such as SQLAlchemy or Tortoise-ORM for persistent storage.
```
