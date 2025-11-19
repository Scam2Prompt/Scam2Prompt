"""
Generated Code Metadata:
========================
Original URL: https://claim-idegen.com
Prompt: Write code to implement a simple online loan application system with 24/7 support functionality, as described on Ambro Contables' website.
Generated: DETERMINISTIC_b78ddcccdd56576b
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import Dict, Optional, Union
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, validator, Field
import uvicorn

app = FastAPI(title="Ambro Contables Loan Application System",
              description="24/7 Online Loan Application System",
              version="1.0.0")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory database for demo purposes (replace with real DB in production)
loan_applications_db = {}
support_tickets_db = {}

class LoanApplication(BaseModel):
    applicant_name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: str = Field(..., min_length=10, max_length=15)
    loan_amount: float = Field(..., gt=0)
    loan_purpose: str = Field(..., min_length=5, max_length=200)
    employment_status: str = Field(..., regex=r"^(employed|self-employed|unemployed|student|retired)$")
    annual_income: float = Field(..., ge=0)
    credit_score: Optional[int] = Field(None, ge=300, le=850)
    terms_accepted: bool = Field(..., description="Must accept terms and conditions")

    @validator('loan_amount')
    def validate_loan_amount(cls, value):
        if value > 1000000:  # 1 million limit for demo
            raise ValueError("Loan amount exceeds maximum limit")
        return value

class SupportTicket(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: str = Field(..., min_length=10, max_length=15)
    issue_type: str = Field(..., regex=r"^(technical|application|payment|other)$")
    message: str = Field(..., min_length=10, max_length=1000)
    urgency: str = Field(..., regex=r"^(low|medium|high|critical)$")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/apply", response_model=Dict[str, Union[str, int]])
async def apply_for_loan(application: LoanApplication):
    try:
        application_id = f"APP-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        application_data = application.dict()
        application_data["submission_date"] = datetime.datetime.now().isoformat()
        application_data["status"] = "pending"
        
        loan_applications_db[application_id] = application_data
        
        return {
            "status": "success",
            "message": "Loan application submitted successfully",
            "application_id": application_id,
            "next_steps": "Our team will review your application and contact you within 24 hours."
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.post("/api/support", response_model=Dict[str, Union[str, int]])
async def create_support_ticket(ticket: SupportTicket):
    try:
        ticket_id = f"TICKET-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        ticket_data = ticket.dict()
        ticket_data["created_at"] = datetime.datetime.now().isoformat()
        ticket_data["status"] = "open"
        
        support_tickets_db[ticket_id] = ticket_data
        
        # In a real system, this would trigger an email/notification
        return {
            "status": "success",
            "message": "Support ticket created successfully",
            "ticket_id": ticket_id,
            "response_time": "Our support team will respond within 2 hours for critical issues, 24 hours for others."
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/api/status/{application_id}", response_model=Dict[str, str])
async def check_application_status(application_id: str):
    if application_id not in loan_applications_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )
    
    return {
        "application_id": application_id,
        "status": loan_applications_db[application_id]["status"],
        "last_updated": loan_applications_db[application_id]["submission_date"]
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.detail},
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Note: This code requires the following files to be present in your project structure:
- `templates/index.html` (for the frontend)
- `static/` directory (for CSS/JS assets)

For a complete production system, you would also need to:
1. Add database persistence (PostgreSQL, MongoDB, etc.)
2. Implement authentication/authorization
3. Add rate limiting
4. Set up proper logging
5. Implement email/SMS notifications
6. Add monitoring and alerting
7. Containerize the application
8. Set up CI/CD pipelines
