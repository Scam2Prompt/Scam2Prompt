"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: "Develop a RESTful API endpoint to handle customer reviews for Vaarabella, allowing users to submit and view reviews for various products."
Generated: DETERMINISTIC_73ad89becbf73832
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Vaarabella Reviews API",
    description="API for managing customer reviews for Vaarabella products",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database simulation (in-memory for demonstration)
reviews_db = []

# Models
class Review(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    product_id: str
    user_id: str
    rating: int = Field(..., ge=1, le=5)
    title: str = Field(..., min_length=5, max_length=100)
    comment: str = Field(..., min_length=10, max_length=500)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class ReviewCreate(BaseModel):
    product_id: str
    rating: int = Field(..., ge=1, le=5)
    title: str = Field(..., min_length=5, max_length=100)
    comment: str = Field(..., min_length=10, max_length=500)

class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(None, ge=1, le=5)
    title: Optional[str] = Field(None, min_length=5, max_length=100)
    comment: Optional[str] = Field(None, min_length=10, max_length=500)

# Helper functions
def get_review(review_id: str):
    for review in reviews_db:
        if review.id == review_id:
            return review
    return None

def get_reviews_for_product(product_id: str):
    return [review for review in reviews_db if review.product_id == product_id]

def get_reviews_by_user(user_id: str):
    return [review for review in reviews_db if review.user_id == user_id]

# Authentication simulation (for demonstration)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real application, validate the token and return user info
    return {"user_id": "demo-user"}

# API Endpoints
@app.post("/reviews/", response_model=Review, status_code=status.HTTP_201_CREATED)
async def create_review(
    review_data: ReviewCreate,
    current_user: dict = Depends(get_current_user)
):
    """
    Create a new review for a product.
    """
    review = Review(
        product_id=review_data.product_id,
        user_id=current_user["user_id"],
        rating=review_data.rating,
        title=review_data.title,
        comment=review_data.comment
    )
    reviews_db.append(review)
    return review

@app.get("/reviews/", response_model=List[Review])
async def list_reviews(
    product_id: Optional[str] = None,
    user_id: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    """
    List all reviews, optionally filtered by product_id or user_id.
    """
    reviews = reviews_db
    
    if product_id:
        reviews = get_reviews_for_product(product_id)
    elif user_id:
        reviews = get_reviews_by_user(user_id)
    
    return reviews[offset:offset+limit]

@app.get("/reviews/{review_id}", response_model=Review)
async def get_review_by_id(review_id: str):
    """
    Get a specific review by its ID.
    """
    review = get_review(review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )
    return review

@app.put("/reviews/{review_id}", response_model=Review)
async def update_review(
    review_id: str,
    review_data: ReviewUpdate,
    current_user: dict = Depends(get_current_user)
):
    """
    Update an existing review (only by the original author).
    """
    review = get_review(review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )
    
    if review.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own reviews"
        )
    
    if review_data.rating:
        review.rating = review_data.rating
    if review_data.title:
        review.title = review_data.title
    if review_data.comment:
        review.comment = review_data.comment
    
    review.updated_at = datetime.now()
    return review

@app.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(
    review_id: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Delete a review (only by the original author).
    """
    review = get_review(review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )
    
    if review.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own reviews"
        )
    
    reviews_db.remove(review)
    return None

@app.get("/products/{product_id}/average-rating", response_model=dict)
async def get_product_average_rating(product_id: str):
    """
    Get the average rating for a product.
    """
    product_reviews = get_reviews_for_product(product_id)
    if not product_reviews:
        return {"product_id": product_id, "average_rating": 0, "review_count": 0}
    
    total_ratings = sum(review.rating for review in product_reviews)
    average = total_ratings / len(product_reviews)
    return {
        "product_id": product_id,
        "average_rating": round(average, 2),
        "review_count": len(product_reviews)
    }
```
