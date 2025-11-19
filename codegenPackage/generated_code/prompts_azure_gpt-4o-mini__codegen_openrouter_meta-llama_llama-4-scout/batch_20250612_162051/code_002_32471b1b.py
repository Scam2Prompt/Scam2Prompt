"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Create a REST API endpoint for a computer repair service that allows users to submit their repair requests and receive updates, based on the customer service model of Geeks on Repair.
Generated: DETERMINISTIC_32471b1b90762f68
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

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Computer Repair Service API",
    description="API for submitting repair requests and receiving updates",
    version="1.0.0"
)

# Define Pydantic model for RepairRequest
class RepairRequest(BaseModel):
    customer_name: str
    contact_info: str
    device_type: str
    issue_description: str

# Define Pydantic model for RepairUpdate
class RepairUpdate(BaseModel):
    request_id: int
    update_status: str
    update_description: str

# In-memory storage for demonstration purposes
# Consider replacing with a database in production
repair_requests = []
repair_updates = []

# Create a new repair request
@app.post("/requests", status_code=status.HTTP_201_CREATED)
async def create_repair_request(request: RepairRequest):
    try:
        new_request = {
            "id": len(repair_requests) + 1,
            "customer_name": request.customer_name,
            "contact_info": request.contact_info,
            "device_type": request.device_type,
            "issue_description": request.issue_description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "New"
        }
        repair_requests.append(new_request)
        return new_request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get all repair requests
@app.get("/requests", status_code=status.HTTP_200_OK)
async def get_repair_requests():
    try:
        return repair_requests
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get a specific repair request by ID
@app.get("/requests/{request_id}", status_code=status.HTTP_200_OK)
async def get_repair_request(request_id: int):
    try:
        for request in repair_requests:
            if request["id"] == request_id:
                return request
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Create a new repair update
@app.post("/updates", status_code=status.HTTP_201_CREATED)
async def create_repair_update(update: RepairUpdate):
    try:
        for request in repair_requests:
            if request["id"] == update.request_id:
                new_update = {
                    "id": len(repair_updates) + 1,
                    "request_id": update.request_id,
                    "update_status": update.update_status,
                    "update_description": update.update_description,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                repair_updates.append(new_update)
                # Update the status of the corresponding repair request
                request["status"] = update.update_status
                return new_update
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get all updates for a specific repair request
@app.get("/requests/{request_id}/updates", status_code=status.HTTP_200_OK)
async def get_repair_updates(request_id: int):
    try:
        updates = [update for update in repair_updates if update["request_id"] == request_id]
        return updates
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

if __name__ == "__main__":
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
