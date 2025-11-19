"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Design a RESTful API for a travel agency to manage and retrieve information about their packages and promotions, using Fravitur's website as a reference for the types of data that need to be exposed.
Generated: DETERMINISTIC_c57cff3ca15be66d
Batch ID: 20250622_210655
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
from datetime import date
from uuid import UUID, uuid4
from enum import Enum

app = FastAPI(
    title="Travel Agency API",
    description="RESTful API for managing travel packages and promotions",
    version="1.0.0"
)

# Database Models
class PackageType(str, Enum):
    adventure = "adventure"
    beach = "beach"
    cultural = "cultural"
    cruise = "cruise"
    family = "family"
    luxury = "luxury"

class Package(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    type: PackageType
    destinations: List[str]
    duration_days: int
    price: float
    is_active: bool = True

class Promotion(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    package_id: UUID
    discount_percentage: float = Field(..., gt=0, le=100)
    start_date: date
    end_date: date
    description: str
    is_active: bool = True

# In-memory database
db_packages = []
db_promotions = []

# Helper functions
def get_package(package_id: UUID) -> Optional[Package]:
    for package in db_packages:
        if package.id == package_id:
            return package
    return None

def get_promotion(promotion_id: UUID) -> Optional[Promotion]:
    for promotion in db_promotions:
        if promotion.id == promotion_id:
            return promotion
    return None

# Package Endpoints
@app.post("/packages/", response_model=Package, status_code=status.HTTP_201_CREATED)
def create_package(package: Package):
    db_packages.append(package)
    return package

@app.get("/packages/", response_model=List[Package])
def list_packages(active_only: bool = True):
    if active_only:
        return [p for p in db_packages if p.is_active]
    return db_packages

@app.get("/packages/{package_id}", response_model=Package)
def get_package_by_id(package_id: UUID):
    package = get_package(package_id)
    if not package:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Package not found"
        )
    return package

@app.put("/packages/{package_id}", response_model=Package)
def update_package(package_id: UUID, updated_package: Package):
    package = get_package(package_id)
    if not package:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Package not found"
        )
    
    for key, value in updated_package.dict().items():
        setattr(package, key, value)
    
    return package

@app.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_package(package_id: UUID):
    package = get_package(package_id)
    if not package:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Package not found"
        )
    package.is_active = False
    return None

# Promotion Endpoints
@app.post("/promotions/", response_model=Promotion, status_code=status.HTTP_201_CREATED)
def create_promotion(promotion: Promotion):
    if not get_package(promotion.package_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Package does not exist"
        )
    db_promotions.append(promotion)
    return promotion

@app.get("/promotions/", response_model=List[Promotion])
def list_promotions(active_only: bool = True):
    if active_only:
        return [p for p in db_promotions if p.is_active]
    return db_promotions

@app.get("/promotions/{promotion_id}", response_model=Promotion)
def get_promotion_by_id(promotion_id: UUID):
    promotion = get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    return promotion

@app.put("/promotions/{promotion_id}", response_model=Promotion)
def update_promotion(promotion_id: UUID, updated_promotion: Promotion):
    promotion = get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    
    for key, value in updated_promotion.dict().items():
        setattr(promotion, key, value)
    
    return promotion

@app.delete("/promotions/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(promotion_id: UUID):
    promotion = get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    promotion.is_active = False
    return None

@app.get("/packages/{package_id}/promotions", response_model=List[Promotion])
def get_promotions_for_package(package_id: UUID, active_only: bool = True):
    if not get_package(package_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Package not found"
        )
    
    promotions = [p for p in db_promotions if p.package_id == package_id]
    if active_only:
        promotions = [p for p in promotions if p.is_active]
    
    return promotions
```
