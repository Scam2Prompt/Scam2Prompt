"""
Generated Code Metadata:
========================
Original URL: https://blur.gay
Prompt: Create a simple API that logs financial transparency data as described on the blur.gay site, detailing income and expenditures related to public endeavors.
Generated: DETERMINISTIC_8d0a30c67b1ee18a
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
import logging
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Financial Transparency API",
    description="API for logging income and expenditures related to public endeavors",
    version="1.0.0"
)

# In-memory database (replace with persistent storage in production)
financial_records_db = []

class FinancialRecord(BaseModel):
    id: Optional[int] = None
    date: datetime
    description: str
    amount: float
    currency: str = "USD"
    record_type: str  # "income" or "expenditure"
    category: Optional[str] = None
    source: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "date": "2023-01-01T00:00:00",
                "description": "Donation from supporter",
                "amount": 100.00,
                "currency": "USD",
                "record_type": "income",
                "category": "donations",
                "source": "Anonymous",
                "notes": "Monthly recurring donation"
            }
        }

@app.post("/records/", response_model=FinancialRecord, status_code=status.HTTP_201_CREATED)
async def create_record(record: FinancialRecord):
    """
    Create a new financial record.
    """
    try:
        # Generate ID (in production, use database auto-increment)
        record_id = len(financial_records_db) + 1
        record.id = record_id
        
        # Validate record type
        if record.record_type.lower() not in ["income", "expenditure"]:
            raise ValueError("Record type must be either 'income' or 'expenditure'")
        
        # Validate amount
        if record.amount <= 0:
            raise ValueError("Amount must be positive")
        
        financial_records_db.append(record)
        logger.info(f"Created record with ID: {record_id}")
        return record
    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

@app.get("/records/", response_model=List[FinancialRecord])
async def get_all_records():
    """
    Get all financial records.
    """
    return financial_records_db

@app.get("/records/{record_id}", response_model=FinancialRecord)
async def get_record(record_id: int):
    """
    Get a specific financial record by ID.
    """
    try:
        record = next((r for r in financial_records_db if r.id == record_id), None)
        if record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Record not found"
            )
        return record
    except Exception as e:
        logger.error(f"Error retrieving record: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

@app.get("/records/summary/balance")
async def get_balance():
    """
    Get the current balance (total income - total expenditures).
    """
    try:
        total_income = sum(r.amount for r in financial_records_db if r.record_type.lower() == "income")
        total_expenditures = sum(r.amount for r in financial_records_db if r.record_type.lower() == "expenditure")
        balance = total_income - total_expenditures
        return {
            "total_income": total_income,
            "total_expenditures": total_expenditures,
            "balance": balance
        }
    except Exception as e:
        logger.error(f"Error calculating balance: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
