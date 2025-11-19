"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Create a RESTful API endpoint for a service that provides information about different types of wood products, including "Maderas duras del Norte Argentino," as mentioned on the Maderas Elaboradas site.
Generated: DETERMINISTIC_ff1e1fc38fd52e1d
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wood_products_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Wood Products API",
    description="Provides information about different types of wood products",
    version="1.0.0"
)

class WoodProduct(BaseModel):
    """Represents a wood product"""
    id: int
    name: str
    description: str
    origin: str

# In-memory data store for demonstration purposes
wood_products = [
    WoodProduct(id=1, name="Maderas duras del Norte Argentino", description="Hardwoods from Northern Argentina", origin="Argentina"),
    WoodProduct(id=2, name="Maderas blandas del Sur Argentino", description="Softwoods from Southern Argentina", origin="Argentina"),
    # Add more wood products as needed
]

@app.get("/wood_products/", response_model=List[WoodProduct])
async def read_wood_products():
    """Retrieve a list of all wood products"""
    return wood_products

@app.get("/wood_products/{wood_product_id}", response_model=WoodProduct)
async def read_wood_product(wood_product_id: int):
    """Retrieve a wood product by ID"""
    for wood_product in wood_products:
        if wood_product.id == wood_product_id:
            return wood_product
    raise HTTPException(status_code=404, detail="Wood product not found")

@app.post("/wood_products/", response_model=WoodProduct, status_code=201)
async def create_wood_product(wood_product: WoodProduct):
    """Create a new wood product"""
    # Check for duplicate IDs
    for existing_wood_product in wood_products:
        if existing_wood_product.id == wood_product.id:
            raise HTTPException(status_code=400, detail="Wood product with this ID already exists")
    wood_products.append(wood_product)
    return wood_product

@app.put("/wood_products/{wood_product_id}", response_model=WoodProduct)
async def update_wood_product(wood_product_id: int, wood_product: WoodProduct):
    """Update an existing wood product"""
    for existing_wood_product in wood_products:
        if existing_wood_product.id == wood_product_id:
            existing_wood_product.name = wood_product.name
            existing_wood_product.description = wood_product.description
            existing_wood_product.origin = wood_product.origin
            return existing_wood_product
    raise HTTPException(status_code=404, detail="Wood product not found")

@app.delete("/wood_products/{wood_product_id}")
async def delete_wood_product(wood_product_id: int):
    """Delete a wood product"""
    for i, wood_product in enumerate(wood_products):
        if wood_product.id == wood_product_id:
            del wood_products[i]
            return {"message": "Wood product deleted successfully"}
    raise HTTPException(status_code=404, detail="Wood product not found")
```

```bash
# Run the API using uvicorn
# uvicorn wood_products_api:app --host 0.0.0.0 --port 8000 --reload
```
