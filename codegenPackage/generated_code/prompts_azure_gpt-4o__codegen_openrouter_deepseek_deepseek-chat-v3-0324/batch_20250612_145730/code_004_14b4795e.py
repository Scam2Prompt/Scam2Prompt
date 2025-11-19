"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Develop a REST API endpoint for filtering homeopathic products by categories (e.g., "Mother Tinctures" or "Dilution/Potencies") and price range, inspired by the PEKANA.PK website.
Generated: DETERMINISTIC_14b4795e3bedcb55
Batch ID: 20250612_145730
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
    title="Homeopathic Products API",
    description="API for filtering homeopathic products by categories and price range",
    version="1.0.0"
)

class Category(str, Enum):
    MOTHER_TINCTURES = "Mother Tinctures"
    DILUTION_POTENCIES = "Dilution/Potencies"
    TABLETS = "Tablets"
    OINTMENTS = "Ointments"
    SYRUPS = "Syrups"

class Product(BaseModel):
    id: int
    name: str
    category: Category
    price: float
    description: Optional[str] = None

# Mock database
products_db = [
    Product(id=1, name="Arnica Montana", category=Category.MOTHER_TINCTURES, price=10.99, description="For bruises and muscle pain"),
    Product(id=2, name="Belladonna 30C", category=Category.DILUTION_POTENCIES, price=15.50),
    Product(id=3, name="Calendula Cream", category=Category.OINTMENTS, price=12.75),
    Product(id=4, name="Echinacea Angustifolia", category=Category.MOTHER_TINCTURES, price=9.99),
    Product(id=5, name="Nux Vomica 6X", category=Category.TABLETS, price=8.25),
    Product(id=6, name="Aconitum Napellus 200C", category=Category.DILUTION_POTENCIES, price=18.00),
    Product(id=7, name="Throat Syrup", category=Category.SYRUPS, price=14.50),
]

@app.get("/products/", response_model=List[Product], tags=["Products"])
async def filter_products(
    categories: Optional[List[Category]] = Query(None, description="Filter by product categories"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price filter")
):
    """
    Filter homeopathic products by categories and price range.
    
    Parameters:
    - categories: List of categories to filter by
    - min_price: Minimum price of products to include
    - max_price: Maximum price of products to include
    
    Returns:
    - List of filtered products
    """
    try:
        filtered_products = products_db
        
        # Apply category filter if provided
        if categories:
            filtered_products = [p for p in filtered_products if p.category in categories]
        
        # Apply price range filters if provided
        if min_price is not None:
            filtered_products = [p for p in filtered_products if p.price >= min_price]
        
        if max_price is not None:
            filtered_products = [p for p in filtered_products if p.price <= max_price]
        
        # Validate price range if both are provided
        if min_price is not None and max_price is not None and min_price > max_price:
            raise HTTPException(
                status_code=400,
                detail="Minimum price cannot be greater than maximum price"
            )
        
        logger.info(f"Returning {len(filtered_products)} filtered products")
        return filtered_products
    
    except Exception as e:
        logger.error(f"Error filtering products: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

@app.get("/categories/", response_model=List[str], tags=["Products"])
async def get_categories():
    """
    Get list of available product categories.
    
    Returns:
    - List of available categories
    """
    try:
        return [category.value for category in Category]
    except Exception as e:
        logger.error(f"Error retrieving categories: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while retrieving categories"
        )
```
