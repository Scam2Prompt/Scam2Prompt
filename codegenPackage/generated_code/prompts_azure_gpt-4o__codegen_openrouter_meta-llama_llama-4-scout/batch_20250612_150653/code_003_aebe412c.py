"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a REST API design for querying and ordering reinforced concrete products (ЖБИ) categorized by construction type (e.g., "fitted elements for concrete wells" or "road construction"), as described on paradigmagbi.ru.
Generated: DETERMINISTIC_aebe412c9beafcea
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**reinforced_concrete_products_api.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Reinforced Concrete Products API",
    description="API for querying and ordering reinforced concrete products",
    version="1.0.0"
)

# Define a model for the reinforced concrete product
class ReinforcedConcreteProduct(BaseModel):
    id: int
    name: str
    construction_type: str
    description: str

# Define a model for the product order
class ProductOrder(BaseModel):
    product_id: int
    quantity: int

# In-memory data store for demonstration purposes
# Replace with a database connection in production
products = [
    ReinforcedConcreteProduct(
        id=1,
        name="Fitted element for concrete well",
        construction_type="fitted elements for concrete wells",
        description="Reinforced concrete product for well construction"
    ),
    ReinforcedConcreteProduct(
        id=2,
        name="Road plate",
        construction_type="road construction",
        description="Reinforced concrete product for road construction"
    ),
    # Add more products here...
]

# Get all products
@app.get("/products/", response_model=List[ReinforcedConcreteProduct])
async def get_products(construction_type: str = None):
    """
    Get a list of reinforced concrete products.

    Args:
    - construction_type (str): Filter products by construction type.

    Returns:
    - List[ReinforcedConcreteProduct]: A list of reinforced concrete products.
    """
    if construction_type:
        return [product for product in products if product.construction_type == construction_type]
    return products

# Get product by ID
@app.get("/products/{product_id}", response_model=ReinforcedConcreteProduct)
async def get_product(product_id: int):
    """
    Get a reinforced concrete product by ID.

    Args:
    - product_id (int): The ID of the product.

    Returns:
    - ReinforcedConcreteProduct: The reinforced concrete product.

    Raises:
    - HTTPException: If the product is not found.
    """
    product = next((product for product in products if product.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Create a new product order
@app.post("/orders/")
async def create_order(order: ProductOrder):
    """
    Create a new product order.

    Args:
    - order (ProductOrder): The product order.

    Returns:
    - dict: A success message.

    Raises:
    - HTTPException: If the product is not found.
    """
    product = next((product for product in products if product.id == order.product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Process the order (e.g., add to database, send notification)
    return {"message": "Order created successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**schemas.py**
```python
from pydantic import BaseModel

class ReinforcedConcreteProductSchema(BaseModel):
    id: int
    name: str
    construction_type: str
    description: str

class ProductOrderSchema(BaseModel):
    product_id: int
    quantity: int
```

**main.py**
```python
from reinforced_concrete_products_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**requirements.txt**
```
fastapi
pydantic
uvicorn
```
