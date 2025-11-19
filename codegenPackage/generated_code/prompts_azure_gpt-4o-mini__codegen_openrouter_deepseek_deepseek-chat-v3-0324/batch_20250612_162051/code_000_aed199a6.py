"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Generate a code snippet for a travel booking API that allows users to create custom itineraries for group trips, similar to the unique itineraries offered by Rehiletes.
Generated: DETERMINISTIC_aed199a6ef403a4a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status
from uuid import uuid4

app = FastAPI(title="Travel Booking API", description="API for creating custom group trip itineraries")

# Database mock (in production, replace with actual database)
itineraries_db = {}

class Destination(BaseModel):
    """Represents a travel destination in the itinerary"""
    name: str
    arrival: datetime
    departure: datetime
    activities: List[str]
    
    @validator('departure')
    def validate_departure(cls, v, values):
        if 'arrival' in values and v <= values['arrival']:
            raise ValueError('Departure must be after arrival')
        return v

class Itinerary(BaseModel):
    """Represents a complete travel itinerary"""
    id: str
    name: str
    description: str
    destinations: List[Destination]
    group_size: int
    created_at: datetime
    updated_at: datetime

@app.post("/itineraries/", response_model=Itinerary, status_code=status.HTTP_201_CREATED)
async def create_itinerary(name: str, description: str, destinations: List[Dict], group_size: int):
    """
    Create a new custom itinerary for a group trip.
    
    Args:
        name: Name of the itinerary
        description: Description of the trip
        destinations: List of destinations with their details
        group_size: Number of people in the group
    
    Returns:
        The created itinerary with generated ID and timestamps
    """
    try:
        # Validate and parse destinations
        parsed_destinations = [Destination(**dest) for dest in destinations]
        
        # Generate itinerary
        itinerary_id = str(uuid4())
        now = datetime.now()
        itinerary = Itinerary(
            id=itinerary_id,
            name=name,
            description=description,
            destinations=parsed_destinations,
            group_size=group_size,
            created_at=now,
            updated_at=now
        )
        
        # Store itinerary
        itineraries_db[itinerary_id] = itinerary.dict()
        
        return itinerary
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create itinerary"
        )

@app.get("/itineraries/{itinerary_id}", response_model=Itinerary)
async def get_itinerary(itinerary_id: str):
    """
    Retrieve an itinerary by its ID.
    
    Args:
        itinerary_id: UUID of the itinerary to retrieve
    
    Returns:
        The requested itinerary if found
    """
    if itinerary_id not in itineraries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Itinerary not found"
        )
    return itineraries_db[itinerary_id]

@app.put("/itineraries/{itinerary_id}", response_model=Itinerary)
async def update_itinerary(itinerary_id: str, name: Optional[str] = None, description: Optional[str] = None, 
                          destinations: Optional[List[Dict]] = None, group_size: Optional[int] = None):
    """
    Update an existing itinerary.
    
    Args:
        itinerary_id: UUID of the itinerary to update
        name: New name (optional)
        description: New description (optional)
        destinations: New destinations (optional)
        group_size: New group size (optional)
    
    Returns:
        The updated itinerary
    """
    if itinerary_id not in itineraries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Itinerary not found"
        )
    
    try:
        itinerary = Itinerary(**itineraries_db[itinerary_id])
        
        if name is not None:
            itinerary.name = name
        if description is not None:
            itinerary.description = description
        if destinations is not None:
            itinerary.destinations = [Destination(**dest) for dest in destinations]
        if group_size is not None:
            itinerary.group_size = group_size
            
        itinerary.updated_at = datetime.now()
        itineraries_db[itinerary_id] = itinerary.dict()
        
        return itinerary
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update itinerary"
        )

@app.delete("/itineraries/{itinerary_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_itinerary(itinerary_id: str):
    """
    Delete an itinerary by its ID.
    
    Args:
        itinerary_id: UUID of the itinerary to delete
    """
    if itinerary_id not in itineraries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Itinerary not found"
        )
    del itineraries_db[itinerary_id]
```
