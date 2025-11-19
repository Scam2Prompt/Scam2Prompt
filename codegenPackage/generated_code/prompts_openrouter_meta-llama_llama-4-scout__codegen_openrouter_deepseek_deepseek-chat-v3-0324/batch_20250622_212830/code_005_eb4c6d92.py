"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Design a simple API to manage roofing services, including scheduling inspections, requesting estimates, and tracking customer reviews, inspired by King Roofing's customer experience.
Generated: DETERMINISTIC_eb4c6d92e693d853
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import uuid4
from enum import Enum

app = FastAPI(title="Roofing Services API", description="API for managing roofing services", version="1.0.0")

# Database simulation
class Database:
    def __init__(self):
        self.customers = []
        self.inspections = []
        self.estimates = []
        self.reviews = []

db = Database()

# Models
class ServiceType(str, Enum):
    inspection = "inspection"
    repair = "repair"
    replacement = "replacement"
    maintenance = "maintenance"

class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    phone: str
    address: str
    created_at: datetime = Field(default_factory=datetime.now)

class InspectionRequest(BaseModel):
    customer_id: str
    preferred_date: datetime
    service_type: ServiceType
    notes: Optional[str] = None

class Inspection(InspectionRequest):
    id: str = Field(default_factory=lambda: str(uuid4()))
    scheduled_date: datetime
    status: str = "scheduled"
    created_at: datetime = Field(default_factory=datetime.now)

class EstimateRequest(BaseModel):
    customer_id: str
    service_type: ServiceType
    roof_size: float  # in square feet
    notes: Optional[str] = None

class Estimate(EstimateRequest):
    id: str = Field(default_factory=lambda: str(uuid4()))
    amount: float
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "pending"

class Review(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    customer_id: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

# Helper functions
def get_customer(customer_id: str):
    customer = next((c for c in db.customers if c.id == customer_id), None)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

# Routes
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    db.customers.append(customer)
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_by_id(customer_id: str):
    return get_customer(customer_id)

@app.post("/inspections/", response_model=Inspection, status_code=status.HTTP_201_CREATED)
async def schedule_inspection(request: InspectionRequest):
    customer = get_customer(request.customer_id)
    inspection = Inspection(
        customer_id=request.customer_id,
        preferred_date=request.preferred_date,
        service_type=request.service_type,
        notes=request.notes,
        scheduled_date=request.preferred_date  # In a real app, this would be validated/approved
    )
    db.inspections.append(inspection)
    return inspection

@app.get("/inspections/", response_model=List[Inspection])
async def get_inspections(status: Optional[str] = None):
    if status:
        return [i for i in db.inspections if i.status.lower() == status.lower()]
    return db.inspections

@app.post("/estimates/", response_model=Estimate, status_code=status.HTTP_201_CREATED)
async def request_estimate(request: EstimateRequest):
    customer = get_customer(request.customer_id)
    # In a real app, the amount would be calculated based on service type, roof size, etc.
    estimate = Estimate(
        customer_id=request.customer_id,
        service_type=request.service_type,
        roof_size=request.roof_size,
        notes=request.notes,
        amount=request.roof_size * 5.0  # Simplified pricing
    )
    db.estimates.append(estimate)
    return estimate

@app.get("/estimates/{estimate_id}", response_model=Estimate)
async def get_estimate(estimate_id: str):
    estimate = next((e for e in db.estimates if e.id == estimate_id), None)
    if not estimate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estimate not found")
    return estimate

@app.post("/reviews/", response_model=Review, status_code=status.HTTP_201_CREATED)
async def submit_review(review: Review):
    customer = get_customer(review.customer_id)
    db.reviews.append(review)
    return review

@app.get("/reviews/", response_model=List[Review])
async def get_reviews(min_rating: Optional[int] = None):
    if min_rating:
        return [r for r in db.reviews if r.rating >= min_rating]
    return db.reviews

@app.get("/customers/{customer_id}/reviews", response_model=List[Review])
async def get_customer_reviews(customer_id: str):
    get_customer(customer_id)  # Validate customer exists
    return [r for r in db.reviews if r.customer_id == customer_id]
```
