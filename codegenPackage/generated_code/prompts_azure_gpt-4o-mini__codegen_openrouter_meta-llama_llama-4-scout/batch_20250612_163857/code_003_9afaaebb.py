"""
Generated Code Metadata:
========================
Original URL: https://flaviadossantos.co
Prompt: Create a RESTful API endpoint to fetch product information for the "Disney / Pixar's Soul Men's NY Jazz Night Logo Tee."
Generated: DETERMINISTIC_9afaaebbe331198e
Batch ID: 20250612_163857
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

app = FastAPI()

# Define a Pydantic model for the product information
class ProductInfo(BaseModel):
    """Product information model"""
    id: int
    name: str
    description: str
    price: float
    brand: str
    style: str

# In-memory product database (replace with a real database in production)
products = {
    1: ProductInfo(
        id=1,
        name="Disney / Pixar's Soul Men's NY Jazz Night Logo Tee",
        description="A stylish tee featuring the NY Jazz Night logo from Disney / Pixar's Soul.",
        price=24.99,
        brand="Disney",
        style="T-Shirt"
    )
}

# Define a route to fetch product information by ID or name
@app.get("/products/{product_id}", response_model=ProductInfo)
async def get_product_by_id(product_id: int):
    """
    Fetch product information by ID.

    Args:
    product_id (int): The ID of the product.

    Returns:
    ProductInfo: The product information.

    Raises:
    HTTPException: If the product is not found.
    """
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Define a route to fetch product information by name
@app.get("/products/", response_model=ProductInfo)
async def get_product_by_name(name: Optional[str] = None):
    """
    Fetch product information by name.

    Args:
    name (str, optional): The name of the product. Defaults to None.

    Returns:
    ProductInfo: The product information.

    Raises:
    HTTPException: If the product is not found.
    """
    if not name:
        raise HTTPException(status_code=400, detail="Product name is required")
    for product in products.values():
        if product.name.lower() == name.lower():
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Define a main function to run the application
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
