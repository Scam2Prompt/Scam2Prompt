"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: "Generate a RESTful API endpoint for creating and managing distribution partnerships with VIDA TRADE LLC, including parameters for customized marketing support and flexible payment terms."
Generated: DETERMINISTIC_d2c39f57d821e8ec
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
from typing import Optional, List
from uuid import uuid4, UUID
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="VIDA TRADE LLC Partnership API",
    description="API for managing distribution partnerships with VIDA TRADE LLC",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
db = {}

# Models
class MarketingSupportLevel(str, Enum):
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"

class PaymentTerm(str, Enum):
    NET_15 = "net_15"
    NET_30 = "net_30"
    NET_60 = "net_60"
    CUSTOM = "custom"

class PartnershipCreate(BaseModel):
    partner_name: str = Field(..., min_length=2, max_length=100)
    contact_email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    marketing_support: MarketingSupportLevel = MarketingSupportLevel.STANDARD
    payment_terms: PaymentTerm = PaymentTerm.NET_30
    custom_payment_terms: Optional[str] = Field(None, max_length=200)
    marketing_budget: Optional[float] = Field(None, gt=0)
    notes: Optional[str] = Field(None, max_length=500)

class PartnershipResponse(PartnershipCreate):
    partnership_id: UUID
    created_at: datetime
    updated_at: datetime
    status: str = "active"

# Helper functions
def get_partnership_or_404(partnership_id: UUID):
    partnership = db.get(str(partnership_id))
    if not partnership:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Partnership not found"
        )
    return partnership

# Endpoints
@app.post("/partnerships/", response_model=PartnershipResponse, status_code=status.HTTP_201_CREATED)
async def create_partnership(partnership: PartnershipCreate):
    """
    Create a new distribution partnership with VIDA TRADE LLC.
    
    Parameters:
    - partner_name: Name of the partner organization
    - contact_email: Valid email address for primary contact
    - marketing_support: Level of marketing support (basic, standard, premium)
    - payment_terms: Payment terms (net_15, net_30, net_60, custom)
    - custom_payment_terms: Required if payment_terms is 'custom'
    - marketing_budget: Optional budget for marketing support
    - notes: Additional notes about the partnership
    """
    partnership_id = uuid4()
    now = datetime.utcnow()
    
    if partnership.payment_terms == PaymentTerm.CUSTOM and not partnership.custom_payment_terms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="custom_payment_terms is required when payment_terms is 'custom'"
        )
    
    partnership_data = partnership.dict()
    partnership_data.update({
        "partnership_id": partnership_id,
        "created_at": now,
        "updated_at": now,
        "status": "active"
    })
    
    db[str(partnership_id)] = partnership_data
    return partnership_data

@app.get("/partnerships/{partnership_id}", response_model=PartnershipResponse)
async def get_partnership(partnership_id: UUID):
    """
    Retrieve details of a specific partnership.
    """
    return get_partnership_or_404(partnership_id)

@app.get("/partnerships/", response_model=List[PartnershipResponse])
async def list_partnerships(status_filter: Optional[str] = None):
    """
    List all partnerships, optionally filtered by status.
    """
    partnerships = list(db.values())
    if status_filter:
        partnerships = [p for p in partnerships if p["status"].lower() == status_filter.lower()]
    return partnerships

@app.patch("/partnerships/{partnership_id}", response_model=PartnershipResponse)
async def update_partnership(
    partnership_id: UUID,
    marketing_support: Optional[MarketingSupportLevel] = None,
    payment_terms: Optional[PaymentTerm] = None,
    custom_payment_terms: Optional[str] = None,
    marketing_budget: Optional[float] = None,
    notes: Optional[str] = None
):
    """
    Update specific fields of a partnership.
    """
    partnership = get_partnership_or_404(partnership_id)
    
    if payment_terms == PaymentTerm.CUSTOM and not custom_payment_terms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="custom_payment_terms is required when payment_terms is 'custom'"
        )
    
    if marketing_support:
        partnership["marketing_support"] = marketing_support
    if payment_terms:
        partnership["payment_terms"] = payment_terms
    if custom_payment_terms:
        partnership["custom_payment_terms"] = custom_payment_terms
    if marketing_budget is not None:
        partnership["marketing_budget"] = marketing_budget
    if notes is not None:
        partnership["notes"] = notes
    
    partnership["updated_at"] = datetime.utcnow()
    return partnership

@app.delete("/partnerships/{partnership_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deactivate_partnership(partnership_id: UUID):
    """
    Deactivate a partnership (soft delete).
    """
    partnership = get_partnership_or_404(partnership_id)
    partnership["status"] = "inactive"
    partnership["updated_at"] = datetime.utcnow()
    return None
```
