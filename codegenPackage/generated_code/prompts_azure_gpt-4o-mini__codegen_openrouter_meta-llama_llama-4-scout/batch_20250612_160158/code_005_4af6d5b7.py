"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Construct a RESTful API endpoint that provides tailored funding options for property finance based on user input regarding project type and funding needs.
Generated: DETERMINISTIC_4af6d5b72b597e50
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Property Finance API",
    description="Provides tailored funding options for property finance",
    version="1.0.0"
)

class FundingOption(BaseModel):
    """Represents a funding option"""
    name: str
    interest_rate: float
    loan_term: int

class ProjectDetails(BaseModel):
    """Represents project details"""
    project_type: str
    funding_needs: float

class FundingResponse(BaseModel):
    """Represents funding response"""
    funding_options: List[FundingOption]

# In-memory data store for demonstration purposes
# Replace with a database connection in production
funding_options_data = {
    "residential": [
        FundingOption(name="Mortgage", interest_rate=3.5, loan_term=25),
        FundingOption(name="Home Equity Loan", interest_rate=4.5, loan_term=15)
    ],
    "commercial": [
        FundingOption(name="Commercial Mortgage", interest_rate=4.0, loan_term=20),
        FundingOption(name="Business Loan", interest_rate=5.0, loan_term=10)
    ]
}

@app.post("/funding-options", response_model=FundingResponse)
async def get_funding_options(project_details: ProjectDetails):
    """
    Provides tailored funding options based on project type and funding needs.

    Args:
    - project_details (ProjectDetails): Project type and funding needs

    Returns:
    - funding_response (FundingResponse): List of funding options
    """
    try:
        project_type = project_details.project_type.lower()
        if project_type not in funding_options_data:
            raise HTTPException(status_code=400, detail="Invalid project type")

        funding_needs = project_details.funding_needs
        if funding_needs <= 0:
            raise HTTPException(status_code=400, detail="Funding needs must be greater than zero")

        funding_options = funding_options_data[project_type]
        # Filter funding options based on funding needs (example: only show options with loan term > 10 years)
        filtered_funding_options = [option for option in funding_options if option.loan_term > 10]

        return FundingResponse(funding_options=filtered_funding_options)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# test_app.py

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_funding_options_valid_input():
    project_details = {
        "project_type": "residential",
        "funding_needs": 100000.0
    }
    response = client.post("/funding-options", json=project_details)
    assert response.status_code == 200
    assert len(response.json()["funding_options"]) > 0

def test_get_funding_options_invalid_project_type():
    project_details = {
        "project_type": "invalid",
        "funding_needs": 100000.0
    }
    response = client.post("/funding-options", json=project_details)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid project type"

def test_get_funding_options_invalid_funding_needs():
    project_details = {
        "project_type": "residential",
        "funding_needs": -100000.0
    }
    response = client.post("/funding-options", json=project_details)
    assert response.status_code == 400
    assert response.json()["detail"] == "Funding needs must be greater than zero"

def test_get_funding_options_internal_server_error():
    # Simulate internal server error
    project_details = {
        "project_type": "residential",
        "funding_needs": None
    }
    response = client.post("/funding-options", json=project_details)
    assert response.status_code == 500
```

### Run the application
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Run tests
```bash
pytest test_app.py
```
