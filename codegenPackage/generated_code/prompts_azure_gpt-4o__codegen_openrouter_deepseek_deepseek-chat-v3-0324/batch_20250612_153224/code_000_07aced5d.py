"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Write code to create an e-commerce product catalog API that includes categories like "Kids Clothing," "Women's Clothing," "Jewelry," and "Accessories," with support for product variants and discounts.
Generated: DETERMINISTIC_07aced5d1bae7adb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="E-Commerce Product Catalog API",
    description="API for managing product catalog with categories, variants, and discounts",
    version="1.0.0"
)

# Database models (in-memory for this example)
class ProductVariant(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    price: float
    sku: str
    stock: int
    attributes: dict = {}

class Discount(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    discount_percent: float = Field(..., ge=0, le=100)
    active: bool = True
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(days=30))

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    category: str
    variants: List[ProductVariant] = []
    discounts: List[Discount] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# In-memory database
db: List[Product] = []

# Helper functions
def get_product_by_id(product_id: UUID) -> Optional[Product]:
    for product in db:
        if product.id == product_id:
            return product
    return None

def get_variant_by_id(product: Product, variant_id: UUID) -> Optional[ProductVariant]:
    for variant in product.variants:
        if variant.id == variant_id:
            return variant
    return None

def get_discount_by_id(product: Product, discount_id: UUID) -> Optional[Discount]:
    for discount in product.discounts:
        if discount.id == discount_id:
            return discount
    return None

# API Endpoints
@app.get("/products", response_model=List[Product], tags=["Products"])
async def list_products(category: Optional[str] = None):
    """List all products, optionally filtered by category"""
    if category:
        return [product for product in db if product.category.lower() == category.lower()]
    return db

@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, tags=["Products"])
async def create_product(product: Product):
    """Create a new product"""
    db.append(product)
    logger.info(f"Created product: {product.name} (ID: {product.id})")
    return product

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
async def get_product(product_id: UUID):
    """Get a specific product by ID"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
async def update_product(product_id: UUID, updated_product: Product):
    """Update a product"""
    for idx, product in enumerate(db):
        if product.id == product_id:
            updated_product.id = product_id
            updated_product.created_at = product.created_at
            updated_product.updated_at = datetime.utcnow()
            db[idx] = updated_product
            logger.info(f"Updated product: {updated_product.name} (ID: {product_id})")
            return updated_product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
async def delete_product(product_id: UUID):
    """Delete a product"""
    for idx, product in enumerate(db):
        if product.id == product_id:
            db.pop(idx)
            logger.info(f"Deleted product with ID: {product_id}")
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

@app.post("/products/{product_id}/variants", response_model=ProductVariant, tags=["Variants"])
async def add_variant(product_id: UUID, variant: ProductVariant):
    """Add a variant to a product"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product.variants.append(variant)
    product.updated_at = datetime.utcnow()
    logger.info(f"Added variant {variant.name} to product ID: {product_id}")
    return variant

@app.put("/products/{product_id}/variants/{variant_id}", response_model=ProductVariant, tags=["Variants"])
async def update_variant(
    product_id: UUID,
    variant_id: UUID,
    updated_variant: ProductVariant
):
    """Update a product variant"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    for idx, variant in enumerate(product.variants):
        if variant.id == variant_id:
            updated_variant.id = variant_id
            product.variants[idx] = updated_variant
            product.updated_at = datetime.utcnow()
            logger.info(f"Updated variant {variant_id} for product ID: {product_id}")
            return updated_variant
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Variant not found"
    )

@app.delete("/products/{product_id}/variants/{variant_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Variants"])
async def delete_variant(product_id: UUID, variant_id: UUID):
    """Delete a product variant"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    for idx, variant in enumerate(product.variants):
        if variant.id == variant_id:
            product.variants.pop(idx)
            product.updated_at = datetime.utcnow()
            logger.info(f"Deleted variant {variant_id} from product ID: {product_id}")
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Variant not found"
    )

@app.post("/products/{product_id}/discounts", response_model=Discount, tags=["Discounts"])
async def add_discount(product_id: UUID, discount: Discount):
    """Add a discount to a product"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    product.discounts.append(discount)
    product.updated_at = datetime.utcnow()
    logger.info(f"Added discount {discount.name} to product ID: {product_id}")
    return discount

@app.put("/products/{product_id}/discounts/{discount_id}", response_model=Discount, tags=["Discounts"])
async def update_discount(
    product_id: UUID,
    discount_id: UUID,
    updated_discount: Discount
):
    """Update a product discount"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    for idx, discount in enumerate(product.discounts):
        if discount.id == discount_id:
            updated_discount.id = discount_id
            product.discounts[idx] = updated_discount
            product.updated_at = datetime.utcnow()
            logger.info(f"Updated discount {discount_id} for product ID: {product_id}")
            return updated_discount
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Discount not found"
    )

@app.delete("/products/{product_id}/discounts/{discount_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Discounts"])
async def delete_discount(product_id: UUID, discount_id: UUID):
    """Delete a product discount"""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    for idx, discount in enumerate(product.discounts):
        if discount.id == discount_id:
            product.discounts.pop(idx)
            product.updated_at = datetime.ut
