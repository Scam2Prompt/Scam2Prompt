"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Suggest an API for implementing a virtual consultation system that provides advice on therapies like "De-addiction Therapy," "Anger Management," and "Anxiety Management," based on the Green Apples e-Rx Clinic's services.
Generated: DETERMINISTIC_f5b2c0c032ab8cca
Batch ID: 20250612_153224
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
from typing import Optional, List
from enum import Enum

app = FastAPI(
    title="Green Apples e-Rx Virtual Consultation API",
    description="API for virtual consultations on therapies like De-addiction, Anger Management, and Anxiety Management",
    version="1.0.0"
)

class TherapyType(str, Enum):
    DE_ADDICTION = "De-addiction Therapy"
    ANGER_MANAGEMENT = "Anger Management"
    ANXIETY_MANAGEMENT = "Anxiety Management"

class ConsultationRequest(BaseModel):
    therapy_type: TherapyType
    patient_id: str
    symptoms: List[str]
    additional_notes: Optional[str] = None

class TherapyAdvice(BaseModel):
    therapy_type: TherapyType
    advice: str
    recommended_sessions: int
    resources: List[str]

class ErrorResponse(BaseModel):
    detail: str

# Mock database of therapy advice
THERAPY_ADVICE_DB = {
    TherapyType.DE_ADDICTION: {
        "advice": "Begin with cognitive behavioral therapy and consider support groups. Avoid triggers.",
        "recommended_sessions": 12,
        "resources": [
            "NA Meeting Locator",
            "Cognitive Behavioral Therapy Workbook"
        ]
    },
    TherapyType.ANGER_MANAGEMENT: {
        "advice": "Practice relaxation techniques and communication skills. Identify triggers early.",
        "recommended_sessions": 8,
        "resources": [
            "Anger Management Workbook",
            "Mindfulness Meditation Guide"
        ]
    },
    TherapyType.ANXIETY_MANAGEMENT: {
        "advice": "Combine exposure therapy with mindfulness exercises. Consider gradual exposure to triggers.",
        "recommended_sessions": 10,
        "resources": [
            "Anxiety Relief Workbook",
            "Breathing Exercise Videos"
        ]
    }
}

@app.post(
    "/consult",
    response_model=TherapyAdvice,
    responses={
        404: {"model": ErrorResponse, "description": "Therapy type not found"},
        422: {"model": ErrorResponse, "description": "Validation error"}
    }
)
async def get_therapy_advice(consultation: ConsultationRequest):
    """
    Get personalized therapy advice based on consultation request.
    """
    if consultation.therapy_type not in THERAPY_ADVICE_DB:
        raise HTTPException(
            status_code=404,
            detail=f"Therapy type {consultation.therapy_type} not supported"
        )
    
    advice_data = THERAPY_ADVICE_DB[consultation.therapy_type]
    return TherapyAdvice(
        therapy_type=consultation.therapy_type,
        advice=advice_data["advice"],
        recommended_sessions=advice_data["recommended_sessions"],
        resources=advice_data["resources"]
    )

@app.get("/therapies", response_model=List[TherapyType])
async def list_available_therapies():
    """
    Get list of all available therapy types.
    """
    return list(TherapyType)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
