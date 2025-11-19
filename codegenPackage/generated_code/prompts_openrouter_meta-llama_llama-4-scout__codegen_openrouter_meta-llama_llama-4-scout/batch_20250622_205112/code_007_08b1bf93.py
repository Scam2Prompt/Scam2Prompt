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
# wallet_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Wallet API",
    description="API for retrieving wallet net worth",
    version="1.0.0"
)

class WalletInsight(BaseModel):
    """Model for wallet insights data"""
    total_assets: float
    total_liabilities: float
    net_worth: float

class WalletNetWorthResponse(BaseModel):
    """Model for wallet net worth response"""
    net_worth: float
    insights: Optional[WalletInsight]

# Sample in-memory data store (replace with actual database or data source)
wallet_insights_data = {
    "wallet_123": WalletInsight(
        total_assets=10000.0,
        total_liabilities=5000.0,
        net_worth=5000.0
    )
}

@app.get("/wallets/{wallet_id}/net-worth")
async def get_wallet_net_worth(wallet_id: str):
    """
    Retrieves the net worth of a wallet.

    Args:
    wallet_id (str): The ID of the wallet.

    Returns:
    WalletNetWorthResponse: The net worth of the wallet and optional insights.

    Raises:
    HTTPException: If the wallet is not found.
    """
    try:
        insights = wallet_insights_data.get(wallet_id)
        if insights is None:
            raise HTTPException(status_code=404, detail="Wallet not found")

        response = WalletNetWorthResponse(
            net_worth=insights.net_worth,
            insights=insights
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```json
// Sample response
{
  "net_worth": 5000.0,
  "insights": {
    "total_assets": 10000.0,
    "total_liabilities": 5000.0,
    "net_worth": 5000.0
  }
}
```
