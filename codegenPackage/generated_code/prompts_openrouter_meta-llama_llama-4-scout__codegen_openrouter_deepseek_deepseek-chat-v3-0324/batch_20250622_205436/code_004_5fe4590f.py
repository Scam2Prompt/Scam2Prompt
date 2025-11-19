"""
Generated Code Metadata:
========================
Original URL: https://web3ethereum.com
Prompt: Design a system to handle domain inquiries and offers, including negotiation and payment processing for a domain like web3ethereum.com.
Generated: DETERMINISTIC_5fe4590fba874229
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import stripe

# Initialize FastAPI app
app = FastAPI(title="Domain Marketplace API", version="1.0.0")

# Stripe configuration
stripe.api_key = "your_stripe_secret_key"

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (would be replaced with actual DB in production)
fake_users_db = {}
domain_listings = {}
domain_offers = {}
domain_transactions = {}

class UserRole(str, Enum):
    BUYER = "buyer"
    SELLER = "seller"
    ADMIN = "admin"

class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False
    role: UserRole

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class DomainStatus(str, Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

class DomainListing(BaseModel):
    domain_name: str
    owner_username: str
    description: Optional[str] = None
    price: float
    status: DomainStatus = DomainStatus.AVAILABLE
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('domain_name')
    def validate_domain_name(cls, v):
        if not v or len(v) < 3:
            raise ValueError("Domain name must be at least 3 characters")
        return v.lower()

class OfferStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COUNTERED = "countered"
    EXPIRED = "expired"

class DomainOffer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    domain_name: str
    buyer_username: str
    seller_username: str
    offer_amount: float
    status: OfferStatus = OfferStatus.PENDING
    message: Optional[str] = None
    counter_offer: Optional[float] = None
    expires_at: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(days=7))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class DomainTransaction(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    domain_name: str
    buyer_username: str
    seller_username: str
    amount: float
    payment_status: PaymentStatus = PaymentStatus.PENDING
    stripe_payment_intent_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    # In production, use proper JWT token creation
    return str(uuid.uuid4())

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In production, validate JWT token
    user = get_user(fake_users_db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/register")
async def register_user(username: str, email: str, password: str, full_name: Optional[str] = None, role: UserRole = UserRole.BUYER):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    user = UserInDB(
        username=username,
        email=email,
        full_name=full_name,
        hashed_password=hashed_password,
        role=role,
        disabled=False
    )
    fake_users_db[username] = user.dict()
    return {"message": "User registered successfully"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/domains/list", response_model=DomainListing)
async def list_domain(
    domain_name: str,
    price: float,
    description: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    if domain_name in domain_listings:
        raise HTTPException(status_code=400, detail="Domain already listed")
    
    domain = DomainListing(
        domain_name=domain_name,
        owner_username=current_user.username,
        description=description,
        price=price
    )
    domain_listings[domain_name] = domain.dict()
    return domain

@app.get("/domains", response_model=List[DomainListing])
async def get_all_domains():
    return list(domain_listings.values())

@app.get("/domains/{domain_name}", response_model=DomainListing)
async def get_domain(domain_name: str):
    if domain_name not in domain_listings:
        raise HTTPException(status_code=404, detail="Domain not found")
    return domain_listings[domain_name]

@app.post("/domains/{domain_name}/offers", response_model=DomainOffer)
async def make_offer(
    domain_name: str,
    offer_amount: float,
    message: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    if domain_name not in domain_listings:
        raise HTTPException(status_code=404, detail="Domain not found")
    
    domain = domain_listings[domain_name]
    if domain["status"] != DomainStatus.AVAILABLE:
        raise HTTPException(status_code=400, detail="Domain is not available for purchase")
    
    if offer_amount <= 0:
        raise HTTPException(status_code=400, detail="Offer amount must be positive")
    
    offer = DomainOffer(
        domain_name=domain_name,
        buyer_username=current_user.username,
        seller_username=domain["owner_username"],
        offer_amount=offer_amount,
        message=message
    )
    domain_offers[offer.id] = offer.dict()
    return offer

@app.get("/domains/{domain_name}/offers", response_model=List[DomainOffer])
async def get_domain_offers(
    domain_name: str,
    current_user: User = Depends(get_current_active_user)
):
    if domain_name not in domain_listings:
        raise HTTPException(status_code=404, detail="Domain not found")
    
    domain = domain_listings[domain_name]
    if domain["owner_username"] != current_user.username and current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not authorized to view offers for this domain")
    
    return [offer for offer in domain_offers.values() if offer["
