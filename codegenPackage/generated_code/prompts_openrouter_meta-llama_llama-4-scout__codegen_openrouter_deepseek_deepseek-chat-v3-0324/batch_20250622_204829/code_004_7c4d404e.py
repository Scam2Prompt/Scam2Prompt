"""
Generated Code Metadata:
========================
Original URL: https://ethbod.com
Prompt: "Design an API for tracking Ethereum pledges, including endpoints for making pledges and retrieving pledge history."
Generated: DETERMINISTIC_7c4d404e85955993
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Ethereum Pledge Tracker API
# This API allows users to make pledges on the Ethereum blockchain and retrieve their pledge history.

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="Ethereum Pledge Tracker API",
    description="API for tracking Ethereum pledges",
    version="1.0.0"
)

# Database simulation (in production, replace with a real database)
pledge_db = []

class Pledge(BaseModel):
    pledge_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_address: str
    amount_eth: float
    message: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tx_hash: Optional[str] = None

    @validator('amount_eth')
    def validate_amount(cls, v):
        if v <= 0:
            raise ValueError('Amount must be positive')
        return v

    @validator('user_address')
    def validate_address(cls, v):
        if not v.startswith('0x') or len(v) != 42:
            raise ValueError('Invalid Ethereum address')
        return v

class PledgeCreate(BaseModel):
    user_address: str
    amount_eth: float
    message: Optional[str] = None

class PledgeResponse(BaseModel):
    pledge_id: str
    user_address: str
    amount_eth: float
    message: Optional[str]
    timestamp: datetime
    tx_hash: Optional[str]

@app.post("/pledges/", response_model=PledgeResponse, status_code=status.HTTP_201_CREATED)
async def create_pledge(pledge: PledgeCreate):
    """
    Create a new Ethereum pledge.
    """
    try:
        new_pledge = Pledge(**pledge.dict())
        pledge_db.append(new_pledge)
        return new_pledge
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/pledges/", response_model=List[PledgeResponse])
async def get_all_pledges():
    """
    Get all pledges in the system.
    """
    return pledge_db

@app.get("/pledges/{pledge_id}", response_model=PledgeResponse)
async def get_pledge(pledge_id: str):
    """
    Get a specific pledge by ID.
    """
    pledge = next((p for p in pledge_db if p.pledge_id == pledge_id), None)
    if not pledge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pledge not found"
        )
    return pledge

@app.get("/pledges/user/{user_address}", response_model=List[PledgeResponse])
async def get_user_pledges(user_address: str):
    """
    Get all pledges for a specific user address.
    """
    user_pledges = [p for p in pledge_db if p.user_address == user_address]
    if not user_pledges:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No pledges found for this address"
        )
    return user_pledges

@app.put("/pledges/{pledge_id}/confirm", response_model=PledgeResponse)
async def confirm_pledge(pledge_id: str, tx_hash: str):
    """
    Confirm a pledge by adding its transaction hash.
    """
    pledge = next((p for p in pledge_db if p.pledge_id == pledge_id), None)
    if not pledge:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pledge not found"
        )
    
    if not tx_hash.startswith('0x') or len(tx_hash) != 66:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid transaction hash"
        )
    
    pledge.tx_hash = tx_hash
    return pledge
```
