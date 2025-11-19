"""
Generated Code Metadata:
========================
Original URL: https://haynatural.oil.ph
Prompt: Design a simple API for tracking customer testimonials and reviews for Hay Natural Oil, including fields for rating, review text, and condition treated.
Generated: DETERMINISTIC_fdae221094806ea0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, conint
from typing import Optional
from datetime import datetime
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hay Natural Oil Testimonials API",
    description="API for tracking customer testimonials and reviews",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database simulation
testimonials_db = []

# Models
class Testimonial(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    customer_name: str = Field(..., min_length=1, max_length=100)
    rating: conint(ge=1, le=5)
    review_text: str = Field(..., min_length=10, max_length=1000)
    condition_treated: str = Field(..., min_length=3, max_length=100)
    date_submitted: datetime = Field(default_factory=datetime.now)
    approved: bool = Field(default=False)

class TestimonialUpdate(BaseModel):
    customer_name: Optional[str] = Field(None, min_length=1, max_length=100)
    rating: Optional[conint(ge=1, le=5)]
    review_text: Optional[str] = Field(None, min_length=10, max_length=1000)
    condition_treated: Optional[str] = Field(None, min_length=3, max_length=100)
    approved: Optional[bool]

# API Endpoints
@app.post("/testimonials/", status_code=status.HTTP_201_CREATED)
async def create_testimonial(testimonial: Testimonial):
    """
    Create a new testimonial entry.
    """
    testimonials_db.append(testimonial.dict())
    return {"message": "Testimonial created successfully", "id": testimonial.id}

@app.get("/testimonials/", response_model=list[Testimonial])
async def get_testimonials(approved: Optional[bool] = None):
    """
    Get all testimonials, optionally filtered by approval status.
    """
    if approved is None:
        return testimonials_db
    return [t for t in testimonials_db if t["approved"] == approved]

@app.get("/testimonials/{testimonial_id}", response_model=Testimonial)
async def get_testimonial(testimonial_id: str):
    """
    Get a specific testimonial by ID.
    """
    testimonial = next((t for t in testimonials_db if t["id"] == testimonial_id), None)
    if not testimonial:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )
    return testimonial

@app.put("/testimonials/{testimonial_id}")
async def update_testimonial(testimonial_id: str, update_data: TestimonialUpdate):
    """
    Update a testimonial by ID.
    """
    testimonial = next((t for t in testimonials_db if t["id"] == testimonial_id), None)
    if not testimonial:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )
    
    update_data = update_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        testimonial[field] = value
    
    return {"message": "Testimonial updated successfully"}

@app.delete("/testimonials/{testimonial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_testimonial(testimonial_id: str):
    """
    Delete a testimonial by ID.
    """
    global testimonials_db
    initial_length = len(testimonials_db)
    testimonials_db = [t for t in testimonials_db if t["id"] != testimonial_id]
    
    if len(testimonials_db) == initial_length:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )

@app.get("/testimonials/average-rating")
async def get_average_rating(approved: Optional[bool] = None):
    """
    Get the average rating of all testimonials, optionally filtered by approval status.
    """
    filtered = testimonials_db if approved is None else [t for t in testimonials_db if t["approved"] == approved]
    if not filtered:
        return {"average_rating": 0, "count": 0}
    
    total = sum(t["rating"] for t in filtered)
    count = len(filtered)
    return {"average_rating": total / count, "count": count}
```
