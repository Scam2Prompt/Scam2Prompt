"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Generate code to create a customer loyalty program API that allows users to register, earn points, and redeem rewards, similar to the "باشگاه مشتریان گلدن" system mentioned on the website.
Generated: DETERMINISTIC_5135ba71e0f0ce0a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Golden Customer Club API",
    description="API for managing customer loyalty program",
    version="1.0.0"
)

# Database models (in-memory for this example)
class Customer(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    registration_date: datetime
    points: int = 0

class Reward(BaseModel):
    id: str
    name: str
    description: str
    points_required: int
    stock: int

class Transaction(BaseModel):
    id: str
    customer_id: str
    amount: int
    transaction_type: str  # 'earn' or 'redeem'
    date: datetime
    reward_id: Optional[str] = None

# In-memory databases
customers_db = {}
rewards_db = {}
transactions_db = {}

# Helper functions
def get_customer(customer_id: str) -> Customer:
    if customer_id not in customers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customers_db[customer_id]

def get_reward(reward_id: str) -> Reward:
    if reward_id not in rewards_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reward not found"
        )
    return rewards_db[reward_id]

# Request models
class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class PointsEarn(BaseModel):
    customer_id: str
    amount: int

class RewardCreate(BaseModel):
    name: str
    description: str
    points_required: int
    stock: int

class RewardRedeem(BaseModel):
    customer_id: str
    reward_id: str

# API Endpoints
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def register_customer(customer: CustomerCreate):
    """Register a new customer in the loyalty program"""
    customer_id = str(uuid.uuid4())
    new_customer = Customer(
        id=customer_id,
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        registration_date=datetime.now()
    )
    customers_db[customer_id] = new_customer
    logger.info(f"New customer registered: {customer_id}")
    return new_customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_details(customer_id: str):
    """Get customer details by ID"""
    return get_customer(customer_id)

@app.post("/points/earn", response_model=Transaction)
async def earn_points(points: PointsEarn):
    """Add points to a customer's account"""
    customer = get_customer(points.customer_id)
    customer.points += points.amount
    
    transaction_id = str(uuid.uuid4())
    new_transaction = Transaction(
        id=transaction_id,
        customer_id=points.customer_id,
        amount=points.amount,
        transaction_type="earn",
        date=datetime.now()
    )
    transactions_db[transaction_id] = new_transaction
    
    logger.info(f"Customer {points.customer_id} earned {points.amount} points")
    return new_transaction

@app.post("/rewards/", response_model=Reward, status_code=status.HTTP_201_CREATED)
async def create_reward(reward: RewardCreate):
    """Create a new reward in the system"""
    reward_id = str(uuid.uuid4())
    new_reward = Reward(
        id=reward_id,
        name=reward.name,
        description=reward.description,
        points_required=reward.points_required,
        stock=reward.stock
    )
    rewards_db[reward_id] = new_reward
    logger.info(f"New reward created: {reward_id}")
    return new_reward

@app.get("/rewards/", response_model=List[Reward])
async def list_rewards():
    """List all available rewards"""
    return list(rewards_db.values())

@app.post("/rewards/redeem", response_model=Transaction)
async def redeem_reward(redeem: RewardRedeem):
    """Redeem a reward using customer points"""
    customer = get_customer(redeem.customer_id)
    reward = get_reward(redeem.reward_id)
    
    if customer.points < reward.points_required:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough points to redeem this reward"
        )
    
    if reward.stock <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This reward is out of stock"
        )
    
    # Update customer points and reward stock
    customer.points -= reward.points_required
    reward.stock -= 1
    
    # Record transaction
    transaction_id = str(uuid.uuid4())
    new_transaction = Transaction(
        id=transaction_id,
        customer_id=redeem.customer_id,
        amount=reward.points_required,
        transaction_type="redeem",
        date=datetime.now(),
        reward_id=redeem.reward_id
    )
    transactions_db[transaction_id] = new_transaction
    
    logger.info(f"Customer {redeem.customer_id} redeemed reward {redeem.reward_id}")
    return new_transaction

@app.get("/transactions/{customer_id}", response_model=List[Transaction])
async def get_customer_transactions(customer_id: str):
    """Get all transactions for a customer"""
    get_customer(customer_id)  # Validate customer exists
    return [t for t in transactions_db.values() if t.customer_id == customer_id]

# Sample data initialization
def initialize_sample_data():
    """Initialize sample data for testing"""
    sample_customer = CustomerCreate(
        name="Sample Customer",
        email="sample@example.com",
        phone="09123456789"
    )
    register_customer(sample_customer)
    
    sample_reward = RewardCreate(
        name="10% Discount",
        description="10% discount on next purchase",
        points_required=100,
        stock=50
    )
    create_reward(sample_reward)

# Initialize sample data when starting
initialize_sample_data()
```
