"""
Generated Code Metadata:
========================
Original URL: https://44-cm7.pages.dev
Prompt: Design a RESTful API for managing collectible items, including features like claiming and selling, using the Pudgy Penguins "GoldFeathers" as an example.
Generated: DETERMINISTIC_2cf64fb2dea61ab7
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID
from enum import Enum

app = FastAPI(
    title="Collectible Items API",
    description="Manage collectible items, including claiming and selling",
    version="1.0.0"
)

# Define a custom enum for transaction types
class TransactionType(str, Enum):
    claim = "claim"
    sell = "sell"

# Define a Pydantic model for collectible items
class CollectibleItem(BaseModel):
    id: UUID
    name: str
    description: str
    owner: str | None = None

# Define a Pydantic model for transactions
class Transaction(BaseModel):
    item_id: UUID
    transaction_type: TransactionType
    buyer: str | None = None
    seller: str | None = None

# In-memory storage for collectible items (replace with a database in production)
collectible_items: List[CollectibleItem] = [
    CollectibleItem(id=UUID("0f1f1f1f-1f1f-1f1f-1f1f-1f1f1f1f1f1f"), name="GoldFeathers", description="Rare Pudgy Penguins GoldFeathers"),
]

# In-memory storage for transactions (replace with a database in production)
transactions: List[Transaction] = []

# API endpoint to get all collectible items
@app.get("/items/", response_model=List[CollectibleItem])
async def get_collectible_items():
    return collectible_items

# API endpoint to get a collectible item by ID
@app.get("/items/{item_id}", response_model=CollectibleItem)
async def get_collectible_item(item_id: UUID):
    item = next((item for item in collectible_items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

# API endpoint to claim a collectible item
@app.post("/items/{item_id}/claim", response_model=Transaction)
async def claim_collectible_item(item_id: UUID):
    item = next((item for item in collectible_items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    if item.owner is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item is already owned")
    item.owner = "claimer"
    transaction = Transaction(item_id=item_id, transaction_type=TransactionType.claim)
    transactions.append(transaction)
    return transaction

# API endpoint to sell a collectible item
@app.post("/items/{item_id}/sell", response_model=Transaction)
async def sell_collectible_item(item_id: UUID, buyer: str):
    item = next((item for item in collectible_items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    if item.owner is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item is not owned")
    if item.owner == buyer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Buyer and seller cannot be the same")
    transaction = Transaction(item_id=item_id, transaction_type=TransactionType.sell, buyer=buyer, seller=item.owner)
    transactions.append(transaction)
    item.owner = buyer
    return transaction

# API endpoint to get all transactions
@app.get("/transactions/", response_model=List[Transaction])
async def get_transactions():
    return transactions
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
