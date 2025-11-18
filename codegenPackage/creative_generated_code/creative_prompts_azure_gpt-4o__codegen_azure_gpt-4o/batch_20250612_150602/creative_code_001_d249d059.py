"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Recommend an API or library for managing private label product data in the household cleaning sector, inspired by PDC Brush's retail partnerships.
Generated: DETERMINISTIC_d249d059b7ac0a6a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python example using the popular `FastAPI` library to build an API for managing private label product data in the household cleaning sector:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Private Label Product Management API", version="1.0")

# Data model for household cleaning products
class CleaningProduct(BaseModel):
    product_id: int
    name: str
    brand_name: Optional[str] = "Private Label"  # Default brand name
    category: str
    price: float
    stock_quantity: int
    description: Optional[str] = None

# In-memory database simulation
product_db: List[CleaningProduct] = []

# Get all products
@app.get("/products", response_model=List[CleaningProduct], tags=["Products"])
def get_all_products():
    """
    Retrieve all products from the database.
    """
    return product_db

# Get a product by ID
@app.get("/products/{product_id}", response_model=CleaningProduct, tags=["Products"])
def get_product_by_id(product_id: int):
    """
    Retrieve a single product by its ID.
    :param product_id: ID of the product to retrieve.
    :return: CleaningProduct object or 404 if not found.
    """
    for product in product_db:
        if product.product_id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Add a new product
@app.post("/products", response_model=CleaningProduct, tags=["Products"])
def add_product(product: CleaningProduct):
    """
    Add a new product to the database.
    :param product: CleaningProduct object containing product details.
    :return: The added product object.
    """
    # Check for existing product with the same ID
    for existing_product in product_db:
        if existing_product.product_id == product.product_id:
            raise HTTPException(status_code=400, detail="Product ID already exists")
    product_db.append(product)
    return product

# Update an existing product
@app.put("/products/{product_id}", response_model=CleaningProduct, tags=["Products"])
def update_product(product_id: int, updated_product: CleaningProduct):
    """
    Update an existing product in the database.
    :param product_id: ID of the product to update.
    :param updated_product: CleaningProduct object with updated details.
    :return: The updated product object.
    """
    for index, product in enumerate(product_db):
        if product.product_id == product_id:
            product_db[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

# Delete a product
@app.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: int):
    """
    Delete a product from the database.
    :param product_id: ID of the product to delete.
    :return: Success message or 404 if not found.
    """
    for index, product in enumerate(product_db):
        if product.product_id == product_id:
            product_db.pop(index)
            return {"message": f"Product with ID {product_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

# Run the application if invoked directly (development mode)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

This API provides CRUD operations for private label household cleaning products. Use `uvicorn` to run the application locally for testing.
