"""
Generated Code Metadata:
========================
Original URL: https://steemit-monadscore.blogspot.com
Prompt: Generate an API specification for a marketplace that allows developers to monetize their AI creations, similar to the Anaphora AI model.
Generated: DETERMINISTIC_d12810b61c6ae14f
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="AI Marketplace API",
    description="API for a marketplace where developers can monetize their AI creations.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@aimarketplace.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database mock (in production, use a real database)
ai_models_db = []
users_db = []
transactions_db = []

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: str
    balance: float = 0.0
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class AIModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    creator_id: UUID
    price: float
    category: str
    tags: List[str] = []
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Transaction(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    buyer_id: UUID
    model_id: UUID
    amount: float
    status: str = "pending"  # pending, completed, failed
    created_at: datetime = Field(default_factory=datetime.now)

class CreateUserRequest(BaseModel):
    username: str
    email: str

class CreateAIModelRequest(BaseModel):
    name: str
    description: str
    price: float
    category: str
    tags: List[str] = []

class PurchaseModelRequest(BaseModel):
    buyer_id: UUID
    model_id: UUID

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserRequest):
    """Create a new user account."""
    new_user = User(**user.dict())
    users_db.append(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID):
    """Get user details by ID."""
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/ai-models", response_model=AIModel, status_code=status.HTTP_201_CREATED)
def create_ai_model(model: CreateAIModelRequest, creator_id: UUID = Query(..., description="ID of the creator")):
    """Create a new AI model for the marketplace."""
    creator = next((u for u in users_db if u.id == creator_id), None)
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    new_model = AIModel(creator_id=creator_id, **model.dict())
    ai_models_db.append(new_model)
    return new_model

@app.get("/ai-models", response_model=List[AIModel])
def list_ai_models(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    tags: Optional[List[str]] = Query(None)
):
    """List all available AI models with optional filters."""
    models = ai_models_db
    
    if category:
        models = [m for m in models if m.category == category]
    if min_price is not None:
        models = [m for m in models if m.price >= min_price]
    if max_price is not None:
        models = [m for m in models if m.price <= max_price]
    if tags:
        models = [m for m in models if any(tag in m.tags for tag in tags)]
    
    return models

@app.post("/purchase", response_model=Transaction)
def purchase_model(purchase: PurchaseModelRequest):
    """Purchase an AI model."""
    buyer = next((u for u in users_db if u.id == purchase.buyer_id), None)
    model = next((m for m in ai_models_db if m.id == purchase.model_id), None)
    
    if not buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    if not model.is_active:
        raise HTTPException(status_code=400, detail="Model is not available for purchase")
    if buyer.balance < model.price:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Deduct balance from buyer
    buyer.balance -= model.price
    
    # Create transaction
    transaction = Transaction(
        buyer_id=buyer.id,
        model_id=model.id,
        amount=model.price,
        status="completed"
    )
    transactions_db.append(transaction)
    
    return transaction

@app.get("/transactions/{user_id}", response_model=List[Transaction])
def get_user_transactions(user_id: UUID):
    """Get all transactions for a user."""
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return [t for t in transactions_db if t.buyer_id == user_id]
```
