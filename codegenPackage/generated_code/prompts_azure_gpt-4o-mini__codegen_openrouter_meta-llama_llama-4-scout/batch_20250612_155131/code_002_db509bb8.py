"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Create an API endpoint that enables users to request legal and financial advice for debt management, reflecting the services described on the Arbitum Consulting website.
Generated: DETERMINISTIC_db509bb8f1487408
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Debt Management API",
    description="API for requesting legal and financial advice for debt management",
    version="1.0.0",
)

# Define a model for the advice request
class AdviceRequest(BaseModel):
    """Request body for advice requests"""
    name: str
    email: str
    phone_number: str
    debt_amount: float
    debt_type: str
    advice_type: str  # "legal" or "financial"

# Define a model for the advice response
class AdviceResponse(BaseModel):
    """Response body for advice requests"""
    id: int
    name: str
    email: str
    phone_number: str
    debt_amount: float
    debt_type: str
    advice_type: str
    message: str

# In-memory storage for demonstration purposes
advice_requests = []
id_counter = 1

@app.post("/advice", response_model=AdviceResponse, status_code=status.HTTP_201_CREATED)
async def create_advice_request(request: AdviceRequest):
    """
    Create a new advice request.

    :param request: Advice request body
    :return: Created advice response
    """
    global id_counter
    try:
        # Validate advice type
        if request.advice_type not in ["legal", "financial"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid advice type")

        # Create a new advice request
        advice_request = AdviceResponse(
            id=id_counter,
            name=request.name,
            email=request.email,
            phone_number=request.phone_number,
            debt_amount=request.debt_amount,
            debt_type=request.debt_type,
            advice_type=request.advice_type,
            message="Request received. We will contact you soon."
        )
        advice_requests.append(advice_request)
        id_counter += 1
        return advice_request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/advice/{advice_id}", response_model=AdviceResponse)
async def get_advice_request(advice_id: int):
    """
    Get an advice request by ID.

    :param advice_id: Advice request ID
    :return: Advice response
    """
    try:
        advice_request = next((ar for ar in advice_requests if ar.id == advice_id), None)
        if advice_request is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Advice request not found")
        return advice_request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/advice/{advice_id}", response_model=AdviceResponse)
async def update_advice_request(advice_id: int, request: AdviceRequest):
    """
    Update an advice request.

    :param advice_id: Advice request ID
    :param request: Advice request body
    :return: Updated advice response
    """
    try:
        advice_request = next((ar for ar in advice_requests if ar.id == advice_id), None)
        if advice_request is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Advice request not found")

        # Validate advice type
        if request.advice_type not in ["legal", "financial"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid advice type")

        # Update the advice request
        advice_request.name = request.name
        advice_request.email = request.email
        advice_request.phone_number = request.phone_number
        advice_request.debt_amount = request.debt_amount
        advice_request.debt_type = request.debt_type
        advice_request.advice_type = request.advice_type
        return advice_request
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/advice/{advice_id}")
async def delete_advice_request(advice_id: int):
    """
    Delete an advice request.

    :param advice_id: Advice request ID
    """
    try:
        global advice_requests
        advice_requests = [ar for ar in advice_requests if ar.id != advice_id]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```
