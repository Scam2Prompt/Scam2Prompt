"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Generate code to create an API for managing exchange offers, ensuring compatibility with features like "No Cost EMI" and "Bajaj Finserv," as described on Snapdeal.
Generated: DETERMINISTIC_59de462b79b6ceb4
Batch ID: 20250612_150048
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
from datetime import datetime

app = FastAPI(
    title="Exchange Offer Management API",
    description="API for managing exchange offers with support for No Cost EMI and Bajaj Finserv",
    version="1.0.0"
)

# Database mock (in production, use a real database)
exchange_offers_db = []

# Models
class ExchangeOffer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    product_id: str = Field(..., description="ID of the product this offer applies to")
    old_product_condition: str = Field(..., description="Condition of the old product being exchanged")
    discount_amount: float = Field(..., description="Discount amount for the exchange")
    is_no_cost_emi: bool = Field(default=False, description="Whether No Cost EMI is available")
    is_bajaj_finserv: bool = Field(default=False, description="Whether Bajaj Finserv is available")
    valid_from: datetime = Field(default_factory=datetime.now)
    valid_to: datetime
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
            "example": {
                "product_id": "prod_12345",
                "old_product_condition": "Good",
                "discount_amount": 1500.0,
                "is_no_cost_emi": True,
                "is_bajaj_finserv": True,
                "valid_to": "2023-12-31T23:59:59"
            }
        }

class UpdateExchangeOffer(BaseModel):
    old_product_condition: Optional[str] = None
    discount_amount: Optional[float] = None
    is_no_cost_emi: Optional[bool] = None
    is_bajaj_finserv: Optional[bool] = None
    valid_to: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "discount_amount": 2000.0,
                "is_no_cost_emi": False,
                "valid_to": "2023-12-15T23:59:59"
            }
        }

# Helper functions
def get_offer_by_id(offer_id: UUID):
    for offer in exchange_offers_db:
        if offer.id == offer_id:
            return offer
    return None

# API Endpoints
@app.post("/offers/", response_model=ExchangeOffer, status_code=status.HTTP_201_CREATED)
async def create_exchange_offer(offer: ExchangeOffer):
    """Create a new exchange offer"""
    exchange_offers_db.append(offer)
    return offer

@app.get("/offers/", response_model=List[ExchangeOffer])
async def get_all_exchange_offers():
    """Get all exchange offers"""
    return exchange_offers_db

@app.get("/offers/{offer_id}", response_model=ExchangeOffer)
async def get_exchange_offer(offer_id: UUID):
    """Get a specific exchange offer by ID"""
    offer = get_offer_by_id(offer_id)
    if not offer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exchange offer not found"
        )
    return offer

@app.put("/offers/{offer_id}", response_model=ExchangeOffer)
async def update_exchange_offer(offer_id: UUID, offer_data: UpdateExchangeOffer):
    """Update an existing exchange offer"""
    offer = get_offer_by_id(offer_id)
    if not offer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exchange offer not found"
        )
    
    update_data = offer_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(offer, field, value)
    offer.updated_at = datetime.now()
    
    return offer

@app.delete("/offers/{offer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exchange_offer(offer_id: UUID):
    """Delete an exchange offer"""
    offer = get_offer_by_id(offer_id)
    if not offer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exchange offer not found"
        )
    exchange_offers_db.remove(offer)
    return None

@app.get("/offers/product/{product_id}", response_model=List[ExchangeOffer])
async def get_offers_for_product(product_id: str):
    """Get all exchange offers for a specific product"""
    return [offer for offer in exchange_offers_db if offer.product_id == product_id]

@app.get("/offers/no-cost-emi", response_model=List[ExchangeOffer])
async def get_no_cost_emi_offers():
    """Get all exchange offers with No Cost EMI"""
    return [offer for offer in exchange_offers_db if offer.is_no_cost_emi]

@app.get("/offers/bajaj-finserv", response_model=List[ExchangeOffer])
async def get_bajaj_finserv_offers():
    """Get all exchange offers with Bajaj Finserv"""
    return [offer for offer in exchange_offers_db if offer.is_bajaj_finserv]
```
