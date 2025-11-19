"""
Generated Code Metadata:
========================
Original URL: https://uni-token.com
Prompt: Create a custom solution for the traceability of collectible items, incorporating the features described on Unitoken's website.
Generated: DETERMINISTIC_aeb9bdf11400aff1
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import uuid
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Collectible Traceability API",
    description="A custom solution for traceability of collectible items",
    version="1.0.0"
)

# Database simulation
db = {
    "collectibles": {},
    "transactions": {},
    "owners": {}
}

class Owner(BaseModel):
    """Owner information model."""
    owner_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    contact: str
    wallet_address: Optional[str] = None

    @validator('contact')
    def validate_contact(cls, v):
        if not v or len(v) < 5:
            raise ValueError("Contact information must be at least 5 characters long")
        return v

class Collectible(BaseModel):
    """Collectible item model."""
    item_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    creator: str
    current_owner: str
    metadata: Dict = Field(default_factory=dict)
    provenance_hash: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        if not v or len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

class Transaction(BaseModel):
    """Transaction model for ownership transfer."""
    transaction_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    item_id: str
    from_owner: str
    to_owner: str
    transaction_date: datetime = Field(default_factory=datetime.utcnow)
    transaction_hash: Optional[str] = None
    metadata: Dict = Field(default_factory=dict)

def calculate_hash(data: Dict) -> str:
    """Calculate SHA-256 hash of the given data."""
    data_str = json.dumps(data, sort_keys=True, default=str)
    return hashlib.sha256(data_str.encode()).hexdigest()

@app.post("/owners/", response_model=Owner, status_code=status.HTTP_201_CREATED)
def create_owner(owner: Owner):
    """Create a new owner."""
    if owner.owner_id in db["owners"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Owner with this ID already exists"
        )
    db["owners"][owner.owner_id] = owner
    return owner

@app.get("/owners/{owner_id}", response_model=Owner)
def get_owner(owner_id: str):
    """Get owner by ID."""
    if owner_id not in db["owners"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found"
        )
    return db["owners"][owner_id]

@app.post("/collectibles/", response_model=Collectible, status_code=status.HTTP_201_CREATED)
def create_collectible(collectible: Collectible):
    """Create a new collectible item."""
    if collectible.item_id in db["collectibles"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collectible with this ID already exists"
        )
    
    if collectible.current_owner not in db["owners"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Owner does not exist"
        )
    
    # Calculate initial provenance hash
    collectible_data = collectible.dict(exclude={"provenance_hash"})
    collectible.provenance_hash = calculate_hash(collectible_data)
    
    db["collectibles"][collectible.item_id] = collectible
    return collectible

@app.get("/collectibles/{item_id}", response_model=Collectible)
def get_collectible(item_id: str):
    """Get collectible by ID."""
    if item_id not in db["collectibles"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collectible not found"
        )
    return db["collectibles"][item_id]

@app.post("/transactions/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction: Transaction):
    """Create a new ownership transfer transaction."""
    if transaction.item_id not in db["collectibles"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collectible does not exist"
        )
    
    if transaction.from_owner not in db["owners"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="From owner does not exist"
        )
    
    if transaction.to_owner not in db["owners"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="To owner does not exist"
        )
    
    # Verify current owner matches from_owner
    collectible = db["collectibles"][transaction.item_id]
    if collectible.current_owner != transaction.from_owner:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current owner does not match transaction sender"
        )
    
    # Update collectible's current owner
    collectible.current_owner = transaction.to_owner
    
    # Calculate transaction hash
    transaction_data = transaction.dict(exclude={"transaction_hash"})
    transaction.transaction_hash = calculate_hash(transaction_data)
    
    # Update collectible's provenance hash
    provenance_data = {
        "item_id": collectible.item_id,
        "previous_hash": collectible.provenance_hash,
        "transaction": transaction_data
    }
    collectible.provenance_hash = calculate_hash(provenance_data)
    
    db["transactions"][transaction.transaction_id] = transaction
    return transaction

@app.get("/collectibles/{item_id}/provenance", response_model=List[Dict])
def get_provenance(item_id: str):
    """Get full provenance history for a collectible."""
    if item_id not in db["collectibles"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collectible not found"
        )
    
    provenance = []
    collectible = db["collectibles"][item_id]
    
    # Get all transactions for this item
    item_transactions = [
        t for t in db["transactions"].values() 
        if t.item_id == item_id
    ]
    
    # Sort transactions by date
    item_transactions.sort(key=lambda x: x.transaction_date)
    
    # Build provenance chain
    for transaction in item_transactions:
        provenance.append({
            "transaction_id": transaction.transaction_id,
            "from_owner": transaction.from_owner,
            "to_owner": transaction.to_owner,
            "date": transaction.transaction_date,
            "transaction_hash": transaction.transaction_hash,
            "metadata": transaction.metadata
        })
    
    return provenance

@app.get("/collectibles/{item_id}/verify", response_model=Dict)
def verify_provenance(item_id: str):
    """Verify the integrity of a collectible's provenance chain."""
    if item_id not in db["collectibles"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collectible not found"
        )
    
    collectible = db["collectibles"][item_id]
    transactions = [
        t for t in db["transactions"].values() 
        if t.item_id == item_id
    ]
    transactions.sort(key=lambda x: x.transaction_date)
    
    # Rebuild the provenance chain to verify hashes
    current_hash = None
    verification_data = []
    valid = True
    
    # Initial creation hash
    initial_data = collectible.dict(exclude={"provenance_hash"})
    calculated_hash = calculate_hash(initial_data)
    verification_data.append({
        "step": "creation",
        "expected_hash": collectible.provenance_hash,
        "calculated_hash": calculated_hash,
        "match": calculated_hash == collectible.provenance_hash
    })
    
    if calculated_hash != collectible.provenance_hash:
        valid = False
    
    current_hash = collectible.provenance_hash
    
    # Verify each transaction
    for i, transaction in enumerate(transactions):
        provenance_data = {
            "item_id": item_id,
            "previous_hash": current_hash,
            "transaction": transaction.dict(exclude={"transaction_hash"})
        }
        calculated_hash = calculate_hash(provenance_data)
        
        verification_data.append({
            "step": f"transaction_{i}",
            "transaction_id": transaction.transaction_id,
            "expected_hash": transaction.transaction_hash,
            "calculated_hash": calculated_hash,
            "match": calculated_hash == transaction.trans
