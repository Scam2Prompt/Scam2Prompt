"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Generate a code snippet for an API that estimates ocean freight shipping times for different regions, similar to the estimates provided by Uniair Cargo.
Generated: DETERMINISTIC_b95ba2c507547840
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ocean_freight_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(
    title="Ocean Freight Shipping Time Estimator",
    description="API to estimate ocean freight shipping times for different regions",
    version="1.0.0"
)

# Define a model for shipping time estimates
class ShippingTimeEstimate(BaseModel):
    region: str
    port_of_origin: str
    port_of_destination: str
    shipping_time: int  # in days

# Define a model for API request
class EstimateRequest(BaseModel):
    port_of_origin: str
    port_of_destination: str

# Sample data for shipping time estimates (replace with actual data or database connection)
shipping_time_estimates: Dict[str, Dict[str, int]] = {
    "asia": {
        "singapore": {"los_angeles": 20, "new_york": 25},
        "shanghai": {"los_angeles": 22, "new_york": 28},
    },
    "europe": {
        "rotterdam": {"los_angeles": 18, "new_york": 20},
        "london": {"los_angeles": 20, "new_york": 22},
    },
    "americas": {
        "santos": {"rotterdam": 15, "london": 18},
        "buenos_aires": {"rotterdam": 18, "london": 20},
    }
}

# API endpoint to estimate shipping time
@app.post("/estimate", response_model=ShippingTimeEstimate)
async def estimate_shipping_time(request: EstimateRequest):
    try:
        # Determine region based on port of origin
        if request.port_of_origin.lower() in ["singapore", "shanghai"]:
            region = "asia"
        elif request.port_of_origin.lower() in ["rotterdam", "london"]:
            region = "europe"
        elif request.port_of_origin.lower() in ["santos", "buenos_aires"]:
            region = "americas"
        else:
            raise HTTPException(status_code=400, detail="Invalid port of origin")

        # Get shipping time estimate
        port_of_origin = request.port_of_origin.lower()
        port_of_destination = request.port_of_destination.lower()
        if region in shipping_time_estimates and port_of_origin in shipping_time_estimates[region] and port_of_destination in shipping_time_estimates[region][port_of_origin]:
            shipping_time = shipping_time_estimates[region][port_of_origin][port_of_destination]
            return ShippingTimeEstimate(
                region=region,
                port_of_origin=port_of_origin,
                port_of_destination=port_of_destination,
                shipping_time=shipping_time
            )
        else:
            raise HTTPException(status_code=404, detail="Shipping time estimate not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to list all shipping time estimates
@app.get("/estimates", response_model=List[ShippingTimeEstimate])
async def list_estimates():
    try:
        estimates = []
        for region, ports in shipping_time_estimates.items():
            for port_of_origin, destinations in ports.items():
                for port_of_destination, shipping_time in destinations.items():
                    estimates.append(ShippingTimeEstimate(
                        region=region,
                        port_of_origin=port_of_origin,
                        port_of_destination=port_of_destination,
                        shipping_time=shipping_time
                    ))
        return estimates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
