"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Create a script to integrate brand-specific offers (e.g., WMF, Sky, SIXT rent a car) into a corporate benefits portal, ensuring proper categorization and display.
Generated: DETERMINISTIC_a63fb869f2e11a43
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Enum for offer categories
class OfferCategory(str, Enum):
    TRAVEL = "travel"
    SHOPPING = "shopping"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"

# Enum for brand names
class BrandName(str, Enum):
    WMF = "WMF"
    SKY = "Sky"
    SIXT = "SIXT Rent a Car"

# Pydantic model for offer data validation
class Offer(BaseModel):
    id: str
    brand: BrandName
    title: str
    description: str
    category: OfferCategory
    discount: Optional[float] = None
    valid_from: datetime
    valid_to: datetime
    terms_and_conditions: str
    is_active: bool = True

    @validator('valid_to')
    def validate_dates(cls, v, values):
        if 'valid_from' in values and v < values['valid_from']:
            raise ValueError("valid_to must be after valid_from")
        return v

# In-memory database simulation
class OfferDatabase:
    def __init__(self):
        self.offers: Dict[str, Offer] = {}

    def add_offer(self, offer: Offer) -> None:
        if offer.id in self.offers:
            raise ValueError(f"Offer with ID {offer.id} already exists")
        self.offers[offer.id] = offer

    def get_offer(self, offer_id: str) -> Optional[Offer]:
        return self.offers.get(offer_id)

    def get_offers_by_brand(self, brand: BrandName) -> List[Offer]:
        return [offer for offer in self.offers.values() if offer.brand == brand]

    def get_offers_by_category(self, category: OfferCategory) -> List[Offer]:
        return [offer for offer in self.offers.values() if offer.category == category]

    def get_active_offers(self) -> List[Offer]:
        return [offer for offer in self.offers.values() if offer.is_active]

    def update_offer(self, offer_id: str, updated_offer: Offer) -> None:
        if offer_id not in self.offers:
            raise ValueError(f"Offer with ID {offer_id} not found")
        self.offers[offer_id] = updated_offer

    def delete_offer(self, offer_id: str) -> None:
        if offer_id not in self.offers:
            raise ValueError(f"Offer with ID {offer_id} not found")
        del self.offers[offer_id]

# FastAPI application
app = FastAPI(title="Corporate Benefits Portal API")
db = OfferDatabase()

# Sample data initialization
def initialize_sample_data():
    sample_offers = [
        {
            "id": "1",
            "brand": BrandName.WMF,
            "title": "WMF Premium Kitchen Set",
            "description": "20% discount on all premium kitchen sets",
            "category": OfferCategory.SHOPPING,
            "discount": 20.0,
            "valid_from": datetime(2023, 1, 1),
            "valid_to": datetime(2023, 12, 31),
            "terms_and_conditions": "Valid for employees only",
            "is_active": True
        },
        {
            "id": "2",
            "brand": BrandName.SKY,
            "title": "Sky Entertainment Package",
            "description": "Free 3 months subscription to Sky Entertainment",
            "category": OfferCategory.ENTERTAINMENT,
            "valid_from": datetime(2023, 1, 1),
            "valid_to": datetime(2023, 6, 30),
            "terms_and_conditions": "New customers only",
            "is_active": True
        },
        {
            "id": "3",
            "brand": BrandName.SIXT,
            "title": "SIXT Weekend Special",
            "description": "15% discount on weekend car rentals",
            "category": OfferCategory.TRAVEL,
            "discount": 15.0,
            "valid_from": datetime(2023, 1, 1),
            "valid_to": datetime(2023, 12, 31),
            "terms_and_conditions": "Minimum 2-day rental",
            "is_active": True
        }
    ]
    
    for offer_data in sample_offers:
        try:
            offer = Offer(**offer_data)
            db.add_offer(offer)
        except Exception as e:
            logger.error(f"Failed to add sample offer {offer_data['id']}: {str(e)}")

initialize_sample_data()

# API Endpoints
@app.post("/offers/", response_model=Offer, status_code=status.HTTP_201_CREATED)
async def create_offer(offer: Offer):
    try:
        db.add_offer(offer)
        logger.info(f"Created new offer: {offer.id}")
        return offer
    except ValueError as e:
        logger.error(f"Error creating offer: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/offers/{offer_id}", response_model=Offer)
async def read_offer(offer_id: str):
    offer = db.get_offer(offer_id)
    if not offer:
        logger.error(f"Offer not found: {offer_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Offer not found"
        )
    return offer

@app.get("/offers/brand/{brand}", response_model=List[Offer])
async def read_offers_by_brand(brand: BrandName):
    return db.get_offers_by_brand(brand)

@app.get("/offers/category/{category}", response_model=List[Offer])
async def read_offers_by_category(category: OfferCategory):
    return db.get_offers_by_category(category)

@app.get("/offers/active/", response_model=List[Offer])
async def read_active_offers():
    return db.get_active_offers()

@app.put("/offers/{offer_id}", response_model=Offer)
async def update_offer(offer_id: str, offer: Offer):
    try:
        db.update_offer(offer_id, offer)
        logger.info(f"Updated offer: {offer_id}")
        return offer
    except ValueError as e:
        logger.error(f"Error updating offer: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@app.delete("/offers/{offer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_offer(offer_id: str):
    try:
        db.delete_offer(offer_id)
        logger.info(f"Deleted offer: {offer_id}")
    except ValueError as e:
        logger.error(f"Error deleting offer: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Main entry point for running the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
