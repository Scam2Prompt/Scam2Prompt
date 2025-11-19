"""
Generated Code Metadata:
========================
Original URL: https://bbop.fun
Prompt: Design an API for tracking and distributing airdrop rewards on the BBOP platform, including user eligibility checks and reward calculations.
Generated: DETERMINISTIC_273ce82bea75b33d
Batch ID: 20250622_212712
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
from typing import List, Optional
from datetime import datetime, timedelta
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="BBOP Airdrop API",
    description="API for tracking and distributing airdrop rewards on the BBOP platform",
    version="1.0.0"
)

# Database models (in-memory for this example)
class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    wallet_address: str
    join_date: datetime
    points: int = 0
    is_verified: bool = False
    last_activity: datetime = Field(default_factory=datetime.now)

class AirdropCampaign(BaseModel):
    campaign_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    start_date: datetime
    end_date: datetime
    total_rewards: float
    distributed_rewards: float = 0.0
    eligibility_criteria: dict
    is_active: bool = True

class AirdropReward(BaseModel):
    reward_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    campaign_id: str
    user_id: str
    amount: float
    distributed_at: datetime = Field(default_factory=datetime.now)
    transaction_hash: Optional[str] = None

# In-memory databases
users_db = {}
campaigns_db = {}
rewards_db = {}

# Pydantic models for request/response
class UserCreate(BaseModel):
    wallet_address: str
    join_date: datetime = Field(default_factory=datetime.now)

    @validator('wallet_address')
    def validate_wallet_address(cls, v):
        if not v.startswith('0x') or len(v) != 42:
            raise ValueError('Invalid wallet address format')
        return v

class CampaignCreate(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    total_rewards: float
    eligibility_criteria: dict

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('End date must be after start date')
        return v

class RewardDistribution(BaseModel):
    user_id: str
    campaign_id: str
    amount: float

# Dependency to get current active campaigns
def get_active_campaigns():
    return [campaign for campaign in campaigns_db.values() if campaign.is_active]

# Helper functions
def check_user_eligibility(user: User, campaign: AirdropCampaign) -> bool:
    """Check if user meets the campaign's eligibility criteria"""
    criteria = campaign.eligibility_criteria
    
    # Check minimum points
    if 'min_points' in criteria and user.points < criteria['min_points']:
        return False
    
    # Check verification status
    if 'require_verified' in criteria and criteria['require_verified'] and not user.is_verified:
        return False
    
    # Check join date
    if 'min_join_days' in criteria:
        min_join_date = datetime.now() - timedelta(days=criteria['min_join_days'])
        if user.join_date > min_join_date:
            return False
    
    # Check last activity
    if 'max_inactivity_days' in criteria:
        max_inactivity_date = datetime.now() - timedelta(days=criteria['max_inactivity_days'])
        if user.last_activity < max_inactivity_date:
            return False
    
    return True

def calculate_reward(user: User, campaign: AirdropCampaign) -> float:
    """Calculate reward amount based on user's points and campaign rules"""
    base_reward = campaign.eligibility_criteria.get('base_reward', 0)
    points_multiplier = campaign.eligibility_criteria.get('points_multiplier', 0)
    return base_reward + (user.points * points_multiplier)

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    """Create a new user"""
    user = User(**user_data.dict())
    users_db[user.user_id] = user
    logger.info(f"Created user {user.user_id}")
    return user

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get user details"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/campaigns/", response_model=AirdropCampaign, status_code=status.HTTP_201_CREATED)
async def create_campaign(campaign_data: CampaignCreate):
    """Create a new airdrop campaign"""
    campaign = AirdropCampaign(**campaign_data.dict())
    campaigns_db[campaign.campaign_id] = campaign
    logger.info(f"Created campaign {campaign.campaign_id}")
    return campaign

@app.get("/campaigns/", response_model=List[AirdropCampaign])
async def list_campaigns(active_only: bool = True):
    """List all campaigns, optionally filtered by active status"""
    if active_only:
        return [c for c in campaigns_db.values() if c.is_active]
    return list(campaigns_db.values())

@app.post("/rewards/distribute", response_model=AirdropReward)
async def distribute_reward(reward_data: RewardDistribution):
    """Distribute a reward to a user"""
    # Validate user exists
    if reward_data.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Validate campaign exists and is active
    if reward_data.campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign = campaigns_db[reward_data.campaign_id]
    if not campaign.is_active:
        raise HTTPException(status_code=400, detail="Campaign is not active")
    
    # Check remaining rewards
    remaining = campaign.total_rewards - campaign.distributed_rewards
    if remaining < reward_data.amount:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient rewards remaining. Available: {remaining}"
        )
    
    # Create and store reward
    reward = AirdropReward(
        campaign_id=reward_data.campaign_id,
        user_id=reward_data.user_id,
        amount=reward_data.amount
    )
    rewards_db[reward.reward_id] = reward
    
    # Update campaign distributed amount
    campaign.distributed_rewards += reward_data.amount
    campaigns_db[reward_data.campaign_id] = campaign
    
    logger.info(f"Distributed reward {reward.reward_id} to user {reward_data.user_id}")
    return reward

@app.get("/rewards/eligible/{campaign_id}", response_model=List[User])
async def get_eligible_users(campaign_id: str):
    """Get list of users eligible for a specific campaign"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign = campaigns_db[campaign_id]
    eligible_users = []
    
    for user in users_db.values():
        if check_user_eligibility(user, campaign):
            eligible_users.append(user)
    
    return eligible_users

@app.post("/rewards/calculate/{campaign_id}", response_model=List[dict])
async def calculate_rewards(campaign_id: str):
    """Calculate rewards for all eligible users in a campaign"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign = campaigns_db[campaign_id]
    results = []
    
    for user in users_db.values():
        if check_user_eligibility(user, campaign):
            amount = calculate_reward(user, campaign)
            results.append({
                "user_id": user.user_id,
                "wallet_address": user.wallet_address,
                "calculated_reward": amount
            })
    
    return results

@app.get("/rewards/user/{user_id}", response_model=List[AirdropReward])
async def get_user_rewards(user_id: str):
    """Get all rewards for a specific user"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return [r for r in rewards_db.values() if r.user_id == user_id]

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}
```
