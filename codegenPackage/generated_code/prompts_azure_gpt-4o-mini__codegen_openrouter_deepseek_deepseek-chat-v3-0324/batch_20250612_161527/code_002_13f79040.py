"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: Create a REST API endpoint for handling civil and commercial litigation cases, inspired by the adversarial proceedings services provided by Ramdays.
Generated: DETERMINISTIC_13f79040a9e0f519
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Ramdays Litigation Case Management API",
    description="REST API for handling civil and commercial litigation cases",
    version="1.0.0"
)

# Database simulation
cases_db = []

# Models
class Party(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    type: str  # e.g., plaintiff, defendant, third-party
    contact_info: Optional[str] = None

class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: Optional[str] = None
    upload_date: datetime = Field(default_factory=datetime.now)
    file_url: str

class Hearing(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    date: datetime
    location: str
    purpose: str
    outcome: Optional[str] = None

class Case(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    case_number: str
    title: str
    description: str
    jurisdiction: str
    case_type: str  # civil or commercial
    filing_date: datetime = Field(default_factory=datetime.now)
    status: str = "pending"  # pending, active, settled, dismissed, appealed
    parties: List[Party] = []
    documents: List[Document] = []
    hearings: List[Hearing] = []
    notes: Optional[str] = None

class CaseCreate(BaseModel):
    case_number: str
    title: str
    description: str
    jurisdiction: str
    case_type: str

class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None

# Helper functions
def find_case(case_id: str):
    for case in cases_db:
        if case.id == case_id:
            return case
    return None

# Endpoints
@app.post("/cases/", response_model=Case, status_code=status.HTTP_201_CREATED)
async def create_case(case_data: CaseCreate):
    """Create a new litigation case"""
    try:
        new_case = Case(**case_data.dict())
        cases_db.append(new_case)
        logger.info(f"Created new case: {new_case.id}")
        return new_case
    except Exception as e:
        logger.error(f"Error creating case: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create case"
        )

@app.get("/cases/", response_model=List[Case])
async def get_cases(status_filter: Optional[str] = None, case_type: Optional[str] = None):
    """Get all cases with optional filtering"""
    try:
        filtered_cases = cases_db
        
        if status_filter:
            filtered_cases = [case for case in filtered_cases if case.status.lower() == status_filter.lower()]
        
        if case_type:
            filtered_cases = [case for case in filtered_cases if case.case_type.lower() == case_type.lower()]
        
        return filtered_cases
    except Exception as e:
        logger.error(f"Error retrieving cases: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve cases"
        )

@app.get("/cases/{case_id}", response_model=Case)
async def get_case(case_id: str):
    """Get a specific case by ID"""
    case = find_case(case_id)
    if not case:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Case not found"
        )
    return case

@app.put("/cases/{case_id}", response_model=Case)
async def update_case(case_id: str, case_data: CaseUpdate):
    """Update case information"""
    try:
        case = find_case(case_id)
        if not case:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Case not found"
            )
        
        update_data = case_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(case, field, value)
        
        logger.info(f"Updated case: {case_id}")
        return case
    except Exception as e:
        logger.error(f"Error updating case {case_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update case"
        )

@app.delete("/cases/{case_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_case(case_id: str):
    """Delete a case"""
    try:
        global cases_db
        case = find_case(case_id)
        if not case:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Case not found"
            )
        
        cases_db = [case for case in cases_db if case.id != case_id]
        logger.info(f"Deleted case: {case_id}")
    except Exception as e:
        logger.error(f"Error deleting case {case_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete case"
        )

@app.post("/cases/{case_id}/parties/", response_model=Case)
async def add_party(case_id: str, party: Party):
    """Add a party to a case"""
    try:
        case = find_case(case_id)
        if not case:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Case not found"
            )
        
        case.parties.append(party)
        logger.info(f"Added party {party.id} to case {case_id}")
        return case
    except Exception as e:
        logger.error(f"Error adding party to case {case_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add party"
        )

@app.post("/cases/{case_id}/documents/", response_model=Case)
async def add_document(case_id: str, document: Document):
    """Add a document to a case"""
    try:
        case = find_case(case_id)
        if not case:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Case not found"
            )
        
        case.documents.append(document)
        logger.info(f"Added document {document.id} to case {case_id}")
        return case
    except Exception as e:
        logger.error(f"Error adding document to case {case_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add document"
        )

@app.post("/cases/{case_id}/hearings/", response_model=Case)
async def schedule_hearing(case_id: str, hearing: Hearing):
    """Schedule a hearing for a case"""
    try:
        case = find_case(case_id)
        if not case:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Case not found"
            )
        
        case.hearings.append(hearing)
        logger.info(f"Scheduled hearing {hearing.id} for case {case_id}")
        return case
    except Exception as e:
        logger.error(f"Error scheduling hearing for case {case_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to schedule hearing"
        )
```
