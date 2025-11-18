"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vimsa.com.br
Prompt: Develop a RESTful API in Python (using Flask or FastAPI) that allows users to query bus schedules and recharge points for Vimsa transportation cards.
Generated: DETERMINISTIC_50019e7f22edda72
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Restful API for querying bus schedules and recharge points for Vimsa transportation cards
# Framework: FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample data (in a real-world application, this would come from a database)
bus_schedules = [
    {"route_id": 1, "route_name": "Route 1", "departure_time": "08:00 AM", "arrival_time": "09:00 AM"},
    {"route_id": 2, "route_name": "Route 2", "departure_time": "09:30 AM", "arrival_time": "10:30 AM"},
]

recharge_points = [
    {"point_id": 1, "name": "Central Station", "location": "Downtown"},
    {"point_id": 2, "name": "Mall Kiosk", "location": "Main Mall"},
]

# Models for request and response validation
class BusSchedule(BaseModel):
    route_id: int
    route_name: str
    departure_time: str
    arrival_time: str


class RechargePoint(BaseModel):
    point_id: int
    name: str
    location: str


@app.get("/bus-schedules", response_model=List[BusSchedule])
def get_bus_schedules():
    """
    Endpoint to fetch all bus schedules.
    """
    return bus_schedules


@app.get("/bus-schedules/{route_id}", response_model=BusSchedule)
def get_bus_schedule_by_id(route_id: int):
    """
    Endpoint to fetch a specific bus schedule by route ID.
    """
    for schedule in bus_schedules:
        if schedule["route_id"] == route_id:
            return schedule
    raise HTTPException(status_code=404, detail="Bus schedule not found")


@app.get("/recharge-points", response_model=List[RechargePoint])
def get_recharge_points():
    """
    Endpoint to fetch all recharge points.
    """
    return recharge_points


@app.get("/recharge-points/{point_id}", response_model=RechargePoint)
def get_recharge_point_by_id(point_id: int):
    """
    Endpoint to fetch a specific recharge point by point ID.
    """
    for point in recharge_points:
        if point["point_id"] == point_id:
            return point
    raise HTTPException(status_code=404, detail="Recharge point not found")


# Error handling for generic 404 errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """
    Custom error handler for HTTP exceptions.
    """
    return {
        "error": True,
        "message": exc.detail
    }

# Run the application with `uvicorn` in production:
# Example: uvicorn main:app --host 0.0.0.0 --port 8000
```
