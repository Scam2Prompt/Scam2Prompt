"""
Generated Code Metadata:
========================
Original URL: https://symibyotic.fi
Prompt: Design a RESTful API for managing domain name sales, including endpoints for buying, leasing, and transferring domains, inspired by the features on symibyotic.fi.
Generated: DETERMINISTIC_5baa770b5edf323e
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timedelta
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Domain Management API",
    description="RESTful API for managing domain name sales, leasing, and transfers",
    version="1.0.0"
)

# Database models (in-memory for this example)
class Domain(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    owner_id: str
    status: str = "available"  # available, leased, sold, pending_transfer
    price: Optional[float] = None
    lease_price: Optional[float] = None
    lease_duration: Optional[int] = None  # in days
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    username: str
    email: str
    balance: float = 0.0

class Transaction(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    domain_id: str
    user_id: str
    type: str  # purchase, lease, transfer
    amount: float
    status: str = "pending"  # pending, completed, failed
    created_at: datetime = Field(default_factory=datetime.utcnow)

# In-memory databases
domains_db: List[Domain] = []
users_db: List[User] = []
transactions_db: List[Transaction] = []

# Helper functions
def get_domain(domain_id: str) -> Domain:
    for domain in domains_db:
        if domain.id == domain_id:
            return domain
    raise HTTPException(status_code=404, detail="Domain not found")

def get_user(user_id: str) -> User:
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

def update_domain_status(domain_id: str, status: str):
    for domain in domains_db:
        if domain.id == domain_id:
            domain.status = status
            domain.updated_at = datetime.utcnow()
            return
    raise HTTPException(status_code=404, detail="Domain not found")

def update_user_balance(user_id: str, amount: float):
    for user in users_db:
        if user.id == user_id:
            user.balance += amount
            return
    raise HTTPException(status_code=404, detail="User not found")

# Request models
class DomainCreate(BaseModel):
    name: str
    owner_id: str
    price: Optional[float] = None
    lease_price: Optional[float] = None
    lease_duration: Optional[int] = None

class DomainUpdate(BaseModel):
    price: Optional[float] = None
    lease_price: Optional[float] = None
    lease_duration: Optional[int] = None
    status: Optional[str] = None

class PurchaseRequest(BaseModel):
    user_id: str
    domain_id: str

class LeaseRequest(BaseModel):
    user_id: str
    domain_id: str
    duration_days: int

class TransferRequest(BaseModel):
    from_user_id: str
    to_user_id: str
    domain_id: str

# Domain endpoints
@app.post("/domains/", response_model=Domain, status_code=status.HTTP_201_CREATED)
def create_domain(domain: DomainCreate):
    """Create a new domain listing"""
    new_domain = Domain(
        name=domain.name,
        owner_id=domain.owner_id,
        price=domain.price,
        lease_price=domain.lease_price,
        lease_duration=domain.lease_duration
    )
    domains_db.append(new_domain)
    logger.info(f"Created domain {new_domain.name} with ID {new_domain.id}")
    return new_domain

@app.get("/domains/", response_model=List[Domain])
def list_domains(status_filter: Optional[str] = None):
    """List all domains, optionally filtered by status"""
    if status_filter:
        return [domain for domain in domains_db if domain.status == status_filter]
    return domains_db

@app.get("/domains/{domain_id}", response_model=Domain)
def get_domain_by_id(domain_id: str):
    """Get details of a specific domain"""
    return get_domain(domain_id)

@app.put("/domains/{domain_id}", response_model=Domain)
def update_domain_details(domain_id: str, update: DomainUpdate):
    """Update domain details"""
    domain = get_domain(domain_id)
    
    if update.price is not None:
        domain.price = update.price
    if update.lease_price is not None:
        domain.lease_price = update.lease_price
    if update.lease_duration is not None:
        domain.lease_duration = update.lease_duration
    if update.status is not None:
        domain.status = update.status
    
    domain.updated_at = datetime.utcnow()
    logger.info(f"Updated domain {domain_id}")
    return domain

# Purchase endpoints
@app.post("/purchase/", response_model=Transaction)
def purchase_domain(request: PurchaseRequest):
    """Purchase a domain"""
    domain = get_domain(request.domain_id)
    user = get_user(request.user_id)
    
    if domain.status != "available":
        raise HTTPException(status_code=400, detail="Domain is not available for purchase")
    
    if domain.price is None:
        raise HTTPException(status_code=400, detail="Domain is not for sale")
    
    if user.balance < domain.price:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    
    # Create transaction
    transaction = Transaction(
        domain_id=domain.id,
        user_id=user.id,
        type="purchase",
        amount=domain.price
    )
    transactions_db.append(transaction)
    
    # Process transaction
    try:
        update_user_balance(user.id, -domain.price)
        update_user_balance(domain.owner_id, domain.price)
        update_domain_status(domain.id, "sold")
        domain.owner_id = user.id
        transaction.status = "completed"
        logger.info(f"Completed purchase of domain {domain.id} by user {user.id}")
    except Exception as e:
        transaction.status = "failed"
        logger.error(f"Failed to process purchase: {str(e)}")
        raise HTTPException(status_code=500, detail="Transaction failed")
    
    return transaction

# Lease endpoints
@app.post("/lease/", response_model=Transaction)
def lease_domain(request: LeaseRequest):
    """Lease a domain"""
    domain = get_domain(request.domain_id)
    user = get_user(request.user_id)
    
    if domain.status != "available":
        raise HTTPException(status_code=400, detail="Domain is not available for lease")
    
    if domain.lease_price is None or domain.lease_duration is None:
        raise HTTPException(status_code=400, detail="Domain is not available for lease")
    
    total_price = domain.lease_price * (request.duration_days / domain.lease_duration)
    
    if user.balance < total_price:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    
    # Create transaction
    transaction = Transaction(
        domain_id=domain.id,
        user_id=user.id,
        type="lease",
        amount=total_price
    )
    transactions_db.append(transaction)
    
    # Process transaction
    try:
        update_user_balance(user.id, -total_price)
        update_user_balance(domain.owner_id, total_price)
        update_domain_status(domain.id, "leased")
        domain.lease_duration = request.duration_days
        transaction.status = "completed"
        logger.info(f"Completed lease of domain {domain.id} by user {user.id}")
    except Exception as e:
        transaction.status = "failed"
        logger.error(f"Failed to process lease: {str(e)}")
        raise HTTPException(status_code=500, detail="Transaction failed")
    
    return transaction

# Transfer endpoints
@app.post("/transfer/", response_model=Transaction)
def transfer_domain(request: TransferRequest):
    """Transfer domain ownership"""
    domain = get_domain(request.domain_id)
    from_user = get_user(request.from_user_id)
    to_user = get_user(request.to_user_id)
    
    if domain.owner_id != from_user.id:
        raise HTTPException(status_code=403, detail="User does not own this domain")
    
    if domain.status != "available":
        raise HTTPException(status_code=400, detail="Domain is not available for transfer")
    
    # Create transaction
    transaction = Transaction(
        domain_id=domain.id,
        user_id=to_user.id,
        type="transfer",
        amount=0  # Free transfer, could be modified to include fees
    )
    transactions_db.append(
