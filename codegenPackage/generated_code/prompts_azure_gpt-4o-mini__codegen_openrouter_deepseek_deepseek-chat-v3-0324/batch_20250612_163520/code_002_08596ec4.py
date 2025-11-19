"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Create an API endpoint that provides information about live entertainment events at White Pines Lodge, including details about the Pines Dinner Theater and its annual Christmas show.
Generated: DETERMINISTIC_08596ec404ab6ee3
Batch ID: 20250612_163520
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
from datetime import date
import uvicorn

app = FastAPI(
    title="White Pines Lodge Entertainment API",
    description="API for accessing live entertainment events at White Pines Lodge",
    version="1.0.0"
)

class Event(BaseModel):
    id: int
    name: str
    description: str
    event_type: str
    date: date
    time: str
    venue: str
    price: float
    is_sold_out: bool = False
    performers: Optional[List[str]] = None

# Mock database of events
EVENTS_DB = [
    Event(
        id=1,
        name="Pines Dinner Theater: Broadway Nights",
        description="An evening of Broadway's greatest hits performed live with gourmet dining",
        event_type="Dinner Theater",
        date=date(2023, 11, 15),
        time="19:00",
        venue="Pines Dinner Theater",
        price=75.00,
        performers=["Broadway Stars Ensemble"]
    ),
    Event(
        id=2,
        name="Annual Christmas Spectacular",
        description="White Pines Lodge's famous holiday show with dinner and festive performances",
        event_type="Christmas Show",
        date=date(2023, 12, 20),
        time="18:30",
        venue="Pines Dinner Theater",
        price=85.00,
        is_sold_out=True,
        performers=["The Pines Singers", "Holiday Dancers", "Special Guest Santa"]
    ),
    Event(
        id=3,
        name="Jazz Under the Pines",
        description="An intimate evening of jazz music in our cozy lodge setting",
        event_type="Music Performance",
        date=date(2023, 11, 22),
        time="20:00",
        venue="Main Lodge",
        price=35.00
    )
]

@app.get("/events", response_model=List[Event], tags=["Events"])
async def get_all_events():
    """Get all upcoming events at White Pines Lodge"""
    return EVENTS_DB

@app.get("/events/{event_id}", response_model=Event, tags=["Events"])
async def get_event(event_id: int):
    """Get a specific event by ID"""
    event = next((e for e in EVENTS_DB if e.id == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.get("/events/type/{event_type}", response_model=List[Event], tags=["Events"])
async def get_events_by_type(event_type: str):
    """Get events filtered by type (e.g., 'Dinner Theater', 'Christmas Show')"""
    filtered_events = [e for e in EVENTS_DB if e.event_type.lower() == event_type.lower()]
    if not filtered_events:
        raise HTTPException(
            status_code=404,
            detail=f"No events found for type '{event_type}'"
        )
    return filtered_events

@app.get("/dinner-theater", response_model=List[Event], tags=["Dinner Theater"])
async def get_dinner_theater_events():
    """Get all Pines Dinner Theater events"""
    return get_events_by_type("Dinner Theater")

@app.get("/christmas-show", response_model=Event, tags=["Christmas Show"])
async def get_christmas_show():
    """Get information about the annual Christmas show"""
    christmas_show = next(
        (e for e in EVENTS_DB if e.event_type == "Christmas Show"),
        None
    )
    if not christmas_show:
        raise HTTPException(
            status_code=404,
            detail="Christmas show information not available"
        )
    return christmas_show

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
