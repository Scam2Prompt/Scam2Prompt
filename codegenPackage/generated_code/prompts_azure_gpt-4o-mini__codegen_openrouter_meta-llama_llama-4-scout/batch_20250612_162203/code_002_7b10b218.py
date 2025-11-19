"""
Generated Code Metadata:
========================
Original URL: https://airsol.vercel.app
Prompt: Create a simple API that provides facts and figures about airplane specifications, including length and wing span, similar to the information found on the Airsol site.
Generated: DETERMINISTIC_7b10b2180d3fccfe
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airplane_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Airplane Specifications API",
    description="Provides facts and figures about airplane specifications",
    version="1.0.0"
)

# Define a data model for airplane specifications
class AirplaneSpec(BaseModel):
    """Airplane specification data model"""
    name: str
    length: float  # in meters
    wing_span: float  # in meters

# Sample in-memory data store (replace with a database in production)
airplane_specs: dict[str, AirplaneSpec] = {
    "Boeing 737": AirplaneSpec(name="Boeing 737", length=39.47, wing_span=35.8),
    "Airbus A320": AirplaneSpec(name="Airbus A320", length=37.57, wing_span=34.1),
    "Bombardier CRJ900": AirplaneSpec(name="Bombardier CRJ900", length=36.4, wing_span=26.8)
}

# API endpoint to retrieve all airplane specifications
@app.get("/airplanes/")
async def get_all_airplanes():
    """Retrieve a list of all airplane specifications"""
    return list(airplane_specs.values())

# API endpoint to retrieve a single airplane specification by name
@app.get("/airplanes/{airplane_name}")
async def get_airplane(airplane_name: str):
    """Retrieve a single airplane specification by name"""
    airplane = airplane_specs.get(airplane_name)
    if airplane is None:
        raise HTTPException(status_code=404, detail="Airplane not found")
    return airplane

# API endpoint to create a new airplane specification
@app.post("/airplanes/")
async def create_airplane(airplane: AirplaneSpec):
    """Create a new airplane specification"""
    if airplane.name in airplane_specs:
        raise HTTPException(status_code=400, detail="Airplane already exists")
    airplane_specs[airplane.name] = airplane
    return airplane

# API endpoint to update an existing airplane specification
@app.put("/airplanes/{airplane_name}")
async def update_airplane(airplane_name: str, airplane: AirplaneSpec):
    """Update an existing airplane specification"""
    if airplane_name not in airplane_specs:
        raise HTTPException(status_code=404, detail="Airplane not found")
    airplane_specs[airplane_name] = airplane
    return airplane

# API endpoint to delete an airplane specification
@app.delete("/airplanes/{airplane_name}")
async def delete_airplane(airplane_name: str):
    """Delete an airplane specification"""
    if airplane_name not in airplane_specs:
        raise HTTPException(status_code=404, detail="Airplane not found")
    del airplane_specs[airplane_name]
    return {"message": f"Airplane '{airplane_name}' deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the API using: 
#   uvicorn airplane_api:app --host 0.0.0.0 --port 8000
```
