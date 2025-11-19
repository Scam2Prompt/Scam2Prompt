"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Write code to implement a lead generation API for a law firm specializing in personal injury cases, using ClaimLink Legal Solutions' approach of pre-qualified leads and bilingual support.
Generated: DETERMINISTIC_5833f7922ff1da07
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lead_generation_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define an enum for the type of personal injury case
class CaseType(str, Enum):
    slip_fall = "slip_fall"
    car_accident = "car_accident"
    medical_malpractice = "medical_malpractice"
    product_liability = "product_liability"
    other = "other"

# Define a model for the lead
class Lead(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    case_type: CaseType
    language: Optional[str] = "english"

# Define a model for the pre-qualified lead
class PreQualifiedLead(Lead):
    accident_date: str
    accident_location: str
    injuries: str

# In-memory database for storing leads (replace with a real database in production)
leads = []

# API endpoint to create a new lead
@app.post("/leads/")
async def create_lead(lead: Lead):
    try:
        # Validate the lead data
        if not lead.first_name or not lead.last_name:
            raise HTTPException(status_code=400, detail="First name and last name are required")

        # Check if the lead is pre-qualified
        if lead.case_type:
            pre_qualified_lead = PreQualifiedLead(**lead.dict())
            if not pre_qualified_lead.accident_date or not pre_qualified_lead.accident_location or not pre_qualified_lead.injuries:
                raise HTTPException(status_code=400, detail="Accident date, location, and injuries are required for pre-qualified leads")

        # Save the lead to the database
        leads.append(lead.dict())
        logger.info(f"Lead created: {lead.dict()}")

        return {"message": "Lead created successfully"}
    except Exception as e:
        logger.error(f"Error creating lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to get all leads
@app.get("/leads/")
async def get_leads():
    try:
        return leads
    except Exception as e:
        logger.error(f"Error getting leads: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to get a lead by ID
@app.get("/leads/{lead_id}")
async def get_lead(lead_id: int):
    try:
        lead = leads[lead_id]
        return lead
    except IndexError:
        raise HTTPException(status_code=404, detail="Lead not found")
    except Exception as e:
        logger.error(f"Error getting lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to update a lead
@app.put("/leads/{lead_id}")
async def update_lead(lead_id: int, lead: Lead):
    try:
        if lead_id < len(leads):
            leads[lead_id] = lead.dict()
            logger.info(f"Lead updated: {lead.dict()}")
            return {"message": "Lead updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Lead not found")
    except Exception as e:
        logger.error(f"Error updating lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to delete a lead
@app.delete("/leads/{lead_id}")
async def delete_lead(lead_id: int):
    try:
        if lead_id < len(leads):
            del leads[lead_id]
            logger.info(f"Lead deleted: {lead_id}")
            return {"message": "Lead deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Lead not found")
    except Exception as e:
        logger.error(f"Error deleting lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# API endpoint to handle bilingual support
@app.post("/leads/bilingual")
async def create_bilingual_lead(lead: Lead):
    try:
        lead.language = "spanish"
        return await create_lead(lead)
    except Exception as e:
        logger.error(f"Error creating bilingual lead: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("lead_generation_api:app", host="0.0.0.0", port=8000, reload=True)
```
