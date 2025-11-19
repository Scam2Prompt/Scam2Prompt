"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Create a REST API endpoint for querying product details like drinking cups and plastic cutlery, inspired by Isoplas Corporation's product catalog structure.
Generated: DETERMINISTIC_f1f272ab5d0b099b
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Product Catalog API",
    description="API for querying product details like drinking cups and plastic cutlery",
    version="1.0.0"
)

# Database mock (in a real application, this would be a database connection)
products_db = [
    {
        "id": "CUP001",
        "name": "Eco-Friendly Paper Cup",
        "category": "drinking-cups",
        "material": "paper",
        "capacity_ml": 250,
        "price": 0.15,
        "stock": 1000,
        "description": "Biodegradable paper cup with PLA lining"
    },
    {
        "id": "CUP002",
        "name": "Clear Plastic Cup",
        "category": "drinking-cups",
        "material": "PET",
        "capacity_ml": 500,
        "price": 0.20,
        "stock": 800,
        "description": "Transparent PET plastic cup"
    },
    {
        "id": "CUT001",
        "name": "White Plastic Fork",
        "category": "cutlery",
        "material": "PP",
        "price": 0.05,
        "stock": 5000,
        "description": "Standard white polypropylene fork"
    },
    {
        "id": "CUT002",
        "name": "Black Plastic Knife",
        "category": "cutlery",
        "material": "PS",
        "price": 0.06,
        "stock": 4500,
        "description": "Black polystyrene knife"
    }
]

class Product(BaseModel):
    id: str
    name: str
    category: str
    material: str
    price: float
    stock: int
    description: str
    capacity_ml: Optional[int] = None  # Only for drinking cups

@app.get("/products/", response_model=List[Product])
async def get_products(
    category: Optional[str] = Query(None, description="Filter by product category (e.g., 'drinking-cups', 'cutlery')"),
    material: Optional[str] = Query(None, description="Filter by material (e.g., 'PET', 'PP', 'PS')"),
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter"),
    in_stock: Optional[bool] = Query(None, description="Only show products with stock available")
):
    """
    Retrieve a list of products with optional filtering.
    """
    try:
        filtered_products = products_db.copy()
        
        if category:
            filtered_products = [p for p in filtered_products if p["category"] == category]
        
        if material:
            filtered_products = [p for p in filtered_products if p["material"] == material]
        
        if min_price is not None:
            filtered_products = [p for p in filtered_products if p["price"] >= min_price]
        
        if max_price is not None:
            filtered_products = [p for p in filtered_products if p["price"] <= max_price]
        
        if in_stock:
            filtered_products = [p for p in filtered_products if p["stock"] > 0]
        
        logger.info(f"Retrieved {len(filtered_products)} products with applied filters")
        return filtered_products
    
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    """
    Retrieve details for a specific product by ID.
    """
    try:
        product = next((p for p in products_db if p["id"] == product_id), None)
        if not product:
            logger.warning(f"Product with ID {product_id} not found")
            raise HTTPException(status_code=404, detail="Product not found")
        
        logger.info(f"Retrieved product with ID {product_id}")
        return product
    
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/categories/", response_model=List[str])
async def get_categories():
    """
    Retrieve list of available product categories.
    """
    try:
        categories = list({p["category"] for p in products_db})
        logger.info(f"Retrieved {len(categories)} product categories")
        return categories
    except Exception as e:
        logger.error(f"Error retrieving categories: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
