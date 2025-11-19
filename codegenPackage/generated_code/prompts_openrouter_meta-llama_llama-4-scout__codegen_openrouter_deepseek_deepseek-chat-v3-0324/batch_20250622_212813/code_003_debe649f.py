"""
Generated Code Metadata:
========================
Original URL: https://sosphon.xyz
Prompt: Design an API to manage $SOPH staking positions, including staking, unstaking, and claiming rewards, while maintaining attractive returns as the total stake rate grows.
Generated: DETERMINISTIC_debe649f53d99c4c
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Standard library imports
import time
from typing import Dict, List, Optional, Tuple
from decimal import Decimal, getcontext

# Third-party imports
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator

# Initialize FastAPI app
app = FastAPI(
    title="SOPH Staking API",
    description="API for managing SOPH token staking positions",
    version="1.0.0"
)

# Configure decimal precision
getcontext().prec = 18

# Constants
MIN_STAKE_AMOUNT = Decimal('100')  # Minimum stake amount in SOPH
MIN_STAKE_DURATION = 86400  # Minimum stake duration in seconds (1 day)
BASE_APY = Decimal('0.05')  # Base APY (5%)
APY_SCALING_FACTOR = Decimal('0.0001')  # APY increases by 0.01% per SOPH staked

# In-memory storage (replace with database in production)
staking_positions: Dict[str, Dict] = {}
total_staked: Decimal = Decimal('0')
reward_pool: Decimal = Decimal('1000000')  # Initial reward pool

class StakeRequest(BaseModel):
    amount: Decimal = Field(..., gt=0, description="Amount of SOPH to stake")
    duration: int = Field(..., ge=MIN_STAKE_DURATION, description="Staking duration in seconds")
    wallet_address: str = Field(..., min_length=42, max_length=42, description="User's wallet address")

    @validator('amount')
    def validate_amount(cls, v):
        if v < MIN_STAKE_AMOUNT:
            raise ValueError(f"Minimum stake amount is {MIN_STAKE_AMOUNT} SOPH")
        return v

class UnstakeRequest(BaseModel):
    position_id: str = Field(..., description="ID of the staking position to unstake")
    wallet_address: str = Field(..., min_length=42, max_length=42, description="User's wallet address")

class ClaimRequest(BaseModel):
    position_id: str = Field(..., description="ID of the staking position to claim rewards from")
    wallet_address: str = Field(..., min_length=42, max_length=42, description="User's wallet address")

class StakingPosition(BaseModel):
    position_id: str
    wallet_address: str
    amount: Decimal
    duration: int
    start_time: int
    end_time: int
    claimed_rewards: Decimal = Decimal('0')
    last_claim_time: Optional[int] = None

class RewardInfo(BaseModel):
    position_id: str
    pending_rewards: Decimal
    current_apy: Decimal

@app.post("/stake", response_model=StakingPosition, status_code=status.HTTP_201_CREATED)
async def stake_tokens(stake_request: StakeRequest):
    """Create a new staking position."""
    global total_staked, reward_pool
    
    position_id = f"pos_{int(time.time())}_{stake_request.wallet_address[-6:]}"
    start_time = int(time.time())
    end_time = start_time + stake_request.duration
    
    new_position = {
        "position_id": position_id,
        "wallet_address": stake_request.wallet_address,
        "amount": stake_request.amount,
        "duration": stake_request.duration,
        "start_time": start_time,
        "end_time": end_time,
        "claimed_rewards": Decimal('0'),
        "last_claim_time": None
    }
    
    staking_positions[position_id] = new_position
    total_staked += stake_request.amount
    
    return new_position

@app.post("/unstake", response_model=StakingPosition)
async def unstake_tokens(unstake_request: UnstakeRequest):
    """Unstake tokens from a position and claim any pending rewards."""
    global total_staked
    
    position = staking_positions.get(unstake_request.position_id)
    if not position:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staking position not found"
        )
    
    if position["wallet_address"] != unstake_request.wallet_address:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wallet address does not match staking position"
        )
    
    current_time = int(time.time())
    if current_time < position["end_time"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Staking period has not ended yet"
        )
    
    # Claim any remaining rewards
    rewards = _calculate_rewards(position)
    position["claimed_rewards"] += rewards
    _update_reward_pool(rewards)
    
    total_staked -= position["amount"]
    return position

@app.post("/claim", response_model=RewardInfo)
async def claim_rewards(claim_request: ClaimRequest):
    """Claim rewards from a staking position."""
    position = staking_positions.get(claim_request.position_id)
    if not position:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staking position not found"
        )
    
    if position["wallet_address"] != claim_request.wallet_address:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wallet address does not match staking position"
        )
    
    rewards = _calculate_rewards(position)
    if rewards <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No rewards available to claim"
        )
    
    position["claimed_rewards"] += rewards
    position["last_claim_time"] = int(time.time())
    _update_reward_pool(rewards)
    
    current_apy = _calculate_current_apy()
    return {
        "position_id": position["position_id"],
        "pending_rewards": rewards,
        "current_apy": current_apy
    }

@app.get("/positions/{wallet_address}", response_model=List[StakingPosition])
async def get_positions(wallet_address: str):
    """Get all staking positions for a wallet address."""
    return [pos for pos in staking_positions.values() if pos["wallet_address"] == wallet_address]

@app.get("/rewards/{position_id}", response_model=RewardInfo)
async def get_reward_info(position_id: str):
    """Get reward information for a staking position."""
    position = staking_positions.get(position_id)
    if not position:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staking position not found"
        )
    
    rewards = _calculate_rewards(position)
    current_apy = _calculate_current_apy()
    
    return {
        "position_id": position_id,
        "pending_rewards": rewards,
        "current_apy": current_apy
    }

@app.get("/pool_info", response_model=Dict[str, Decimal])
async def get_pool_info():
    """Get information about the staking pool."""
    return {
        "total_staked": total_staked,
        "reward_pool": reward_pool,
        "current_apy": _calculate_current_apy()
    }

def _calculate_rewards(position: Dict) -> Decimal:
    """Calculate pending rewards for a staking position."""
    current_time = int(time.time())
    last_claim = position.get("last_claim_time", position["start_time"])
    
    if current_time <= last_claim:
        return Decimal('0')
    
    staked_amount = position["amount"]
    duration = min(current_time, position["end_time"]) - last_claim
    apy = _calculate_apy_at_time(last_claim)
    
    # Calculate rewards: (amount * APY * time) / (seconds in year)
    seconds_in_year = Decimal('31536000')
    rewards = (staked_amount * apy * Decimal(duration)) / seconds_in_year
    
    return rewards

def _calculate_apy_at_time(timestamp: int) -> Decimal:
    """Calculate the APY at a specific point in time."""
    # In a real implementation, you would query historical total_staked
    # For simplicity, we use current total_staked in this example
    return BASE_APY + (total_staked * APY_SCALING_FACTOR)

def _calculate_current_apy() -> Decimal:
    """Calculate the current APY based on total staked."""
    return BASE_APY + (total_staked * APY_SCALING_FACTOR)

def _update_reward_pool(claimed_amount: Decimal):
    """Update the reward pool when rewards are claimed."""
    global reward_pool
    reward_pool -= claimed_amount
    if reward_pool < 0:
        reward_pool = Decimal('0')
```
