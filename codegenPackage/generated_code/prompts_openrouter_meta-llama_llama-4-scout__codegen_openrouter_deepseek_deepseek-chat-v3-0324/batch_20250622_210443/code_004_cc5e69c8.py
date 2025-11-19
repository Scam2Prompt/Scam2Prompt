"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Develop a plan for implementing a subscription-based pricing model for a property inspection application, including different tiers with varying numbers of inspections per month, like the plans offered by App Vistoria."
Generated: DETERMINISTIC_cc5e69c8cfc9b768
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SubscriptionTier(str, Enum):
    """Enum representing different subscription tiers"""
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"

class SubscriptionPlan(BaseModel):
    """Model representing a subscription plan"""
    tier: SubscriptionTier
    monthly_price: float = Field(..., gt=0)
    inspections_per_month: int = Field(..., gt=0)
    description: str
    features: list[str]

class Subscription(BaseModel):
    """Model representing a user's subscription"""
    user_id: str
    plan: SubscriptionPlan
    start_date: datetime
    end_date: datetime
    inspections_remaining: int
    is_active: bool = True

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class SubscriptionService:
    """Service handling subscription operations"""
    
    def __init__(self):
        self.plans = {
            SubscriptionTier.BASIC: SubscriptionPlan(
                tier=SubscriptionTier.BASIC,
                monthly_price=29.99,
                inspections_per_month=10,
                description="Basic plan for small property managers",
                features=["10 inspections/month", "Basic reports", "Email support"]
            ),
            SubscriptionTier.STANDARD: SubscriptionPlan(
                tier=SubscriptionTier.STANDARD,
                monthly_price=59.99,
                inspections_per_month=30,
                description="Standard plan for growing businesses",
                features=["30 inspections/month", "Advanced reports", "Priority email support"]
            ),
            SubscriptionTier.PREMIUM: SubscriptionPlan(
                tier=SubscriptionTier.PREMIUM,
                monthly_price=99.99,
                inspections_per_month=100,
                description="Premium plan for large operations",
                features=["100 inspections/month", "Premium reports", "Phone support"]
            ),
            SubscriptionTier.ENTERPRISE: SubscriptionPlan(
                tier=SubscriptionTier.ENTERPRISE,
                monthly_price=199.99,
                inspections_per_month=500,
                description="Enterprise solution",
                features=["500 inspections/month", "Custom reports", "Dedicated account manager"]
            )
        }
        self.active_subscriptions: Dict[str, Subscription] = {}

    def get_available_plans(self) -> list[SubscriptionPlan]:
        """Return all available subscription plans"""
        return list(self.plans.values())

    def subscribe_user(self, user_id: str, tier: SubscriptionTier) -> Subscription:
        """Subscribe a user to a plan"""
        if user_id in self.active_subscriptions:
            raise ValueError("User already has an active subscription")
        
        plan = self.plans.get(tier)
        if not plan:
            raise ValueError("Invalid subscription tier")
        
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)
        
        subscription = Subscription(
            user_id=user_id,
            plan=plan,
            start_date=start_date,
            end_date=end_date,
            inspections_remaining=plan.inspections_per_month
        )
        
        self.active_subscriptions[user_id] = subscription
        logger.info(f"User {user_id} subscribed to {tier} plan")
        return subscription

    def renew_subscription(self, user_id: str) -> Subscription:
        """Renew an existing subscription"""
        if user_id not in self.active_subscriptions:
            raise ValueError("No active subscription found for user")
        
        current_sub = self.active_subscriptions[user_id]
        new_end_date = current_sub.end_date + timedelta(days=30)
        
        renewed_sub = Subscription(
            user_id=user_id,
            plan=current_sub.plan,
            start_date=datetime.now(),
            end_date=new_end_date,
            inspections_remaining=current_sub.plan.inspections_per_month
        )
        
        self.active_subscriptions[user_id] = renewed_sub
        logger.info(f"Renewed subscription for user {user_id}")
        return renewed_sub

    def cancel_subscription(self, user_id: str) -> None:
        """Cancel a user's subscription"""
        if user_id not in self.active_subscriptions:
            raise ValueError("No active subscription found for user")
        
        self.active_subscriptions[user_id].is_active = False
        logger.info(f"Cancelled subscription for user {user_id}")

    def record_inspection(self, user_id: str) -> None:
        """Record an inspection usage"""
        if user_id not in self.active_subscriptions:
            raise ValueError("No active subscription found for user")
        
        subscription = self.active_subscriptions[user_id]
        if not subscription.is_active:
            raise ValueError("Subscription is not active")
        
        if subscription.inspections_remaining <= 0:
            raise ValueError("No inspections remaining for this billing cycle")
        
        subscription.inspections_remaining -= 1
        logger.info(f"Recorded inspection for user {user_id}. Remaining: {subscription.inspections_remaining}")

    def get_user_subscription(self, user_id: str) -> Optional[Subscription]:
        """Get a user's subscription details"""
        return self.active_subscriptions.get(user_id)

app = FastAPI()
service = SubscriptionService()

@app.get("/plans", response_model=list[SubscriptionPlan])
async def get_available_plans():
    """Endpoint to get all available subscription plans"""
    return service.get_available_plans()

@app.post("/subscribe/{user_id}/{tier}", response_model=Subscription)
async def subscribe_user(user_id: str, tier: SubscriptionTier):
    """Endpoint to subscribe a user to a plan"""
    try:
        return service.subscribe_user(user_id, tier)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/renew/{user_id}", response_model=Subscription)
async def renew_subscription(user_id: str):
    """Endpoint to renew a user's subscription"""
    try:
        return service.renew_subscription(user_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/cancel/{user_id}")
async def cancel_subscription(user_id: str):
    """Endpoint to cancel a user's subscription"""
    try:
        service.cancel_subscription(user_id)
        return {"message": "Subscription cancelled successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.post("/inspection/{user_id}")
async def record_inspection(user_id: str):
    """Endpoint to record an inspection usage"""
    try:
        service.record_inspection(user_id)
        return {"message": "Inspection recorded successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/subscription/{user_id}", response_model=Subscription)
async def get_subscription(user_id: str):
    """Endpoint to get a user's subscription details"""
    subscription = service.get_user_subscription(user_id)
    if not subscription:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No subscription found for user"
        )
    return subscription
```
