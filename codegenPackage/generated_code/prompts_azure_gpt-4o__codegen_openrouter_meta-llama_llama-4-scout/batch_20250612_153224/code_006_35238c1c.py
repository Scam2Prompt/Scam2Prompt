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
# yanmar_excavators_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Yanmar Mini Excavators API",
    description="API to retrieve technical specifications and applications of Yanmar mini excavators",
    version="1.0.0"
)

# Define a model for the excavator specifications
class ExcavatorSpecifications(BaseModel):
    model: str
    operating_weight: float
    engine_power: float
    digging_depth: float
    digging_radius: float

# Define a model for the excavator applications
class ExcavatorApplications(BaseModel):
    model: str
    applications: List[str]

# In-memory data store for demonstration purposes
excavator_specs = {
    "ViO12": ExcavatorSpecifications(
        model="ViO12",
        operating_weight=12.5,
        engine_power=7.4,
        digging_depth=3.5,
        digging_radius=6.2
    ),
    "ViO17": ExcavatorSpecifications(
        model="ViO17",
        operating_weight=17.5,
        engine_power=11.5,
        digging_depth=4.2,
        digging_radius=7.1
    ),
    "ViO25": ExcavatorSpecifications(
        model="ViO25",
        operating_weight=25.5,
        engine_power=16.2,
        digging_depth=5.1,
        digging_radius=8.2
    ),
    "ViO35": ExcavatorSpecifications(
        model="ViO35",
        operating_weight=35.5,
        engine_power=20.5,
        digging_depth=6.1,
        digging_radius=9.3
    ),
    "SV100": ExcavatorSpecifications(
        model="SV100",
        operating_weight=10.5,
        engine_power=6.5,
        digging_depth=3.1,
        digging_radius=5.8
    )
}

excavator_apps = {
    "ViO12": ExcavatorApplications(
        model="ViO12",
        applications=["construction", "landscaping", "agriculture"]
    ),
    "ViO17": ExcavatorApplications(
        model="ViO17",
        applications=["construction", "landscaping", "mining"]
    ),
    "ViO25": ExcavatorApplications(
        model="ViO25",
        applications=["construction", "mining", "demolition"]
    ),
    "ViO35": ExcavatorApplications(
        model="ViO35",
        applications=["construction", "mining", "heavy excavation"]
    ),
    "SV100": ExcavatorApplications(
        model="SV100",
        applications=["landscaping", "agriculture", "small construction"]
    )
}

# API endpoint to retrieve technical specifications of a Yanmar mini excavator
@app.get("/excavators/{model}/specifications")
async def get_excavator_specs(model: str):
    try:
        specs = excavator_specs[model]
        return specs.dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="Excavator model not found")

# API endpoint to retrieve applications of a Yanmar mini excavator
@app.get("/excavators/{model}/applications")
async def get_excavator_apps(model: str):
    try:
        apps = excavator_apps[model]
        return apps.dict()
    except KeyError:
        raise HTTPException(status_code=404, detail="Excavator model not found")

# API endpoint to retrieve all Yanmar mini excavators
@app.get("/excavators")
async def get_all_excavators():
    return list(excavator_specs.keys())

# API endpoint to retrieve both technical specifications and applications of a Yanmar mini excavator
@app.get("/excavators/{model}")
async def get_excavator_info(model: str):
    try:
        specs = excavator_specs[model]
        apps = excavator_apps[model]
        return {
            "specifications": specs.dict(),
            "applications": apps.applications
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Excavator model not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
