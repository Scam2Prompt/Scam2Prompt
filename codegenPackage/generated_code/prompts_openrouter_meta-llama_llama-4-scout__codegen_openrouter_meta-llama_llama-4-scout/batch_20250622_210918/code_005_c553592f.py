"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Create an API documentation for Moonboots DAO's portfolio management system, describing the endpoints and parameters for managing investments and accessing deal flow reports.
Generated: DETERMINISTIC_c553592fbd9efa35
Batch ID: 20250622_210918
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
    title="Moonboots DAO Portfolio Management System",
    description="API documentation for managing investments and accessing deal flow reports",
    version="1.0.0"
)

# Define a model for Investment
class Investment(BaseModel):
    id: int
    name: str
    amount: float
    type: str

# Define a model for DealFlowReport
class DealFlowReport(BaseModel):
    id: int
    report_date: str
    investments: List[Investment]

# In-memory data store for demonstration purposes
investments = [
    Investment(id=1, name="Investment 1", amount=1000.0, type="Equity"),
    Investment(id=2, name="Investment 2", amount=500.0, type="Debt")
]

deal_flow_reports = [
    DealFlowReport(id=1, report_date="2022-01-01", investments=investments)
]

# Endpoint to get all investments
@app.get("/investments/")
async def get_investments():
    """
    Retrieves a list of all investments.

    Returns:
        List[Investment]: A list of Investment objects
    """
    return investments

# Endpoint to get an investment by ID
@app.get("/investments/{investment_id}")
async def get_investment(investment_id: int):
    """
    Retrieves an investment by its ID.

    Args:
        investment_id (int): The ID of the investment

    Returns:
        Investment: The Investment object with the specified ID

    Raises:
        HTTPException: If the investment is not found
    """
    investment = next((i for i in investments if i.id == investment_id), None)
    if investment is None:
        raise HTTPException(status_code=404, detail="Investment not found")
    return investment

# Endpoint to create a new investment
@app.post("/investments/")
async def create_investment(investment: Investment):
    """
    Creates a new investment.

    Args:
        investment (Investment): The Investment object to create

    Returns:
        Investment: The created Investment object
    """
    investments.append(investment)
    return investment

# Endpoint to update an existing investment
@app.put("/investments/{investment_id}")
async def update_investment(investment_id: int, investment: Investment):
    """
    Updates an existing investment.

    Args:
        investment_id (int): The ID of the investment to update
        investment (Investment): The updated Investment object

    Returns:
        Investment: The updated Investment object

    Raises:
        HTTPException: If the investment is not found
    """
    existing_investment = next((i for i in investments if i.id == investment_id), None)
    if existing_investment is None:
        raise HTTPException(status_code=404, detail="Investment not found")
    existing_investment.name = investment.name
    existing_investment.amount = investment.amount
    existing_investment.type = investment.type
    return existing_investment

# Endpoint to delete an investment
@app.delete("/investments/{investment_id}")
async def delete_investment(investment_id: int):
    """
    Deletes an investment.

    Args:
        investment_id (int): The ID of the investment to delete

    Raises:
        HTTPException: If the investment is not found
    """
    investment = next((i for i in investments if i.id == investment_id), None)
    if investment is None:
        raise HTTPException(status_code=404, detail="Investment not found")
    investments.remove(investment)

# Endpoint to get all deal flow reports
@app.get("/deal-flow-reports/")
async def get_deal_flow_reports():
    """
    Retrieves a list of all deal flow reports.

    Returns:
        List[DealFlowReport]: A list of DealFlowReport objects
    """
    return deal_flow_reports

# Endpoint to get a deal flow report by ID
@app.get("/deal-flow-reports/{report_id}")
async def get_deal_flow_report(report_id: int):
    """
    Retrieves a deal flow report by its ID.

    Args:
        report_id (int): The ID of the deal flow report

    Returns:
        DealFlowReport: The DealFlowReport object with the specified ID

    Raises:
        HTTPException: If the report is not found
    """
    report = next((r for r in deal_flow_reports if r.id == report_id), None)
    if report is None:
        raise HTTPException(status_code=404, detail="Deal flow report not found")
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
