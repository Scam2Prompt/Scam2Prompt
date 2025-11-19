"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Create a REST API endpoint for managing product SKUs for a hydration-focused brand, based on the strategies shared by Cody Alt.
Generated: DETERMINISTIC_14f36fb4e7e49c30
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from uuid import UUID
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI(
    title="Hydration-Focused Brand Product SKUs API",
    description="API for managing product SKUs",
    version="1.0.0"
)

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///hydration_brand.db"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Define Product SKU model
class ProductSKU(Base):
    __tablename__ = "product_skus"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    stock_quantity = Column(Integer, index=True)

# Create database tables
Base.metadata.create_all(bind=engine)

# Define Pydantic model for product SKUs
class ProductSKURequest(BaseModel):
    sku: str
    name: str
    price: float
    stock_quantity: int

    class Config:
        schema_extra = {
            "example": {
                "sku": "HYDRATE-001",
                "name": "Hydrate Water Bottle",
                "price": 19.99,
                "stock_quantity": 100
            }
        }

# Define Pydantic model for product SKU response
class ProductSKUResponse(BaseModel):
    id: int
    sku: str
    name: str
    price: float
    stock_quantity: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "sku": "HYDRATE-001",
                "name": "Hydrate Water Bottle",
                "price": 19.99,
                "stock_quantity": 100
            }
        }

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create product SKU endpoint
@app.post("/product-skus/", status_code=status.HTTP_201_CREATED, response_model=ProductSKUResponse)
async def create_product_sku(product_sku: ProductSKURequest, db: SessionLocal = get_db):
    # Check if SKU already exists
    existing_sku = db.query(ProductSKU).filter(ProductSKU.sku == product_sku.sku).first()
    if existing_sku:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SKU already exists")

    # Create new product SKU
    new_sku = ProductSKU(
        sku=product_sku.sku,
        name=product_sku.name,
        price=product_sku.price,
        stock_quantity=product_sku.stock_quantity
    )
    db.add(new_sku)
    db.commit()
    db.refresh(new_sku)

    return ProductSKUResponse(
        id=new_sku.id,
        sku=new_sku.sku,
        name=new_sku.name,
        price=new_sku.price,
        stock_quantity=new_sku.stock_quantity
    )

# Read product SKUs endpoint
@app.get("/product-skus/", status_code=status.HTTP_200_OK, response_model=List[ProductSKUResponse])
async def read_product_skus(db: SessionLocal = get_db):
    product_skus = db.query(ProductSKU).all()
    return [
        ProductSKUResponse(
            id=sku.id,
            sku=sku.sku,
            name=sku.name,
            price=sku.price,
            stock_quantity=sku.stock_quantity
        ) for sku in product_skus
    ]

# Read product SKU endpoint
@app.get("/product-skus/{sku}", status_code=status.HTTP_200_OK, response_model=ProductSKUResponse)
async def read_product_sku(sku: str, db: SessionLocal = get_db):
    product_sku = db.query(ProductSKU).filter(ProductSKU.sku == sku).first()
    if not product_sku:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product SKU not found")

    return ProductSKUResponse(
        id=product_sku.id,
        sku=product_sku.sku,
        name=product_sku.name,
        price=product_sku.price,
        stock_quantity=product_sku.stock_quantity
    )

# Update product SKU endpoint
@app.put("/product-skus/{sku}", status_code=status.HTTP_200_OK, response_model=ProductSKUResponse)
async def update_product_sku(sku: str, product_sku: ProductSKURequest, db: SessionLocal = get_db):
    existing_sku = db.query(ProductSKU).filter(ProductSKU.sku == sku).first()
    if not existing_sku:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product SKU not found")

    # Update existing product SKU
    existing_sku.name = product_sku.name
    existing_sku.price = product_sku.price
    existing_sku.stock_quantity = product_sku.stock_quantity
    db.commit()
    db.refresh(existing_sku)

    return ProductSKUResponse(
        id=existing_sku.id,
        sku=existing_sku.sku,
        name=existing_sku.name,
        price=existing_sku.price,
        stock_quantity=existing_sku.stock_quantity
    )

# Delete product SKU endpoint
@app.delete("/product-skus/{sku}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_sku(sku: str, db: SessionLocal = get_db):
    product_sku = db.query(ProductSKU).filter(ProductSKU.sku == sku).first()
    if not product_sku:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product SKU not found")

    db.delete(product_sku)
    db.commit()

    return {"message": "Product SKU deleted successfully"}
```
