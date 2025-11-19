"""
Generated Code Metadata:
========================
Original URL: https://dizneypin.com
Prompt: "Suggest a set of RESTful API endpoints for managing Disney merchandise inventory, including endpoints for retrieving products by category, updating product stock levels, and processing orders."
Generated: DETERMINISTIC_7e17fa6d48d5bbb1
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Disney Merchandise Inventory API",
    description="API for managing Disney merchandise inventory",
    version="1.0.0"
)

# Define a model for Product
class Product(BaseModel):
    id: int
    name: str
    category: str
    stock_level: int
    price: float

# Define a model for Order
class Order(BaseModel):
    product_id: int
    quantity: int

# In-memory data store for products (replace with a database in production)
products: List[Product] = [
    Product(id=1, name="Mickey Mouse T-Shirt", category="Apparel", stock_level=100, price=19.99),
    Product(id=2, name="Disney Princess Doll", category="Toys", stock_level=50, price=14.99),
    Product(id=3, name="The Lion King Poster", category="Home Decor", stock_level=200, price=9.99)
]

# Endpoint to retrieve all products
@app.get("/products", response_model=List[Product])
def get_products():
    """Retrieve a list of all products"""
    return products

# Endpoint to retrieve products by category
@app.get("/products/category/{category}", response_model=List[Product])
def get_products_by_category(category: str):
    """Retrieve a list of products by category"""
    return [product for product in products if product.category.lower() == category.lower()]

# Endpoint to retrieve a product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Retrieve a product by ID"""
    product = next((product for product in products if product.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# Endpoint to update product stock levels
@app.patch("/products/{product_id}/stock", response_model=Product)
def update_product_stock(product_id: int, stock_level: int):
    """Update the stock level of a product"""
    product = next((product for product in products if product.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product.stock_level = stock_level
    return product

# Endpoint to process an order
@app.post("/orders", response_model=dict)
def process_order(order: Order):
    """Process an order"""
    product = next((product for product in products if product.id == order.product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    if product.stock_level < order.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient stock")
    product.stock_level -= order.quantity
    return {"message": "Order processed successfully"}

# Endpoint to create a new product
@app.post("/products", response_model=Product)
def create_product(product: Product):
    """Create a new product"""
    existing_product = next((product for product in products if product.id == product.id), None)
    if existing_product is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product already exists")
    products.append(product)
    return product

# Endpoint to update a product
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    """Update a product"""
    existing_product = next((product for product in products if product.id == product_id), None)
    if existing_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    existing_product.name = product.name
    existing_product.category = product.category
    existing_product.price = product.price
    return existing_product

# Endpoint to delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete a product"""
    product = next((product for product in products if product.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    products.remove(product)
    return {"message": "Product deleted successfully"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
