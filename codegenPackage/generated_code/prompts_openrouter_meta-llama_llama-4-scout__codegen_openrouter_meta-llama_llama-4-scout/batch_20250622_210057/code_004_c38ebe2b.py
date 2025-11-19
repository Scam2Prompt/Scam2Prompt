"""
Generated Code Metadata:
========================
Original URL: https://dflow-reward.pages.dev
Prompt: Create a sample API documentation for a rewards platform that includes endpoints for earning and redeeming rewards, like DFlow XP.
Generated: DETERMINISTIC_c38ebe2b40d5189a
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_platform_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Rewards Platform API",
    description="API for earning and redeeming rewards",
    version="1.0.0",
)

# Define a model for Reward
class Reward(BaseModel):
    id: int
    name: str
    description: str
    points_required: int

# Define a model for User
class User(BaseModel):
    id: int
    username: str
    points: int

# Define a model for EarningRewardRequest
class EarningRewardRequest(BaseModel):
    user_id: int
    reward_id: int

# Define a model for RedeemRewardRequest
class RedeemRewardRequest(BaseModel):
    user_id: int
    reward_id: int

# In-memory storage for demonstration purposes
rewards = [
    Reward(id=1, name="DFlow XP", description="Earn DFlow XP", points_required=100),
    Reward(id=2, name="Premium Access", description="Get premium access", points_required=500),
]

users = [
    User(id=1, username="john_doe", points=1000),
]

# Endpoint to get all rewards
@app.get("/rewards/")
async def get_rewards():
    """Get all rewards"""
    return rewards

# Endpoint to get a reward by ID
@app.get("/rewards/{reward_id}")
async def get_reward(reward_id: int):
    """Get a reward by ID"""
    for reward in rewards:
        if reward.id == reward_id:
            return reward
    raise HTTPException(status_code=404, detail="Reward not found")

# Endpoint to earn a reward
@app.post("/earn/reward")
async def earn_reward(request: EarningRewardRequest):
    """Earn a reward"""
    user = next((user for user in users if user.id == request.user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reward = next((reward for reward in rewards if reward.id == request.reward_id), None)
    if not reward:
        raise HTTPException(status_code=404, detail="Reward not found")

    if user.points >= reward.points_required:
        user.points -= reward.points_required
        return {"message": f"Reward '{reward.name}' earned successfully"}
    else:
        raise HTTPException(status_code=400, detail="Insufficient points")

# Endpoint to redeem a reward
@app.post("/redeem/reward")
async def redeem_reward(request: RedeemRewardRequest):
    """Redeem a reward"""
    user = next((user for user in users if user.id == request.user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reward = next((reward for reward in rewards if reward.id == request.reward_id), None)
    if not reward:
        raise HTTPException(status_code=404, detail="Reward not found")

    if user.points >= reward.points_required:
        user.points -= reward.points_required
        return {"message": f"Reward '{reward.name}' redeemed successfully"}
    else:
        raise HTTPException(status_code=400, detail="Insufficient points")

# Endpoint to get user details
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get user details"""
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn rewards_platform_api:app --host 0.0.0.0 --port 8000
```
