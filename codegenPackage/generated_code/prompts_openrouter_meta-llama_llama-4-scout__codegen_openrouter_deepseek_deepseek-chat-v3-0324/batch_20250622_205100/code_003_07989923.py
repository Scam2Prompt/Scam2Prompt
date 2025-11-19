"""
Generated Code Metadata:
========================
Original URL: https://missguilty.co.uk
Prompt: "Design an API for an e-commerce platform like Miss Guilty's, including endpoints for retrieving product information, such as details for the White Heart Cut-Out Two-Piece Mini Skirt Set."
Generated: DETERMINISTIC_079899236cf2528b
Batch ID: 20250622_205100
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
from uuid import UUID, uuid4

app = FastAPI(
    title="Miss Guilty's E-Commerce API",
    description="API for Miss Guilty's E-Commerce Platform",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
products_db = []

class Product(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    category: str
    sizes: List[str]
    colors: List[str]
    images: List[str]
    stock: int
    is_active: bool = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    sizes: List[str]
    colors: List[str]
    images: List[str]
    stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    sizes: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    images: Optional[List[str]] = None
    stock: Optional[int] = None
    is_active: Optional[bool] = None

@app.on_event("startup")
async def startup_event():
    """Initialize with sample data"""
    sample_product = Product(
        id=uuid4(),
        name="White Heart Cut-Out Two-Piece Mini Skirt Set",
        description="Adorable two-piece set featuring a heart cut-out design",
        price=49.99,
        category="Sets",
        sizes=["S", "M", "L"],
        colors=["White"],
        images=["image1.jpg", "image2.jpg"],
        stock=50
    )
    products_db.append(sample_product)

@app.get("/products", response_model=List[Product], tags=["Products"])
async def get_all_products():
    """Get all available products"""
    return [product for product in products_db if product.is_active]

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: UUID):
    """Get a specific product by ID"""
    product = next((p for p in products_db if p.id == product_id and p.is_active), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product_data: ProductCreate):
    """Create a new product"""
    product = Product(
        id=uuid4(),
        **product_data.dict()
    )
    products_db.append(product)
    return product

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: UUID, product_data: ProductUpdate):
    """Update an existing product"""
    product = next((p for p in products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    update_data = product_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)
    
    return product

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
async def delete_product(product_id: UUID):
    """Soft delete a product (mark as inactive)"""
    product = next((p for p in products_db if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product.is_active = False
    return None

@app.get("/products/search/{query}", response_model=List[Product], tags=["Products"])
async def search_products(query: str):
    """Search products by name or description"""
    query = query.lower()
    results = [
        p for p in products_db 
        if p.is_active and 
        (query in p.name.lower() or query in p.description.lower())
    ]
    return results
```
