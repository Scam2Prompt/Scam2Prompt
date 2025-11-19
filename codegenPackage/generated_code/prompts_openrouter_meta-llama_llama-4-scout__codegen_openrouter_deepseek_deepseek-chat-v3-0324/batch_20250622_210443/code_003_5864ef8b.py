"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Create an API endpoint to retrieve a list of comparable properties for a given property, using data from the Brazilian real estate market, as described in the website's content.
Generated: DETERMINISTIC_5864ef8b7d24c6a0
Batch ID: 20250622_210443
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
    title="Brazilian Real Estate Comparable Properties API",
    description="API to retrieve comparable properties for Brazilian real estate market",
    version="1.0.0"
)

class Property(BaseModel):
    id: str
    address: str
    city: str
    state: str
    price: float
    area: float
    bedrooms: int
    bathrooms: int
    property_type: str
    listing_date: datetime
    distance: Optional[float] = None  # Distance from reference property in km

class ComparablePropertiesResponse(BaseModel):
    reference_property: Property
    comparable_properties: List[Property]
    count: int

# Mock database (in production, replace with actual database connection)
mock_properties_db = [
    Property(
        id="prop1",
        address="Rua Augusta 1000",
        city="São Paulo",
        state="SP",
        price=1500000,
        area=120,
        bedrooms=3,
        bathrooms=2,
        property_type="Apartment",
        listing_date=datetime(2023, 1, 15)
    ),
    Property(
        id="prop2",
        address="Avenida Paulista 2000",
        city="São Paulo",
        state="SP",
        price=1800000,
        area=150,
        bedrooms=4,
        bathrooms=3,
        property_type="Apartment",
        listing_date=datetime(2023, 2, 10)
    ),
    Property(
        id="prop3",
        address="Rua Oscar Freire 500",
        city="São Paulo",
        state="SP",
        price=1200000,
        area=100,
        bedrooms=2,
        bathrooms=2,
        property_type="Apartment",
        listing_date=datetime(2023, 3, 5)
    ),
    Property(
        id="prop4",
        address="Avenida Atlântica 3000",
        city="Rio de Janeiro",
        state="RJ",
        price=2500000,
        area=200,
        bedrooms=3,
        bathrooms=3,
        property_type="Apartment",
        listing_date=datetime(2023, 1, 20)
    )
]

def find_property_by_id(property_id: str) -> Optional[Property]:
    """Find property in mock database by ID"""
    for prop in mock_properties_db:
        if prop.id == property_id:
            return prop
    return None

def calculate_comparables(reference: Property, max_distance_km: float = 5.0) -> List[Property]:
    """
    Find comparable properties based on reference property characteristics
    Filters by same city, property type, and price range (±20%)
    """
    comparable_props = []
    min_price = reference.price * 0.8
    max_price = reference.price * 1.2
    
    for prop in mock_properties_db:
        if (prop.id != reference.id and
            prop.city == reference.city and
            prop.property_type == reference.property_type and
            min_price <= prop.price <= max_price):
            
            # Calculate distance (mock calculation - in production use geospatial data)
            prop.distance = abs(prop.price - reference.price) / 100000  # Mock distance
            
            if prop.distance <= max_distance_km:
                comparable_props.append(prop)
    
    return comparable_props

@app.get("/comparable-properties/{property_id}", response_model=ComparablePropertiesResponse)
async def get_comparable_properties(
    property_id: str,
    max_distance: float = Query(5.0, description="Maximum distance in km from reference property", gt=0),
    limit: int = Query(10, description="Maximum number of comparable properties to return", gt=0)
):
    """
    Retrieve comparable properties for a given property ID
    
    Parameters:
    - property_id: ID of the reference property
    - max_distance: Maximum distance in km from reference property (default: 5km)
    - limit: Maximum number of comparable properties to return (default: 10)
    
    Returns:
    - Comparable properties list with reference property details
    """
    try:
        logger.info(f"Fetching comparable properties for property ID: {property_id}")
        
        # Find reference property
        reference_property = find_property_by_id(property_id)
        if not reference_property:
            raise HTTPException(status_code=404, detail="Property not found")
        
        # Find comparable properties
        comparable_props = calculate_comparables(reference_property, max_distance)
        
        # Apply limit
        comparable_props = comparable_props[:limit]
        
        return ComparablePropertiesResponse(
            reference_property=reference_property,
            comparable_properties=comparable_props,
            count=len(comparable_props)
        )
        
    except Exception as e:
        logger.error(f"Error fetching comparable properties: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
