"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: What are some best practices for creating a fundraising campaign API for an NGO, taking cues from the initiatives of Amma Parivaar Orphanage?
Generated: DETERMINISTIC_e8f8ccddb0574b94
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime
import uuid
import logging
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="NGO Fundraising Campaign API",
    description="API for managing fundraising campaigns for NGOs inspired by Amma Parivaar Orphanage initiatives",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@ngofundraising.org"
    },
    license_info={
        "name": "MIT",
    },
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in a real app, this would connect to a proper database)
fake_db = {
    "users": {},
    "campaigns": {},
    "donations": {}
}

# Pydantic models for request/response validation
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class User(UserBase):
    id: str
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class CampaignBase(BaseModel):
    title: str
    description: str
    target_amount: float
    start_date: datetime
    end_date: datetime

class CampaignCreate(CampaignBase):
    @validator('end_date')
    def end_date_after_start_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('End date must be after start date')
        return v

class Campaign(CampaignBase):
    id: str
    current_amount: float
    is_active: bool
    created_by: str
    created_at: datetime

    class Config:
        orm_mode = True

class DonationBase(BaseModel):
    amount: float
    campaign_id: str
    donor_name: str
    donor_email: EmailStr
    is_anonymous: bool = False

class DonationCreate(DonationBase):
    @validator('amount')
    def amount_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be positive')
        return v

class Donation(DonationBase):
    id: str
    donation_date: datetime
    transaction_id: str

    class Config:
        orm_mode = True

# Helper functions
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, email: str):
    if email in db["users"]:
        user_dict = db["users"][email]
        return User(**user_dict)
    return None

def authenticate_user(db, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

# API endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user account"""
    if user.email in fake_db["users"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user.password)
    user_id = str(uuid.uuid4())
    db_user = {
        "id": user_id,
        "email": user.email,
        "full_name": user.full_name,
        "password": hashed_password,
        "is_active": True,
        "is_admin": False
    }
    fake_db["users"][user.email] = db_user
    logger.info(f"Created new user: {user.email}")
    return db_user

@app.post("/campaigns/", response_model=Campaign, status_code=status.HTTP_201_CREATED)
async def create_campaign(campaign: CampaignCreate, current_user: User = Depends(oauth2_scheme)):
    """Create a new fundraising campaign"""
    campaign_id = str(uuid.uuid4())
    db_campaign = {
        "id": campaign_id,
        **campaign.dict(),
        "current_amount": 0.0,
        "is_active": True,
        "created_by": current_user.id,
        "created_at": datetime.now()
    }
    fake_db["campaigns"][campaign_id] = db_campaign
    logger.info(f"Created new campaign: {campaign.title}")
    return db_campaign

@app.get("/campaigns/", response_model=List[Campaign])
async def list_campaigns(active_only: bool = True):
    """List all fundraising campaigns (optionally only active ones)"""
    campaigns = list(fake_db["campaigns"].values())
    if active_only:
        campaigns = [c for c in campaigns if c["is_active"]]
    return campaigns

@app.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str):
    """Get details of a specific campaign"""
    if campaign_id not in fake_db["campaigns"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    return fake_db["campaigns"][campaign_id]

@app.post("/donations/", response_model=Donation, status_code=status.HTTP_201_CREATED)
async def create_donation(donation: DonationCreate):
    """Create a new donation for a campaign"""
    if donation.campaign_id not in fake_db["campaigns"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    donation_id = str(uuid.uuid4())
    transaction_id = str(uuid.uuid4())
    db_donation = {
        "id": donation_id,
        **donation.dict(),
        "donation_date": datetime.now(),
        "transaction_id": transaction_id
    }
    
    # Update campaign amount
    fake_db["campaigns"][donation.campaign_id]["current_amount"] += donation.amount
    
    fake_db["donations"][donation_id] = db_donation
    logger.info(f"New donation received: {donation.amount} for campaign {donation.campaign_id}")
    return db_donation

@app.get("/donations/{donation_id}", response_model=Donation)
async def get_donation(donation_id: str):
    """Get details of a specific donation"""
    if donation_id not in fake_db["donations"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Donation not found"
        )
    return fake_db["donations"][donation_id]

@app.get("/campaigns/{campaign_id}/donations", response_model=List[Donation])
async def get_campaign_donations(campaign_id: str):
    """Get all donations for a specific campaign"""
    if campaign_id not in fake_db["campaigns"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    
    donations = [d for d in fake_db["donations"].values() if d["campaign_id"] == campaign_id]
    return donations

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
