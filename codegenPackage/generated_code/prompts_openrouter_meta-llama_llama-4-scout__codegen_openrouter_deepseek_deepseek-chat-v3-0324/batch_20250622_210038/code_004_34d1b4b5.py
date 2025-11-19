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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="UPVC Door Systems API",
    description="API for retrieving information about different types of UPVC door systems",
    version="1.0.0"
)

class DoorSystem(BaseModel):
    id: int
    name: str
    description: str
    advantages: List[str]
    installation_services: Optional[List[str]] = None

# Mock database
door_systems_db = [
    {
        "id": 1,
        "name": "Casement Doors",
        "description": "Traditional hinged doors that open outward or inward.",
        "advantages": [
            "Excellent security",
            "Good thermal insulation",
            "Wide range of designs"
        ],
        "installation_services": [
            "Standard installation",
            "Custom fitting",
            "Hardware upgrade"
        ]
    },
    {
        "id": 2,
        "name": "Sliding Doors",
        "description": "Doors that slide horizontally on tracks.",
        "advantages": [
            "Space-saving",
            "Modern appearance",
            "Smooth operation"
        ],
        "installation_services": [
            "Track installation",
            "Panel replacement",
            "Weatherproofing"
        ]
    }
]

@app.get("/door-systems/", response_model=List[DoorSystem], tags=["Door Systems"])
async def get_all_door_systems():
    """
    Retrieve all available UPVC door systems.
    """
    return door_systems_db

@app.get("/door-systems/{door_id}", response_model=DoorSystem, tags=["Door Systems"])
async def get_door_system(door_id: int):
    """
    Retrieve a specific UPVC door system by ID.
    
    Parameters:
    - door_id: The ID of the door system to retrieve
    """
    door = next((d for d in door_systems_db if d["id"] == door_id), None)
    if not door:
        raise HTTPException(status_code=404, detail="Door system not found")
    return door

@app.get("/door-systems/search/", response_model=List[DoorSystem], tags=["Door Systems"])
async def search_door_systems(name: Optional[str] = None):
    """
    Search for UPVC door systems by name.
    
    Parameters:
    - name: Optional name to search for (case-insensitive partial match)
    """
    if not name:
        return door_systems_db
    
    results = [d for d in door_systems_db if name.lower() in d["name"].lower()]
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
