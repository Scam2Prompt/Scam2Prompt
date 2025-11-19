"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Create a RESTful API specification for a home healthcare service that includes endpoints for booking medical consultations and ambulance requests.
Generated: DETERMINISTIC_c09326e67a77d41c
Batch ID: 20250612_160526
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
from typing import Optional

app = FastAPI(
    title="Home Healthcare Service API",
    description="API for booking medical consultations and ambulance requests",
    version="1.0.0",
)

# Define a model for the medical consultation request
class ConsultationRequest(BaseModel):
    patient_name: str
    patient_contact: str
    doctor_specialty: str
    consultation_date: str
    consultation_time: str

# Define a model for the ambulance request
class AmbulanceRequest(BaseModel):
    patient_name: str
    patient_contact: str
    pickup_location: str
    destination: str
    emergency_level: str

# In-memory storage for demonstration purposes
consultation_requests = []
ambulance_requests = []

# Endpoint to book a medical consultation
@app.post("/consultations", status_code=status.HTTP_201_CREATED)
async def book_consultation(request: ConsultationRequest):
    try:
        consultation_requests.append(request.dict())
        return {"message": "Consultation booked successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get all consultation requests
@app.get("/consultations", status_code=status.HTTP_200_OK)
async def get_consultations():
    try:
        return consultation_requests
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to book an ambulance
@app.post("/ambulances", status_code=status.HTTP_201_CREATED)
async def book_ambulance(request: AmbulanceRequest):
    try:
        ambulance_requests.append(request.dict())
        return {"message": "Ambulance requested successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to get all ambulance requests
@app.get("/ambulances", status_code=status.HTTP_200_OK)
async def get_ambulances():
    try:
        return ambulance_requests
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to cancel a consultation request
@app.delete("/consultations/{consultation_id}", status_code=status.HTTP_200_OK)
async def cancel_consultation(consultation_id: int):
    try:
        if consultation_id < len(consultation_requests):
            del consultation_requests[consultation_id]
            return {"message": "Consultation cancelled successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Endpoint to cancel an ambulance request
@app.delete("/ambulances/{ambulance_id}", status_code=status.HTTP_200_OK)
async def cancel_ambulance(ambulance_id: int):
    try:
        if ambulance_id < len(ambulance_requests):
            del ambulance_requests[ambulance_id]
            return {"message": "Ambulance request cancelled successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ambulance request not found")
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
# Run using: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
