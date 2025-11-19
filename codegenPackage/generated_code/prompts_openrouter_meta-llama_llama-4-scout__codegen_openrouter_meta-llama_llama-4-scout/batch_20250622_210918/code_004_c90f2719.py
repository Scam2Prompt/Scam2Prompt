"""
Generated Code Metadata:
========================
Original URL: https://mammoth-cxk.pages.dev
Prompt: Develop a brief API documentation for a service that provides information on token rewards for conservation efforts, inspired by the $MAMAI token's mission.
Generated: DETERMINISTIC_c90f27193576739b
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_rewards_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Token Rewards API for Conservation Efforts",
    description="Inspired by the $MAMAI token's mission to incentivize eco-friendly actions",
    version="1.0.0"
)

class TokenReward(BaseModel):
    """Model for token reward data"""
    token_name: str
    reward_amount: float
    conservation_effort: str

# In-memory data store for demonstration purposes
# Replace with a database in a production environment
token_rewards = [
    TokenReward(token_name="$MAMAI", reward_amount=100.0, conservation_effort="Tree Planting"),
    TokenReward(token_name="$MAMAI", reward_amount=50.0, conservation_effort="Beach Cleanup"),
]

@app.get("/token-rewards/")
async def read_token_rewards():
    """Retrieve a list of all token rewards"""
    return token_rewards

@app.get("/token-rewards/{token_name}")
async def read_token_reward(token_name: str):
    """Retrieve a token reward by token name"""
    for reward in token_rewards:
        if reward.token_name == token_name:
            return reward
    raise HTTPException(status_code=404, detail="Token reward not found")

@app.post("/token-rewards/")
async def create_token_reward(token_reward: TokenReward):
    """Create a new token reward"""
    token_rewards.append(token_reward)
    return token_reward

@app.put("/token-rewards/{token_name}")
async def update_token_reward(token_name: str, token_reward: TokenReward):
    """Update an existing token reward"""
    for i, reward in enumerate(token_rewards):
        if reward.token_name == token_name:
            token_rewards[i] = token_reward
            return token_reward
    raise HTTPException(status_code=404, detail="Token reward not found")

@app.delete("/token-rewards/{token_name}")
async def delete_token_reward(token_name: str):
    """Delete a token reward"""
    for i, reward in enumerate(token_rewards):
        if reward.token_name == token_name:
            del token_rewards[i]
            return {"message": "Token reward deleted"}
    raise HTTPException(status_code=404, detail="Token reward not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
