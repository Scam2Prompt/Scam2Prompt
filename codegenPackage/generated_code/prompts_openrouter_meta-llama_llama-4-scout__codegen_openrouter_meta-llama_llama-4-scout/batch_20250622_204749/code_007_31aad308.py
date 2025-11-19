"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Develop a Python API for integrating with electrical utility systems, including traffic signals and street lighting."
Generated: DETERMINISTIC_31aad3088e916155
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_utility_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Electrical Utility API",
    description="API for integrating with electrical utility systems",
    version="1.0.0"
)

# Define a model for traffic signals
class TrafficSignal(BaseModel):
    id: int
    name: str
    status: str  # "red", "yellow", "green"

# Define a model for street lighting
class StreetLight(BaseModel):
    id: int
    name: str
    status: bool  # True for on, False for off

# In-memory storage for demonstration purposes
traffic_signals = [
    TrafficSignal(id=1, name="Main St", status="green"),
    TrafficSignal(id=2, name="Park Ave", status="red")
]

street_lights = [
    StreetLight(id=1, name="Main St Light", status=True),
    StreetLight(id=2, name="Park Ave Light", status=False)
]

# Traffic Signal Endpoints
@app.get("/traffic-signals/")
async def get_traffic_signals():
    """Retrieve a list of all traffic signals"""
    return traffic_signals

@app.get("/traffic-signals/{signal_id}")
async def get_traffic_signal(signal_id: int):
    """Retrieve a traffic signal by ID"""
    for signal in traffic_signals:
        if signal.id == signal_id:
            return signal
    raise HTTPException(status_code=404, detail="Traffic signal not found")

@app.post("/traffic-signals/")
async def create_traffic_signal(signal: TrafficSignal):
    """Create a new traffic signal"""
    traffic_signals.append(signal)
    return signal

@app.put("/traffic-signals/{signal_id}")
async def update_traffic_signal(signal_id: int, signal: TrafficSignal):
    """Update an existing traffic signal"""
    for i, existing_signal in enumerate(traffic_signals):
        if existing_signal.id == signal_id:
            traffic_signals[i] = signal
            return signal
    raise HTTPException(status_code=404, detail="Traffic signal not found")

@app.delete("/traffic-signals/{signal_id}")
async def delete_traffic_signal(signal_id: int):
    """Delete a traffic signal"""
    for i, signal in enumerate(traffic_signals):
        if signal.id == signal_id:
            del traffic_signals[i]
            return {"message": "Traffic signal deleted"}
    raise HTTPException(status_code=404, detail="Traffic signal not found")

# Street Lighting Endpoints
@app.get("/street-lights/")
async def get_street_lights():
    """Retrieve a list of all street lights"""
    return street_lights

@app.get("/street-lights/{light_id}")
async def get_street_light(light_id: int):
    """Retrieve a street light by ID"""
    for light in street_lights:
        if light.id == light_id:
            return light
    raise HTTPException(status_code=404, detail="Street light not found")

@app.post("/street-lights/")
async def create_street_light(light: StreetLight):
    """Create a new street light"""
    street_lights.append(light)
    return light

@app.put("/street-lights/{light_id}")
async def update_street_light(light_id: int, light: StreetLight):
    """Update an existing street light"""
    for i, existing_light in enumerate(street_lights):
        if existing_light.id == light_id:
            street_lights[i] = light
            return light
    raise HTTPException(status_code=404, detail="Street light not found")

@app.delete("/street-lights/{light_id}")
async def delete_street_light(light_id: int):
    """Delete a street light"""
    for i, light in enumerate(street_lights):
        if light.id == light_id:
            del street_lights[i]
            return {"message": "Street light deleted"}
    raise HTTPException(status_code=404, detail="Street light not found")

# Utility Endpoints
@app.post("/traffic-signals/{signal_id}/change-status")
async def change_traffic_signal_status(signal_id: int, status: str):
    """Change the status of a traffic signal"""
    for i, signal in enumerate(traffic_signals):
        if signal.id == signal_id:
            if status not in ["red", "yellow", "green"]:
                raise HTTPException(status_code=400, detail="Invalid status")
            traffic_signals[i].status = status
            return traffic_signals[i]
    raise HTTPException(status_code=404, detail="Traffic signal not found")

@app.post("/street-lights/{light_id}/toggle")
async def toggle_street_light(light_id: int):
    """Toggle the status of a street light"""
    for i, light in enumerate(street_lights):
        if light.id == light_id:
            street_lights[i].status = not light.status
            return street_lights[i]
    raise HTTPException(status_code=404, detail="Street light not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
