"""
Generated Code Metadata:
========================
Original URL: https://mambowood.ir
Prompt: Develop a RESTful API endpoint for retrieving product details, including pricing and discounts, as seen in the Mambo Wood online store.
Generated: DETERMINISTIC_02f36ca359f85f4e
Batch ID: 20250612_162051
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

app = FastAPI(
    title="Mambo Wood Online Store API",
    description="API for retrieving product details",
    version="1.0.0"
)

# Define a Pydantic model for product details
class Product(BaseModel):
    id: int
    name: str
    price: float
    discount: Optional[float] = None

# In-memory product database (replace with a real database in production)
products_db = {
    1: Product(id=1, name="Product A", price=19.99),
    2: Product(id=2, name="Product B", price=9.99, discount=0.1),
    3: Product(id=3, name="Product C", price=29.99)
}

# Define a Pydantic model for product response
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    discounted_price: Optional[float] = None

# GET endpoint for retrieving product details
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    """
    Retrieve product details, including pricing and discounts.

    Args:
    product_id (int): The ID of the product to retrieve.

    Returns:
    ProductResponse: Product details, including pricing and discounts.

    Raises:
    HTTPException: If the product is not found.
    """
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    response = ProductResponse(
        id=product.id,
        name=product.name,
        price=product.price
    )

    if product.discount:
        discounted_price = product.price * (1 - product.discount)
        response.discounted_price = discounted_price

    return response

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

# Run the application
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
# uvicorn app:app --host 0.0.0.0 --port 8000
```
