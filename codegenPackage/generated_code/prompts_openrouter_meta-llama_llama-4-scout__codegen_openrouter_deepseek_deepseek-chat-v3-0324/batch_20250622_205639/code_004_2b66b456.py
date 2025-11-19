"""
Generated Code Metadata:
========================
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: "Create an API recommendation for financial data serving, inspired by the structure and files found on world-liberty-financial.alnagi-group.com."
Generated: DETERMINISTIC_2b66b4567b86abd5
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Data API Recommendation
Inspired by world-liberty-financial.alnagi-group.com structure
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import datetime
import uvicorn

# Define data models
class FinancialData(BaseModel):
    date: datetime.date
    symbol: str
    open_price: float
    close_price: float
    high: float
    low: float
    volume: int

class FinancialDataResponse(BaseModel):
    data: List[FinancialData]
    pagination: dict

class ErrorResponse(BaseModel):
    detail: str

# Initialize FastAPI app
app = FastAPI(
    title="Financial Data API",
    description="API for serving financial market data",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@financial-api.com"
    },
    license_info={
        "name": "MIT",
    },
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database (in production, replace with actual database connection)
mock_db = []

# Helper function for pagination
def paginate_data(data: list, page: int, limit: int):
    start = (page - 1) * limit
    end = start + limit
    return {
        "data": data[start:end],
        "pagination": {
            "page": page,
            "limit": limit,
            "total": len(data),
            "pages": (len(data) + limit - 1) // limit
        }
    }

# API endpoints
@app.get(
    "/api/financial-data",
    response_model=FinancialDataResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Get financial data",
    description="Retrieve paginated financial data with optional filters"
)
async def get_financial_data(
    symbol: Optional[str] = Query(None, description="Stock symbol filter"),
    start_date: Optional[datetime.date] = Query(None, description="Start date filter"),
    end_date: Optional[datetime.date] = Query(None, description="End date filter"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page")
):
    try:
        # Apply filters
        filtered_data = mock_db
        if symbol:
            filtered_data = [d for d in filtered_data if d.symbol == symbol]
        if start_date:
            filtered_data = [d for d in filtered_data if d.date >= start_date]
        if end_date:
            filtered_data = [d for d in filtered_data if d.date <= end_date]

        # Paginate results
        result = paginate_data(filtered_data, page, limit)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.post(
    "/api/financial-data",
    response_model=FinancialData,
    status_code=201,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    summary="Add financial data",
    description="Add new financial data record"
)
async def add_financial_data(data: FinancialData):
    try:
        mock_db.append(data)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to add data: {str(e)}"
        )

# Health check endpoint
@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
