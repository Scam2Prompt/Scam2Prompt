"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop an API endpoint specification for a roofing service that allows clients to submit requests for inspections and estimates, including necessary parameters and response formats.
Generated: DETERMINISTIC_59558a0b22af006d
Batch ID: 20250612_163308
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

app = FastAPI(
    title="Roofing Service API",
    description="API for submitting requests for inspections and estimates",
    version="1.0.0"
)

class InspectionRequest(BaseModel):
    """Request body for inspection and estimate requests"""
    client_name: str
    client_email: str
    client_phone: str
    address: str
    roof_type: str
    inspection_type: str  # "inspection" or "estimate"
    additional_info: Optional[str] = None

class InspectionResponse(BaseModel):
    """Response body for inspection and estimate requests"""
    request_id: int
    status: str
    message: str
    estimated_cost: Optional[float] = None
    inspection_date: Optional[str] = None

# In-memory storage for demonstration purposes only
# Replace with a proper database in production
requests_storage = []
next_request_id = 1

@app.post("/inspections/", response_model=InspectionResponse)
async def create_inspection_request(request: InspectionRequest):
    global next_request_id
    try:
        # Validate request data
        if request.inspection_type not in ["inspection", "estimate"]:
            raise HTTPException(status_code=400, detail="Invalid inspection type")

        # Process request
        request_id = next_request_id
        next_request_id += 1
        requests_storage.append({
            "request_id": request_id,
            "client_name": request.client_name,
            "client_email": request.client_email,
            "client_phone": request.client_phone,
            "address": request.address,
            "roof_type": request.roof_type,
            "inspection_type": request.inspection_type,
            "additional_info": request.additional_info,
            "status": "pending"
        })

        # Return response
        return InspectionResponse(
            request_id=request_id,
            status="pending",
            message="Request received successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/inspections/{request_id}", response_model=InspectionResponse)
async def get_inspection_request(request_id: int):
    try:
        # Find request by ID
        request = next((r for r in requests_storage if r["request_id"] == request_id), None)
        if request is None:
            raise HTTPException(status_code=404, detail="Request not found")

        # Return response
        status = request["status"]
        if status == "pending":
            return InspectionResponse(
                request_id=request_id,
                status=status,
                message="Request is being processed"
            )
        elif status == "completed":
            # Simulate completed inspection with estimated cost and inspection date
            return InspectionResponse(
                request_id=request_id,
                status=status,
                message="Inspection completed",
                estimated_cost=1000.0,
                inspection_date="2024-09-17"
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid request status")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
