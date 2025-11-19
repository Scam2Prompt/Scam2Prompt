"""
Generated Code Metadata:
========================
Original URL: https://jesse-presales1.pages.dev
Prompt: Design an API for tracking and displaying real-time information about a token sale, including metrics like presale cap, total supply, and exchange rates, as seen on this $JESSE presale page.
Generated: DETERMINISTIC_79c38e0aac9c5e75
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_sale_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Token Sale API",
    description="API for tracking and displaying real-time information about a token sale",
    version="1.0.0"
)

class TokenSale(BaseModel):
    """Model representing a token sale"""
    presale_cap: float
    total_supply: float
    exchange_rate: float
    current_supply: Optional[float] = 0.0
    current_price: Optional[float] = 0.0

class TokenSaleUpdate(BaseModel):
    """Model for updating token sale information"""
    presale_cap: Optional[float]
    total_supply: Optional[float]
    exchange_rate: Optional[float]
    current_supply: Optional[float]
    current_price: Optional[float]

# In-memory storage for demonstration purposes
# Consider replacing with a database in production
token_sale_data = TokenSale(
    presale_cap=1000000.0,
    total_supply=10000000.0,
    exchange_rate=0.1
)

@app.get("/token-sale/")
async def get_token_sale():
    """Retrieve token sale information"""
    return token_sale_data

@app.put("/token-sale/")
async def update_token_sale(update: TokenSaleUpdate):
    """Update token sale information"""
    global token_sale_data
    
    # Update fields if provided
    if update.presale_cap:
        token_sale_data.presale_cap = update.presale_cap
    if update.total_supply:
        token_sale_data.total_supply = update.total_supply
    if update.exchange_rate:
        token_sale_data.exchange_rate = update.exchange_rate
    if update.current_supply:
        token_sale_data.current_supply = update.current_supply
    if update.current_price:
        token_sale_data.current_price = update.current_price
    
    return token_sale_data

@app.get("/token-sale/metrics/")
async def get_token_sale_metrics():
    """Retrieve token sale metrics"""
    if token_sale_data.total_supply == 0:
        raise HTTPException(status_code=400, detail="Total supply is zero")
    
    metrics = {
        "presale_cap": token_sale_data.presale_cap,
        "total_supply": token_sale_data.total_supply,
        "exchange_rate": token_sale_data.exchange_rate,
        "current_supply": token_sale_data.current_supply,
        "current_price": token_sale_data.current_price,
        "sold_out": token_sale_data.current_supply >= token_sale_data.presale_cap,
        "percentage_sold": (token_sale_data.current_supply / token_sale_data.presale_cap) * 100 if token_sale_data.presale_cap > 0 else 0
    }
    
    return metrics

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn token_sale_api:app --host 0.0.0.0 --port 8000
```
