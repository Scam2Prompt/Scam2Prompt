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
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Business Listings API",
    description="API for retrieving business listings for sale",
    version="1.0.0"
)

class BusinessListing(BaseModel):
    """Model for business listings"""
    id: int
    name: str
    location: str
    price: float
    description: str

# In-memory data store for demonstration purposes
# Replace with a database connection in production
business_listings: List[BusinessListing] = [
    BusinessListing(
        id=1,
        name="Lighting Store",
        location="São Paulo",
        price=100000.0,
        description="A lighting store in São Paulo"
    ),
    BusinessListing(
        id=2,
        name="Furniture Shop",
        location="Rio de Janeiro",
        price=50000.0,
        description="A furniture shop in Rio de Janeiro"
    )
]

@app.get("/listings/", response_model=List[BusinessListing])
async def get_listings(location: str = None, min_price: float = None, max_price: float = None):
    """
    Retrieve a list of business listings for sale.

    Args:
    - location (str): Filter by location
    - min_price (float): Filter by minimum price
    - max_price (float): Filter by maximum price

    Returns:
    - A list of business listings
    """
    try:
        filtered_listings = business_listings.copy()

        if location:
            filtered_listings = [listing for listing in filtered_listings if listing.location == location]

        if min_price:
            filtered_listings = [listing for listing in filtered_listings if listing.price >= min_price]

        if max_price:
            filtered_listings = [listing for listing in filtered_listings if listing.price <= max_price]

        return filtered_listings

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/listings/{listing_id}", response_model=BusinessListing)
async def get_listing(listing_id: int):
    """
    Retrieve a business listing by ID.

    Args:
    - listing_id (int): The ID of the listing

    Returns:
    - A business listing
    """
    try:
        listing = next((listing for listing in business_listings if listing.id == listing_id), None)

        if listing is None:
            raise HTTPException(status_code=404, detail="Listing not found")

        return listing

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
# or 
# python app.py 
```
