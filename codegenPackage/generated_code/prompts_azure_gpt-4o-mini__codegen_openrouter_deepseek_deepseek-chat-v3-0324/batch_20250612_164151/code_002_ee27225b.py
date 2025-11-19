"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: Create an API endpoint that retrieves customer reviews for a men's grooming salon, ensuring it filters by service type (e.g., massage, hair removal) and includes ratings and comments.
Generated: DETERMINISTIC_ee27225b26a9b42a
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Men's Grooming Salon Reviews API",
    description="API for retrieving customer reviews for a men's grooming salon",
    version="1.0.0"
)

# Database mock (in production, replace with actual database connection)
reviews_db = [
    {
        "id": 1,
        "customer_name": "John Doe",
        "service_type": "haircut",
        "rating": 5,
        "comment": "Excellent service, very professional barber.",
        "date": "2023-10-15"
    },
    {
        "id": 2,
        "customer_name": "Mike Smith",
        "service_type": "massage",
        "rating": 4,
        "comment": "Good massage but room was a bit cold.",
        "date": "2023-10-10"
    },
    {
        "id": 3,
        "customer_name": "Alex Johnson",
        "service_type": "hair_removal",
        "rating": 3,
        "comment": "Average experience, took longer than expected.",
        "date": "2023-09-28"
    },
    {
        "id": 4,
        "customer_name": "Sam Wilson",
        "service_type": "haircut",
        "rating": 5,
        "comment": "Best haircut I've ever had!",
        "date": "2023-09-20"
    },
]

class Review(BaseModel):
    id: int
    customer_name: str
    service_type: str
    rating: int
    comment: str
    date: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "customer_name": "John Doe",
                "service_type": "haircut",
                "rating": 5,
                "comment": "Excellent service!",
                "date": "2023-10-15"
            }
        }

@app.get("/reviews/", response_model=List[Review], tags=["Reviews"])
def get_reviews(
    service_type: Optional[str] = Query(
        None,
        description="Filter reviews by service type (e.g., haircut, massage, hair_removal)",
        example="haircut"
    ),
    min_rating: Optional[int] = Query(
        None,
        description="Minimum rating to filter reviews (1-5)",
        ge=1,
        le=5
    )
):
    """
    Retrieve customer reviews with optional filters by service type and minimum rating.
    """
    try:
        filtered_reviews = reviews_db
        
        # Apply service type filter if provided
        if service_type:
            filtered_reviews = [review for review in filtered_reviews 
                              if review["service_type"].lower() == service_type.lower()]
        
        # Apply rating filter if provided
        if min_rating is not None:
            filtered_reviews = [review for review in filtered_reviews 
                              if review["rating"] >= min_rating]
        
        if not filtered_reviews:
            raise HTTPException(
                status_code=404,
                detail="No reviews found matching the criteria"
            )
            
        return filtered_reviews
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing your request: {str(e)}"
        )

@app.get("/reviews/{review_id}", response_model=Review, tags=["Reviews"])
def get_review_by_id(review_id: int):
    """
    Retrieve a specific review by its ID.
    """
    try:
        review = next((r for r in reviews_db if r["id"] == review_id), None)
        if not review:
            raise HTTPException(
                status_code=404,
                detail=f"Review with ID {review_id} not found"
            )
        return review
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing your request: {str(e)}"
        )

@app.get("/services/", tags=["Services"])
def get_available_services():
    """
    Retrieve list of available service types.
    """
    try:
        services = list({review["service_type"] for review in reviews_db})
        return {"available_services": services}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing your request: {str(e)}"
        )
```
