"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a product recommendation API for an e-commerce platform that specializes in sports categories like "Beach Vôlei," "Rugby," and "Ginástica Rítmica."
Generated: DETERMINISTIC_bcea1e18f138a747
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sports E-commerce Recommendation API",
    description="API for product recommendations in sports categories",
    version="1.0.0"
)

class SportCategory(str, Enum):
    BEACH_VOLEI = "Beach Vôlei"
    RUGBY = "Rugby"
    GINASTICA_RITMICA = "Ginástica Rítmica"

class Product(BaseModel):
    id: str
    name: str
    category: SportCategory
    price: float
    rating: float
    popularity: int

class RecommendationRequest(BaseModel):
    user_id: str
    category: Optional[SportCategory] = None
    limit: Optional[int] = 5

class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[Product]

# Mock database
mock_products = [
    Product(
        id="1",
        name="Beach Volleyball Net",
        category=SportCategory.BEACH_VOLEI,
        price=89.99,
        rating=4.5,
        popularity=120
    ),
    Product(
        id="2",
        name="Rugby Ball",
        category=SportCategory.RUGBY,
        price=29.99,
        rating=4.2,
        popularity=85
    ),
    Product(
        id="3",
        name="Rhythmic Gymnastics Ribbon",
        category=SportCategory.GINASTICA_RITMICA,
        price=19.99,
        rating=4.7,
        popularity=65
    ),
    Product(
        id="4",
        name="Beach Volleyball",
        category=SportCategory.BEACH_VOLEI,
        price=24.99,
        rating=4.3,
        popularity=110
    ),
    Product(
        id="5",
        name="Rugby Jersey",
        category=SportCategory.RUGBY,
        price=49.99,
        rating=4.0,
        popularity=75
    ),
    Product(
        id="6",
        name="Gymnastics Leotard",
        category=SportCategory.GINASTICA_RITMICA,
        price=39.99,
        rating=4.6,
        popularity=90
    ),
]

@app.get("/health", status_code=200)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/recommendations", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """
    Get product recommendations based on user and category.
    
    Args:
        request: RecommendationRequest containing user_id and optional category filter
    
    Returns:
        List of recommended products
    """
    try:
        logger.info(f"Generating recommendations for user {request.user_id}")
        
        # Filter products by category if specified
        if request.category:
            filtered_products = [
                p for p in mock_products if p.category == request.category
            ]
        else:
            filtered_products = mock_products
        
        # Sort by rating and popularity (simple recommendation algorithm)
        sorted_products = sorted(
            filtered_products,
            key=lambda x: (x.rating, x.popularity),
            reverse=True
        )
        
        # Apply limit
        recommendations = sorted_products[:request.limit]
        
        return RecommendationResponse(
            user_id=request.user_id,
            recommendations=recommendations
        )
        
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating recommendations"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
