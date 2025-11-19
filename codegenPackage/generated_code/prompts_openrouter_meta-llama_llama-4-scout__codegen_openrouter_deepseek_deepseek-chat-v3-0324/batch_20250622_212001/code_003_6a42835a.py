"""
Generated Code Metadata:
========================
Original URL: https://staking.chainbase.co
Prompt: "Design an API endpoint for users to query their staking balances on a platform like Chainbase, including request and response schema."
Generated: DETERMINISTIC_6a42835a59d4cb46
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Staking Balance API",
    description="API for querying user staking balances on Chainbase-like platforms",
    version="1.0.0"
)

# Database mock (in production, replace with actual database connection)
mock_db = {
    "0x1234567890abcdef": {
        "total_staked": 1000.5,
        "rewards": 50.2,
        "last_updated": "2023-10-15T12:00:00Z"
    },
    "0xabcdef1234567890": {
        "total_staked": 2500.75,
        "rewards": 125.3,
        "last_updated": "2023-10-14T15:30:00Z"
    }
}

class StakingBalanceRequest(BaseModel):
    """Request schema for staking balance query"""
    wallet_address: str
    include_rewards: Optional[bool] = True

class StakingBalanceResponse(BaseModel):
    """Response schema for staking balance"""
    wallet_address: str
    total_staked: float
    rewards: Optional[float] = None
    last_updated: datetime
    success: bool
    message: Optional[str] = None

@app.get(
    "/staking/balance",
    response_model=StakingBalanceResponse,
    summary="Get staking balance for a wallet",
    description="Returns the staking balance and optional rewards for a given wallet address",
    tags=["Staking"]
)
async def get_staking_balance(request: StakingBalanceRequest):
    """
    Retrieve staking balance information for a given wallet address.
    
    Args:
        request (StakingBalanceRequest): Contains wallet_address and include_rewards flag
    
    Returns:
        StakingBalanceResponse: Contains staking details or error message
    """
    try:
        wallet_address = request.wallet_address.lower()
        
        if wallet_address not in mock_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Wallet address not found in staking records"
            )
        
        data = mock_db[wallet_address]
        response_data = {
            "wallet_address": wallet_address,
            "total_staked": data["total_staked"],
            "last_updated": data["last_updated"],
            "success": True
        }
        
        if request.include_rewards:
            response_data["rewards"] = data["rewards"]
        
        return StakingBalanceResponse(**response_data)
    
    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {str(e)}"
        )

# For production, you would also want to add:
# - Authentication middleware
# - Rate limiting
# - Proper database connection handling
# - Logging
# - Caching for frequently accessed data
# - Input validation beyond Pydantic
```
