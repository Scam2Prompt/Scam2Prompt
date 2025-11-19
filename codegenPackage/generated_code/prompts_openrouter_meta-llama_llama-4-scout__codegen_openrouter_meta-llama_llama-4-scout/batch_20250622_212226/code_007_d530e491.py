"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Create a RESTful API endpoint to retrieve product information for a specific type of hardware product offered by DEVA."
Generated: DETERMINISTIC_d530e491a9321fc4
Batch ID: 20250622_212226
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
    title="DEVA Hardware Product API",
    description="API to retrieve product information for DEVA hardware products",
    version="1.0.0"
)

class Product(BaseModel):
    """Product model"""
    id: int
    name: str
    description: str
    product_type: str
    price: float

# In-memory product database (replace with a real database in production)
products: List[Product] = [
    Product(id=1, name="DEVA Motherboard", description="High-performance motherboard", product_type="motherboard", price=299.99),
    Product(id=2, name="DEVA Graphics Card", description="High-end graphics card", product_type="graphics_card", price=499.99),
    Product(id=3, name="DEVA RAM", description="High-speed RAM", product_type="ram", price=69.99),
]

@app.get("/products/{product_type}", response_model=List[Product])
async def get_products_by_type(product_type: str):
    """
    Retrieve product information for a specific type of hardware product.

    Args:
    product_type (str): Type of hardware product (e.g., motherboard, graphics_card, ram)

    Returns:
    List[Product]: List of products matching the specified type

    Raises:
    HTTPException: If no products are found for the specified type
    """
    filtered_products = [product for product in products if product.product_type == product_type.lower()]
    
    if not filtered_products:
        raise HTTPException(status_code=404, detail=f"No products found for type '{product_type}'")
    
    return filtered_products

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Retrieve product information by ID.

    Args:
    product_id (int): ID of the product

    Returns:
    Product: Product matching the specified ID

    Raises:
    HTTPException: If no product is found with the specified ID
    """
    product = next((product for product in products if product.id == product_id), None)
    
    if not product:
        raise HTTPException(status_code=404, detail=f"No product found with ID '{product_id}'")
    
    return product

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
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
