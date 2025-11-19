"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Create a RESTful API endpoint to retrieve information about different types of UPVC door systems, such as casement doors and sliding doors, including their advantages and installation services."
Generated: DETERMINISTIC_34d1b4b51dbb0d6f
Batch ID: 20250622_210038
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

app = FastAPI(
    title="UPVC Door Systems API",
    description="Retrieve information about different types of UPVC door systems",
    version="1.0.0",
)

class DoorSystem(BaseModel):
    """Base model for UPVC door systems"""
    door_type: str
    advantages: list[str]
    installation_services: list[str]

class UPVCDoorSystemService:
    """Service class to manage UPVC door systems data"""
    def __init__(self):
        self.door_systems = {
            "casement_doors": DoorSystem(
                door_type="Casement Doors",
                advantages=["Energy Efficiency", "Low Maintenance", "Security"],
                installation_services=["Standard Installation", "Premium Installation"]
            ),
            "sliding_doors": DoorSystem(
                door_type="Sliding Doors",
                advantages=["Space Saving", "Easy Operation", "Modern Look"],
                installation_services=["Standard Installation", "Premium Installation"]
            ),
            # Add more door systems as needed
        }

    def get_door_system(self, door_type: str):
        """Retrieve a specific door system by type"""
        return self.door_systems.get(door_type.lower().replace(" ", "_"))

    def get_all_door_systems(self):
        """Retrieve all available door systems"""
        return list(self.door_systems.values())

door_system_service = UPVCDoorSystemService()

@app.get("/door-systems/")
async def read_door_systems():
    """Retrieve all available UPVC door systems"""
    return door_system_service.get_all_door_systems()

@app.get("/door-systems/{door_type}")
async def read_door_system(door_type: str):
    """Retrieve a specific UPVC door system by type"""
    door_system = door_system_service.get_door_system(door_type)
    if not door_system:
        raise HTTPException(status_code=404, detail="Door system not found")
    return door_system

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return exc

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
# Run the application
# uvicorn app:app --host 0.0.0.0 --port 8000
```
