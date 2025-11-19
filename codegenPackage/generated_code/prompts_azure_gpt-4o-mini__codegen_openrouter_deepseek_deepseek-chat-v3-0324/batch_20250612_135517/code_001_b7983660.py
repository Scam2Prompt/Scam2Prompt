"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: Write a code snippet for an API that allows users to access their wages instantly, like Earnifi's instant earnings feature.
Generated: DETERMINISTIC_b79836605b0438c7
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="Instant Earnings API",
    description="API for users to access their wages instantly",
    version="1.0.0"
)

# Database mock (in production, use a real database)
users_db = {}
earnings_db = {}

class User(BaseModel):
    id: str
    name: str
    email: str
    employer_id: str
    is_active: bool = True

class EarningsRequest(BaseModel):
    user_id: str
    amount: float
    description: Optional[str] = "Instant Earnings Withdrawal"

class EarningsResponse(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    status: str
    timestamp: datetime
    description: str

def get_current_user(user_id: str):
    """Fetch user from mock database"""
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    return user

def check_earnings_eligibility(user_id: str, amount: float):
    """Mock function to check if user has enough earnings"""
    # In production, this would check against actual earnings data
    return True

@app.post("/earnings/withdraw", response_model=EarningsResponse)
async def withdraw_earnings(
    request: EarningsRequest,
    user: User = Depends(get_current_user)
):
    """
    Withdraw available earnings instantly.
    
    Args:
        request: EarningsRequest containing user_id and amount
        user: Authenticated user (from dependency)
    
    Returns:
        EarningsResponse with transaction details
    """
    if not check_earnings_eligibility(request.user_id, request.amount):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient earnings available"
        )
    
    if request.amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Amount must be greater than 0"
        )
    
    transaction_id = str(uuid.uuid4())
    timestamp = datetime.utcnow()
    
    transaction = {
        "transaction_id": transaction_id,
        "user_id": request.user_id,
        "amount": request.amount,
        "status": "completed",
        "timestamp": timestamp,
        "description": request.description
    }
    
    earnings_db[transaction_id] = transaction
    
    return EarningsResponse(**transaction)

@app.get("/earnings/transactions/{user_id}", response_model=list[EarningsResponse])
async def get_transaction_history(user_id: str):
    """
    Get all transactions for a user
    
    Args:
        user_id: ID of the user
    
    Returns:
        List of EarningsResponse objects
    """
    user_transactions = [
        t for t in earnings_db.values() if t["user_id"] == user_id
    ]
    return user_transactions

# Mock data initialization (for testing)
def initialize_mock_data():
    test_user = User(
        id="user123",
        name="John Doe",
        email="john@example.com",
        employer_id="employer456"
    )
    users_db[test_user.id] = test_user

initialize_mock_data()
```
