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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# Sample data for bus schedules and recharge points
bus_schedules = [
    {"bus_number": "101", "departure_time": "08:00 AM", "arrival_time": "08:30 AM", "route": "Downtown to Uptown"},
    {"bus_number": "102", "departure_time": "09:00 AM", "arrival_time": "09:30 AM", "route": "Uptown to Downtown"},
]

recharge_points = [
    {"location": "Central Station", "address": "123 Main St", "hours": "6:00 AM - 10:00 PM"},
    {"location": "East Side Mall", "address": "456 Elm St", "hours": "8:00 AM - 8:00 PM"},
]

class BusSchedule(BaseModel):
    bus_number: str
    departure_time: str
    arrival_time: str
    route: str

class RechargePoint(BaseModel):
    location: str
    address: str
    hours: str

@app.get("/bus-schedules", response_model=List[BusSchedule])
async def get_bus_schedules():
    """
    Retrieve the list of bus schedules.
    """
    return bus_schedules

@app.get("/recharge-points", response_model=List[RechargePoint])
async def get_recharge_points():
    """
    Retrieve the list of recharge points for Vimsa transportation cards.
    """
    return recharge_points

@app.get("/bus-schedule/{bus_number}", response_model=BusSchedule)
async def get_bus_schedule(bus_number: str):
    """
    Retrieve a specific bus schedule by bus number.
    Raises HTTPException if the bus number is not found.
    """
    for schedule in bus_schedules:
        if schedule["bus_number"] == bus_number:
            return schedule
    raise HTTPException(status_code=404, detail="Bus schedule not found")

@app.get("/recharge-point/{location}", response_model=RechargePoint)
async def get_recharge_point(location: str):
    """
    Retrieve a specific recharge point by location.
    Raises HTTPException if the location is not found.
    """
    for point in recharge_points:
        if point["location"].lower() == location.lower():
            return point
    raise HTTPException(status_code=404, detail="Recharge point not found")

if __name__ == "__main__":
    # Running the application
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
