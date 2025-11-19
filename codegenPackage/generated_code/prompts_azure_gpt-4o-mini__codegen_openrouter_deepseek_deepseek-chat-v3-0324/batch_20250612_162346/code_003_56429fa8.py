"""
Generated Code Metadata:
========================
Original URL: https://gapkindo.org
Prompt: Develop a REST API that provides access to rubber price statistics and trends as outlined by GAPKINDO for developers interested in the rubber market.
Generated: DETERMINISTIC_56429fa8cc206200
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import date
import uvicorn
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="GAPKINDO Rubber Price API",
    description="REST API for accessing rubber price statistics and trends from GAPKINDO",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@rubberapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database mock (in production, replace with actual database connection)
rubber_prices_db = []

# Pydantic models for request/response validation
class RubberPrice(BaseModel):
    id: int
    date: date
    price: float
    currency: str = "USD"
    rubber_type: str
    region: str
    source: str = "GAPKINDO"

class PriceTrendResponse(BaseModel):
    period: str
    average_price: float
    min_price: float
    max_price: float
    price_change_percentage: Optional[float] = None

class PriceCreate(BaseModel):
    date: date
    price: float
    currency: str = "USD"
    rubber_type: str
    region: str

# Database initialization with sample data
def initialize_db():
    global rubber_prices_db
    sample_data = [
        {
            "id": 1,
            "date": date(2023, 1, 1),
            "price": 1.50,
            "currency": "USD",
            "rubber_type": "SIR20",
            "region": "Sumatra",
            "source": "GAPKINDO"
        },
        {
            "id": 2,
            "date": date(2023, 1, 2),
            "price": 1.52,
            "currency": "USD",
            "rubber_type": "SIR20",
            "region": "Sumatra",
            "source": "GAPKINDO"
        },
        {
            "id": 3,
            "date": date(2023, 1, 1),
            "price": 1.48,
            "currency": "USD",
            "rubber_type": "RSS3",
            "region": "Kalimantan",
            "source": "GAPKINDO"
        }
    ]
    rubber_prices_db = [RubberPrice(**data) for data in sample_data]

initialize_db()

# Helper functions
def get_next_id():
    return max([price.id for price in rubber_prices_db], default=0) + 1

# API endpoints
@app.get("/prices/", response_model=List[RubberPrice], tags=["Prices"])
async def get_all_prices(
    skip: int = 0,
    limit: int = Query(100, le=1000),
    rubber_type: Optional[str] = None,
    region: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    """
    Get all rubber prices with optional filtering.
    """
    try:
        filtered_prices = rubber_prices_db
        
        if rubber_type:
            filtered_prices = [p for p in filtered_prices if p.rubber_type.lower() == rubber_type.lower()]
        
        if region:
            filtered_prices = [p for p in filtered_prices if p.region.lower() == region.lower()]
        
        if start_date:
            filtered_prices = [p for p in filtered_prices if p.date >= start_date]
        
        if end_date:
            filtered_prices = [p for p in filtered_prices if p.date <= end_date]
        
        return filtered_prices[skip : skip + limit]
    
    except Exception as e:
        logger.error(f"Error fetching prices: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/prices/{price_id}", response_model=RubberPrice, tags=["Prices"])
async def get_price_by_id(price_id: int):
    """
    Get a specific rubber price by ID.
    """
    try:
        price = next((p for p in rubber_prices_db if p.id == price_id), None)
        if price is None:
            raise HTTPException(status_code=404, detail="Price not found")
        return price
    except Exception as e:
        logger.error(f"Error fetching price with ID {price_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/prices/", response_model=RubberPrice, status_code=201, tags=["Prices"])
async def create_price(price: PriceCreate):
    """
    Create a new rubber price entry.
    """
    try:
        new_price = RubberPrice(
            id=get_next_id(),
            **price.dict()
        )
        rubber_prices_db.append(new_price)
        logger.info(f"Created new price entry with ID {new_price.id}")
        return new_price
    except Exception as e:
        logger.error(f"Error creating price: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/trends/", response_model=List[PriceTrendResponse], tags=["Trends"])
async def get_price_trends(
    rubber_type: str,
    region: str,
    period: str = Query("monthly", regex="^(daily|weekly|monthly|yearly)$")
):
    """
    Get price trends for a specific rubber type and region.
    """
    try:
        # In a real implementation, this would query the database for trends
        # This is a simplified mock implementation
        filtered_prices = [p for p in rubber_prices_db 
                          if p.rubber_type.lower() == rubber_type.lower()
                          and p.region.lower() == region.lower()]
        
        if not filtered_prices:
            raise HTTPException(status_code=404, detail="No data found for the specified criteria")
        
        prices = [p.price for p in filtered_prices]
        avg_price = sum(prices) / len(prices)
        
        response = PriceTrendResponse(
            period=period,
            average_price=avg_price,
            min_price=min(prices),
            max_price=max(prices)
        )
        
        return [response]
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error calculating trends: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health", tags=["System"])
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
