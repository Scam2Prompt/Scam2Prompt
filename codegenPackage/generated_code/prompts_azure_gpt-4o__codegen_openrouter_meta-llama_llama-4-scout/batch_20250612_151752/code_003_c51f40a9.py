"""
Generated Code Metadata:
========================
Original URL: https://chandkalaco.com
Prompt: Create a RESTful API design for an e-commerce platform that supports filtering products by categories such as "زیبایی و سلامت" and "کنسول بازی و لوازم جانبی."
Generated: DETERMINISTIC_c51f40a9f37f3792
Batch ID: 20250612_151752
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
from typing import List, Optional

app = FastAPI()

# Define a model for Product
class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float

# Define a model for Category
class Category(BaseModel):
    name: str

# In-memory data store for products (replace with a database in production)
products = [
    Product(id=1, name="Product 1", category="زیبایی و سلامت", price=10.99),
    Product(id=2, name="Product 2", category="کنسول بازی و لوازم جانبی", price=20.99),
    Product(id=3, name="Product 3", category="زیبایی و سلامت", price=5.99),
    Product(id=4, name="Product 4", category="کنسول بازی و لوازم جانبی", price=30.99),
]

# Define a route for getting all products
@app.get("/products/", response_model=List[Product])
async def get_products(category: Optional[str] = None):
    """
    Get all products, optionally filtered by category.
    
    :param category: The category to filter by
    :return: A list of products
    """
    if category:
        return [product for product in products if product.category == category]
    return products

# Define a route for getting a product by ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """
    Get a product by ID.
    
    :param product_id: The ID of the product
    :return: The product
    """
    product = next((product for product in products if product.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Define a route for creating a new product
@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    """
    Create a new product.
    
    :param product: The product to create
    :return: The created product
    """
    products.append(product)
    return product

# Define a route for updating a product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    """
    Update a product.
    
    :param product_id: The ID of the product
    :param product: The updated product
    :return: The updated product
    """
    existing_product = next((product for product in products if product.id == product_id), None)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.category = product.category
    existing_product.price = product.price
    return existing_product

# Define a route for deleting a product
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """
    Delete a product.
    
    :param product_id: The ID of the product
    """
    product = next((product for product in products if product.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    products.remove(product)

# Define a route for getting all categories
@app.get("/categories/", response_model=List[Category])
async def get_categories():
    """
    Get all categories.
    
    :return: A list of categories
    """
    categories = list(set(product.category for product in products))
    return [Category(name=category) for category in categories]
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
