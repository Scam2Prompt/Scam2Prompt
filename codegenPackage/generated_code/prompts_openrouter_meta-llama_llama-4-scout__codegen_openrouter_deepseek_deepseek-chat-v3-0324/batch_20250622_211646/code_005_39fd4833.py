"""
Generated Code Metadata:
========================
Original URL: https://netsecurity.pages.dev
Prompt: "Design a simple API to retrieve and analyze TLS connection metrics, including 'tlsVersion', 'tlsCipher', and 'botManagement.score', and provide a sample API implementation in Python."
Generated: DETERMINISTIC_39fd48336652cf49
Batch ID: 20250622_211646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from datetime import datetime

# Define the data model for TLS metrics
class TLSMetrics(BaseModel):
    tls_version: str
    tls_cipher: str
    bot_management_score: float
    timestamp: datetime

# Sample in-memory database
sample_data = [
    TLSMetrics(
        tls_version="TLSv1.2",
        tls_cipher="ECDHE-RSA-AES256-GCM-SHA384",
        bot_management_score=85.5,
        timestamp=datetime.now()
    ),
    TLSMetrics(
        tls_version="TLSv1.3",
        tls_cipher="AES256-GCM-SHA384",
        bot_management_score=92.0,
        timestamp=datetime.now()
    )
]

app = FastAPI(
    title="TLS Metrics API",
    description="API for retrieving and analyzing TLS connection metrics",
    version="1.0.0"
)

@app.get("/metrics", response_model=List[TLSMetrics])
async def get_all_metrics():
    """
    Retrieve all TLS metrics records.
    """
    return sample_data

@app.get("/metrics/{tls_version}", response_model=List[TLSMetrics])
async def get_metrics_by_version(tls_version: str):
    """
    Retrieve TLS metrics filtered by TLS version.
    """
    filtered = [m for m in sample_data if m.tls_version.lower() == tls_version.lower()]
    if not filtered:
        raise HTTPException(status_code=404, detail="No metrics found for this TLS version")
    return filtered

@app.get("/metrics/score/avg", response_model=float)
async def get_average_score():
    """
    Calculate the average bot management score across all metrics.
    """
    if not sample_data:
        raise HTTPException(status_code=404, detail="No metrics available")
    return sum(m.bot_management_score for m in sample_data) / len(sample_data)

@app.get("/metrics/ciphers", response_model=List[str])
async def get_all_ciphers():
    """
    Retrieve list of all unique TLS ciphers.
    """
    if not sample_data:
        raise HTTPException(status_code=404, detail="No metrics available")
    return list(set(m.tls_cipher for m in sample_data))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
