"""
Generated Code Metadata:
========================
Original URL: https://legatoltd.net
Prompt: Develop a system for integrating legal case management with international law enforcement agencies, similar to The Legato's collaboration with Georgiou&Sterling WRS.
Generated: DETERMINISTIC_8db858d5b412e82b
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
import logging
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status, Security
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Security
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Enums
class CaseStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"

class Jurisdiction(str, Enum):
    US = "US"
    EU = "EU"
    UK = "UK"
    INTERPOL = "INTERPOL"
    OTHER = "OTHER"

# Models
class Agency(BaseModel):
    id: str
    name: str
    jurisdiction: Jurisdiction
    api_endpoint: str
    api_key: str
    is_active: bool = True

class Case(BaseModel):
    id: str
    title: str
    description: str
    status: CaseStatus
    jurisdiction: Jurisdiction
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    agencies_involved: List[str] = []
    documents: List[str] = []

    @validator('updated_at', pre=True, always=True)
    def update_timestamp(cls, v, values):
        return datetime.now()

class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[CaseStatus] = None
    jurisdiction: Optional[Jurisdiction] = None
    agencies_involved: Optional[List[str]] = None
    documents: Optional[List[str]] = None

class Document(BaseModel):
    id: str
    case_id: str
    name: str
    content_type: str
    size: int
    url: str
    uploaded_at: datetime = datetime.now()

# Database (simulated)
db = {
    "agencies": {},
    "cases": {},
    "documents": {},
    "api_keys": {}
}

# App
app = FastAPI(
    title="International Case Management System",
    description="System for integrating legal case management with international law enforcement agencies",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utils
def get_agency(agency_id: str) -> Agency:
    if agency_id not in db["agencies"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agency not found"
        )
    return Agency(**db["agencies"][agency_id])

def get_case(case_id: str) -> Case:
    if case_id not in db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    return Case(**db["cases"][case_id])

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key not in db["api_keys"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key

# API Endpoints
@app.post("/agencies/", status_code=status.HTTP_201_CREATED)
async def register_agency(agency: Agency, api_key: str = Security(verify_api_key)):
    if agency.id in db["agencies"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Agency already exists"
        )
    db["agencies"][agency.id] = agency.dict()
    logger.info(f"Agency registered: {agency.id}")
    return {"message": "Agency registered successfully"}

@app.get("/agencies/{agency_id}", response_model=Agency)
async def get_agency_details(agency_id: str, api_key: str = Security(verify_api_key)):
    return get_agency(agency_id)

@app.post("/cases/", status_code=status.HTTP_201_CREATED, response_model=Case)
async def create_case(case: Case, api_key: str = Security(verify_api_key)):
    if case.id in db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Case ID already exists"
        )
    db["cases"][case.id] = case.dict()
    logger.info(f"Case created: {case.id}")
    return case

@app.get("/cases/{case_id}", response_model=Case)
async def get_case_details(case_id: str, api_key: str = Security(verify_api_key)):
    return get_case(case_id)

@app.patch("/cases/{case_id}", response_model=Case)
async def update_case(
    case_id: str,
    case_update: CaseUpdate,
    api_key: str = Security(verify_api_key)
):
    case = get_case(case_id)
    update_data = case_update.dict(exclude_unset=True)
    updated_case = case.copy(update=update_data)
    db["cases"][case_id] = updated_case.dict()
    logger.info(f"Case updated: {case_id}")
    return updated_case

@app.post("/cases/{case_id}/share/{agency_id}", response_model=Case)
async def share_case_with_agency(
    case_id: str,
    agency_id: str,
    api_key: str = Security(verify_api_key)
):
    case = get_case(case_id)
    agency = get_agency(agency_id)
    
    if agency_id in case.agencies_involved:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Case already shared with this agency"
        )
    
    # Notify agency via their API
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {agency.api_key}"
        }
        payload = {
            "case_id": case_id,
            "title": case.title,
            "jurisdiction": case.jurisdiction.value
        }
        response = requests.post(
            f"{agency.api_endpoint}/cases/notify",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Failed to notify agency {agency_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to notify agency"
        )
    
    # Update case
    updated_agencies = case.agencies_involved + [agency_id]
    updated_case = case.copy(update={"agencies_involved": updated_agencies})
    db["cases"][case_id] = updated_case.dict()
    
    logger.info(f"Case {case_id} shared with agency {agency_id}")
    return updated_case

@app.post("/documents/", status_code=status.HTTP_201_CREATED, response_model=Document)
async def upload_document(document: Document, api_key: str = Security(verify_api_key)):
    if document.id in db["documents"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Document ID already exists"
        )
    if document.case_id not in db["cases"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    db["documents"][document.id] = document.dict()
    
    # Update case with document reference
    case = get_case(document.case_id)
    updated_documents = case.documents + [document.id]
    updated_case = case.copy(update={"documents": updated_documents})
    db["cases"][document.case_id] = updated_case.dict()
    
    logger.info(f"Document uploaded: {document.id} for case {document.case_id}")
    return document

@app.get("/documents/{document_id}", response_model=Document)
async def get_document(document_id: str, api_key: str = Security(verify_api_key)):
    if document_id not in db["documents"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    return Document(**db["documents"][document_id])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
