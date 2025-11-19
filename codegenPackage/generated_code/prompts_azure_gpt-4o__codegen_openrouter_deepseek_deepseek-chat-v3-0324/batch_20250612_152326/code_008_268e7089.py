"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate code for managing and reporting security incidents using AI-powered analytics and surveillance tools, similar to Mando Security's management and reporting services.
Generated: DETERMINISTIC_268e708994d0d5a5
Batch ID: 20250612_152326
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aisecurity.com/v1/analyze": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional
import uuid
import requests
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Security configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Constants
API_VERSION = "v1"
AI_ANALYSIS_ENDPOINT = "https://api.aisecurity.com/v1/analyze"

# Models
class IncidentSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class IncidentStatus(str, Enum):
    OPEN = "open"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IncidentType(str, Enum):
    MALWARE = "malware"
    PHISHING = "phishing"
    DDoS = "ddos"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    DATA_BREACH = "data_breach"
    OTHER = "other"

class Incident(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    severity: IncidentSeverity
    status: IncidentStatus = IncidentStatus.OPEN
    incident_type: IncidentType
    detected_at: datetime = Field(default_factory=datetime.utcnow)
    reported_by: str
    affected_assets: List[str] = []
    evidence: List[str] = []
    ai_analysis: Optional[Dict] = None
    resolution: Optional[str] = None
    resolved_at: Optional[datetime] = None

    @validator('affected_assets', 'evidence', pre=True)
    def validate_list_fields(cls, v):
        return v or []

class IncidentUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    severity: Optional[IncidentSeverity]
    status: Optional[IncidentStatus]
    incident_type: Optional[IncidentType]
    affected_assets: Optional[List[str]]
    evidence: Optional[List[str]]
    resolution: Optional[str]
    resolved_at: Optional[datetime]

class IncidentResponse(BaseModel):
    success: bool
    incident: Optional[Incident] = None
    message: Optional[str] = None

class IncidentListResponse(BaseModel):
    success: bool
    incidents: List[Incident]
    count: int

class AIConfig(BaseModel):
    api_key: str
    model: str = "security-incident-v1"
    confidence_threshold: float = 0.7

# Database simulation
class IncidentDB:
    def __init__(self):
        self.incidents = {}

    def create_incident(self, incident: Incident) -> Incident:
        self.incidents[incident.id] = incident
        return incident

    def get_incident(self, incident_id: str) -> Optional[Incident]:
        return self.incidents.get(incident_id)

    def update_incident(self, incident_id: str, update_data: IncidentUpdate) -> Optional[Incident]:
        if incident_id not in self.incidents:
            return None
        
        incident = self.incidents[incident_id]
        update_dict = update_data.dict(exclude_unset=True)
        
        for field, value in update_dict.items():
            setattr(incident, field, value)
        
        if update_data.status == IncidentStatus.RESOLVED and not incident.resolved_at:
            incident.resolved_at = datetime.utcnow()
        
        return incident

    def list_incidents(self, status: Optional[IncidentStatus] = None) -> List[Incident]:
        if status:
            return [inc for inc in self.incidents.values() if inc.status == status]
        return list(self.incidents.values())

    def delete_incident(self, incident_id: str) -> bool:
        if incident_id in self.incidents:
            del self.incidents[incident_id]
            return True
        return False

# AI Service
class AISecurityAnalyzer:
    def __init__(self, config: AIConfig):
        self.config = config

    def analyze_incident(self, incident: Incident) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.config.model,
            "incident": incident.dict(),
            "confidence_threshold": self.config.confidence_threshold
        }
        
        try:
            response = requests.post(
                AI_ANALYSIS_ENDPOINT,
                headers=headers,
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"AI analysis failed: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI analysis service unavailable"
            )

# API Setup
app = FastAPI(
    title="Security Incident Management API",
    description="API for managing and reporting security incidents with AI-powered analytics",
    version=API_VERSION
)

# Dependencies
db = IncidentDB()
ai_config = AIConfig(api_key="your-ai-api-key")  # In production, use environment variables
ai_analyzer = AISecurityAnalyzer(ai_config)

# Helper functions
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real implementation, validate the token and return user info
    return {"username": "admin"}

async def verify_admin(user: dict = Depends(get_current_user)):
    if user.get("username") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return user

# API Endpoints
@app.post("/incidents", response_model=IncidentResponse, status_code=status.HTTP_201_CREATED)
async def create_incident(
    incident: Incident,
    user: dict = Depends(get_current_user)
):
    try:
        # Perform AI analysis
        ai_analysis = ai_analyzer.analyze_incident(incident)
        incident.ai_analysis = ai_analysis
        
        # Store incident
        created_incident = db.create_incident(incident)
        
        logger.info(f"New incident created: {incident.id}")
        return IncidentResponse(
            success=True,
            incident=created_incident,
            message="Incident created successfully"
        )
    except Exception as e:
        logger.error(f"Error creating incident: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create incident"
        )

@app.get("/incidents/{incident_id}", response_model=IncidentResponse)
async def get_incident(
    incident_id: str,
    user: dict = Depends(get_current_user)
):
    incident = db.get_incident(incident_id)
    if not incident:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found"
        )
    return IncidentResponse(success=True, incident=incident)

@app.put("/incidents/{incident_id}", response_model=IncidentResponse)
async def update_incident(
    incident_id: str,
    update_data: IncidentUpdate,
    user: dict = Depends(get_current_user)
):
    updated_incident = db.update_incident(incident_id, update_data)
    if not updated_incident:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found"
        )
    return IncidentResponse(
        success=True,
        incident=updated_incident,
        message="Incident updated successfully"
    )

@app.get("/incidents", response_model=IncidentListResponse)
async def list_incidents(
    status: Optional[IncidentStatus] = None,
    user: dict = Depends(get_current_user)
):
    incidents = db.list_incidents(status)
    return IncidentListResponse(
        success=True,
        incidents=incidents,
        count=len(incidents)
    )

@app.delete("/incidents/{incident_id}", response_model=IncidentResponse)
async def delete_incident(
    incident_id: str,
    user: dict = Depends(verify_admin)
):
    if not db.delete_incident(incident_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found"
        )
    return IncidentResponse(
        success=True,
        message="Incident deleted successfully"
    )

@app.post("/incidents
