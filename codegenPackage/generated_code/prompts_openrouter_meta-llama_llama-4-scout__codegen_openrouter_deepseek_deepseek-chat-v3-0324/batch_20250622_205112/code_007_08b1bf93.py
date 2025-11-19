"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Propose an API endpoint for retrieving wallet net worth and provide a sample response based on Bluwhale's wallet insights data.
Generated: DETERMINISTIC_08b1bf93edb6eb34
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Wallet Insights API",
    description="API for retrieving wallet net worth and insights",
    version="1.0.0"
)

class Asset(BaseModel):
    symbol: str
    name: str
    amount: float
    value_usd: float
    price_usd: float

class WalletNetWorthResponse(BaseModel):
    wallet_address: str
    total_net_worth_usd: float
    assets: list[Asset]
    last_updated: datetime
    chain: str
    error: Optional[str] = None

@app.get(
    "/wallets/{wallet_address}/net-worth",
    response_model=WalletNetWorthResponse,
    summary="Get wallet net worth",
    description="Retrieve the total net worth and asset breakdown for a given wallet address",
    tags=["Wallet Insights"]
)
async def get_wallet_net_worth(wallet_address: str, chain: str = "ethereum"):
    """
    Retrieve wallet net worth and asset breakdown
    
    Args:
        wallet_address: The wallet address to query
        chain: The blockchain network (default: ethereum)
    
    Returns:
        WalletNetWorthResponse with net worth details
    
    Raises:
        HTTPException: If wallet data cannot be retrieved
    """
    try:
        # In a real implementation, this would query Bluwhale's data sources
        # Here we return mock data for demonstration purposes
        mock_response = {
            "wallet_address": wallet_address,
            "total_net_worth_usd": 12543.21,
            "assets": [
                {
                    "symbol": "ETH",
                    "name": "Ethereum",
                    "amount": 2.5,
                    "value_usd": 7500.00,
                    "price_usd": 3000.00
                },
                {
                    "symbol": "WBTC",
                    "name": "Wrapped Bitcoin",
                    "amount": 0.1,
                    "value_usd": 4000.00,
                    "price_usd": 40000.00
                },
                {
                    "symbol": "USDC",
                    "name": "USD Coin",
                    "amount": 1043.21,
                    "value_usd": 1043.21,
                    "price_usd": 1.00
                }
            ],
            "last_updated": datetime.utcnow(),
            "chain": chain
        }
        
        return WalletNetWorthResponse(**mock_response)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving wallet data: {str(e)}"
        )

# Sample response:
"""
{
    "wallet_address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "total_net_worth_usd": 12543.21,
    "assets": [
        {
            "symbol": "ETH",
            "name": "Ethereum",
            "amount": 2.5,
            "value_usd": 7500.00,
            "price_usd": 3000.00
        },
        {
            "symbol": "WBTC",
            "name": "Wrapped Bitcoin",
            "amount": 0.1,
            "value_usd": 4000.00,
            "price_usd": 40000.00
        },
        {
            "symbol": "USDC",
            "name": "USD Coin",
            "amount": 1043.21,
            "value_usd": 1043.21,
            "price_usd": 1.00
        }
    ],
    "last_updated": "2023-11-15T12:34:56.789Z",
    "chain": "ethereum"
}
"""
```
