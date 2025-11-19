"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a REST API endpoint for retrieving products in the "Fitness" category, including subcategories like "Colchonete" and "Extensores."
Generated: DETERMINISTIC_1242561101a79675
Batch ID: 20250612_151414
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
    title="Fitness Products API",
    description="API for retrieving fitness products",
    version="1.0.0"
)

# Define a model for products
class Product(BaseModel):
    id: int
    name: str
    category: str
    subcategory: str

# Sample in-memory data store (replace with a database in production)
products = [
    Product(id=1, name="Colchonete de Yoga", category="Fitness", subcategory="Colchonete"),
    Product(id=2, name="Extensores de Pierna", category="Fitness", subcategory="Extensores"),
    Product(id=3, name="Bicicleta Estática", category="Fitness", subcategory="Equipamiento"),
    Product(id=4, name="Colchonete de Pilates", category="Fitness", subcategory="Colchonete"),
    Product(id=5, name="Pesas Rusas", category="Fitness", subcategory="Equipamiento"),
]

# Define a route for retrieving products in the "Fitness" category
@app.get("/fitness/products/", response_model=List[Product])
async def read_fitness_products(subcategory: str = None):
    """
    Retrieve a list of products in the "Fitness" category.

    Args:
    - subcategory (str): Optional subcategory filter (e.g., "Colchonete", "Extensores")

    Returns:
    - A list of products in the "Fitness" category, filtered by subcategory if provided
    """
    try:
        fitness_products = [product for product in products if product.category == "Fitness"]
        
        if subcategory:
            fitness_products = [product for product in fitness_products if product.subcategory == subcategory]
        
        return fitness_products
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

# Define a route for retrieving a product by ID
@app.get("/fitness/products/{product_id}", response_model=Product)
async def read_fitness_product(product_id: int):
    """
    Retrieve a product by ID.

    Args:
    - product_id (int): The ID of the product to retrieve

    Returns:
    - The product with the specified ID, or a 404 error if not found
    """
    try:
        product = next((product for product in products if product.id == product_id), None)
        
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        return product
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
