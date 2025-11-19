"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Develop an API that integrates patient health data (oral health, digestive health, and emotional well-being) for a clinic like Jané Clinic, enabling personalized treatment recommendations.
Generated: DETERMINISTIC_fc1d10b6fd72746e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import logging
from datetime import date

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Jané Clinic Health Data API",
    description="API for integrating patient health data and providing personalized treatment recommendations",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
patients_db = {}
treatments_db = {}

class HealthCategory(str, Enum):
    ORAL = "oral"
    DIGESTIVE = "digestive"
    EMOTIONAL = "emotional"

class HealthMetric(BaseModel):
    category: HealthCategory
    name: str
    value: float
    date_recorded: date
    notes: Optional[str] = None

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    health_metrics: List[HealthMetric] = []
    medical_history: Optional[List[str]] = None
    allergies: Optional[List[str]] = None

class TreatmentRecommendation(BaseModel):
    patient_id: str
    recommendations: List[str]
    rationale: str
    priority: int = Field(ge=1, le=3, description="Priority level from 1 (high) to 3 (low)")

@app.post("/patients/", response_model=Patient, status_code=201)
async def create_patient(patient: Patient):
    """Create a new patient record"""
    if patient.id in patients_db:
        raise HTTPException(status_code=400, detail="Patient ID already exists")
    patients_db[patient.id] = patient
    logger.info(f"Created patient record for {patient.name}")
    return patient

@app.get("/patients/{patient_id}", response_model=Patient)
async def get_patient(patient_id: str):
    """Retrieve a patient's record"""
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients_db[patient_id]

@app.post("/patients/{patient_id}/metrics", response_model=Patient)
async def add_health_metric(patient_id: str, metric: HealthMetric):
    """Add a health metric to a patient's record"""
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient = patients_db[patient_id]
    patient.health_metrics.append(metric)
    logger.info(f"Added {metric.category} health metric for patient {patient_id}")
    return patient

@app.get("/patients/{patient_id}/recommendations", response_model=TreatmentRecommendation)
async def get_treatment_recommendations(patient_id: str):
    """Generate personalized treatment recommendations based on health data"""
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient = patients_db[patient_id]
    recommendations = []
    rationale = ""

    # Analyze oral health
    oral_metrics = [m for m in patient.health_metrics if m.category == HealthCategory.ORAL]
    if oral_metrics:
        avg_oral_score = sum(m.value for m in oral_metrics) / len(oral_metrics)
        if avg_oral_score < 5:
            recommendations.append("Schedule dental cleaning and examination")
            rationale += "Low oral health score detected. "

    # Analyze digestive health
    digestive_metrics = [m for m in patient.health_metrics if m.category == HealthCategory.DIGESTIVE]
    if digestive_metrics:
        avg_digestive_score = sum(m.value for m in digestive_metrics) / len(digestive_metrics)
        if avg_digestive_score < 4:
            recommendations.append("Consult with gastroenterologist")
            rationale += "Digestive health concerns identified. "

    # Analyze emotional well-being
    emotional_metrics = [m for m in patient.health_metrics if m.category == HealthCategory.EMOTIONAL]
    if emotional_metrics:
        avg_emotional_score = sum(m.value for m in emotional_metrics) / len(emotional_metrics)
        if avg_emotional_score < 3:
            recommendations.append("Recommend counseling or therapy session")
            rationale += "Emotional well-being indicators suggest support may be beneficial. "

    if not recommendations:
        recommendations.append("No specific recommendations at this time")
        rationale = "All health indicators within normal ranges"

    treatment = TreatmentRecommendation(
        patient_id=patient_id,
        recommendations=recommendations,
        rationale=rationale,
        priority=1 if "emergency" in rationale.lower() else 2
    )
    
    treatments_db[patient_id] = treatment
    return treatment

@app.get("/treatments/{patient_id}", response_model=TreatmentRecommendation)
async def get_treatment(patient_id: str):
    """Retrieve treatment recommendations for a patient"""
    if patient_id not in treatments_db:
        raise HTTPException(status_code=404, detail="No treatment recommendations found for this patient")
    return treatments_db[patient_id]

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handle unexpected errors"""
    logger.error(f"Unexpected error: {exc}")
    return HTTPException(status_code=500, detail="Internal server error")

# For production, you would add:
# - Authentication middleware
# - Rate limiting
# - Database connection pooling
# - Proper configuration management
# - Monitoring and metrics endpoints
```
