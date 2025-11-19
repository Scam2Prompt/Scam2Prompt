"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a RESTful API endpoint that allows users to submit requests for custom kitchen cabinetry designs, reflecting the modern and practical approach of Linea 7.
Generated: DETERMINISTIC_5080097632bda7af
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**kitchen_cabinetry_api.py**
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Linea 7 Kitchen Cabinetry Design API",
    description="Submit requests for custom kitchen cabinetry designs",
    version="1.0.0"
)

# Define the request model for cabinetry design
class CabinetryDesignRequest(BaseModel):
    """Request model for custom kitchen cabinetry design"""
    customer_name: str
    email: str
    phone_number: str
    design_description: str
    measurements: dict
    materials: list[str]
    created_at: Optional[datetime] = datetime.now()

# Define the response model for cabinetry design request
class CabinetryDesignResponse(BaseModel):
    """Response model for custom kitchen cabinetry design request"""
    id: UUID
    customer_name: str
    email: str
    phone_number: str
    design_description: str
    measurements: dict
    materials: list[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

# In-memory storage for demonstration purposes
# Replace with a proper database in production
design_requests = {}

@app.post("/designs", status_code=status.HTTP_201_CREATED, response_model=CabinetryDesignResponse)
async def create_design_request(request: CabinetryDesignRequest):
    """Create a new custom kitchen cabinetry design request"""
    design_request_id = UUID(str(len(design_requests) + 1))
    design_requests[design_request_id] = CabinetryDesignResponse(
        id=design_request_id,
        customer_name=request.customer_name,
        email=request.email,
        phone_number=request.phone_number,
        design_description=request.design_description,
        measurements=request.measurements,
        materials=request.materials,
        created_at=request.created_at
    )
    return design_requests[design_request_id]

@app.get("/designs/{design_request_id}", status_code=status.HTTP_200_OK, response_model=CabinetryDesignResponse)
async def get_design_request(design_request_id: UUID):
    """Retrieve a custom kitchen cabinetry design request by ID"""
    if design_request_id not in design_requests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Design request not found")
    return design_requests[design_request_id]

@app.put("/designs/{design_request_id}", status_code=status.HTTP_200_OK, response_model=CabinetryDesignResponse)
async def update_design_request(design_request_id: UUID, request: CabinetryDesignRequest):
    """Update a custom kitchen cabinetry design request"""
    if design_request_id not in design_requests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Design request not found")
    design_requests[design_request_id] = CabinetryDesignResponse(
        id=design_request_id,
        customer_name=request.customer_name,
        email=request.email,
        phone_number=request.phone_number,
        design_description=request.design_description,
        measurements=request.measurements,
        materials=request.materials,
        created_at=design_requests[design_request_id].created_at,
        updated_at=datetime.now()
    )
    return design_requests[design_request_id]

@app.delete("/designs/{design_request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_design_request(design_request_id: UUID):
    """Delete a custom kitchen cabinetry design request"""
    if design_request_id not in design_requests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Design request not found")
    del design_requests[design_request_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
**main function to run**
```bash
uvicorn kitchen_cabinetry_api:app --host 0.0.0.0 --port 8000 --reload
```
