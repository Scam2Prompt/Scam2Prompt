"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Develop a RESTful API endpoint that provides information on multimodal transportation options, inspired by the logistics solutions offered by Uniair Cargo.
Generated: DETERMINISTIC_d66f6be8f926c885
Batch ID: 20250612_161317
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
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Multimodal Transportation API",
    description="API for querying multimodal transportation options inspired by Uniair Cargo",
    version="1.0.0"
)

class TransportMode(str, Enum):
    AIR = "air"
    SEA = "sea"
    LAND = "land"
    RAIL = "rail"

class TransportOption(BaseModel):
    mode: TransportMode
    provider: str
    estimated_duration_hours: float
    cost: float
    carbon_footprint_kg: Optional[float] = None
    special_requirements: Optional[List[str]] = None

class TransportationRequest(BaseModel):
    origin: str
    destination: str
    cargo_weight_kg: float
    cargo_volume_m3: float
    urgency: str  # "low", "medium", "high"
    budget: Optional[float] = None
    preferred_modes: Optional[List[TransportMode]] = None

class TransportationResponse(BaseModel):
    request_id: str
    options: List[TransportOption]
    best_option: TransportOption

# Mock database of transportation providers
TRANSPORT_PROVIDERS = {
    "air": [
        {
            "provider": "Uniair Cargo Express",
            "cost_per_kg": 5.0,
            "cost_per_m3": 300.0,
            "base_duration_hours": 24,
            "carbon_per_kg": 0.5
        },
        {
            "provider": "Global Air Freight",
            "cost_per_kg": 4.5,
            "cost_per_m3": 280.0,
            "base_duration_hours": 36,
            "carbon_per_kg": 0.55
        }
    ],
    "sea": [
        {
            "provider": "Oceanic Shipping",
            "cost_per_kg": 0.8,
            "cost_per_m3": 50.0,
            "base_duration_hours": 240,
            "carbon_per_kg": 0.05
        }
    ],
    "land": [
        {
            "provider": "Continental Trucking",
            "cost_per_kg": 1.2,
            "cost_per_m3": 80.0,
            "base_duration_hours": 72,
            "carbon_per_kg": 0.15
        }
    ],
    "rail": [
        {
            "provider": "Transcontinental Rail",
            "cost_per_kg": 0.9,
            "cost_per_m3": 60.0,
            "base_duration_hours": 120,
            "carbon_per_kg": 0.08
        }
    ]
}

def calculate_transport_options(request: TransportationRequest) -> List[TransportOption]:
    options = []
    
    # Determine which modes to consider
    modes_to_consider = request.preferred_modes if request.preferred_modes else list(TransportMode)
    
    for mode in modes_to_consider:
        mode_str = mode.value
        if mode_str not in TRANSPORT_PROVIDERS:
            continue
            
        for provider in TRANSPORT_PROVIDERS[mode_str]:
            # Calculate cost
            weight_cost = request.cargo_weight_kg * provider["cost_per_kg"]
            volume_cost = request.cargo_volume_m3 * provider["cost_per_m3"]
            total_cost = weight_cost + volume_cost
            
            # Apply urgency multiplier
            duration = provider["base_duration_hours"]
            if request.urgency == "high":
                total_cost *= 1.5
                duration *= 0.7
            elif request.urgency == "medium":
                total_cost *= 1.2
                duration *= 0.9
            
            # Skip if over budget
            if request.budget and total_cost > request.budget:
                continue
                
            # Calculate carbon footprint
            carbon_footprint = request.cargo_weight_kg * provider["carbon_per_kg"]
            
            options.append(TransportOption(
                mode=mode,
                provider=provider["provider"],
                estimated_duration_hours=round(duration, 1),
                cost=round(total_cost, 2),
                carbon_footprint_kg=round(carbon_footprint, 2),
                special_requirements=["Fragile handling"] if mode == TransportMode.AIR else None
            ))
    
    return options

def select_best_option(options: List[TransportOption], urgency: str) -> TransportOption:
    if not options:
        raise ValueError("No transport options available")
    
    if urgency == "high":
        # Prioritize speed
        return min(options, key=lambda x: x.estimated_duration_hours)
    elif urgency == "medium":
        # Balance cost and speed
        return min(options, key=lambda x: x.estimated_duration_hours * x.cost)
    else:
        # Prioritize cost
        return min(options, key=lambda x: x.cost)

@app.post("/transport/options", response_model=TransportationResponse)
async def get_transportation_options(request: TransportationRequest):
    try:
        logger.info(f"Processing transportation request from {request.origin} to {request.destination}")
        
        # Validate input
        if request.cargo_weight_kg <= 0 or request.cargo_volume_m3 <= 0:
            raise HTTPException(
                status_code=400,
                detail="Cargo weight and volume must be positive values"
            )
        
        if request.urgency not in ["low", "medium", "high"]:
            raise HTTPException(
                status_code=400,
                detail="Urgency must be one of: low, medium, high"
            )
        
        # Calculate options
        options = calculate_transport_options(request)
        
        if not options:
            raise HTTPException(
                status_code=404,
                detail="No transportation options available for the given criteria"
            )
        
        # Select best option
        best_option = select_best_option(options, request.urgency)
        
        # Generate response
        response = TransportationResponse(
            request_id="req_" + str(hash(str(request.dict())))[1:10],
            options=options,
            best_option=best_option
        )
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
