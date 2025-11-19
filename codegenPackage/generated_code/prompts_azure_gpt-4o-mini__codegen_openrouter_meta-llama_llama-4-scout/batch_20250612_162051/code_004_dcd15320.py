"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Outline a RESTful API endpoint that allows users to retrieve featured properties for sale, similar to the listings showcased on the Nueva Ciudad platform.
Generated: DETERMINISTIC_dcd153202bfbedfd
Batch ID: 20250612_162051
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
    title="Nueva Ciudad Featured Properties API",
    description="API endpoint to retrieve featured properties for sale",
    version="1.0.0"
)

class Property(BaseModel):
    """Model representing a property"""
    id: int
    title: str
    description: str
    price: float
    location: str
    features: List[str]

class FeaturedPropertiesResponse(BaseModel):
    """Model representing the response for featured properties"""
    properties: List[Property]

# In-memory data store for demonstration purposes
featured_properties = [
    Property(
        id=1,
        title="Luxury Mansion",
        description="Beautiful mansion with 5 bedrooms and a pool",
        price=1000000.0,
        location="Nueva Ciudad",
        features=["pool", "5 bedrooms", "garden"]
    ),
    Property(
        id=2,
        title="Cozy Apartment",
        description="Cozy apartment with 2 bedrooms and a balcony",
        price=200000.0,
        location="Nueva Ciudad",
        features=["balcony", "2 bedrooms", "gym"]
    )
]

@app.get("/featured-properties", response_model=FeaturedPropertiesResponse)
async def get_featured_properties():
    """
    Retrieve a list of featured properties for sale.

    Returns:
        A list of featured properties
    """
    try:
        return FeaturedPropertiesResponse(properties=featured_properties)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return {"error": exc.detail}

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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
