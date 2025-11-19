"""
Generated Code Metadata:
========================
Original URL: https://vsisithashai.pages.dev
Prompt: Develop a simple API that allows users to access the Hash AI mining facility's performance metrics and ROI calculations for various cryptocurrencies.
Generated: DETERMINISTIC_19234f584725e405
Batch ID: 20250612_161700
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
from typing import Dict, List

app = FastAPI(
    title="Hash AI Mining Facility API",
    description="Access performance metrics and ROI calculations for various cryptocurrencies",
    version="1.0.0"
)

# Define a model for cryptocurrency performance metrics
class CryptoMetrics(BaseModel):
    name: str
    hash_rate: float
    power_consumption: float
    revenue: float

# Define a model for ROI calculations
class ROICalculation(BaseModel):
    cryptocurrency: str
    investment: float
    daily_revenue: float
    roi_days: float

# Sample in-memory data store for demonstration purposes
# In a production environment, consider using a database
crypto_metrics: Dict[str, CryptoMetrics] = {
    "Bitcoin": CryptoMetrics(name="Bitcoin", hash_rate=100.0, power_consumption=500.0, revenue=50.0),
    "Ethereum": CryptoMetrics(name="Ethereum", hash_rate=50.0, power_consumption=300.0, revenue=30.0),
}

@app.get("/metrics/")
async def get_all_metrics():
    """Return a list of all cryptocurrency performance metrics"""
    return list(crypto_metrics.values())

@app.get("/metrics/{crypto_name}")
async def get_metric(crypto_name: str):
    """Return the performance metrics for a specific cryptocurrency"""
    try:
        return crypto_metrics[crypto_name]
    except KeyError:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")

@app.post("/roi/")
async def calculate_roi(roi_calculation: ROICalculation):
    """Calculate the ROI for a specific cryptocurrency investment"""
    try:
        roi = roi_calculation.investment / (roi_calculation.daily_revenue * roi_calculation.roi_days)
        return {"cryptocurrency": roi_calculation.cryptocurrency, "roi": roi}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Invalid input: division by zero")

@app.get("/roi/{crypto_name}")
async def get_roi(crypto_name: str, investment: float, days: float):
    """Return the ROI calculation for a specific cryptocurrency investment"""
    try:
        metric = crypto_metrics[crypto_name]
        daily_revenue = metric.revenue
        roi_days = days
        roi = investment / (daily_revenue * roi_days)
        return {"cryptocurrency": crypto_name, "roi": roi}
    except KeyError:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Invalid input: division by zero")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt

fastapi
pydantic
uvicorn
```

```bash
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
