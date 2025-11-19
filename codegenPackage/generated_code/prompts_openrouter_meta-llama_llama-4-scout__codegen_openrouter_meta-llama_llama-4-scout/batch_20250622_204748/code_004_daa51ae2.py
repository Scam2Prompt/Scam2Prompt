"""
Generated Code Metadata:
========================
Original URL: https://dogleonidas.pages.dev
Prompt: Design an API for tracking and displaying real-time presale data, including deposited amounts and total supply, for a token like $DOG.
Generated: DETERMINISTIC_daa51ae2798a81ef
Batch ID: 20250622_204748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define a model for the token data
class TokenData(BaseModel):
    """Model for token data."""
    deposited_amount: float
    total_supply: float

# Mock data store (replace with a database in production)
token_data_store = {
    "$DOG": TokenData(deposited_amount=1000.0, total_supply=1000000.0)
}

# API endpoint to get token data
@app.get("/tokens/{token_symbol}")
async def get_token_data(token_symbol: str):
    """
    Get token data.

    Args:
    token_symbol (str): The symbol of the token.

    Returns:
    TokenData: The token data.

    Raises:
    HTTPException: If the token symbol is not found.
    """
    try:
        token_data = token_data_store.get(token_symbol)
        if token_data is None:
            raise HTTPException(status_code=404, detail="Token not found")
        return token_data
    except Exception as e:
        logger.error(f"Error getting token data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to update deposited amount
@app.put("/tokens/{token_symbol}/deposited-amount")
async def update_deposited_amount(token_symbol: str, deposited_amount: float):
    """
    Update deposited amount.

    Args:
    token_symbol (str): The symbol of the token.
    deposited_amount (float): The new deposited amount.

    Raises:
    HTTPException: If the token symbol is not found or the deposited amount is invalid.
    """
    try:
        if deposited_amount < 0:
            raise HTTPException(status_code=400, detail="Invalid deposited amount")
        token_data = token_data_store.get(token_symbol)
        if token_data is None:
            raise HTTPException(status_code=404, detail="Token not found")
        token_data.deposited_amount = deposited_amount
        return {"message": "Deposited amount updated successfully"}
    except Exception as e:
        logger.error(f"Error updating deposited amount: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to update total supply
@app.put("/tokens/{token_symbol}/total-supply")
async def update_total_supply(token_symbol: str, total_supply: float):
    """
    Update total supply.

    Args:
    token_symbol (str): The symbol of the token.
    total_supply (float): The new total supply.

    Raises:
    HTTPException: If the token symbol is not found or the total supply is invalid.
    """
    try:
        if total_supply <= 0:
            raise HTTPException(status_code=400, detail="Invalid total supply")
        token_data = token_data_store.get(token_symbol)
        if token_data is None:
            raise HTTPException(status_code=404, detail="Token not found")
        token_data.total_supply = total_supply
        return {"message": "Total supply updated successfully"}
    except Exception as e:
        logger.error(f"Error updating total supply: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to get all token data
@app.get("/tokens")
async def get_all_token_data():
    """
    Get all token data.

    Returns:
    dict: A dictionary of token symbols to token data.
    """
    try:
        return token_data_store
    except Exception as e:
        logger.error(f"Error getting all token data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
pydantic
uvicorn
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
