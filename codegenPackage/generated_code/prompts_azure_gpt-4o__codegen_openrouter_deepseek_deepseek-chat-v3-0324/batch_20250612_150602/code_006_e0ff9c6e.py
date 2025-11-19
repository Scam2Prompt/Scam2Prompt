"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Design an API endpoint for retrieving product categories such as "Protein," "Calcium," "Magnesium," and "Vitamine" from the PlusMedica Shop website, ensuring compatibility with bariatric patient needs.
Generated: DETERMINISTIC_e0ff9c6e04eb2b46
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PlusMedica Shop API",
    description="API for retrieving bariatric-friendly product categories",
    version="1.0.0"
)

class Category(BaseModel):
    id: int
    name: str
    description: str
    bariatric_compatible: bool

# Mock database of product categories
CATEGORIES_DB = [
    {
        "id": 1,
        "name": "Protein",
        "description": "High-protein supplements for bariatric patients",
        "bariatric_compatible": True
    },
    {
        "id": 2,
        "name": "Calcium",
        "description": "Calcium supplements for bone health",
        "bariatric_compatible": True
    },
    {
        "id": 3,
        "name": "Magnesium",
        "description": "Magnesium supplements for muscle function",
        "bariatric_compatible": True
    },
    {
        "id": 4,
        "name": "Vitamins",
        "description": "Essential vitamins for bariatric patients",
        "bariatric_compatible": True
    },
    {
        "id": 5,
        "name": "General Supplements",
        "description": "Regular supplements not specifically for bariatric patients",
        "bariatric_compatible": False
    }
]

@app.get("/categories", response_model=List[Category], tags=["Categories"])
async def get_categories(bariatric_only: bool = True):
    """
    Retrieve product categories from PlusMedica Shop.
    
    Args:
        bariatric_only (bool): If True, returns only bariatric-compatible categories.
                              Defaults to True.
    
    Returns:
        List[Category]: List of product categories matching the criteria.
    """
    try:
        if bariatric_only:
            filtered_categories = [c for c in CATEGORIES_DB if c["bariatric_compatible"]]
            logger.info(f"Returning {len(filtered_categories)} bariatric-compatible categories")
            return filtered_categories
        logger.info(f"Returning all {len(CATEGORIES_DB)} categories")
        return CATEGORIES_DB
    except Exception as e:
        logger.error(f"Error retrieving categories: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error while retrieving categories"
        )

@app.get("/categories/{category_id}", response_model=Category, tags=["Categories"])
async def get_category(category_id: int):
    """
    Retrieve a specific product category by ID.
    
    Args:
        category_id (int): The ID of the category to retrieve.
    
    Returns:
        Category: The requested category details.
    
    Raises:
        HTTPException: 404 if category is not found.
    """
    try:
        category = next((c for c in CATEGORIES_DB if c["id"] == category_id), None)
        if not category:
            logger.warning(f"Category with ID {category_id} not found")
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )
        logger.info(f"Returning category with ID {category_id}")
        return category
    except Exception as e:
        logger.error(f"Error retrieving category {category_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error while retrieving category"
        )
```
