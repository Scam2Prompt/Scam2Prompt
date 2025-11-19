"""
Generated Code Metadata:
========================
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Design an API for tracking cryptocurrency pre-sale data, including metrics like pre-sale cap, token supply, and exchange rates, using the $BCKR pre-sale as a reference.
Generated: DETERMINISTIC_0209fb2b34ea7a9e
Batch ID: 20250622_205836
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

app = FastAPI(
    title="Cryptocurrency Pre-Sale Tracker",
    description="API for tracking cryptocurrency pre-sale data",
    version="1.0.0"
)

class PreSale(BaseModel):
    """Pre-sale data model"""
    id: int
    name: str
    cap: float  # pre-sale cap
    token_supply: int  # total token supply
    exchange_rate: float  # exchange rate

class PreSaleData(BaseModel):
    """Pre-sale data with metrics"""
    pre_sale: PreSale
    metrics: dict

# In-memory data store (replace with a database in production)
pre_sales: List[PreSale] = [
    PreSale(
        id=1,
        name="$BCKR Pre-Sale",
        cap=1000000.0,
        token_supply=1000000,
        exchange_rate=0.1
    )
]

@app.get("/pre-sales/")
async def get_pre_sales():
    """Retrieve a list of all pre-sales"""
    return pre_sales

@app.get("/pre-sales/{pre_sale_id}")
async def get_pre_sale(pre_sale_id: int):
    """Retrieve a pre-sale by ID"""
    for pre_sale in pre_sales:
        if pre_sale.id == pre_sale_id:
            return pre_sale
    raise HTTPException(status_code=404, detail="Pre-sale not found")

@app.post("/pre-sales/")
async def create_pre_sale(pre_sale: PreSale):
    """Create a new pre-sale"""
    pre_sales.append(pre_sale)
    return pre_sale

@app.put("/pre-sales/{pre_sale_id}")
async def update_pre_sale(pre_sale_id: int, pre_sale: PreSale):
    """Update an existing pre-sale"""
    for i, existing_pre_sale in enumerate(pre_sales):
        if existing_pre_sale.id == pre_sale_id:
            pre_sales[i] = pre_sale
            return pre_sale
    raise HTTPException(status_code=404, detail="Pre-sale not found")

@app.delete("/pre-sales/{pre_sale_id}")
async def delete_pre_sale(pre_sale_id: int):
    """Delete a pre-sale"""
    for i, existing_pre_sale in enumerate(pre_sales):
        if existing_pre_sale.id == pre_sale_id:
            del pre_sales[i]
            return {"message": "Pre-sale deleted"}
    raise HTTPException(status_code=404, detail="Pre-sale not found")

@app.get("/pre-sales/{pre_sale_id}/metrics")
async def get_pre_sale_metrics(pre_sale_id: int):
    """Retrieve metrics for a pre-sale"""
    for pre_sale in pre_sales:
        if pre_sale.id == pre_sale_id:
            metrics = {
                "market_cap": pre_sale.cap * pre_sale.exchange_rate,
                "token_velocity": pre_sale.token_supply / pre_sale.cap
            }
            return PreSaleData(pre_sale=pre_sale, metrics=metrics)
    raise HTTPException(status_code=404, detail="Pre-sale not found")

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
