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
# exchange_offer_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Exchange Offer API",
    description="API for managing exchange offers",
    version="1.0.0",
)

class ExchangeOfferType(str, Enum):
    """Exchange offer types"""
    NO_COST_EMI = "no_cost_emi"
    BAJAJ_FINSERV = "bajaj_finserv"

class ExchangeOffer(BaseModel):
    """Exchange offer model"""
    id: int
    name: str
    description: str
    offer_type: ExchangeOfferType
    min_price: float
    max_price: float
    discount_percentage: float

class ExchangeOfferRequest(BaseModel):
    """Exchange offer request model"""
    name: str
    description: str
    offer_type: ExchangeOfferType
    min_price: float
    max_price: float
    discount_percentage: float

# In-memory exchange offer storage (replace with a database in production)
exchange_offers: List[ExchangeOffer] = [
    ExchangeOffer(
        id=1,
        name="No Cost EMI Offer",
        description="No cost EMI offer for 6 months",
        offer_type=ExchangeOfferType.NO_COST_EMI,
        min_price=1000.0,
        max_price=50000.0,
        discount_percentage=10.0,
    ),
    ExchangeOffer(
        id=2,
        name="Bajaj Finserv Offer",
        description="Bajaj Finserv offer with 12% discount",
        offer_type=ExchangeOfferType.BAJAJ_FINSERV,
        min_price=500.0,
        max_price=20000.0,
        discount_percentage=12.0,
    ),
]

@app.get("/exchange-offers/", response_model=List[ExchangeOffer])
def get_exchange_offers():
    """Get all exchange offers"""
    return exchange_offers

@app.get("/exchange-offers/{offer_id}", response_model=ExchangeOffer)
def get_exchange_offer(offer_id: int):
    """Get an exchange offer by ID"""
    offer = next((offer for offer in exchange_offers if offer.id == offer_id), None)
    if offer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exchange offer not found")
    return offer

@app.post("/exchange-offers/", response_model=ExchangeOffer, status_code=status.HTTP_201_CREATED)
def create_exchange_offer(offer: ExchangeOfferRequest):
    """Create a new exchange offer"""
    new_offer_id = max(offer.id for offer in exchange_offers) + 1 if exchange_offers else 1
    new_offer = ExchangeOffer(
        id=new_offer_id,
        name=offer.name,
        description=offer.description,
        offer_type=offer.offer_type,
        min_price=offer.min_price,
        max_price=offer.max_price,
        discount_percentage=offer.discount_percentage,
    )
    exchange_offers.append(new_offer)
    return new_offer

@app.put("/exchange-offers/{offer_id}", response_model=ExchangeOffer)
def update_exchange_offer(offer_id: int, offer: ExchangeOfferRequest):
    """Update an exchange offer"""
    existing_offer = next((offer for offer in exchange_offers if offer.id == offer_id), None)
    if existing_offer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exchange offer not found")
    existing_offer.name = offer.name
    existing_offer.description = offer.description
    existing_offer.offer_type = offer.offer_type
    existing_offer.min_price = offer.min_price
    existing_offer.max_price = offer.max_price
    existing_offer.discount_percentage = offer.discount_percentage
    return existing_offer

@app.delete("/exchange-offers/{offer_id}")
def delete_exchange_offer(offer_id: int):
    """Delete an exchange offer"""
    global exchange_offers
    exchange_offers = [offer for offer in exchange_offers if offer.id != offer_id]
    return {"message": "Exchange offer deleted successfully"}

@app.get("/exchange-offers/apply/", response_model=dict)
def apply_exchange_offer(offer_id: Optional[int] = None, offer_type: Optional[ExchangeOfferType] = None):
    """Apply an exchange offer"""
    if offer_id:
        offer = next((offer for offer in exchange_offers if offer.id == offer_id), None)
        if offer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exchange offer not found")
        return {"offer_id": offer_id, "discount": offer.discount_percentage}
    elif offer_type:
        offers = [offer for offer in exchange_offers if offer.offer_type == offer_type]
        if not offers:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No offers found for the given type")
        return {"offers": [{"id": offer.id, "discount": offer.discount_percentage} for offer in offers]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Offer ID or type is required")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
