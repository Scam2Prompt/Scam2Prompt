"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Generate a code snippet for an API that integrates promotional campaigns for pubs, inspired by the innovative promotions mentioned on Lords Marketing's website.
Generated: DETERMINISTIC_a0da0b8f39f84539
Batch ID: 20250612_162051
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
from datetime import datetime
import uuid

app = FastAPI(
    title="Pub Promotions API",
    description="API for managing promotional campaigns for pubs, inspired by Lords Marketing's innovative promotions.",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
promotions_db = []

class Promotion(BaseModel):
    id: str
    pub_id: str
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    discount_percentage: Optional[float] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

class CreatePromotionRequest(BaseModel):
    pub_id: str
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    discount_percentage: Optional[float] = None

class UpdatePromotionRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    discount_percentage: Optional[float] = None
    is_active: Optional[bool] = None

@app.post("/promotions/", response_model=Promotion, status_code=status.HTTP_201_CREATED)
async def create_promotion(promotion: CreatePromotionRequest):
    """
    Create a new promotional campaign for a pub.
    """
    # Validate dates
    if promotion.start_date >= promotion.end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date must be after start date"
        )

    # Create promotion object
    now = datetime.now()
    promotion_id = str(uuid.uuid4())
    new_promotion = Promotion(
        id=promotion_id,
        pub_id=promotion.pub_id,
        title=promotion.title,
        description=promotion.description,
        start_date=promotion.start_date,
        end_date=promotion.end_date,
        discount_percentage=promotion.discount_percentage,
        is_active=True,
        created_at=now,
        updated_at=now
    )

    # Store in database
    promotions_db.append(new_promotion)
    return new_promotion

@app.get("/promotions/", response_model=List[Promotion])
async def get_promotions(pub_id: Optional[str] = None, active_only: bool = False):
    """
    Get all promotions, optionally filtered by pub_id and active status.
    """
    result = promotions_db
    
    if pub_id:
        result = [p for p in result if p.pub_id == pub_id]
    
    if active_only:
        now = datetime.now()
        result = [p for p in result if p.is_active and p.start_date <= now <= p.end_date]
    
    return result

@app.get("/promotions/{promotion_id}", response_model=Promotion)
async def get_promotion(promotion_id: str):
    """
    Get a specific promotion by ID.
    """
    promotion = next((p for p in promotions_db if p.id == promotion_id), None)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
    return promotion

@app.put("/promotions/{promotion_id}", response_model=Promotion)
async def update_promotion(promotion_id: str, update_data: UpdatePromotionRequest):
    """
    Update a promotion's details.
    """
    # Find promotion
    promotion = next((p for p in promotions_db if p.id == promotion_id), None)
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )

    # Validate dates if being updated
    if update_data.start_date and update_data.end_date:
        if update_data.start_date >= update_data.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End date must be after start date"
            )

    # Update fields
    update_dict = update_data.dict(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(promotion, field, value)
    promotion.updated_at = datetime.now()

    return promotion

@app.delete("/promotions/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promotion(promotion_id: str):
    """
    Delete a promotion.
    """
    global promotions_db
    initial_length = len(promotions_db)
    promotions_db = [p for p in promotions_db if p.id != promotion_id]
    
    if len(promotions_db) == initial_length:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Promotion not found"
        )
```
