"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Outline a RESTful API that supports financing requests for agricultural equipment, detailing the necessary endpoints and data structures.
Generated: DETERMINISTIC_7de30095087036d5
Batch ID: 20250612_155712
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
from uuid import uuid4, UUID
from datetime import datetime

app = FastAPI(
    title="Agricultural Equipment Financing API",
    description="A RESTful API for managing financing requests for agricultural equipment",
    version="1.0.0"
)

# Data Models
class Equipment(BaseModel):
    id: UUID
    name: str
    type: str
    price: float
    manufacturer: str
    model_year: int

class FinancingRequest(BaseModel):
    id: UUID
    farmer_id: UUID
    equipment_id: UUID
    requested_amount: float
    term_months: int
    interest_rate: float
    status: str  # e.g., "pending", "approved", "rejected"
    created_at: datetime
    updated_at: datetime

class Farmer(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str
    farm_size_acres: float
    credit_score: int

class FinancingRequestCreate(BaseModel):
    farmer_id: UUID
    equipment_id: UUID
    requested_amount: float
    term_months: int

class FinancingRequestUpdate(BaseModel):
    status: str

# In-memory database (replace with actual DB in production)
equipment_db = []
financing_requests_db = []
farmers_db = []

# Endpoints
@app.get("/equipment", response_model=List[Equipment], tags=["Equipment"])
def list_equipment():
    """List all available agricultural equipment"""
    return equipment_db

@app.get("/equipment/{equipment_id}", response_model=Equipment, tags=["Equipment"])
def get_equipment(equipment_id: UUID):
    """Get details of a specific equipment"""
    equipment = next((e for e in equipment_db if e.id == equipment_id), None)
    if not equipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Equipment not found"
        )
    return equipment

@app.post("/financing-requests", response_model=FinancingRequest, status_code=status.HTTP_201_CREATED, tags=["Financing Requests"])
def create_financing_request(request: FinancingRequestCreate):
    """Create a new financing request"""
    farmer = next((f for f in farmers_db if f.id == request.farmer_id), None)
    if not farmer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farmer not found"
        )
    
    equipment = next((e for e in equipment_db if e.id == request.equipment_id), None)
    if not equipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Equipment not found"
        )
    
    financing_request = FinancingRequest(
        id=uuid4(),
        farmer_id=request.farmer_id,
        equipment_id=request.equipment_id,
        requested_amount=request.requested_amount,
        term_months=request.term_months,
        interest_rate=calculate_interest_rate(farmer.credit_score),
        status="pending",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    financing_requests_db.append(financing_request)
    return financing_request

@app.get("/financing-requests", response_model=List[FinancingRequest], tags=["Financing Requests"])
def list_financing_requests():
    """List all financing requests"""
    return financing_requests_db

@app.get("/financing-requests/{request_id}", response_model=FinancingRequest, tags=["Financing Requests"])
def get_financing_request(request_id: UUID):
    """Get details of a specific financing request"""
    request = next((r for r in financing_requests_db if r.id == request_id), None)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Financing request not found"
        )
    return request

@app.patch("/financing-requests/{request_id}", response_model=FinancingRequest, tags=["Financing Requests"])
def update_financing_request_status(request_id: UUID, update: FinancingRequestUpdate):
    """Update the status of a financing request"""
    request = next((r for r in financing_requests_db if r.id == request_id), None)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Financing request not found"
        )
    
    request.status = update.status
    request.updated_at = datetime.now()
    return request

@app.get("/farmers/{farmer_id}/financing-requests", response_model=List[FinancingRequest], tags=["Farmers"])
def get_farmer_financing_requests(farmer_id: UUID):
    """Get all financing requests for a specific farmer"""
    farmer = next((f for f in farmers_db if f.id == farmer_id), None)
    if not farmer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farmer not found"
        )
    
    return [r for r in financing_requests_db if r.farmer_id == farmer_id]

# Helper functions
def calculate_interest_rate(credit_score: int) -> float:
    """Calculate interest rate based on credit score"""
    if credit_score >= 800:
        return 3.5
    elif credit_score >= 700:
        return 4.5
    elif credit_score >= 600:
        return 6.0
    else:
        return 8.5
```
