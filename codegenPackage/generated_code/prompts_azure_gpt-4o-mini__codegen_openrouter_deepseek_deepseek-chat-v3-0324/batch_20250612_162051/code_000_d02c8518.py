"""
Generated Code Metadata:
========================
Original URL: https://inkasluxury.com
Prompt: Generate a code snippet for a travel booking API that allows users to customize their itineraries for tours in Peru, similar to the personalized experiences offered by Inkas Luxury.
Generated: DETERMINISTIC_d02c8518d6584ab9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
from enum import Enum

app = FastAPI(
    title="Peru Travel Booking API",
    description="API for customizing travel itineraries for tours in Peru",
    version="1.0.0"
)

class ActivityType(str, Enum):
    CULTURAL = "cultural"
    ADVENTURE = "adventure"
    NATURE = "nature"
    LUXURY = "luxury"
    CULINARY = "culinary"

class AccommodationType(str, Enum):
    HOTEL = "hotel"
    LODGE = "lodge"
    BOUTIQUE = "boutique"
    LUXURY_HOTEL = "luxury_hotel"
    HOMESTAY = "homestay"

class TransportationType(str, Enum):
    PRIVATE_VAN = "private_van"
    BUS = "bus"
    TRAIN = "train"
    FLIGHT = "flight"
    BOAT = "boat"

class Activity(BaseModel):
    name: str = Field(..., example="Machu Picchu Guided Tour")
    type: ActivityType
    duration_hours: float = Field(..., gt=0, example=4.5)
    description: Optional[str] = None

class Accommodation(BaseModel):
    name: str = Field(..., example="Belmond Sanctuary Lodge")
    type: AccommodationType
    nights: int = Field(..., gt=0, example=2)
    description: Optional[str] = None

class Transportation(BaseModel):
    type: TransportationType
    description: str = Field(..., example="Private van from Cusco to Ollantaytambo")

class ItineraryRequest(BaseModel):
    start_date: date
    end_date: date
    travelers: int = Field(..., gt=0, example=2)
    preferred_activities: List[ActivityType]
    preferred_accommodations: List[AccommodationType]
    special_requests: Optional[str] = None

class ItineraryResponse(BaseModel):
    itinerary_id: str
    start_date: date
    end_date: date
    activities: List[Activity]
    accommodations: List[Accommodation]
    transportations: List[Transportation]
    total_cost: float
    confirmation_message: str

# Mock database for demonstration
mock_activities = {
    ActivityType.CULTURAL: [
        Activity(
            name="Machu Picchu Guided Tour",
            type=ActivityType.CULTURAL,
            duration_hours=4.5,
            description="Private guided tour of Machu Picchu with expert local guide"
        )
    ],
    ActivityType.ADVENTURE: [
        Activity(
            name="Inca Trail Hike",
            type=ActivityType.ADVENTURE,
            duration_hours=8,
            description="4-day trek through the Andes to Machu Picchu"
        )
    ]
}

mock_accommodations = {
    AccommodationType.LUXURY_HOTEL: [
        Accommodation(
            name="Belmond Sanctuary Lodge",
            type=AccommodationType.LUXURY_HOTEL,
            nights=2,
            description="Luxury hotel located at the gates of Machu Picchu"
        )
    ]
}

mock_transportations = {
    "default": [
        Transportation(
            type=TransportationType.PRIVATE_VAN,
            description="Private van from Cusco to Ollantaytambo"
        )
    ]
}

@app.post("/itineraries/", response_model=ItineraryResponse, status_code=status.HTTP_201_CREATED)
async def create_itinerary(request: ItineraryRequest):
    """
    Create a customized travel itinerary based on user preferences.
    """
    try:
        # Validate date range
        if request.start_date >= request.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="End date must be after start date"
            )

        # Calculate trip duration
        trip_duration = (request.end_date - request.start_date).days

        # Select activities based on preferences
        selected_activities = []
        for activity_type in request.preferred_activities:
            if activity_type in mock_activities:
                selected_activities.extend(mock_activities[activity_type])

        if not selected_activities:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No activities available for selected preferences"
            )

        # Select accommodations based on preferences
        selected_accommodations = []
        for accommodation_type in request.preferred_accommodations:
            if accommodation_type in mock_accommodations:
                selected_accommodations.extend(mock_accommodations[accommodation_type])

        if not selected_accommodations:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No accommodations available for selected preferences"
            )

        # Mock response generation
        itinerary_id = f"ITIN-{request.start_date.strftime('%Y%m%d')}-{request.travelers}"
        total_cost = 1500 * request.travelers * trip_duration  # Simplified cost calculation

        return ItineraryResponse(
            itinerary_id=itinerary_id,
            start_date=request.start_date,
            end_date=request.end_date,
            activities=selected_activities,
            accommodations=selected_accommodations,
            transportations=mock_transportations["default"],
            total_cost=total_cost,
            confirmation_message="Your custom Peru itinerary has been created successfully!"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/itineraries/{itinerary_id}", response_model=ItineraryResponse)
async def get_itinerary(itinerary_id: str):
    """
    Retrieve a previously created itinerary by ID.
    """
    # In a real implementation, this would fetch from a database
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Endpoint not implemented in this demo"
    )
```
