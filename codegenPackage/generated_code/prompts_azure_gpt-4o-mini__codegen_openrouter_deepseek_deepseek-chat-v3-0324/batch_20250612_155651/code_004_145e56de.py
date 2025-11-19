"""
Generated Code Metadata:
========================
Original URL: https://a.aciumreward.com
Prompt: Suggest best practices for developing an API for a rewards management system based on Acium Reward's functionalities.
Generated: DETERMINISTIC_145e56de1e3cc161
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_api.py
"""
API for a rewards management system inspired by Acium Reward's functionalities.
This module provides endpoints to manage rewards, users, and transactions.
"""

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Rewards Management API",
    description="API for managing user rewards and transactions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Database simulation
rewards_db = []
users_db = []
transactions_db = []

# Models
class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    points_balance: int = 0
    tier: str = "basic"
    created_at: datetime = Field(default_factory=datetime.now)

class Reward(BaseModel):
    reward_id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    points_required: int
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

class Transaction(BaseModel):
    transaction_id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    points: int
    type: str  # 'earn' or 'redeem'
    reward_id: Optional[UUID] = None
    timestamp: datetime = Field(default_factory=datetime.now)

# Helper functions
def get_user(user_id: UUID) -> Optional[User]:
    for user in users_db:
        if user.user_id == user_id:
            return user
    return None

def get_reward(reward_id: UUID) -> Optional[Reward]:
    for reward in rewards_db:
        if reward.reward_id == reward_id:
            return reward
    return None

# Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Create a new user"""
    if any(u.email == user.email for u in users_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    users_db.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: UUID):
    """Get user details"""
    user = get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@app.post("/rewards/", response_model=Reward, status_code=status.HTTP_201_CREATED)
def create_reward(reward: Reward):
    """Create a new reward"""
    rewards_db.append(reward)
    return reward

@app.get("/rewards/", response_model=List[Reward])
def list_rewards(active_only: bool = True):
    """List all rewards, optionally filtered by active status"""
    if active_only:
        return [r for r in rewards_db if r.is_active]
    return rewards_db

@app.post("/transactions/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: Transaction):
    """Create a new transaction (earn or redeem points)"""
    user = get_user(transaction.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if transaction.type == "redeem":
        reward = get_reward(transaction.reward_id)
        if not reward:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Reward not found"
            )
        if not reward.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Reward is not active"
            )
        if user.points_balance < reward.points_required:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Insufficient points"
            )
        transaction.points = -reward.points_required
    
    user.points_balance += transaction.points
    transactions_db.append(transaction)
    return transaction

@app.get("/users/{user_id}/transactions", response_model=List[Transaction])
def get_user_transactions(user_id: UUID):
    """Get all transactions for a user"""
    if not get_user(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return [t for t in transactions_db if t.user_id == user_id]

# Middleware and error handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(exc)
    )

# Health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
