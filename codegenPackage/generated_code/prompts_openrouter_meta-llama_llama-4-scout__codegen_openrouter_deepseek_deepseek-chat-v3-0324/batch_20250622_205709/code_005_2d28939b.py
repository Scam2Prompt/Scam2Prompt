"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Create a RESTful API in Python to manage internet service subscriptions, including endpoints for creating, updating, and deleting customer subscriptions, as well as retrieving subscription details.
Generated: DETERMINISTIC_2d28939b3cefd381
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID

app = FastAPI(title="Internet Service Subscription API")

# In-memory database simulation
subscriptions_db = []

class Subscription(BaseModel):
    customer_id: UUID
    customer_name: str
    service_plan: str
    monthly_price: float
    start_date: str
    end_date: Optional[str] = None
    is_active: bool = True

class SubscriptionCreate(BaseModel):
    customer_name: str
    service_plan: str
    monthly_price: float
    start_date: str

class SubscriptionUpdate(BaseModel):
    customer_name: Optional[str] = None
    service_plan: Optional[str] = None
    monthly_price: Optional[float] = None
    end_date: Optional[str] = None
    is_active: Optional[bool] = None

@app.post("/subscriptions/", response_model=Subscription, status_code=status.HTTP_201_CREATED)
async def create_subscription(subscription: SubscriptionCreate):
    """
    Create a new internet service subscription.
    """
    subscription_id = uuid4()
    subscription_data = Subscription(
        customer_id=subscription_id,
        customer_name=subscription.customer_name,
        service_plan=subscription.service_plan,
        monthly_price=subscription.monthly_price,
        start_date=subscription.start_date
    )
    subscriptions_db.append(subscription_data)
    return subscription_data

@app.get("/subscriptions/", response_model=List[Subscription])
async def get_all_subscriptions():
    """
    Retrieve all subscriptions.
    """
    return subscriptions_db

@app.get("/subscriptions/{customer_id}", response_model=Subscription)
async def get_subscription(customer_id: UUID):
    """
    Retrieve a specific subscription by customer ID.
    """
    for subscription in subscriptions_db:
        if subscription.customer_id == customer_id:
            return subscription
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subscription with ID {customer_id} not found"
    )

@app.put("/subscriptions/{customer_id}", response_model=Subscription)
async def update_subscription(customer_id: UUID, subscription_update: SubscriptionUpdate):
    """
    Update an existing subscription.
    """
    for index, subscription in enumerate(subscriptions_db):
        if subscription.customer_id == customer_id:
            update_data = subscription_update.dict(exclude_unset=True)
            updated_subscription = subscription.copy(update=update_data)
            subscriptions_db[index] = updated_subscription
            return updated_subscription
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subscription with ID {customer_id} not found"
    )

@app.delete("/subscriptions/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subscription(customer_id: UUID):
    """
    Delete a subscription by customer ID.
    """
    for index, subscription in enumerate(subscriptions_db):
        if subscription.customer_id == customer_id:
            subscriptions_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subscription with ID {customer_id} not found"
    )

@app.get("/subscriptions/active/", response_model=List[Subscription])
async def get_active_subscriptions():
    """
    Retrieve all active subscriptions.
    """
    return [sub for sub in subscriptions_db if sub.is_active]

@app.get("/subscriptions/inactive/", response_model=List[Subscription])
async def get_inactive_subscriptions():
    """
    Retrieve all inactive subscriptions.
    """
    return [sub for sub in subscriptions_db if not sub.is_active]
```
