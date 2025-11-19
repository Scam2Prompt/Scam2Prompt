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
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI(
    title="Travel Agency API",
    description="Manage and retrieve information about packages and promotions",
    version="1.0.0"
)

# Define Pydantic models for request and response bodies
class Package(BaseModel):
    id: int
    name: str
    description: str
    price: float
    duration: int
    departure_date: date
    return_date: Optional[date]

class Promotion(BaseModel):
    id: int
    package_id: int
    discount: float
    start_date: date
    end_date: date

class PackageResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    duration: int
    departure_date: date
    return_date: Optional[date]
    promotions: List[Promotion]

class PromotionResponse(BaseModel):
    id: int
    package_id: int
    discount: float
    start_date: date
    end_date: date

# In-memory data store (replace with a database in production)
packages = [
    Package(id=1, name="Package 1", description="Description 1", price=1000.0, duration=7, departure_date=date(2024, 9, 1), return_date=date(2024, 9, 8)),
    Package(id=2, name="Package 2", description="Description 2", price=2000.0, duration=14, departure_date=date(2024, 10, 1), return_date=date(2024, 10, 15)),
]

promotions = [
    Promotion(id=1, package_id=1, discount=10.0, start_date=date(2024, 8, 1), end_date=date(2024, 8, 31)),
    Promotion(id=2, package_id=2, discount=20.0, start_date=date(2024, 9, 1), end_date=date(2024, 9, 30)),
]

# GET /
@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"message": "Travel Agency API"}

# GET /packages
@app.get("/packages/", response_model=List[PackageResponse], status_code=status.HTTP_200_OK)
async def read_packages():
    result = []
    for package in packages:
        package_promotions = [p for p in promotions if p.package_id == package.id]
        result.append(PackageResponse(id=package.id, name=package.name, description=package.description, price=package.price, duration=package.duration, departure_date=package.departure_date, return_date=package.return_date, promotions=package_promotions))
    return result

# GET /packages/{package_id}
@app.get("/packages/{package_id}", response_model=PackageResponse, status_code=status.HTTP_200_OK)
async def read_package(package_id: int):
    package = next((p for p in packages if p.id == package_id), None)
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
    package_promotions = [p for p in promotions if p.package_id == package.id]
    return PackageResponse(id=package.id, name=package.name, description=package.description, price=package.price, duration=package.duration, departure_date=package.departure_date, return_date=package.return_date, promotions=package_promotions)

# GET /promotions
@app.get("/promotions/", response_model=List[PromotionResponse], status_code=status.HTTP_200_OK)
async def read_promotions():
    return promotions

# GET /promotions/{promotion_id}
@app.get("/promotions/{promotion_id}", response_model=PromotionResponse, status_code=status.HTTP_200_OK)
async def read_promotion(promotion_id: int):
    promotion = next((p for p in promotions if p.id == promotion_id), None)
    if promotion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    return promotion

# POST /packages
@app.post("/packages/", response_model=PackageResponse, status_code=status.HTTP_201_CREATED)
async def create_package(package: Package):
    packages.append(package)
    return PackageResponse(id=package.id, name=package.name, description=package.description, price=package.price, duration=package.duration, departure_date=package.departure_date, return_date=package.return_date, promotions=[])

# POST /promotions
@app.post("/promotions/", response_model=PromotionResponse, status_code=status.HTTP_201_CREATED)
async def create_promotion(promotion: Promotion):
    promotions.append(promotion)
    return promotion

# PUT /packages/{package_id}
@app.put("/packages/{package_id}", response_model=PackageResponse, status_code=status.HTTP_200_OK)
async def update_package(package_id: int, package: Package):
    existing_package = next((p for p in packages if p.id == package_id), None)
    if existing_package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
    existing_package.name = package.name
    existing_package.description = package.description
    existing_package.price = package.price
    existing_package.duration = package.duration
    existing_package.departure_date = package.departure_date
    existing_package.return_date = package.return_date
    package_promotions = [p for p in promotions if p.package_id == package_id]
    return PackageResponse(id=existing_package.id, name=existing_package.name, description=existing_package.description, price=existing_package.price, duration=existing_package.duration, departure_date=existing_package.departure_date, return_date=existing_package.return_date, promotions=package_promotions)

# PUT /promotions/{promotion_id}
@app.put("/promotions/{promotion_id}", response_model=PromotionResponse, status_code=status.HTTP_200_OK)
async def update_promotion(promotion_id: int, promotion: Promotion):
    existing_promotion = next((p for p in promotions if p.id == promotion_id), None)
    if existing_promotion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    existing_promotion.package_id = promotion.package_id
    existing_promotion.discount = promotion.discount
    existing_promotion.start_date = promotion.start_date
    existing_promotion.end_date = promotion.end_date
    return existing_promotion

# DELETE /packages/{package_id}
@app.delete("/packages/{package_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_package(package_id: int):
    package = next((p for p in packages if p.id == package_id), None)
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
    packages.remove(package)

# DELETE /promotions/{promotion_id}
@app.delete("/promotions/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promotion(promotion_id: int):
    promotion = next((p for p in promotions if p.id == promotion_id), None)
    if promotion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found")
    promotions.remove(promotion)
```
