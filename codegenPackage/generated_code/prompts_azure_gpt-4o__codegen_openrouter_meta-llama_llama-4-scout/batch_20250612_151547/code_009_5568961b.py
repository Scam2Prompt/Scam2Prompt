"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Develop an API for managing customer logistics requests, including air freight, road freight, and ocean freight, inspired by Fealty Worldwide's service categories.
Generated: DETERMINISTIC_5568961b33fb7f84
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Customer Logistics Requests API",
    description="API for managing customer logistics requests",
    version="1.0.0",
)

class FreightType(str, Enum):
    air = "air"
    road = "road"
    ocean = "ocean"

class LogisticsRequest(BaseModel):
    customer_name: str
    freight_type: FreightType
    shipment_description: str
    weight: float
    dimensions: Optional[str] = None

    @validator('weight')
    def weight_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Weight must be a positive number')
        return v

class LogisticsRequestResponse(BaseModel):
    request_id: int
    customer_name: str
    freight_type: FreightType
    shipment_description: str
    weight: float
    dimensions: Optional[str] = None

# In-memory storage for demonstration purposes
# Replace with a database in production
logistics_requests = []
request_id_counter = 1

@app.post("/logistics_requests", response_model=LogisticsRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_logistics_request(request: LogisticsRequest):
    global request_id_counter
    try:
        new_request = LogisticsRequestResponse(
            request_id=request_id_counter,
            customer_name=request.customer_name,
            freight_type=request.freight_type,
            shipment_description=request.shipment_description,
            weight=request.weight,
            dimensions=request.dimensions,
        )
        logistics_requests.append(new_request.dict())
        request_id_counter += 1
        return new_request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/logistics_requests", response_model=List[LogisticsRequestResponse])
async def get_all_logistics_requests():
    try:
        return [LogisticsRequestResponse(**request) for request in logistics_requests]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/logistics_requests/{request_id}", response_model=LogisticsRequestResponse)
async def get_logistics_request(request_id: int):
    try:
        for request in logistics_requests:
            if request['request_id'] == request_id:
                return LogisticsRequestResponse(**request)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logistics request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/logistics_requests/{request_id}", response_model=LogisticsRequestResponse)
async def update_logistics_request(request_id: int, request: LogisticsRequest):
    try:
        for i, existing_request in enumerate(logistics_requests):
            if existing_request['request_id'] == request_id:
                updated_request = LogisticsRequestResponse(
                    request_id=request_id,
                    customer_name=request.customer_name,
                    freight_type=request.freight_type,
                    shipment_description=request.shipment_description,
                    weight=request.weight,
                    dimensions=request.dimensions,
                )
                logistics_requests[i] = updated_request.dict()
                return updated_request
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logistics request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/logistics_requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_logistics_request(request_id: int):
    try:
        for i, existing_request in enumerate(logistics_requests):
            if existing_request['request_id'] == request_id:
                del logistics_requests[i]
                return {"message": "Logistics request deleted successfully"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logistics request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

```python
# main.py
from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
