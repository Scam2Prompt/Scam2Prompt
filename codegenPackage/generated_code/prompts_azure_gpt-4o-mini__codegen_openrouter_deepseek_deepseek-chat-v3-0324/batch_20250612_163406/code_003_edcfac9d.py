"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Create an API endpoint for listing automotive tools and tires with pricing and installment options, as seen on the Itamarati Online website.
Generated: DETERMINISTIC_edcfac9d5a7f04d0
Batch ID: 20250612_163406
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
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Automotive Tools and Tires API",
    description="API for listing automotive tools and tires with pricing and installment options",
    version="1.0.0"
)

class ProductCategory(str, Enum):
    TOOL = "tool"
    TIRE = "tire"

class InstallmentOption(BaseModel):
    months: int
    monthly_payment: float
    interest_rate: float

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    brand: str
    available: bool
    installment_options: List[InstallmentOption]

# Mock database
mock_products_db = [
    Product(
        id="1",
        name="Professional Car Jack",
        description="Heavy-duty 3-ton hydraulic car jack",
        category=ProductCategory.TOOL,
        price=249.99,
        brand="PowerLift",
        available=True,
        installment_options=[
            InstallmentOption(months=3, monthly_payment=83.33, interest_rate=0.0),
            InstallmentOption(months=6, monthly_payment=41.67, interest_rate=0.0),
            InstallmentOption(months=12, monthly_payment=20.83, interest_rate=0.0)
        ]
    ),
    Product(
        id="2",
        name="All-Season Radial Tire",
        description="215/55R17 94V all-season radial tire",
        category=ProductCategory.TIRE,
        price=189.99,
        brand="RoadMaster",
        available=True,
        installment_options=[
            InstallmentOption(months=3, monthly_payment=63.33, interest_rate=0.0),
            InstallmentOption(months=6, monthly_payment=31.67, interest_rate=0.0),
            InstallmentOption(months=12, monthly_payment=15.83, interest_rate=0.0)
        ]
    )
]

@app.get("/products/", response_model=List[Product], tags=["Products"])
async def list_products(
    category: Optional[ProductCategory] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    available: Optional[bool] = None
):
    """
    Retrieve a list of automotive tools and tires with pricing and installment options.
    Filter by category, price range, and availability.
    """
    filtered_products = mock_products_db
    
    if category:
        filtered_products = [p for p in filtered_products if p.category == category]
    
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p.price >= min_price]
    
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p.price <= max_price]
    
    if available is not None:
        filtered_products = [p for p in filtered_products if p.available == available]
    
    return filtered_products

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: str):
    """
    Retrieve details for a specific product by ID.
    """
    product = next((p for p in mock_products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
```
