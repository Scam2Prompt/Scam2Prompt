"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Create an API documentation for retrieving information about Emanuelson Reels' products, including their specifications, prices, and related accessories like leather cases."
Generated: DETERMINISTIC_09c12ce28349b1a5
Batch ID: 20250622_210655
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
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Emanuelson Reels Product API",
    description="API for retrieving information about Emanuelson Reels' products, specifications, prices, and accessories.",
    version="1.0.0",
    contact={
        "name": "Emanuelson Reels Support",
        "email": "support@emanuelsonreels.com"
    },
    license_info={
        "name": "Proprietary"
    }
)

class Accessory(BaseModel):
    """Model for product accessories like leather cases"""
    id: str
    name: str
    description: str
    price: float
    compatible_products: List[str]

class Product(BaseModel):
    """Model for Emanuelson Reels products"""
    id: str
    name: str
    description: str
    specifications: dict
    price: float
    accessories: List[Accessory] = []

# Mock database
products_db = {
    "ER100": {
        "id": "ER100",
        "name": "Emanuelson Classic Reel",
        "description": "Premium fishing reel with classic design",
        "specifications": {
            "weight": "250g",
            "gear_ratio": "5.2:1",
            "bearings": "Stainless steel",
            "line_capacity": "150yds/12lb"
        },
        "price": 199.99,
        "accessories": [
            {
                "id": "LC100",
                "name": "Leather Case",
                "description": "Premium leather case for protection",
                "price": 49.99,
                "compatible_products": ["ER100", "ER200"]
            }
        ]
    },
    "ER200": {
        "id": "ER200",
        "name": "Emanuelson Pro Reel",
        "description": "Professional grade fishing reel",
        "specifications": {
            "weight": "220g",
            "gear_ratio": "6.3:1",
            "bearings": "Ceramic",
            "line_capacity": "200yds/20lb"
        },
        "price": 299.99,
        "accessories": [
            {
                "id": "LC100",
                "name": "Leather Case",
                "description": "Premium leather case for protection",
                "price": 49.99,
                "compatible_products": ["ER100", "ER200"]
            },
            {
                "id": "SP200",
                "name": "Spare Spool",
                "description": "Additional spool for quick line changes",
                "price": 29.99,
                "compatible_products": ["ER200"]
            }
        ]
    }
}

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Get all Emanuelson Reels products"""
    return list(products_db.values())

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: str):
    """Get a specific product by ID"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.get("/accessories", response_model=List[Accessory], tags=["Accessories"])
async def get_all_accessories():
    """Get all available accessories"""
    accessories = []
    for product in products_db.values():
        accessories.extend(product["accessories"])
    # Remove duplicates
    unique_accessories = {acc["id"]: acc for acc in accessories}.values()
    return list(unique_accessories)

@app.get("/products/{product_id}/accessories", response_model=List[Accessory], tags=["Products"])
async def get_product_accessories(product_id: str):
    """Get accessories for a specific product"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]["accessories"]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
