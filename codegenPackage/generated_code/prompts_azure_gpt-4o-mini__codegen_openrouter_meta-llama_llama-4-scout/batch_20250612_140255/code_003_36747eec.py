"""
Generated Code Metadata:
========================
Original URL: https://noble-doodles-genesis-box.testnet.nfts2.me
Prompt: How can I create an API endpoint to handle reports of scam NFT collections similar to NFTs 2 Me?
Generated: DETERMINISTIC_36747eece5f18866
Batch ID: 20250612_140255
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
from uuid import UUID
from logging.config import dictConfig
import logging

# Configure logging
dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
})

app = FastAPI()

# Define a logger
logger = logging.getLogger(__name__)

# Define the scam report model
class ScamReport(BaseModel):
    """Model for scam reports"""
    collection_name: str
    collection_address: str
    reason: str
    reporter: Optional[str]

# In-memory scam report storage (replace with a database in production)
scam_reports = []

@app.post("/reports", status_code=status.HTTP_201_CREATED)
async def create_scam_report(report: ScamReport):
    """Create a new scam report"""
    try:
        # Validate the report
        if not report.collection_name or not report.collection_address or not report.reason:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid report data")

        # Generate a unique report ID
        report_id = str(UUID(int=1))

        # Store the report
        scam_reports.append({
            "id": report_id,
            "collection_name": report.collection_name,
            "collection_address": report.collection_address,
            "reason": report.reason,
            "reporter": report.reporter
        })

        # Log the report
        logger.info(f"New scam report created: {report_id}")

        return {"id": report_id, "message": "Scam report created successfully"}

    except Exception as e:
        logger.error(f"Error creating scam report: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create scam report")

@app.get("/reports", status_code=status.HTTP_200_OK)
async def get_scam_reports():
    """Retrieve all scam reports"""
    try:
        return scam_reports

    except Exception as e:
        logger.error(f"Error retrieving scam reports: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve scam reports")

@app.get("/reports/{report_id}", status_code=status.HTTP_200_OK)
async def get_scam_report(report_id: str):
    """Retrieve a scam report by ID"""
    try:
        report = next((report for report in scam_reports if report["id"] == report_id), None)
        if report is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scam report not found")

        return report

    except Exception as e:
        logger.error(f"Error retrieving scam report: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to retrieve scam report")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
