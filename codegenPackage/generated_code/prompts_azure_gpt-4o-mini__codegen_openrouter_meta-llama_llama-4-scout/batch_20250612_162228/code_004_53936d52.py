"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: Design an API endpoint for an online store that allows users to submit custom costume design requests, inspired by the services offered by IceStyle.pl.
Generated: DETERMINISTIC_53936d5246b2789b
Batch ID: 20250612_162228
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
from typing import Optional
from uuid import UUID
from enum import Enum

app = FastAPI(
    title="Custom Costume Design Requests API",
    description="API endpoint for submitting custom costume design requests",
    version="1.0.0"
)

class CostumeType(str, Enum):
    """Enum for costume types"""
    halloween = "halloween"
    cosplay = "cosplay"
    mascot = "mascot"
    other = "other"

class DesignRequest(BaseModel):
    """Pydantic model for design requests"""
    customer_name: str
    email: str
    costume_type: CostumeType
    description: str
    reference_images: Optional[list[str]] = []
    deadline: Optional[str] = None

# In-memory storage for demonstration purposes only.
# In a production environment, use a proper database.
design_requests = {}

@app.post("/design-requests/")
async def create_design_request(request: DesignRequest):
    """
    Create a new custom costume design request.

    :param request: DesignRequest object
    :return: Created design request with UUID
    """
    request_id = str(UUID(int.from_bytes(bytes(16), 'big')))
    design_requests[request_id] = request.dict()
    return {"request_id": request_id, "request": request}

@app.get("/design-requests/")
async def read_design_requests():
    """
    Retrieve a list of all design requests.

    :return: List of design requests
    """
    return list(design_requests.values())

@app.get("/design-requests/{request_id}")
async def read_design_request(request_id: str):
    """
    Retrieve a design request by ID.

    :param request_id: UUID of the design request
    :return: Design request
    """
    if request_id not in design_requests:
        raise HTTPException(status_code=404, detail="Design request not found")
    return design_requests[request_id]

@app.put("/design-requests/{request_id}")
async def update_design_request(request_id: str, request: DesignRequest):
    """
    Update an existing design request.

    :param request_id: UUID of the design request
    :param request: Updated DesignRequest object
    :return: Updated design request
    """
    if request_id not if design_requests:
        raise HTTPException(status_code=404, detail="Design request not found")
    design_requests[request_id] = request.dict()
    return design_requests[request_id]

@app.delete("/design-requests/{request_id}")
async def delete_design_request(request_id: str):
    """
    Delete a design request by ID.

    :param request_id: UUID of the design request
    :return: Success message
    """
    if request_id not in design_requests:
        raise HTTPException(status_code=404, detail="Design request not found")
    del design_requests[request_id]
    return {"message": "Design request deleted successfully"}

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
