"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Generate a sample API design for a reporting and analytics system tailored to enterprise needs, inspired by MetaCode's focus on reportability and decision-making improvements.
Generated: DETERMINISTIC_e70b02fec6a4d533
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# reporting_analytics_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Reporting and Analytics API",
    description="API for reporting and analytics system tailored to enterprise needs",
    version="1.0.0"
)

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define user model
class User(BaseModel):
    id: int
    username: str
    email: str

# Define report model
class Report(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    data: dict

# Define report creation model
class CreateReport(BaseModel):
    title: str
    description: str
    data: dict

# In-memory user and report storage (replace with database in production)
users: List[User] = [
    User(id=1, username="admin", email="admin@example.com")
]

reports: List[Report] = []

# Authentication
async def get_current_user(token: str = Depends(oauth2_scheme)):
    for user in users:
        if user.username == token:
            return user
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Token endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in users:
        if user.username == form_data.username and user.username == form_data.password:
            return {"access_token": user.username, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Reports endpoint
@app.get("/reports/")
async def read_reports(current_user: User = Depends(get_current_user)):
    return reports

# Report creation endpoint
@app.post("/reports/")
async def create_report(report: CreateReport, current_user: User = Depends(get_current_user)):
    new_report = Report(
        id=len(reports) + 1,
        title=report.title,
        description=report.description,
        created_at=datetime.now(),
        data=report.data
    )
    reports.append(new_report)
    return new_report

# Report details endpoint
@app.get("/reports/{report_id}")
async def read_report(report_id: int, current_user: User = Depends(get_current_user)):
    for report in reports:
        if report.id == report_id:
            return report
    raise HTTPException(status_code=404, detail="Report not found")

# Report update endpoint
@app.put("/reports/{report_id}")
async def update_report(report_id: int, report: CreateReport, current_user: User = Depends(get_current_user)):
    for existing_report in reports:
        if existing_report.id == report_id:
            existing_report.title = report.title
            existing_report.description = report.description
            existing_report.data = report.data
            return existing_report
    raise HTTPException(status_code=404, detail="Report not found")

# Report deletion endpoint
@app.delete("/reports/{report_id}")
async def delete_report(report_id: int, current_user: User = Depends(get_current_user)):
    for report in reports:
        if report.id == report_id:
            reports.remove(report)
            return {"message": "Report deleted"}
    raise HTTPException(status_code=404, detail="Report not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
