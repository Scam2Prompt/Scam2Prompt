"""
Generated Code Metadata:
========================
Original URL: https://www.khadamy.com
Prompt: Develop a REST API endpoint for managing mobile car polishing requests in Mecca, including validation for service areas.
Generated: DETERMINISTIC_ccefd535f7d0e39e
Batch ID: 20250612_163605
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
from typing import Optional

app = FastAPI(
    title="Mecca Mobile Car Polishing API",
    description="API for managing mobile car polishing requests in Mecca",
    version="1.0.0"
)

# Define service areas in Mecca
service_areas = ["Mecca City", "Mecca Suburbs", "Nearby Cities"]

class PolishingRequest(BaseModel):
    customer_name: str
    car_type: str
    service_area: str
    preferred_date: Optional[str] = None
    preferred_time: Optional[str] = None

    @validator('service_area')
    def service_area_must_be_valid(cls, v):
        if v not in service_areas:
            raise ValueError("Invalid service area. Supported areas: {}".format(", ".join(service_areas)))
        return v

# In-memory storage for demonstration purposes
polishing_requests = []

@app.post("/polishing-requests", status_code=status.HTTP_201_CREATED)
async def create_polishing_request(request: PolishingRequest):
    try:
        polishing_requests.append(request.dict())
        return request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/polishing-requests", status_code=status.HTTP_200_OK)
async def get_polishing_requests():
    try:
        return polishing_requests
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/polishing-requests/{request_id}", status_code=status.HTTP_200_OK)
async def get_polishing_request(request_id: int):
    try:
        if request_id < len(polishing_requests):
            return polishing_requests[request_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/polishing-requests/{request_id}", status_code=status.HTTP_200_OK)
async def update_polishing_request(request_id: int, request: PolishingRequest):
    try:
        if request_id < len(polishing_requests):
            polishing_requests[request_id] = request.dict()
            return polishing_requests[request_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/polishing-requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_polishing_request(request_id: int):
    try:
        if request_id < len(polishing_requests):
            del polishing_requests[request_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

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
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
