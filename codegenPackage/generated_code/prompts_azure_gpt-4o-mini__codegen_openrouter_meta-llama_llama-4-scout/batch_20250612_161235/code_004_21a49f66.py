"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: Create a sample API that allows users to book consultations for creative services, reflecting the user experience principles highlighted by Swell Creative Management.
Generated: DETERMINISTIC_21a49f66a020313e
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultation_api.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Creative Services Consultation API",
    description="API for booking consultations for creative services",
    version="1.0.0",
)

# Define the ConsultationRequest model
class ConsultationRequest(BaseModel):
    """Request model for consultation booking"""
    name: str
    email: str
    service: str
    date: str
    time: str
    description: str

# Define the ConsultationResponse model
class ConsultationResponse(BaseModel):
    """Response model for consultation booking"""
    id: int
    name: str
    email: str
    service: str
    date: str
    time: str
    description: str

# In-memory consultation storage (replace with a database in production)
consultations = []
next_consultation_id = 1

# Create a consultation endpoint
@app.post("/consultations", response_model=ConsultationResponse, status_code=status.HTTP_201_CREATED)
async def create_consultation(request: ConsultationRequest):
    global next_consultation_id
    try:
        # Validate date and time
        datetime.strptime(request.date, "%Y-%m-%d")
        datetime.strptime(request.time, "%H:%M")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid date or time format")

    # Create a new consultation
    consultation = ConsultationResponse(
        id=next_consultation_id,
        name=request.name,
        email=request.email,
        service=request.service,
        date=request.date,
        time=request.time,
        description=request.description,
    )
    consultations.append(consultation)
    next_consultation_id += 1
    return consultation

# Get all consultations endpoint
@app.get("/consultations", response_model=List[ConsultationResponse])
async def get_consultations():
    return consultations

# Get a consultation by ID endpoint
@app.get("/consultations/{consultation_id}", response_model=ConsultationResponse)
async def get_consultation(consultation_id: int):
    for consultation in consultations:
        if consultation.id == consultation_id:
            return consultation
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")

# Update a consultation endpoint
@app.put("/consultations/{consultation_id}", response_model=ConsultationResponse)
async def update_consultation(consultation_id: int, request: ConsultationRequest):
    for consultation in consultations:
        if consultation.id == consultation_id:
            try:
                # Validate date and time
                datetime.strptime(request.date, "%Y-%m-%d")
                datetime.strptime(request.time, "%H:%M")
            except ValueError:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid date or time format")

            # Update the consultation
            consultation.name = request.name
            consultation.email = request.email
            consultation.service = request.service
            consultation.date = request.date
            consultation.time = request.time
            consultation.description = request.description
            return consultation
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")

# Delete a consultation endpoint
@app.delete("/consultations/{consultation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_consultation(consultation_id: int):
    for consultation in consultations:
        if consultation.id == consultation_id:
            consultations.remove(consultation)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found")
```
