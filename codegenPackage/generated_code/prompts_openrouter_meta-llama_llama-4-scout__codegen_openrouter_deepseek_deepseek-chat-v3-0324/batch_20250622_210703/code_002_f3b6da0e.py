"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: "Design a mobile application for managers to access real-time business performance indicators and reports using the Solpen Gerencial tool."
Generated: DETERMINISTIC_f3b6da0e486b3575
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solpen_gerencial_app.py
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="Solpen Gerencial Mobile API",
    description="API for mobile access to Solpen Gerencial business performance indicators",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
fake_users_db = {
    "manager1": {
        "username": "manager1",
        "full_name": "John Doe",
        "email": "john@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    }
}

# Models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class PerformanceIndicator(BaseModel):
    id: str
    name: str
    value: float
    target: float
    unit: str
    trend: str  # 'up', 'down', 'neutral'
    last_updated: datetime

class Report(BaseModel):
    id: str
    title: str
    type: str  # 'financial', 'operational', 'sales', etc.
    period: str  # 'daily', 'weekly', 'monthly'
    content: Dict
    generated_at: datetime

class ReportRequest(BaseModel):
    report_type: str
    period: str
    filters: Optional[Dict] = None

# Utility functions
def fake_hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Mock data for indicators and reports
mock_indicators = {
    "sales": PerformanceIndicator(
        id="sales",
        name="Total Sales",
        value=1250000,
        target=1000000,
        unit="USD",
        trend="up",
        last_updated=datetime.now()
    ),
    "profit": PerformanceIndicator(
        id="profit",
        name="Net Profit",
        value=250000,
        target=300000,
        unit="USD",
        trend="down",
        last_updated=datetime.now()
    )
}

mock_reports = {
    "financial_monthly": Report(
        id="financial_monthly",
        title="Monthly Financial Report",
        type="financial",
        period="monthly",
        content={
            "revenue": 1250000,
            "expenses": 1000000,
            "profit": 250000,
            "margin": "20%"
        },
        generated_at=datetime.now()
    )
}

# API endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/indicators/", response_model=List[PerformanceIndicator])
async def get_indicators(current_user: User = Depends(get_current_active_user)):
    return list(mock_indicators.values())

@app.get("/indicators/{indicator_id}", response_model=PerformanceIndicator)
async def get_indicator(indicator_id: str, current_user: User = Depends(get_current_active_user)):
    if indicator_id not in mock_indicators:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return mock_indicators[indicator_id]

@app.post("/reports/generate", response_model=Report)
async def generate_report(
    report_request: ReportRequest,
    current_user: User = Depends(get_current_active_user)
):
    report_id = f"{report_request.report_type}_{report_request.period}"
    if report_id in mock_reports:
        return mock_reports[report_id]
    
    # In a real implementation, this would generate a new report
    raise HTTPException(
        status_code=404,
        detail=f"Report type '{report_request.report_type}' for period '{report_request.period}' not found"
    )

@app.get("/reports/", response_model=List[Report])
async def get_available_reports(current_user: User = Depends(get_current_active_user)):
    return list(mock_reports.values())

@app.get("/reports/{report_id}", response_model=Report)
async def get_report(report_id: str, current_user: User = Depends(get_current_active_user)):
    if report_id not in mock_reports:
        raise HTTPException(status_code=404, detail="Report not found")
    return mock_reports[report_id]

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
