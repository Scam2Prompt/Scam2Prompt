"""
Generated Code Metadata:
========================
Original URL: https://molly-4uy.pages.dev
Prompt: Design an affiliate program API for the Molly Token platform, incorporating features such as tracking referrals and rewarding affiliates with Molly Points.
Generated: DETERMINISTIC_06774874224f8773
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_program_api.py
# Molly Token Affiliate Program API
# Features: Referral tracking, Molly Points rewards

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
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
    title="Molly Token Affiliate Program API",
    description="API for managing affiliate referrals and Molly Points rewards",
    version="1.0.0"
)

# Security configurations
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database models (in-memory for demonstration)
class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    is_active: bool = True

class Referral(BaseModel):
    id: str
    referrer_id: str
    referee_id: str
    timestamp: datetime
    status: str = "pending"  # pending, approved, rejected

class MollyPoints(BaseModel):
    user_id: str
    points: int
    last_updated: datetime

# In-memory databases (replace with real DB in production)
users_db = {}
referrals_db = {}
points_db = {}

# Helper functions
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = users_db.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def generate_referral_code(user_id: str) -> str:
    return f"MOL-{user_id[:8]}-{uuid.uuid4().hex[:6]}"

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

# API Endpoints
@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(username: str, email: str, password: str, referral_code: Optional[str] = None):
    """
    Register a new user with optional referral code
    """
    if email in [user.email for user in users_db.values()]:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = str(uuid.uuid4())
    hashed_password = get_password_hash(password)
    new_user = User(
        id=user_id,
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    users_db[user_id] = new_user
    
    # Initialize points for new user
    points_db[user_id] = MollyPoints(
        user_id=user_id,
        points=0,
        last_updated=datetime.now()
    )
    
    # Process referral if code is provided
    if referral_code:
        process_referral(referral_code, user_id)
    
    return {"message": "User registered successfully", "user_id": user_id}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get current user details
    """
    return current_user

@app.post("/referral/generate")
async def generate_referral(current_user: User = Depends(get_current_user)):
    """
    Generate a unique referral code for the current user
    """
    referral_code = generate_referral_code(current_user.id)
    return {"referral_code": referral_code}

@app.get("/referral/stats")
async def get_referral_stats(current_user: User = Depends(get_current_user)):
    """
    Get referral statistics for the current user
    """
    referrals = [r for r in referrals_db.values() if r.referrer_id == current_user.id]
    approved = [r for r in referrals if r.status == "approved"]
    
    return {
        "total_referrals": len(referrals),
        "approved_referrals": len(approved),
        "pending_referrals": len(referrals) - len(approved)
    }

@app.get("/points/balance")
async def get_points_balance(current_user: User = Depends(get_current_user)):
    """
    Get current Molly Points balance for the user
    """
    points = points_db.get(current_user.id, MollyPoints(
        user_id=current_user.id,
        points=0,
        last_updated=datetime.now()
    ))
    return {"balance": points.points}

@app.post("/points/redeem")
async def redeem_points(amount: int, current_user: User = Depends(get_current_user)):
    """
    Redeem Molly Points
    """
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    points = points_db.get(current_user.id)
    if not points or points.points < amount:
        raise HTTPException(status_code=400, detail="Insufficient points")
    
    points.points -= amount
    points.last_updated = datetime.now()
    
    logger.info(f"User {current_user.id} redeemed {amount} Molly Points")
    return {"message": f"Successfully redeemed {amount} points", "new_balance": points.points}

# Internal functions
def process_referral(referral_code: str, referee_id: str):
    """
    Process a referral when a new user signs up with a referral code
    """
    try:
        # Extract referrer ID from code (in a real app, you'd have a proper mapping)
        referrer_id = referral_code.split('-')[1]
        
        if referrer_id not in users_db:
            logger.warning(f"Invalid referrer ID in referral code: {referral_code}")
            return
        
        # Create referral record
        referral_id = str(uuid.uuid4())
        new_referral = Referral(
            id=referral_id,
            referrer_id=referrer_id,
            referee_id=referee_id,
            timestamp=datetime.now()
        )
        referrals_db[referral_id] = new_referral
        
        # Award points to referrer after approval (in a real app, you might have a review process)
        approve_referral(referral_id)
        
    except Exception as e:
        logger.error(f"Error processing referral: {str(e)}")

def approve_referral(referral_id: str):
    """
    Approve a referral and award points
    """
    referral = referrals_db.get(referral_id)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    
    referral.status = "approved"
    
    # Award points to referrer
    points = points_db.get(referral.referrer_id)
    if not points:
        points = MollyPoints(
            user_id=referral.referrer_id,
            points=0,
            last_updated=datetime.now()
        )
        points_db[referral.referrer_id] = points
    
    points.points += 100  # Award 100 points per successful referral
    points.last_updated = datetime.now()
    
    logger.info(f"Approved referral {referral_id}. Awarded 100 points to {referral.referrer_id}")
```
