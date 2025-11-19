"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Design a RESTful API for managing hot tub and spa inventory, including endpoints for retrieving product information and pricing, inspired by the Country Leisure Mfg product offerings.
Generated: DETERMINISTIC_33759ec7c457d0a3
Batch ID: 20250622_210655
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
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Hot Tub and Spa Inventory API",
    description="RESTful API for managing hot tub and spa inventory",
    version="1.0.0"
)

# Database simulation
inventory_db = []

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str  # e.g., "Hot Tub", "Spa", "Accessory"
    price: float
    dimensions: Optional[str] = None
    capacity: Optional[int] = None  # Gallons
    jets: Optional[int] = None
    material: Optional[str] = None
    in_stock: bool = True
    sku: str

class ProductCreate(BaseModel):
    name: str
    description: str
    category: str
    price: float
    dimensions: Optional[str] = None
    capacity: Optional[int] = None
    jets: Optional[int] = None
    material: Optional[str] = None
    in_stock: bool = True
    sku: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    dimensions: Optional[str] = None
    capacity: Optional[int] = None
    jets: Optional[int] = None
    material: Optional[str] = None
    in_stock: Optional[bool] = None
    sku: Optional[str] = None

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products(category: Optional[str] = None, in_stock: Optional[bool] = None):
    """Retrieve all products with optional filtering by category and stock status"""
    try:
        filtered_products = inventory_db
        if category:
            filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]
        if in_stock is not None:
            filtered_products = [p for p in filtered_products if p["in_stock"] == in_stock]
        return filtered_products
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: str):
    """Retrieve a single product by ID"""
    try:
        product = next((p for p in inventory_db if p["id"] == product_id), None)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return product
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product: ProductCreate):
    """Create a new product"""
    try:
        product_dict = product.dict()
        product_dict["id"] = str(uuid4())
        inventory_db.append(product_dict)
        logger.info(f"Created product: {product_dict['id']}")
        return product_dict
    except Exception as e:
        logger.error(f"Error creating product: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: str, product_update: ProductUpdate):
    """Update an existing product"""
    try:
        product_index = next((i for i, p in enumerate(inventory_db) if p["id"] == product_id), None)
        if product_index is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        existing_product = inventory_db[product_index]
        update_data = product_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            existing_product[field] = value
        
        inventory_db[product_index] = existing_product
        logger.info(f"Updated product: {product_id}")
        return existing_product
    except Exception as e:
        logger.error(f"Error updating product {product_id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
async def delete_product(product_id: str):
    """Delete a product"""
    try:
        product_index = next((i for i, p in enumerate(inventory_db) if p["id"] == product_id), None)
        if product_index is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        
        inventory_db.pop(product_index)
        logger.info(f"Deleted product: {product_id}")
    except Exception as e:
        logger.error(f"Error deleting product {product_id}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.get("/products/search/{query}", response_model=List[Product], tags=["Products"])
async def search_products(query: str):
    """Search products by name or description"""
    try:
        query = query.lower()
        results = [
            p for p in inventory_db
            if query in p["name"].lower() or query in p["description"].lower()
        ]
        return results
    except Exception as e:
        logger.error(f"Error searching products: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@app.get("/products/categories", response_model=List[str], tags=["Products"])
async def get_product_categories():
    """Get all available product categories"""
    try:
        categories = list(set(p["category"] for p in inventory_db))
        return categories
    except Exception as e:
        logger.error(f"Error retrieving categories: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
```
