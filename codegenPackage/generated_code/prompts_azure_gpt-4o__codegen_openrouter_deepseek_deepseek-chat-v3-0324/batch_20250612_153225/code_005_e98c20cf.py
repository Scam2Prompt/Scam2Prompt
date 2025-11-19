"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Develop a REST API endpoint to list products like "Inmunofluor Chlamydia T" and "Inmunofluor Toxoplasmosis" with sorting options, based on the MedPointYE catalog structure.
Generated: DETERMINISTIC_e98c20cf74c741f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ProductCategory(str, Enum):
    DIAGNOSTIC = "diagnostic"
    TREATMENT = "treatment"
    EQUIPMENT = "equipment"

class Product(BaseModel):
    id: str
    name: str
    category: ProductCategory
    price: float
    stock: int
    description: Optional[str] = None

# Mock database
products_db = [
    Product(
        id="prod001",
        name="Inmunofluor Chlamydia T",
        category=ProductCategory.DIAGNOSTIC,
        price=45.99,
        stock=50,
        description="Diagnostic kit for Chlamydia trachomatis"
    ),
    Product(
        id="prod002",
        name="Inmunofluor Toxoplasmosis",
        category=ProductCategory.DIAGNOSTIC,
        price=52.50,
        stock=30,
        description="Diagnostic kit for Toxoplasmosis"
    ),
    Product(
        id="prod003",
        name="Antibiotic X",
        category=ProductCategory.TREATMENT,
        price=12.75,
        stock=100
    )
]

class SortField(str, Enum):
    NAME = "name"
    PRICE = "price"
    STOCK = "stock"

class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"

@app.get("/products/", response_model=List[Product])
async def list_products(
    category: Optional[ProductCategory] = None,
    name_contains: Optional[str] = Query(None, min_length=2, description="Filter products by name containing this string"),
    sort_by: Optional[SortField] = SortField.NAME,
    order: Optional[SortOrder] = SortOrder.ASC,
    limit: Optional[int] = Query(10, gt=0, le=100)
):
    """
    List products with optional filtering and sorting.
    
    Parameters:
    - category: Filter by product category
    - name_contains: Filter products whose name contains this string
    - sort_by: Field to sort by (name, price, stock)
    - order: Sort order (asc, desc)
    - limit: Maximum number of products to return (1-100)
    
    Returns:
    - List of products matching the criteria
    """
    try:
        filtered_products = products_db
        
        # Apply filters
        if category:
            filtered_products = [p for p in filtered_products if p.category == category]
        
        if name_contains:
            filtered_products = [p for p in filtered_products if name_contains.lower() in p.name.lower()]
        
        # Apply sorting
        reverse_sort = order == SortOrder.DESC
        if sort_by == SortField.NAME:
            filtered_products.sort(key=lambda p: p.name.lower(), reverse=reverse_sort)
        elif sort_by == SortField.PRICE:
            filtered_products.sort(key=lambda p: p.price, reverse=reverse_sort)
        elif sort_by == SortField.STOCK:
            filtered_products.sort(key=lambda p: p.stock, reverse=reverse_sort)
        
        # Apply limit
        return filtered_products[:limit]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing your request: {str(e)}")
```
