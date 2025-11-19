"""
Generated Code Metadata:
========================
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Design an API for retrieving 99Bitcoins token rewards, taking into account the user's staking pool percentage and estimated rewards per annum.
Generated: DETERMINISTIC_a78d001d53d96ac1
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
from typing import Optional

app = FastAPI(
    title="99Bitcoins Token Rewards API",
    description="API for retrieving 99Bitcoins token rewards",
    version="1.0.0"
)

class StakingPoolRequest(BaseModel):
    """Request model for staking pool information"""
    pool_percentage: float
    estimated_rewards_per_annum: float

class TokenRewardsResponse(BaseModel):
    """Response model for token rewards"""
    token_rewards: float

@app.get("/token-rewards/", response_model=TokenRewardsResponse)
async def get_token_rewards(request: StakingPoolRequest):
    """
    Retrieves 99Bitcoins token rewards based on user's staking pool percentage and estimated rewards per annum.

    Args:
    - pool_percentage (float): User's staking pool percentage
    - estimated_rewards_per_annum (float): Estimated rewards per annum

    Returns:
    - token_rewards (float): Calculated token rewards
    """
    try:
        # Validate input values
        if request.pool_percentage < 0 or request.pool_percentage > 100:
            raise HTTPException(status_code=400, detail="Pool percentage must be between 0 and 100")

        if request.estimated_rewards_per_annum < 0:
            raise HTTPException(status_code=400, detail="Estimated rewards per annum must be non-negative")

        # Calculate token rewards
        token_rewards = (request.pool_percentage / 100) * request.estimated_rewards_per_annum

        return TokenRewardsResponse(token_rewards=token_rewards)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handles HTTP exceptions"""
    return {"error": exc.detail}, exc.status_code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py (for testing)
from token_rewards_api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_token_rewards():
    response = client.get("/token-rewards/", params={
        "pool_percentage": 10.0,
        "estimated_rewards_per_annum": 1000.0
    })

    assert response.status_code == 200
    assert response.json()["token_rewards"] == 100.0

def test_get_token_rewards_invalid_pool_percentage():
    response = client.get("/token-rewards/", params={
        "pool_percentage": -10.0,
        "estimated_rewards_per_annum": 1000.0
    })

    assert response.status_code == 400
    assert response.json()["error"] == "Pool percentage must be between 0 and 100"

def test_get_token_rewards_invalid_estimated_rewards():
    response = client.get("/token-rewards/", params={
        "pool_percentage": 10.0,
        "estimated_rewards_per_annum": -1000.0
    })

    assert response.status_code == 400
    assert response.json()["error"] == "Estimated rewards per annum must be non-negative"

if __name__ == "__main__":
    test_get_token_rewards()
    test_get_token_rewards_invalid_pool_percentage()
    test_get_token_rewards_invalid_estimated_rewards()
```
