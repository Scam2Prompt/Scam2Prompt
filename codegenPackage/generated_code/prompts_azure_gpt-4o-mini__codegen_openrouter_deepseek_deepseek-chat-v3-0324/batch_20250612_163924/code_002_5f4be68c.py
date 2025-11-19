"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create an API endpoint that retrieves listings for businesses for sale, including details like location and price, similar to the lighting store listing in São Paulo.
Generated: DETERMINISTIC_5f4be68c7e8fd79e
Batch ID: 20250612_163924
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
import uvicorn

app = FastAPI()

# Mock database of business listings
business_listings_db = [
    {
        "id": 1,
        "name": "São Paulo Lighting Store",
        "description": "Premium lighting fixtures store in downtown São Paulo",
        "location": "São Paulo, Brazil",
        "price": 250000,
        "category": "Retail",
        "annual_revenue": 120000,
        "established_year": 2015
    },
    {
        "id": 2,
        "name": "Rio Café",
        "description": "Popular coffee shop in Rio de Janeiro",
        "location": "Rio de Janeiro, Brazil",
        "price": 180000,
        "category": "Food & Beverage",
        "annual_revenue": 95000,
        "established_year": 2018
    },
    {
        "id": 3,
        "name": "Belo Horizonte Gym",
        "description": "Well-established fitness center",
        "location": "Belo Horizonte, Brazil",
        "price": 320000,
        "category": "Fitness",
        "annual_revenue": 150000,
        "established_year": 2012
    }
]

# Pydantic model for business listing response
class BusinessListing(BaseModel):
    id: int
    name: str
    description: str
    location: str
    price: float
    category: str
    annual_revenue: Optional[float] = None
    established_year: Optional[int] = None

# Pydantic model for query parameters
class ListingQueryParams(BaseModel):
    location: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    category: Optional[str] = None

@app.get("/listings", response_model=List[BusinessListing])
def get_business_listings(
    location: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    category: Optional[str] = None
):
    """
    Retrieve business listings with optional filters.
    
    Parameters:
    - location: Filter by location (e.g., "São Paulo")
    - min_price: Minimum price filter
    - max_price: Maximum price filter
    - category: Business category filter
    
    Returns:
    - List of business listings matching the criteria
    """
    filtered_listings = business_listings_db
    
    if location:
        filtered_listings = [listing for listing in filtered_listings 
                            if location.lower() in listing["location"].lower()]
    
    if min_price is not None:
        filtered_listings = [listing for listing in filtered_listings 
                            if listing["price"] >= min_price]
    
    if max_price is not None:
        filtered_listings = [listing for listing in filtered_listings 
                            if listing["price"] <= max_price]
    
    if category:
        filtered_listings = [listing for listing in filtered_listings 
                            if category.lower() == listing["category"].lower()]
    
    return filtered_listings

@app.get("/listings/{listing_id}", response_model=BusinessListing)
def get_listing_by_id(listing_id: int):
    """
    Retrieve a specific business listing by ID.
    
    Parameters:
    - listing_id: ID of the business listing
    
    Returns:
    - The business listing with matching ID
    
    Raises:
    - HTTPException 404 if listing not found
    """
    listing = next((item for item in business_listings_db if item["id"] == listing_id), None)
    if listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
