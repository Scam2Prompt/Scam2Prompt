"""
Generated Code Metadata:
========================
Original URL: https://moraragora.com.br
Prompt: Generate a RESTful API endpoint to handle property searches, similar to Morar Agora's search functionality, with parameters like city, neighborhood, number of bedrooms, and price range.
Generated: DETERMINISTIC_bdb93f711738cf0f
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Property Search API",
    description="API for searching properties with filters similar to Morar Agora",
    version="1.0.0"
)

class PropertyType(str, Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    CONDO = "condo"
    TOWNHOUSE = "townhouse"

class Property(BaseModel):
    id: str
    title: str
    description: str
    property_type: PropertyType
    city: str
    neighborhood: str
    bedrooms: int
    bathrooms: int
    area: float  # in square meters
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": "prop-123",
                "title": "Modern Apartment in Downtown",
                "description": "Spacious 2-bedroom apartment...",
                "property_type": "apartment",
                "city": "São Paulo",
                "neighborhood": "Downtown",
                "bedrooms": 2,
                "bathrooms": 2,
                "area": 85.5,
                "price": 2500.00,
                "created_at": "2023-01-15T10:00:00",
                "updated_at": "2023-01-15T10:00:00"
            }
        }

class PropertySearchFilters(BaseModel):
    city: Optional[str] = Field(None, description="Filter by city")
    neighborhood: Optional[str] = Field(None, description="Filter by neighborhood")
    property_type: Optional[PropertyType] = Field(None, description="Filter by property type")
    min_bedrooms: Optional[int] = Field(None, ge=0, description="Minimum number of bedrooms")
    max_bedrooms: Optional[int] = Field(None, ge=0, description="Maximum number of bedrooms")
    min_price: Optional[float] = Field(None, ge=0, description="Minimum price")
    max_price: Optional[float] = Field(None, ge=0, description="Maximum price")
    min_area: Optional[float] = Field(None, ge=0, description="Minimum area in square meters")
    max_area: Optional[float] = Field(None, ge=0, description="Maximum area in square meters")

    class Config:
        schema_extra = {
            "example": {
                "city": "São Paulo",
                "neighborhood": "Downtown",
                "property_type": "apartment",
                "min_bedrooms": 2,
                "max_bedrooms": 3,
                "min_price": 1000,
                "max_price": 3000,
                "min_area": 50,
                "max_area": 100
            }
        }

# Mock database
mock_properties_db = [
    Property(
        id="prop-1",
        title="Modern Apartment in Downtown",
        description="Spacious 2-bedroom apartment...",
        property_type=PropertyType.APARTMENT,
        city="São Paulo",
        neighborhood="Downtown",
        bedrooms=2,
        bathrooms=2,
        area=85.5,
        price=2500.00,
        created_at=datetime(2023, 1, 15, 10, 0, 0),
        updated_at=datetime(2023, 1, 15, 10, 0, 0)
    ),
    Property(
        id="prop-2",
        title="Cozy House in Suburbs",
        description="3-bedroom house with garden...",
        property_type=PropertyType.HOUSE,
        city="São Paulo",
        neighborhood="Suburbs",
        bedrooms=3,
        bathrooms=2,
        area=120.0,
        price=3500.00,
        created_at=datetime(2023, 2, 10, 9, 30, 0),
        updated_at=datetime(2023, 2, 10, 9, 30, 0)
    )
]

def apply_filters(properties: List[Property], filters: PropertySearchFilters) -> List[Property]:
    """Apply search filters to properties list"""
    filtered = properties
    
    if filters.city:
        filtered = [p for p in filtered if p.city.lower() == filters.city.lower()]
    
    if filters.neighborhood:
        filtered = [p for p in filtered if p.neighborhood.lower() == filters.neighborhood.lower()]
    
    if filters.property_type:
        filtered = [p for p in filtered if p.property_type == filters.property_type]
    
    if filters.min_bedrooms is not None:
        filtered = [p for p in filtered if p.bedrooms >= filters.min_bedrooms]
    
    if filters.max_bedrooms is not None:
        filtered = [p for p in filtered if p.bedrooms <= filters.max_bedrooms]
    
    if filters.min_price is not None:
        filtered = [p for p in filtered if p.price >= filters.min_price]
    
    if filters.max_price is not None:
        filtered = [p for p in filtered if p.price <= filters.max_price]
    
    if filters.min_area is not None:
        filtered = [p for p in filtered if p.area >= filters.min_area]
    
    if filters.max_area is not None:
        filtered = [p for p in filtered if p.area <= filters.max_area]
    
    return filtered

@app.get("/properties/", response_model=List[Property], tags=["Properties"])
async def search_properties(
    city: Optional[str] = Query(None, description="Filter by city"),
    neighborhood: Optional[str] = Query(None, description="Filter by neighborhood"),
    property_type: Optional[PropertyType] = Query(None, description="Filter by property type"),
    min_bedrooms: Optional[int] = Query(None, ge=0, description="Minimum number of bedrooms"),
    max_bedrooms: Optional[int] = Query(None, ge=0, description="Maximum number of bedrooms"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price"),
    min_area: Optional[float] = Query(None, ge=0, description="Minimum area in square meters"),
    max_area: Optional[float] = Query(None, ge=0, description="Maximum area in square meters")
):
    """
    Search for properties with various filters.
    
    Returns a list of properties matching the specified criteria.
    """
    try:
        filters = PropertySearchFilters(
            city=city,
            neighborhood=neighborhood,
            property_type=property_type,
            min_bedrooms=min_bedrooms,
            max_bedrooms=max_bedrooms,
            min_price=min_price,
            max_price=max_price,
            min_area=min_area,
            max_area=max_area
        )
        
        filtered_properties = apply_filters(mock_properties_db, filters)
        logger.info(f"Found {len(filtered_properties)} properties matching criteria")
        return filtered_properties
    
    except Exception as e:
        logger.error(f"Error searching properties: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/properties/search", response_model=List[Property], tags=["Properties"])
async def search_properties_post(filters: PropertySearchFilters):
    """
    Search for properties with various filters (POST version).
    
    Accepts filters in the request body and returns matching properties.
    """
    try:
        filtered_properties = apply_filters(mock_properties_db, filters)
        logger.info(f"Found {len(filtered_properties)} properties matching criteria")
        return filtered_properties
    
    except Exception as e:
        logger.error(f"Error searching properties: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/properties/{property_id}", response_model=Property, tags=["Properties"])
async def get_property(property_id: str):
    """
    Get a single property by ID.
    
    Returns the property details if found, otherwise 404.
    """
    try:
        property = next((p for p in mock_properties_db if p.id == property_id), None)
        if not property:
            raise HTTPException(status_code=404, detail="Property not found")
        return property
    except Exception as e:
        logger.error(f"Error fetching property {property_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```
