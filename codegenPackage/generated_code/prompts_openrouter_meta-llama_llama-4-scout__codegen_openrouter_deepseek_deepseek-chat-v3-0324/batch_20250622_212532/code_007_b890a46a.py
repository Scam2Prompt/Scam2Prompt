"""
Generated Code Metadata:
========================
Original URL: https://spectre-group.limited
Prompt: Design an active bug bounty program similar to Spectre Group Limited's, including guidelines for identifying vulnerabilities in web applications and APIs.
Generated: DETERMINISTIC_b890a46ac2d66b50
Batch ID: 20250622_212532
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bug Bounty Program Implementation
Inspired by Spectre Group Limited's model
"""

import json
import logging
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, validator, HttpUrl, EmailStr
from fastapi import FastAPI, HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
API_KEY = "your-secure-api-key-here"
BOUNTY_PROGRAM_NAME = "Spectre Bug Bounty Program"
VERSION = "1.0.0"

# Security
security = HTTPBearer()

# Models
class SeverityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class VulnerabilityType(str, Enum):
    SQL_INJECTION = "sql_injection"
    XSS = "cross_site_scripting"
    CSRF = "cross_site_request_forgery"
    RCE = "remote_code_execution"
    IDOR = "insecure_direct_object_reference"
    SSRF = "server_side_request_forgery"
    XXE = "xml_external_entity"
    AUTH_BYPASS = "authentication_bypass"
    INFO_DISCLOSURE = "information_disclosure"
    OTHER = "other"

class VulnerabilityReport(BaseModel):
    title: str
    description: str
    steps_to_reproduce: str
    impact: str
    severity: SeverityLevel
    vulnerability_type: VulnerabilityType
    affected_urls: List[HttpUrl]
    proof_of_concept: Optional[str] = None
    reporter_name: Optional[str] = None
    reporter_email: EmailStr
    date_reported: datetime = datetime.now()

    @validator('affected_urls')
    def validate_affected_urls(cls, v):
        if not v:
            raise ValueError("At least one affected URL must be provided")
        return v

class BountyPayment(BaseModel):
    report_id: str
    amount: float
    currency: str = "USD"
    payment_date: datetime = datetime.now()
    transaction_id: str

class ProgramStatus(BaseModel):
    active: bool = True
    last_updated: datetime = datetime.now()
    total_reports: int = 0
    total_paid: float = 0.0
    avg_response_time: float = 0.0

# Database simulation
class Database:
    def __init__(self):
        self.reports = {}
        self.payments = {}
        self.status = ProgramStatus()

db = Database()

# FastAPI app
app = FastAPI(
    title=BOUNTY_PROGRAM_NAME,
    description="A secure bug bounty program for identifying vulnerabilities in web applications and APIs",
    version=VERSION
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper functions
def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return credentials.credentials

def calculate_bounty(severity: SeverityLevel) -> float:
    bounty_table = {
        SeverityLevel.LOW: 100.0,
        SeverityLevel.MEDIUM: 500.0,
        SeverityLevel.HIGH: 2000.0,
        SeverityLevel.CRITICAL: 10000.0
    }
    return bounty_table.get(severity, 0.0)

# API Endpoints
@app.post("/submit-report", response_model=VulnerabilityReport)
async def submit_report(report: VulnerabilityReport, request: Request):
    """
    Submit a new vulnerability report to the bug bounty program.
    """
    report_id = f"REPORT-{datetime.now().timestamp()}"
    db.reports[report_id] = report
    db.status.total_reports += 1
    logger.info(f"New report submitted: {report_id}")
    return report

@app.get("/report/{report_id}", response_model=VulnerabilityReport)
async def get_report(report_id: str, api_key: str = Depends(verify_api_key)):
    """
    Retrieve a specific vulnerability report by ID.
    """
    if report_id not in db.reports:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    return db.reports[report_id]

@app.post("/process-bounty/{report_id}")
async def process_bounty(report_id: str, api_key: str = Depends(verify_api_key)):
    """
    Process bounty payment for a validated vulnerability report.
    """
    if report_id not in db.reports:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    
    report = db.reports[report_id]
    bounty_amount = calculate_bounty(report.severity)
    
    payment = BountyPayment(
        report_id=report_id,
        amount=bounty_amount,
        transaction_id=f"TX-{datetime.now().timestamp()}"
    )
    
    db.payments[report_id] = payment
    db.status.total_paid += bounty_amount
    logger.info(f"Bounty processed for report {report_id}: ${bounty_amount}")
    
    return {"status": "success", "amount": bounty_amount}

@app.get("/program-status", response_model=ProgramStatus)
async def get_program_status():
    """
    Get current status of the bug bounty program.
    """
    return db.status

@app.get("/guidelines")
async def get_guidelines():
    """
    Returns the vulnerability reporting guidelines.
    """
    guidelines = {
        "scope": {
            "in_scope": [
                "All web applications under *.example.com",
                "Public APIs (api.example.com)",
                "Mobile application APIs"
            ],
            "out_of_scope": [
                "Physical security issues",
                "Social engineering attacks",
                "Denial of Service (DoS) vulnerabilities"
            ]
        },
        "testing_guidelines": [
            "Avoid testing on production data",
            "Do not impact other users with your testing",
            "Do not perform automated scanning without prior approval",
            "Respect rate limits and do not spam endpoints"
        ],
        "vulnerability_types": [
            {"type": "SQL Injection", "severity": SeverityLevel.CRITICAL},
            {"type": "Cross-Site Scripting (XSS)", "severity": SeverityLevel.HIGH},
            {"type": "Authentication Bypass", "severity": SeverityLevel.CRITICAL},
            {"type": "Sensitive Data Exposure", "severity": SeverityLevel.HIGH},
            {"type": "CSRF", "severity": SeverityLevel.MEDIUM},
            {"type": "SSRF", "severity": SeverityLevel.HIGH},
            {"type": "XXE", "severity": SeverityLevel.CRITICAL},
            {"type": "IDOR", "severity": SeverityLevel.MEDIUM}
        ],
        "reporting_requirements": [
            "Detailed description of the vulnerability",
            "Steps to reproduce",
            "Impact analysis",
            "Proof of concept (if possible)",
            "Suggested remediation"
        ],
        "legal_terms": [
            "You must comply with all applicable laws",
            "Do not disclose vulnerabilities publicly before we've fixed them",
            "We reserve the right to reject reports that don't follow guidelines"
        ]
    }
    return JSONResponse(content=guidelines)

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred"},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
