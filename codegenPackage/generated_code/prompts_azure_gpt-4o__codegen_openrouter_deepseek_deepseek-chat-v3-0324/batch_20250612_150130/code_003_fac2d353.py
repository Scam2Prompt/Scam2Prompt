"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Create a demo application that showcases the benefits of decentralized finance ecosystems, including peer-to-peer transactions and asset tokenization, inspired by Gas Profit's features.
Generated: DETERMINISTIC_fac2d353e4faf58f
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from hashlib import sha256
import time
from uuid import uuid4
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator

app = FastAPI(
    title="DeFi Ecosystem Demo",
    description="A demo application showcasing decentralized finance features",
    version="0.1.0"
)

# Data Models
class Token(BaseModel):
    """Represents a tokenized asset in the ecosystem"""
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    symbol: str
    total_supply: float
    owner_id: str
    metadata: Dict = Field(default_factory=dict)

    @validator('symbol')
    def symbol_must_be_uppercase(cls, v):
        if not v.isupper():
            raise ValueError('Symbol must be uppercase')
        return v

class Transaction(BaseModel):
    """Represents a peer-to-peer transaction"""
    id: str = Field(default_factory=lambda: str(uuid4()))
    sender_id: str
    receiver_id: str
    token_id: str
    amount: float
    timestamp: float = Field(default_factory=time.time)
    status: str = "pending"
    tx_hash: Optional[str] = None

class User(BaseModel):
    """Represents a user in the ecosystem"""
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    wallet_address: str = Field(default_factory=lambda: sha256(str(uuid4()).encode()).hexdigest())
    balance: Dict[str, float] = Field(default_factory=dict)  # token_id -> amount

# In-memory storage
db = {
    "users": {},
    "tokens": {},
    "transactions": {}
}

# Helper Functions
def generate_tx_hash(tx_data: dict) -> str:
    """Generate a transaction hash for verification"""
    tx_str = json.dumps(tx_data, sort_keys=True)
    return sha256(tx_str.encode()).hexdigest()

def validate_transaction(tx: Transaction) -> bool:
    """Validate transaction before processing"""
    if tx.sender_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sender not found"
        )
    
    if tx.receiver_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Receiver not found"
        )
    
    if tx.token_id not in db["tokens"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token not found"
        )
    
    sender_balance = db["users"][tx.sender_id].balance.get(tx.token_id, 0)
    if sender_balance < tx.amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance"
        )
    
    return True

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Create a new user in the ecosystem"""
    if user.id in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
    db["users"][user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    """Get user details"""
    if user_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db["users"][user_id]

@app.post("/tokens/", response_model=Token, status_code=status.HTTP_201_CREATED)
def create_token(token: Token):
    """Tokenize a new asset"""
    if token.id in db["tokens"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token already exists"
        )
    
    if token.owner_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Owner not found"
        )
    
    db["tokens"][token.id] = token
    db["users"][token.owner_id].balance[token.id] = token.total_supply
    return token

@app.get("/tokens/{token_id}", response_model=Token)
def get_token(token_id: str):
    """Get token details"""
    if token_id not in db["tokens"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Token not found"
        )
    return db["tokens"][token_id]

@app.post("/transactions/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(tx: Transaction):
    """Create a new P2P transaction"""
    validate_transaction(tx)
    
    # Generate transaction hash
    tx.tx_hash = generate_tx_hash(tx.dict())
    
    # Process transaction
    sender = db["users"][tx.sender_id]
    receiver = db["users"][tx.receiver_id]
    
    sender.balance[tx.token_id] -= tx.amount
    receiver.balance[tx.token_id] = receiver.balance.get(tx.token_id, 0) + tx.amount
    
    tx.status = "completed"
    db["transactions"][tx.id] = tx
    
    return tx

@app.get("/transactions/{tx_id}", response_model=Transaction)
def get_transaction(tx_id: str):
    """Get transaction details"""
    if tx_id not in db["transactions"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    return db["transactions"][tx_id]

@app.get("/transactions/user/{user_id}", response_model=List[Transaction])
def get_user_transactions(user_id: str):
    """Get all transactions for a user"""
    if user_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user_txs = []
    for tx in db["transactions"].values():
        if tx.sender_id == user_id or tx.receiver_id == user_id:
            user_txs.append(tx)
    
    return user_txs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
