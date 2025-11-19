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
import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
import httpx
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Electrical Utility Integration API",
    description="API for managing electrical utility systems including traffic signals and street lighting",
    version="1.0.0"
)

class TrafficSignal(BaseModel):
    id: str = Field(..., description="Unique identifier for the traffic signal")
    location: str = Field(..., description="Geographic location of the signal")
    status: str = Field("active", description="Current status of the signal")
    last_maintenance: Optional[datetime] = None
    brightness: Optional[int] = Field(100, ge=0, le=100, description="Brightness level (0-100)")

class StreetLight(BaseModel):
    id: str = Field(..., description="Unique identifier for the street light")
    location: str = Field(..., description="Geographic location of the light")
    status: str = Field("active", description="Current status of the light")
    brightness: int = Field(75, ge=0, le=100, description="Brightness level (0-100)")
    energy_consumption: Optional[float] = None

class UtilitySystemStatus(BaseModel):
    system_name: str
    status: str
    components_online: int
    components_total: int

# Mock database
traffic_signals_db = {}
street_lights_db = {}

@app.on_event("startup")
async def startup_event():
    """Initialize mock data on startup"""
    logger.info("Initializing mock data...")
    traffic_signals_db["ts1"] = TrafficSignal(id="ts1", location="Main St & 1st Ave")
    traffic_signals_db["ts2"] = TrafficSignal(id="ts2", location="Oak St & Pine Ave")
    
    street_lights_db["sl1"] = StreetLight(id="sl1", location="Main St, Block 1")
    street_lights_db["sl2"] = StreetLight(id="sl2", location="Oak St, Block 2")
    logger.info("Mock data initialized")

@app.get("/traffic-signals/", response_model=List[TrafficSignal])
async def get_all_traffic_signals():
    """Get all traffic signals"""
    return list(traffic_signals_db.values())

@app.get("/traffic-signals/{signal_id}", response_model=TrafficSignal)
async def get_traffic_signal(signal_id: str):
    """Get a specific traffic signal by ID"""
    if signal_id not in traffic_signals_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Traffic signal not found"
        )
    return traffic_signals_db[signal_id]

@app.post("/traffic-signals/", response_model=TrafficSignal, status_code=status.HTTP_201_CREATED)
async def create_traffic_signal(signal: TrafficSignal):
    """Create a new traffic signal"""
    if signal.id in traffic_signals_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Traffic signal with this ID already exists"
        )
    traffic_signals_db[signal.id] = signal
    logger.info(f"Created traffic signal with ID: {signal.id}")
    return signal

@app.put("/traffic-signals/{signal_id}", response_model=TrafficSignal)
async def update_traffic_signal(signal_id: str, signal: TrafficSignal):
    """Update an existing traffic signal"""
    if signal_id not in traffic_signals_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Traffic signal not found"
        )
    traffic_signals_db[signal_id] = signal
    logger.info(f"Updated traffic signal with ID: {signal_id}")
    return signal

@app.patch("/traffic-signals/{signal_id}/brightness", response_model=TrafficSignal)
async def adjust_traffic_signal_brightness(signal_id: str, brightness: int):
    """Adjust brightness of a traffic signal"""
    if signal_id not in traffic_signals_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Traffic signal not found"
        )
    if brightness < 0 or brightness > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Brightness must be between 0 and 100"
        )
    traffic_signals_db[signal_id].brightness = brightness
    logger.info(f"Adjusted brightness for traffic signal {signal_id} to {brightness}")
    return traffic_signals_db[signal_id]

@app.get("/street-lights/", response_model=List[StreetLight])
async def get_all_street_lights():
    """Get all street lights"""
    return list(street_lights_db.values())

@app.get("/street-lights/{light_id}", response_model=StreetLight)
async def get_street_light(light_id: str):
    """Get a specific street light by ID"""
    if light_id not in street_lights_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Street light not found"
        )
    return street_lights_db[light_id]

@app.post("/street-lights/", response_model=StreetLight, status_code=status.HTTP_201_CREATED)
async def create_street_light(light: StreetLight):
    """Create a new street light"""
    if light.id in street_lights_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Street light with this ID already exists"
        )
    street_lights_db[light.id] = light
    logger.info(f"Created street light with ID: {light.id}")
    return light

@app.put("/street-lights/{light_id}", response_model=StreetLight)
async def update_street_light(light_id: str, light: StreetLight):
    """Update an existing street light"""
    if light_id not in street_lights_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Street light not found"
        )
    street_lights_db[light_id] = light
    logger.info(f"Updated street light with ID: {light_id}")
    return light

@app.patch("/street-lights/{light_id}/brightness", response_model=StreetLight)
async def adjust_street_light_brightness(light_id: str, brightness: int):
    """Adjust brightness of a street light"""
    if light_id not in street_lights_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Street light not found"
        )
    if brightness < 0 or brightness > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Brightness must be between 0 and 100"
        )
    street_lights_db[light_id].brightness = brightness
    logger.info(f"Adjusted brightness for street light {light_id} to {brightness}")
    return street_lights_db[light_id]

@app.get("/system-status/", response_model=UtilitySystemStatus)
async def get_system_status():
    """Get overall system status"""
    return UtilitySystemStatus(
        system_name="City Electrical Utility System",
        status="operational",
        components_online=len(traffic_signals_db) + len(street_lights_db),
        components_total=len(traffic_signals_db) + len(street_lights_db)
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

async def external_api_call(url: str):
    """Helper function for making external API calls"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="External service unavailable"
        )
    except Exception as e:
        logger.error(f"Error calling external API: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```
