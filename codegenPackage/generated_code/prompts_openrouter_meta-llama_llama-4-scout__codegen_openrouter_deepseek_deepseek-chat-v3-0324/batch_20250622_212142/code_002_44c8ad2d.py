"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Generate a RESTful API endpoint to handle user requests for project estimates, including parameters for project type (e.g., cuisine, toiture, electricité) and location, and return a list of qualified artisans and their quotes.
Generated: DETERMINISTIC_44c8ad2def566c8d
Batch ID: 20250622_212142
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Project Estimation API",
    description="API for getting project estimates from qualified artisans",
    version="1.0.0"
)

# Database mock (in production, this would be a real database connection)
class Artisan(BaseModel):
    id: int
    name: str
    profession: str
    location: str
    rating: float
    min_price: float
    max_price: float
    availability: str

# Mock database
ARTISANS_DB = [
    Artisan(
        id=1,
        name="Jean Dupont",
        profession="cuisine",
        location="Paris",
        rating=4.5,
        min_price=5000,
        max_price=10000,
        availability="within 2 weeks"
    ),
    Artisan(
        id=2,
        name="Marie Martin",
        profession="toiture",
        location="Lyon",
        rating=4.8,
        min_price=8000,
        max_price=15000,
        availability="within 1 week"
    ),
    Artisan(
        id=3,
        name="Pierre Durand",
        profession="electricité",
        location="Marseille",
        rating=4.2,
        min_price=3000,
        max_price=7000,
        availability="immediate"
    ),
    Artisan(
        id=4,
        name="Sophie Lambert",
        profession="cuisine",
        location="Paris",
        rating=4.7,
        min_price=6000,
        max_price=12000,
        availability="within 3 weeks"
    ),
]

class EstimateRequest(BaseModel):
    project_type: str
    location: str
    budget: Optional[float] = None
    urgency: Optional[str] = None

class EstimateResponse(BaseModel):
    artisans: List[Artisan]
    timestamp: str
    request: EstimateRequest

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/estimates", response_model=EstimateResponse)
async def get_estimates(request: EstimateRequest):
    """
    Get project estimates from qualified artisans based on project type and location.
    
    Parameters:
    - project_type: Type of project (e.g., cuisine, toiture, electricité)
    - location: Location where the project will be executed
    - budget: Optional budget constraint
    - urgency: Optional urgency level (e.g., immediate, within 1 week, etc.)
    
    Returns:
    - List of qualified artisans with their price ranges and availability
    """
    try:
        logger.info(f"Received estimate request: {request}")
        
        # Filter artisans by project type and location
        qualified_artisans = [
            artisan for artisan in ARTISANS_DB 
            if artisan.profession.lower() == request.project_type.lower()
            and artisan.location.lower() == request.location.lower()
        ]
        
        if not qualified_artisans:
            raise HTTPException(
                status_code=404,
                detail="No artisans found for the specified criteria"
            )
        
        # Apply optional filters
        if request.budget:
            qualified_artisans = [
                artisan for artisan in qualified_artisans
                if artisan.min_price <= request.budget
            ]
            
        if request.urgency:
            qualified_artisans = [
                artisan for artisan in qualified_artisans
                if artisan.availability.lower() == request.urgency.lower()
            ]
        
        response = EstimateResponse(
            artisans=qualified_artisans,
            timestamp=datetime.now().isoformat(),
            request=request
        )
        
        logger.info(f"Returning {len(qualified_artisans)} artisans")
        return response
        
    except Exception as e:
        logger.error(f"Error processing estimate request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

@app.get("/artisans", response_model=List[Artisan])
async def list_artisans(
    profession: Optional[str] = Query(None, description="Filter by profession"),
    location: Optional[str] = Query(None, description="Filter by location"),
    min_rating: Optional[float] = Query(None, ge=0, le=5, description="Minimum rating")
):
    """List all artisans with optional filters"""
    try:
        artisans = ARTISANS_DB
        
        if profession:
            artisans = [a for a in artisans if a.profession.lower() == profession.lower()]
        
        if location:
            artisans = [a for a in artisans if a.location.lower() == location.lower()]
            
        if min_rating is not None:
            artisans = [a for a in artisans if a.rating >= min_rating]
            
        return artisans
        
    except Exception as e:
        logger.error(f"Error listing artisans: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching artisans"
        )
```
