"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Create an API endpoint for submitting applications for bridge loans that includes validation for project details and funding requirements.
Generated: DETERMINISTIC_c43cef8ed915adcc
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator, constr
from typing import Optional
import re

app = FastAPI(title="Bridge Loan Application API")

class ProjectDetails(BaseModel):
    project_name: constr(min_length=1, max_length=100)
    location: constr(min_length=1, max_length=100)
    description: constr(min_length=1, max_length=500)
    construction_type: constr(min_length=1, max_length=50)

    @validator('project_name', 'location', 'construction_type')
    def validate_alphanumeric(cls, v):
        if not re.match(r'^[a-zA-Z0-9\s\-.,]+$', v):
            raise ValueError('Field must be alphanumeric with allowed special characters (-.,)')
        return v

class FundingRequirements(BaseModel):
    requested_amount: float
    loan_duration_months: int
    has_collateral: bool
    collateral_details: Optional[str] = None

    @validator('requested_amount')
    def validate_amount(cls, v):
        if v <= 0 or v > 10000000:  # Assuming $10M max
            raise ValueError('Amount must be between $1 and $10,000,000')
        return v

    @validator('loan_duration_months')
    def validate_duration(cls, v):
        if v <= 0 or v > 24:  # Assuming max 24 months
            raise ValueError('Loan duration must be between 1 and 24 months')
        return v

    @validator('collateral_details')
    def validate_collateral_details(cls, v, values):
        if values.get('has_collateral') and not v:
            raise ValueError('Collateral details required when collateral exists')
        return v

class ApplicantDetails(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: str
    phone: constr(min_length=10, max_length=15)

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', v):
            raise ValueError('Invalid email format')
        return v

    @validator('phone')
    def validate_phone(cls, v):
        if not re.match(r'^\+?[0-9\s\-]+$', v):
            raise ValueError('Phone number must contain only digits, spaces, or hyphens')
        return v

class BridgeLoanApplication(BaseModel):
    applicant: ApplicantDetails
    project: ProjectDetails
    funding: FundingRequirements

@app.post("/applications/", status_code=status.HTTP_201_CREATED)
async def submit_application(application: BridgeLoanApplication):
    """
    Submit a bridge loan application with:
    - Applicant details
    - Project details
    - Funding requirements
    
    Validates all input data before accepting application.
    """
    # In production, you would save to database here
    return {
        "message": "Application received successfully",
        "application_id": "app_12345",  # Mock application ID
        "status": "under_review"
    }

@app.get("/applications/{application_id}", status_code=status.HTTP_200_OK)
async def get_application_status(application_id: str):
    """
    Check status of a submitted application
    """
    # In production, you would fetch from database here
    if not re.match(r'^app_\d+$', application_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid application ID format"
        )
    
    # Mock response
    return {
        "application_id": application_id,
        "status": "under_review",
        "last_updated": "2023-11-15T12:00:00Z"
    }
```
