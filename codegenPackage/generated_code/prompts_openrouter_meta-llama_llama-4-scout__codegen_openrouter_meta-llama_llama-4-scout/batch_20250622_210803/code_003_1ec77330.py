"""
Generated Code Metadata:
========================
Original URL: https://asd-col.pages.dev
Prompt: Design an API for tracking and displaying real-time presale data, including deposited ETH and $DOG token allocations.
Generated: DETERMINISTIC_1ec77330ada51883
Batch ID: 20250622_210803
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
from typing import List
import logging
from logging.config import dictConfig

# Logging configuration
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
})

# Initialize logger
logger = logging.getLogger()

app = FastAPI()

class TokenAllocation(BaseModel):
    """Model for token allocation"""
    address: str
    eth_deposited: float
    dog_token_allocation: float

class PresaleData(BaseModel):
    """Model for presale data"""
    total_eth_deposited: float
    total_dog_token_allocation: float
    allocations: List[TokenAllocation]

# In-memory data store (replace with a database in production)
presale_data = PresaleData(
    total_eth_deposited=0.0,
    total_dog_token_allocation=0.0,
    allocations=[]
)

@app.get("/presale/data")
async def get_presale_data():
    """Get presale data"""
    return presale_data

@app.post("/presale/deposit")
async def deposit_eth(address: str, amount: float):
    """Deposit ETH"""
    try:
        # Validate input
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Invalid deposit amount")

        # Update in-memory data store
        presale_data.total_eth_deposited += amount
        existing_allocation = next((a for a in presale_data.allocations if a.address == address), None)
        if existing_allocation:
            existing_allocation.eth_deposited += amount
        else:
            presale_data.allocations.append(TokenAllocation(address=address, eth_deposited=amount, dog_token_allocation=0.0))

        logger.info(f"Deposited {amount} ETH from {address}")
        return {"message": "Deposit successful"}
    except Exception as e:
        logger.error(f"Error depositing ETH: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/presale/allocate")
async def allocate_dog_token(address: str, amount: float):
    """Allocate $DOG token"""
    try:
        # Validate input
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Invalid allocation amount")

        # Update in-memory data store
        existing_allocation = next((a for a in presale_data.allocations if a.address == address), None)
        if existing_allocation:
            existing_allocation.dog_token_allocation += amount
            presale_data.total_dog_token_allocation += amount
        else:
            raise HTTPException(status_code=404, detail="Address not found")

        logger.info(f"Allocated {amount} $DOG token to {address}")
        return {"message": "Allocation successful"}
    except Exception as e:
        logger.error(f"Error allocating $DOG token: {str(e)}")
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
# Run with
# uvicorn app:app --host 0.0.0.0 --port 8000
```
