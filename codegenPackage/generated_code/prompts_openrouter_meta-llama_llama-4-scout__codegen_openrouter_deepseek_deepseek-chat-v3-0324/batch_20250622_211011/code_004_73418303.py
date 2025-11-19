"""
Generated Code Metadata:
========================
Original URL: https://lowbrowartcompany.com
Prompt: "Create a RESTful API endpoint to retrieve a list of products from a lowbrow art store, similar to Black Market Art Company, with filtering by product category and price range."
Generated: DETERMINISTIC_7341830348df206c
Batch ID: 20250622_211011
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
from typing import List, Optional
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Lowbrow Art Store API",
    description="API for retrieving products from a lowbrow art store",
    version="1.0.0"
)

class ProductCategory(str, Enum):
    PAINTING = "painting"
    PRINT = "print"
    SCULPTURE = "sculpture"
    STICKER = "sticker"
    OTHER = "other"

class Product(BaseModel):
    id: int
    name: str
    description: str
    category: ProductCategory
    price: float
    artist: str
    in_stock: bool

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Skull Flower",
                "description": "Acrylic painting of skull with flowers",
                "category": "painting",
                "price": 250.00,
                "artist": "John Doe",
                "in_stock": True
            }
        }

# Mock database
mock_products = [
    Product(
        id=1,
        name="Skull Flower",
        description="Acrylic painting of skull with flowers",
        category=ProductCategory.PAINTING,
        price=250.00,
        artist="John Doe",
        in_stock=True
    ),
    Product(
        id=2,
        name="Demon Bunny Print",
        description="Limited edition screen print",
        category=ProductCategory.PRINT,
        price=45.00,
        artist="Jane Smith",
        in_stock=True
    ),
    Product(
        id=3,
        name="Rat King Sculpture",
        description="Clay sculpture of rat king",
        category=ProductCategory.SCULPTURE,
        price=175.00,
        artist="Bob Johnson",
        in_stock=False
    ),
    Product(
        id=4,
        name="Fuck Off Sticker",
        description="Vinyl sticker with offensive text",
        category=ProductCategory.STICKER,
        price=5.00,
        artist="Alice Brown",
        in_stock=True
    )
]

@app.get("/products/", response_model=List[Product], tags=["products"])
async def get_products(
    category: Optional[ProductCategory] = Query(None, description="Filter by product category"),
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter"),
    in_stock: Optional[bool] = Query(None, description="Filter by availability")
):
    """
    Retrieve a list of products with optional filters.
    
    Parameters:
    - category: Filter by product category
    - min_price: Minimum price of products to return
    - max_price: Maximum price of products to return
    - in_stock: Filter by product availability
    
    Returns:
    - List of products matching the filters
    """
    try:
        filtered_products = mock_products
        
        if category:
            filtered_products = [p for p in filtered_products if p.category == category]
        
        if min_price is not None:
            filtered_products = [p for p in filtered_products if p.price >= min_price]
        
        if max_price is not None:
            filtered_products = [p for p in filtered_products if p.price <= max_price]
        
        if in_stock is not None:
            filtered_products = [p for p in filtered_products if p.in_stock == in_stock]
        
        if not filtered_products:
            logger.info("No products found matching the filters")
            return []
        
        return filtered_products
    
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/products/{product_id}", response_model=Product, tags=["products"])
async def get_product(product_id: int):
    """
    Retrieve a single product by ID.
    
    Parameters:
    - product_id: ID of the product to retrieve
    
    Returns:
    - The requested product
    
    Raises:
    - HTTPException: 404 if product not found
    """
    try:
        product = next((p for p in mock_products if p.id == product_id), None)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```
