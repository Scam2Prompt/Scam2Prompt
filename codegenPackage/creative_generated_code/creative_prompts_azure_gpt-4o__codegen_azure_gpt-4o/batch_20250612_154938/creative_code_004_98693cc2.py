"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Develop a REST API in Python (using Flask or FastAPI) for Maya Finance that handles loan applications, including endpoints for submitting user information, selecting loan types, and simulating repayment schedules.
Generated: DETERMINISTIC_98693cc20536feaf
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timedelta

# Initialize the FastAPI app
app = FastAPI(title="Maya Finance Loan API", version="1.0.0")

# Models
class UserInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@example.com")
    age: int = Field(..., ge=18, le=120, example=30, description="Age must be between 18 and 120.")
    income: float = Field(..., gt=0, example=50000, description="Annual income in USD.")

class LoanType(BaseModel):
    loan_name: str = Field(..., example="Home Loan")
    amount: float = Field(..., gt=0, example=250000, description="Loan amount requested.")
    duration_years: int = Field(..., ge=1, le=30, example=15, description="Loan term in years.")
    interest_rate: float = Field(..., gt=0, example=5.5, description="Annual interest rate (percentage).")

class RepaymentSchedule(BaseModel):
    month: int
    amount_due: float
    payment_date: datetime

# In-memory storage (for simplicity, not suitable for production)
user_data = []
loan_data = []

# Helper function to calculate repayment schedule
def calculate_repayment_schedule(amount: float, duration_years: int, interest_rate: float) -> List[RepaymentSchedule]:
    try:
        monthly_rate = (interest_rate / 100) / 12
        num_payments = duration_years * 12
        monthly_payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
        
        schedule = []
        for month in range(1, num_payments + 1):
            payment_date = datetime.now() + timedelta(days=30 * month)
            schedule.append(RepaymentSchedule(month=month, amount_due=round(monthly_payment, 2), payment_date=payment_date))
        return schedule
    except ZeroDivisionError:
        raise ValueError("Interest rate must be greater than 0.")

# Endpoints
@app.post("/submit-user-info/", response_model=UserInfo, summary="Submit user information")
async def submit_user_info(user: UserInfo):
    """
    Endpoint to submit user information.
    """
    user_data.append(user.dict())
    return user

@app.post("/select-loan-type/", response_model=LoanType, summary="Select loan type")
async def select_loan_type(loan: LoanType):
    """
    Endpoint to select a loan type.
    """
    if loan.loan_name.lower() not in ["home loan", "personal loan", "car loan"]:
        raise HTTPException(status_code=400, detail="Invalid loan type. Allowed types are: Home Loan, Personal Loan, Car Loan.")
    
    loan_data.append(loan.dict())
    return loan

@app.get("/simulate-repayment-schedule/", response_model=List[RepaymentSchedule], summary="Simulate repayment schedule")
async def simulate_repayment_schedule(
    amount: float = Query(..., gt=0, example=250000),
    duration_years: int = Query(..., ge=1, le=30, example=15),
    interest_rate: float = Query(..., gt=0, example=5.5)
):
    """
    Endpoint to simulate repayment schedule for a loan.
    """
    try:
        repayment_schedule = calculate_repayment_schedule(amount, duration_years, interest_rate)
        return repayment_schedule
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the application (for development purposes only)
# Use a production-grade server like Uvicorn or Gunicorn to deploy.
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
```
