"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Create a simple API to query Groundcell product information, including sizes, prices, and availability, based on the product codes (EC100, EC150, EC200)."
Generated: DETERMINISTIC_77b7ffd611e771ea
Batch ID: 20250622_205348
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
from typing import Dict, Optional

app = FastAPI(
    title="Groundcell Product API",
    description="API to query Groundcell product information",
    version="1.0.0"
)

# Mock database of products
PRODUCTS_DB = {
    "EC100": {
        "name": "Groundcell Basic",
        "size": "Small",
        "price": 99.99,
        "availability": True,
        "description": "Entry-level Groundcell product"
    },
    "EC150": {
        "name": "Groundcell Pro",
        "size": "Medium",
        "price": 149.99,
        "availability": True,
        "description": "Mid-range Groundcell product"
    },
    "EC200": {
        "name": "Groundcell Premium",
        "size": "Large",
        "price": 199.99,
        "availability": False,
        "description": "Premium Groundcell product"
    }
}

class Product(BaseModel):
    code: str
    name: str
    size: str
    price: float
    availability: bool
    description: str

@app.get("/products", response_model=Dict[str, Product])
async def get_all_products():
    """Get all available products"""
    return PRODUCTS_DB

@app.get("/products/{product_code}", response_model=Product)
async def get_product(product_code: str):
    """Get specific product by product code"""
    product = PRODUCTS_DB.get(product_code.upper())
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with code {product_code} not found"
        )
    return {**{"code": product_code.upper()}, **product}

@app.get("/products/{product_code}/availability", response_model=bool)
async def check_availability(product_code: str):
    """Check availability of a specific product"""
    product = PRODUCTS_DB.get(product_code.upper())
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with code {product_code} not found"
        )
    return product["availability"]

@app.get("/products/{product_code}/price", response_model=float)
async def get_product_price(product_code: str):
    """Get price of a specific product"""
    product = PRODUCTS_DB.get(product_code.upper())
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with code {product_code} not found"
        )
    return product["price"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
