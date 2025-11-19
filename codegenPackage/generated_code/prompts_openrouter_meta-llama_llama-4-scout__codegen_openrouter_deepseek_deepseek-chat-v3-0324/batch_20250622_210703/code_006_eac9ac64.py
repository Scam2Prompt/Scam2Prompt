"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Generate a RESTful API documentation for a server that manages orders and inventory of fiberglass products, including endpoints for creating, reading, updating, and deleting (CRUD) product information."
Generated: DETERMINISTIC_eac9ac64e55e6cc1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(
    title="Fiberglass Products API",
    description="A RESTful API for managing orders and inventory of fiberglass products.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@fiberglassapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database simulation (in-memory for demonstration)
products_db = {}

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    quantity: int
    weight: float
    dimensions: str

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    weight: float
    dimensions: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    weight: Optional[float] = None
    dimensions: Optional[str] = None

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    """
    Create a new fiberglass product in inventory.
    
    - **name**: Product name
    - **description**: Product description
    - **price**: Product price
    - **quantity**: Available quantity
    - **weight**: Product weight in kg
    - **dimensions**: Product dimensions (e.g., "10x20x5 cm")
    """
    product_id = str(uuid.uuid4())
    new_product = Product(
        id=product_id,
        **product.dict()
    )
    products_db[product_id] = new_product
    return new_product

@app.get("/products/", response_model=List[Product])
async def read_products():
    """
    Retrieve a list of all fiberglass products in inventory.
    """
    return list(products_db.values())

@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    """
    Retrieve details of a specific fiberglass product by ID.
    """
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return products_db[product_id]

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product_update: ProductUpdate):
    """
    Update details of a specific fiberglass product by ID.
    
    Only include fields you want to update.
    """
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    stored_product = products_db[product_id]
    update_data = product_update.dict(exclude_unset=True)
    updated_product = stored_product.copy(update=update_data)
    products_db[product_id] = updated_product
    return updated_product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str):
    """
    Delete a fiberglass product from inventory by ID.
    """
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    del products_db[product_id]
    return None
```
