"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Create a logistics dashboard to track shipments across multiple modes of transport (air, sea, and land) and integrate weather defense features as mentioned on the Portline Shipping website.
Generated: DETERMINISTIC_ba7ea368f6805c93
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Logistics Dashboard API",
              description="API for tracking shipments across multiple transport modes with weather defense features",
              version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database for demonstration
shipments_db = []
weather_data_cache = {}

# Models
class Shipment(BaseModel):
    id: str = Field(..., description="Unique shipment ID")
    tracking_number: str = Field(..., description="Tracking number")
    origin: str = Field(..., description="Origin location")
    destination: str = Field(..., description="Destination location")
    mode: str = Field(..., description="Transport mode (air/sea/land)")
    status: str = Field(..., description="Current status")
    estimated_arrival: datetime = Field(..., description="Estimated arrival time")
    current_location: Optional[str] = Field(None, description="Current location coordinates")
    weather_alert: Optional[bool] = Field(False, description="Weather alert status")
    weather_details: Optional[Dict] = Field(None, description="Weather details")

class WeatherRequest(BaseModel):
    location: str = Field(..., description="Location to check weather")
    shipment_id: Optional[str] = Field(None, description="Associated shipment ID")

# API Endpoints
@app.post("/shipments/", response_model=Shipment, status_code=201)
async def create_shipment(shipment: Shipment):
    """Create a new shipment record"""
    if any(s.id == shipment.id for s in shipments_db):
        raise HTTPException(status_code=400, detail="Shipment ID already exists")
    
    shipments_db.append(shipment)
    return shipment

@app.get("/shipments/", response_model=List[Shipment])
async def get_shipments():
    """Get all shipments"""
    return shipments_db

@app.get("/shipments/{shipment_id}", response_model=Shipment)
async def get_shipment(shipment_id: str):
    """Get a specific shipment by ID"""
    shipment = next((s for s in shipments_db if s.id == shipment_id), None)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@app.put("/shipments/{shipment_id}", response_model=Shipment)
async def update_shipment(shipment_id: str, updated_shipment: Shipment):
    """Update a shipment record"""
    index = next((i for i, s in enumerate(shipments_db) if s.id == shipment_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    shipments_db[index] = updated_shipment
    return updated_shipment

@app.delete("/shipments/{shipment_id}", status_code=204)
async def delete_shipment(shipment_id: str):
    """Delete a shipment record"""
    global shipments_db
    shipments_db = [s for s in shipments_db if s.id != shipment_id]
    return None

@app.post("/weather/check", response_model=Dict)
async def check_weather(weather_request: WeatherRequest):
    """Check weather conditions for a location"""
    try:
        # Mock weather API call - in production, replace with actual API call
        if weather_request.location in weather_data_cache:
            weather_data = weather_data_cache[weather_request.location]
        else:
            # Simulate API response
            weather_data = {
                "location": weather_request.location,
                "temperature": 22.5,
                "conditions": "Partly Cloudy",
                "wind_speed": 15,
                "alerts": ["High Winds"],
                "timestamp": datetime.now().isoformat()
            }
            weather_data_cache[weather_request.location] = weather_data
        
        # Update shipment with weather alert if applicable
        if weather_request.shipment_id:
            shipment = next((s for s in shipments_db if s.id == weather_request.shipment_id), None)
            if shipment:
                has_alert = len(weather_data.get("alerts", [])) > 0
                shipment.weather_alert = has_alert
                shipment.weather_details = weather_data
        
        return weather_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather check failed: {str(e)}")

@app.get("/dashboard", response_model=Dict)
async def get_dashboard():
    """Get dashboard summary data"""
    try:
        total_shipments = len(shipments_db)
        air_shipments = len([s for s in shipments_db if s.mode == "air"])
        sea_shipments = len([s for s in shipments_db if s.mode == "sea"])
        land_shipments = len([s for s in shipments_db if s.mode == "land"])
        weather_alerts = len([s for s in shipments_db if s.weather_alert])
        
        return {
            "total_shipments": total_shipments,
            "air_shipments": air_shipments,
            "sea_shipments": sea_shipments,
            "land_shipments": land_shipments,
            "weather_alerts": weather_alerts,
            "last_updated": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dashboard data retrieval failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
