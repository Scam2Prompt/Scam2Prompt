"""
Generated Code Metadata:
========================
Original URL: https://dre-8x7.pages.dev
Prompt: Design an API for a token sale platform that includes endpoints for buying DRE tokens with FTM, given the presale cap and total supply constraints.
Generated: DETERMINISTIC_653104ed6ab94b4b
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

# Define the FastAPI application
app = FastAPI(
    title="DRE Token Sale API",
    description="API for buying DRE tokens with FTM",
    version="1.0.0"
)

# Define the token sale configuration
class TokenSaleConfig:
    def __init__(self, presale_cap: int, total_supply: int):
        """
        Initialize the token sale configuration.

        Args:
        - presale_cap (int): The presale cap in DRE tokens.
        - total_supply (int): The total supply of DRE tokens.
        """
        self.presale_cap = presale_cap
        self.total_supply = total_supply
        self.sold_tokens = 0

# Initialize the token sale configuration
token_sale_config = TokenSaleConfig(presale_cap=1000000, total_supply=2000000)

# Define the request model for buying tokens
class BuyTokensRequest(BaseModel):
    amount: int  # Amount of FTM to spend

# Define the response model for buying tokens
class BuyTokensResponse(BaseModel):
    dre_tokens: int  # Number of DRE tokens purchased
    remaining_ftm: int  # Remaining FTM after purchase

# Define the API endpoint for buying DRE tokens with FTM
@app.post("/buy-tokens", response_model=BuyTokensResponse)
async def buy_tokens(request: BuyTokensRequest):
    try:
        # Calculate the number of DRE tokens to purchase
        dre_tokens = request.amount // 10  # Assuming 1 FTM = 10 DRE tokens
        if dre_tokens > token_sale_config.presale_cap - token_sale_config.sold_tokens:
            raise HTTPException(status_code=400, detail="Insufficient tokens available")

        # Update the sold tokens count
        token_sale_config.sold_tokens += dre_tokens

        # Calculate the remaining FTM
        remaining_ftm = request.amount % 10

        # Return the response
        return BuyTokensResponse(dre_tokens=dre_tokens, remaining_ftm=remaining_ftm)
    except Exception as e:
        # Handle any exceptions
        raise HTTPException(status_code=500, detail=str(e))

# Define the API endpoint for getting the token sale status
@app.get("/token-sale-status")
async def get_token_sale_status():
    try:
        # Return the token sale status
        return JSONResponse(
            content={
                "presale_cap": token_sale_config.presale_cap,
                "total_supply": token_sale_config.total_supply,
                "sold_tokens": token_sale_config.sold_tokens,
                "remaining_tokens": token_sale_config.total_supply - token_sale_config.sold_tokens
            },
            media_type="application/json"
        )
    except Exception as e:
        # Handle any exceptions
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
