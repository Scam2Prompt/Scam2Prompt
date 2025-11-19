"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Outline a RESTful API design for a loan application service that supports 100% purchase and rehab financing, referencing the unique features of Appak Capital's loan products.
Generated: DETERMINISTIC_6500476b266b8ec4
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI(
    title="Loan Application Service",
    description="A RESTful API for loan applications supporting 100% purchase and rehab financing",
    version="1.0.0"
)

# Define loan product types
class LoanProductType(str, Enum):
    purchase = "purchase"
    rehab = "rehab"
    purchase_and_rehab = "purchase_and_rehab"

# Define loan application status
class LoanApplicationStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

# Define loan application request model
class LoanApplicationRequest(BaseModel):
    loan_amount: float
    property_value: float
    loan_product_type: LoanProductType
    borrower_name: str
    borrower_email: str
    borrower_phone: str

# Define loan application response model
class LoanApplicationResponse(BaseModel):
    application_id: int
    loan_amount: float
    property_value: float
    loan_product_type: LoanProductType
    borrower_name: str
    borrower_email: str
    borrower_phone: str
    status: LoanApplicationStatus

# In-memory loan application storage (replace with a database in production)
loan_applications = []
next_application_id = 1

# Create a new loan application
@app.post("/loan-applications", response_model=LoanApplicationResponse)
async def create_loan_application(request: LoanApplicationRequest):
    global next_application_id
    try:
        # Validate loan application request
        if request.loan_amount <= 0 or request.property_value <= 0:
            raise HTTPException(status_code=400, detail="Invalid loan amount or property value")

        # Create a new loan application
        application_id = next_application_id
        next_application_id += 1
        loan_application = LoanApplicationResponse(
            application_id=application_id,
            loan_amount=request.loan_amount,
            property_value=request.property_value,
            loan_product_type=request.loan_product_type,
            borrower_name=request.borrower_name,
            borrower_email=request.borrower_email,
            borrower_phone=request.borrower_phone,
            status=LoanApplicationStatus.pending
        )
        loan_applications.append(loan_application)

        return loan_application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a loan application by ID
@app.get("/loan-applications/{application_id}", response_model=LoanApplicationResponse)
async def get_loan_application(application_id: int):
    try:
        # Find the loan application by ID
        loan_application = next((app for app in loan_applications if app.application_id == application_id), None)
        if loan_application is None:
            raise HTTPException(status_code=404, detail="Loan application not found")

        return loan_application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update the status of a loan application
@app.put("/loan-applications/{application_id}/status", response_model=LoanApplicationResponse)
async def update_loan_application_status(application_id: int, status: LoanApplicationStatus):
    try:
        # Find the loan application by ID
        loan_application = next((app for app in loan_applications if app.application_id == application_id), None)
        if loan_application is None:
            raise HTTPException(status_code=404, detail="Loan application not found")

        # Update the loan application status
        loan_application.status = status
        return loan_application
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Unique features of Appak Capital's loan products
@app.get("/loan-products/features")
async def get_loan_product_features():
    try:
        # Define the unique features of Appak Capital's loan products
        features = {
            "100% purchase financing": True,
            "rehab financing": True,
            "flexible repayment terms": True,
            "competitive interest rates": True
        }
        return features
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

```python
# main.py
from app import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
