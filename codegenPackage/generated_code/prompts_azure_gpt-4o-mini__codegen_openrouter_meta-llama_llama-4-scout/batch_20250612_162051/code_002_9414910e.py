"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Create an API endpoint for a dental clinic that retrieves information about various orthodontic appliances available, including conventional and aesthetic options.
Generated: DETERMINISTIC_9414910e8041f97b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Dental Clinic Orthodontic Appliances API",
    description="API for retrieving information about orthodontic appliances",
    version="1.0.0"
)

class OrthodonticAppliance(BaseModel):
    """Model for orthodontic appliance"""
    id: int
    name: str
    description: str
    appliance_type: str  # conventional or aesthetic

# In-memory data store for demonstration purposes
# Replace with a database in a real application
orthodontic_appliances = [
    OrthodonticAppliance(id=1, name="Metal Braces", description="Traditional metal braces", appliance_type="conventional"),
    OrthodonticAppliance(id=2, name="Clear Braces", description="Aesthetic clear braces", appliance_type="aesthetic"),
    OrthodonticAppliance(id=3, name="Lingual Braces", description="Hidden lingual braces", appliance_type="aesthetic"),
    OrthodonticAppliance(id=4, name="Invisalign", description="Clear aligners", appliance_type="aesthetic"),
]

@app.get("/appliances/", response_model=List[OrthodonticAppliance])
async def read_orthodontic_appliances():
    """Retrieve a list of all orthodontic appliances"""
    return orthodontic_appliances

@app.get("/appliances/{appliance_id}", response_model=OrthodonticAppliance)
async def read_orthodontic_appliance(appliance_id: int):
    """Retrieve information about a specific orthodontic appliance"""
    appliance = next((a for a in orthodontic_appliances if a.id == appliance_id), None)
    if appliance is None:
        raise HTTPException(status_code=404, detail="Appliance not found")
    return appliance

@app.get("/appliances/type/{appliance_type}", response_model=List[OrthodonticAppliance])
async def read_orthodontic_appliances_by_type(appliance_type: str):
    """Retrieve a list of orthodontic appliances by type"""
    appliance_type = appliance_type.lower()
    if appliance_type not in ["conventional", "aesthetic"]:
        raise HTTPException(status_code=400, detail="Invalid appliance type")
    return [a for a in orthodontic_appliances if a.appliance_type == appliance_type]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
