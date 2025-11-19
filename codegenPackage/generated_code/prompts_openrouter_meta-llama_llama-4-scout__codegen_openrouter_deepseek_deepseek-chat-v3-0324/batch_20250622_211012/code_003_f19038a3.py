"""
Generated Code Metadata:
========================
Original URL: https://app-shibabudz.pages.dev
Prompt: Design a referral program API that rewards users with up to 5% of the first token purchase made by their referred friends, similar to the one implemented on the SHIBABUDZ platform.
Generated: DETERMINISTIC_f19038a3e0834e7f
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
import uuid
import logging
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # Should be in environment variables in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Referral Program API", version="1.0.0")

# Database models (would be replaced with actual DB in production)
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    hashed_password: str
    referral_code: str
    referred_by: Optional[str] = None
    wallet_address: Optional[str] = None
    is_active: bool = True

class TokenPurchase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    amount: float
    currency: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    referral_code_used: Optional[str] = None

class ReferralReward(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    referrer_id: str
    referred_user_id: str
    purchase_id: str
    reward_amount: float
    reward_percentage: float = Field(le=5.0)  # Max 5%
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    paid_out: bool = False

# In-memory storage (replace with database in production)
users_db = {}
purchases_db = {}
rewards_db = {}

# Helper functions
def get_user(username: str):
    for user in users_db.values():
        if user.username == username:
            return user
    return None

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

# Models for API requests/responses
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    referral_code: Optional[str] = None

class TokenPurchaseCreate(BaseModel):
    amount: float
    currency: str = "USD"
    referral_code: Optional[str] = None

class ReferralRewardResponse(BaseModel):
    referrer_id: str
    referred_user_id: str
    reward_amount: float
    reward_percentage: float
    purchase_id: str
    paid_out: bool

# API Endpoints
@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    referral_code = str(uuid.uuid4())[:8].upper()
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        referral_code=referral_code,
        referred_by=user.referral_code
    )
    
    users_db[new_user.id] = new_user
    
    # If referral code was used, log it (reward will be processed on first purchase)
    if user.referral_code:
        logger.info(f"User {new_user.id} registered with referral code {user.referral_code}")
    
    return {"message": "User registered successfully", "referral_code": referral_code}

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/purchase", response_model=ReferralRewardResponse)
async def make_purchase(
    purchase: TokenPurchaseCreate,
    current_user: User = Depends(get_current_user)
):
    # Record the purchase
    new_purchase = TokenPurchase(
        user_id=current_user.id,
        amount=purchase.amount,
        currency=purchase.currency,
        referral_code_used=purchase.referral_code
    )
    purchases_db[new_purchase.id] = new_purchase
    
    reward_response = None
    
    # Process referral if code was provided and this is the user's first purchase
    if purchase.referral_code and not any(
        p.user_id == current_user.id for p in purchases_db.values()
    ):
        # Find referrer
        referrer = next(
            (u for u in users_db.values() if u.referral_code == purchase.referral_code),
            None
        )
        
        if referrer:
            # Calculate reward (5% of purchase amount)
            reward_percentage = 5.0
            reward_amount = purchase.amount * (reward_percentage / 100)
            
            # Create referral reward
            new_reward = ReferralReward(
                referrer_id=referrer.id,
                referred_user_id=current_user.id,
                purchase_id=new_purchase.id,
                reward_amount=reward_amount,
                reward_percentage=reward_percentage
            )
            rewards_db[new_reward.id] = new_reward
            
            reward_response = ReferralRewardResponse(
                referrer_id=referrer.id,
                referred_user_id=current_user.id,
                reward_amount=reward_amount,
                reward_percentage=reward_percentage,
                purchase_id=new_purchase.id,
                paid_out=new_reward.paid_out
            )
            
            logger.info(f"Referral reward created: {new_reward.id}")
    
    if reward_response:
        return reward_response
    else:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Purchase recorded but no referral reward applied"
        )

@app.get("/rewards", response_model=List[ReferralRewardResponse])
async def get_user_rewards(current_user: User = Depends(get_current_user)):
    user_rewards = [
        reward for reward in rewards_db.values() 
        if reward.referrer_id == current_user.id
    ]
    return [
        ReferralRewardResponse(
            referrer_id=r.referrer_id,
            referred_user_id=r.referred_user_id,
            reward_amount=r.reward_amount,
            reward_percentage=r.reward_percentage,
            purchase_id=r.purchase_id,
            paid_out=r.paid_out
        ) for r in user_rewards
    ]

@app.post("/rewards/{reward_id}/payout")
async def process_payout(reward_id: str, current_user: User = Depends(get_current_user)):
    if reward_id not in rewards_db:
        raise HTTPException(status_code=404, detail="Reward not found")
    
    reward = rewards_db[reward_id]
    
    if reward.referrer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to process this payout")
    
    if reward.paid_out:
        raise HTTPException(status_code=400, detail="Reward already paid out")
    
    # In production, this would trigger an actual payment to the user's wallet
    reward.paid_out = True
    rewards_db[reward_id] = reward
    
    logger.info(f"Processed payout for reward {reward_id}")
    
    return {"message": "Payout processed successfully", "reward_id": reward_id}
```
