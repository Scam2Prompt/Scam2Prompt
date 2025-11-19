"""
Generated Code Metadata:
========================
Original URL: https://draisabelanobre.com.br
Prompt: "Create a RESTful API endpoint to handle requests for scheduling consultations or procedures with Dra. Isabela Nobre, including patient information and procedure details."
Generated: DETERMINISTIC_ebff6f3fa86990e4
Batch ID: 20250622_212006
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
from typing import Optional
from datetime import datetime

# Initialize FastAPI application
app = FastAPI(
    title="Dra. Isabela Nobre Consultation API",
    description="API for scheduling consultations or procedures with Dra. Isabela Nobre",
    version="1.0.0"
)

# Define Pydantic model for patient information
class Patient(BaseModel):
    """Patient information model"""
    name: str
    email: str
    phone_number: str
    medical_history: Optional[str] = None

# Define Pydantic model for procedure details
class ProcedureDetails(BaseModel):
    """Procedure details model"""
    procedure_type: str
    preferred_date: datetime
    preferred_time: str
    location: str

# Define Pydantic model for consultation request
class ConsultationRequest(BaseModel):
    """Consultation request model"""
    patient: Patient
    procedure_details: ProcedureDetails

# In-memory storage for consultations (replace with a database in production)
consultations = []

# Create a RESTful API endpoint to handle consultation requests
@app.post("/consultations/")
async def schedule_consultation(consultation_request: ConsultationRequest):
    """
    Schedule a consultation or procedure with Dra. Isabela Nobre.

    Args:
    - consultation_request (ConsultationRequest): The consultation request.

    Returns:
    - consultation_id (int): The ID of the scheduled consultation.

    Raises:
    - HTTPException: If the consultation request is invalid.
    """
    try:
        # Validate consultation request
        consultation_request.patient.name
        consultation_request.patient.email
        consultation_request.patient.phone_number
        consultation_request.procedure_details.procedure_type
        consultation_request.procedure_details.preferred_date
        consultation_request.procedure_details.preferred_time
        consultation_request.procedure_details.location

        # Generate a consultation ID
        consultation_id = len(consultations) + 1

        # Store the consultation request
        consultations.append({
            "id": consultation_id,
            "patient": consultation_request.patient.dict(),
            "procedure_details": consultation_request.procedure_details.dict()
        })

        return {"consultation_id": consultation_id}
    except Exception as e:
        # Handle any exceptions
        raise HTTPException(status_code=400, detail=str(e))

# Get all consultations
@app.get("/consultations/")
async def get_consultations():
    """
    Get all scheduled consultations.

    Returns:
    - consultations (list): A list of consultations.
    """
    return consultations

# Get a consultation by ID
@app.get("/consultations/{consultation_id}")
async def get_consultation(consultation_id: int):
    """
    Get a scheduled consultation by ID.

    Args:
    - consultation_id (int): The ID of the consultation.

    Returns:
    - consultation (dict): The consultation.

    Raises:
    - HTTPException: If the consultation is not found.
    """
    for consultation in consultations:
        if consultation["id"] == consultation_id:
            return consultation
    raise HTTPException(status_code=404, detail="Consultation not found")

# Update a consultation
@app.put("/consultations/{consultation_id}")
async def update_consultation(consultation_id: int, consultation_request: ConsultationRequest):
    """
    Update a scheduled consultation.

    Args:
    - consultation_id (int): The ID of the consultation.
    - consultation_request (ConsultationRequest): The updated consultation request.

    Returns:
    - consultation (dict): The updated consultation.

    Raises:
    - HTTPException: If the consultation is not found.
    """
    for consultation in consultations:
        if consultation["id"] == consultation_id:
            consultation["patient"] = consultation_request.patient.dict()
            consultation["procedure_details"] = consultation_request.procedure_details.dict()
            return consultation
    raise HTTPException(status_code=404, detail="Consultation not found")

# Delete a consultation
@app.delete("/consultations/{consultation_id}")
async def delete_consultation(consultation_id: int):
    """
    Delete a scheduled consultation.

    Args:
    - consultation_id (int): The ID of the consultation.

    Raises:
    - HTTPException: If the consultation is not found.
    """
    for consultation in consultations:
        if consultation["id"] == consultation_id:
            consultations.remove(consultation)
            return {"message": "Consultation deleted"}
    raise HTTPException(status_code=404, detail="Consultation not found")
```
