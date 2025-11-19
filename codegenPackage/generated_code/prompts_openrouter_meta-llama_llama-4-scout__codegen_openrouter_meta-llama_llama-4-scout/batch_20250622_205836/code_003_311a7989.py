"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Design an API for tracking cryptocurrency token presales, including fields for presale cap, total supply, and token pricing tiers, inspired by the $ALIEN PRE-SALE webpage.
Generated: DETERMINISTIC_311a79892fbf5452
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_presale_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Cryptocurrency Token Presale API",
    description="API for tracking cryptocurrency token presales",
    version="1.0.0"
)

class TokenPricingTier(BaseModel):
    """Token pricing tier model"""
    tier_name: str
    price: float
    tokens_available: int

class TokenPresale(BaseModel):
    """Token presale model"""
    presale_cap: float
    total_supply: int
    pricing_tiers: List[TokenPricingTier]

# In-memory storage for demonstration purposes
# Replace with a database in a production environment
presales: List[TokenPresale] = []

@app.post("/presales/")
async def create_presale(presale: TokenPresale):
    """Create a new token presale"""
    presales.append(presale)
    return {"message": "Presale created successfully"}

@app.get("/presales/")
async def read_presales():
    """Retrieve all token presales"""
    return presales

@app.get("/presales/{presale_id}")
async def read_presale(presale_id: int):
    """Retrieve a token presale by ID"""
    try:
        return presales[presale_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Presale not found")

@app.put("/presales/{presale_id}")
async def update_presale(presale_id: int, presale: TokenPresale):
    """Update a token presale"""
    try:
        presales[presale_id] = presale
        return {"message": "Presale updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Presale not found")

@app.delete("/presales/{presale_id}")
async def delete_presale(presale_id: int):
    """Delete a token presale"""
    try:
        del presales[presale_id]
        return {"message": "Presale deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Presale not found")

# Example usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py (for testing)

from token_presale_api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_presale():
    presale = {
        "presale_cap": 1000000.0,
        "total_supply": 1000000,
        "pricing_tiers": [
            {"tier_name": "Tier 1", "price": 0.1, "tokens_available": 100000},
            {"tier_name": "Tier 2", "price": 0.2, "tokens_available": 200000}
        ]
    }
    response = client.post("/presales/", json=presale)
    assert response.status_code == 200

def test_read_presales():
    response = client.get("/presales/")
    assert response.status_code == 200

def test_read_presale():
    response = client.get("/presales/0")
    assert response.status_code == 200

def test_update_presale():
    presale = {
        "presale_cap": 1500000.0,
        "total_supply": 1500000,
        "pricing_tiers": [
            {"tier_name": "Tier 1", "price": 0.15, "tokens_available": 150000},
            {"tier_name": "Tier 2", "price": 0.25, "tokens_available": 250000}
        ]
    }
    response = client.put("/presales/0", json=presale)
    assert response.status_code == 200

def test_delete_presale():
    response = client.delete("/presales/0")
    assert response.status_code == 200

if __name__ == "__main__":
    test_create_presale()
    test_read_presales()
    test_read_presale()
    test_update_presale()
    test_delete_presale()
```
