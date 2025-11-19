"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Develop an API to retrieve technical specifications and applications of Yanmar mini excavators, such as ViO12, ViO17, ViO25, ViO35, and SV100, for use in construction, agriculture, and landscaping projects.
Generated: DETERMINISTIC_35238c1ce06aead0
Batch ID: 20250612_153224
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
from typing import Dict, List, Optional

app = FastAPI(
    title="Yanmar Mini Excavator API",
    description="API to retrieve technical specifications and applications of Yanmar mini excavators",
    version="1.0.0"
)

# Database mock (in a real application, this would be a database)
excavators_db = {
    "ViO12": {
        "model": "ViO12",
        "weight_kg": 1250,
        "engine_power_hp": 12.5,
        "bucket_capacity_m3": 0.04,
        "max_digging_depth_m": 2.3,
        "applications": ["landscaping", "small construction", "agriculture"]
    },
    "ViO17": {
        "model": "ViO17",
        "weight_kg": 1750,
        "engine_power_hp": 17.3,
        "bucket_capacity_m3": 0.05,
        "max_digging_depth_m": 2.7,
        "applications": ["construction", "utility work", "landscaping"]
    },
    "ViO25": {
        "model": "ViO25",
        "weight_kg": 2500,
        "engine_power_hp": 24.8,
        "bucket_capacity_m3": 0.07,
        "max_digging_depth_m": 3.2,
        "applications": ["construction", "demolition", "agriculture"]
    },
    "ViO35": {
        "model": "ViO35",
        "weight_kg": 3500,
        "engine_power_hp": 35.2,
        "bucket_capacity_m3": 0.12,
        "max_digging_depth_m": 3.8,
        "applications": ["heavy construction", "mining", "agriculture"]
    },
    "SV100": {
        "model": "SV100",
        "weight_kg": 10000,
        "engine_power_hp": 74,
        "bucket_capacity_m3": 0.45,
        "max_digging_depth_m": 6.5,
        "applications": ["large construction", "quarrying", "industrial"]
    }
}

class Excavator(BaseModel):
    model: str
    weight_kg: float
    engine_power_hp: float
    bucket_capacity_m3: float
    max_digging_depth_m: float
    applications: List[str]

@app.get("/models", response_model=List[str], summary="List all available models")
async def list_models():
    """Return a list of all available excavator models."""
    return list(excavators_db.keys())

@app.get("/specs/{model}", response_model=Excavator, summary="Get specifications for a model")
async def get_specs(model: str):
    """
    Retrieve technical specifications for a specific excavator model.
    
    Parameters:
    - model: The excavator model name (e.g., ViO12, ViO17)
    
    Returns:
    - Full technical specifications for the requested model
    """
    if model not in excavators_db:
        raise HTTPException(status_code=404, detail="Model not found")
    return excavators_db[model]

@app.get("/applications", response_model=Dict[str, List[str]], summary="Get models by application")
async def get_models_by_application(application: Optional[str] = None):
    """
    Get excavator models suitable for specific applications.
    
    Parameters:
    - application: Optional filter for specific application (e.g., 'construction')
    
    Returns:
    - Dictionary with application as key and list of suitable models as value
    """
    if application:
        result = {
            application: [
                model for model, specs in excavators_db.items()
                if application.lower() in [app.lower() for app in specs["applications"]]
            ]
        }
        if not result[application]:
            raise HTTPException(status_code=404, detail="No models found for this application")
        return result
    else:
        return {
            app: [model for model, specs in excavators_db.items() if app in specs["applications"]]
            for app in set(app for specs in excavators_db.values() for app in specs["applications"])
        }

# Error handler for validation errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Health check endpoint
@app.get("/health", status_code=200)
async def health_check():
    return {"status": "healthy"}
```
