"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Design a RESTful API for retrieving information about trekking routes in Tibet, including details about the Mount Kailash Tour.
Generated: DETERMINISTIC_d86b03875a7adf47
Batch ID: 20250622_210914
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
    title="Tibet Trekking Routes API",
    description="API for retrieving information about trekking routes in Tibet",
    version="1.0.0"
)

# Define a model for TrekkingRoute
class TrekkingRoute(BaseModel):
    id: int
    name: str
    description: str
    difficulty_level: str
    distance: float
    duration: str

# Define a model for MountKailashTour
class MountKailashTour(BaseModel):
    id: int
    route_id: int
    tour_name: str
    tour_description: str
    itinerary: List[str]

# In-memory data store for trekking routes and Mount Kailash tours
trekking_routes = [
    TrekkingRoute(
        id=1,
        name="Mount Kailash Circuit",
        description="A challenging trek around Mount Kailash",
        difficulty_level="High",
        distance=52.0,
        duration="5-7 days"
    ),
    TrekkingRoute(
        id=2,
        name="Lake Manasarovar Trek",
        description="A scenic trek to Lake Manasarovar",
        difficulty_level="Medium",
        distance=30.0,
        duration="3-5 days"
    )
]

mount_kailash_tours = [
    MountKailashTour(
        id=1,
        route_id=1,
        tour_name="Standard Mount Kailash Tour",
        tour_description="A standard tour to Mount Kailash",
        itinerary=["Day 1: Arrival in Nepalgunj", "Day 2-3: Drive to Lake Manasarovar", "Day 4-5: Trek to Mount Kailash"]
    ),
    MountKailashTour(
        id=2,
        route_id=1,
        tour_name="Premium Mount Kailash Tour",
        tour_description="A premium tour to Mount Kailash with additional activities",
        itinerary=["Day 1: Arrival in Nepalgunj", "Day 2-3: Drive to Lake Manasarovar", "Day 4-5: Trek to Mount Kailash", "Day 6: Additional activities"]
    )
]

# GET /
@app.get("/")
def read_root():
    return {"message": "Welcome to the Tibet Trekking Routes API"}

# GET /trekking-routes
@app.get("/trekking-routes/", response_model=List[TrekkingRoute])
def read_trekking_routes():
    return trekking_routes

# GET /trekking-routes/{route_id}
@app.get("/trekking-routes/{route_id}", response_model=TrekkingRoute)
def read_trekking_route(route_id: int):
    for route in trekking_routes:
        if route.id == route_id:
            return route
    raise HTTPException(status_code=404, detail="Trekking route not found")

# GET /mount-kailash-tours
@app.get("/mount-kailash-tours/", response_model=List[MountKailashTour])
def read_mount_kailash_tours():
    return mount_kailash_tours

# GET /mount-kailash-tours/{tour_id}
@app.get("/mount-kailash-tours/{tour_id}", response_model=MountKailashTour)
def read_mount_kailash_tour(tour_id: int):
    for tour in mount_kailash_tours:
        if tour.id == tour_id:
            return tour
    raise HTTPException(status_code=404, detail="Mount Kailash tour not found")

# GET /trekking-routes/{route_id}/mount-kailash-tours
@app.get("/trekking-routes/{route_id}/mount-kailash-tours/", response_model=List[MountKailashTour])
def read_mount_kailash_tours_by_route(route_id: int):
    return [tour for tour in mount_kailash_tours if tour.route_id == route_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
