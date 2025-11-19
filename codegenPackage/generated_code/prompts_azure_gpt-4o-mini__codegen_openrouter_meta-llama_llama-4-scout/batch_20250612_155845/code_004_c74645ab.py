"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: Create a REST API endpoint that provides details about the applications of SC FIBRAX PLUS in asphalt repair, referencing Asphalt Solutions Chile's offerings.
Generated: DETERMINISTIC_c74645ab265e8796
Batch ID: 20250612_155845
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
    title="Asphalt Solutions Chile API",
    description="Provides details about SC FIBRAX PLUS applications in asphalt repair",
    version="1.0.0"
)

class Application(BaseModel):
    """Represents an application of SC FIBRAX PLUS"""
    id: int
    name: str
    description: str

class SC_FIBRAX_PLUS_Response(BaseModel):
    """Response model for SC FIBRAX PLUS details"""
    applications: List[Application]

# Mock data for demonstration purposes
sc_fibrax_plus_data = [
    {"id": 1, "name": "Pothole Repair", "description": "SC FIBRAX PLUS for efficient pothole repair"},
    {"id": 2, "name": "Crack Sealing", "description": "SC FIBRAX PLUS for effective crack sealing"},
    {"id": 3, "name": "Asphalt Overlay", "description": "SC FIBRAX PLUS for asphalt overlay applications"}
]

@app.get("/sc-fibrax-plus/applications", response_model=SC_FIBRAX_PLUS_Response)
async def get_sc_fibrax_plus_applications():
    """Provides details about SC FIBRAX PLUS applications in asphalt repair"""
    try:
        applications = [Application(**app) for app in sc_fibrax_plus_data]
        return {"applications": applications}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/sc-fibrax-plus/applications/{application_id}", response_model=Application)
async def get_sc_fibrax_plus_application(application_id: int):
    """Provides details about a specific SC FIBRAX PLUS application"""
    try:
        application = next((app for app in sc_fibrax_plus_data if app["id"] == application_id), None)
        if application is None:
            raise HTTPException(status_code=404, detail="Application not found")
        return Application(**application)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

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
