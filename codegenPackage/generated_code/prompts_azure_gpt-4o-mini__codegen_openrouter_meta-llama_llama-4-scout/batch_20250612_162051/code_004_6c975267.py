"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Outline a RESTful API design for a shipping company that includes endpoints for managing import/export requests and pre-financing options, based on Olgadorks' offerings.
Generated: DETERMINISTIC_6c975267f05ab657
Batch ID: 20250612_162051
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
from typing import List

app = FastAPI(
    title="Shipping Company API",
    description="API for managing import/export requests and pre-financing options",
    version="1.0.0"
)

# Models
class ImportExportRequest(BaseModel):
    id: int
    customer_name: str
    shipment_type: str  # import/export
    status: str  # pending, in_transit, delivered

class PreFinancingOption(BaseModel):
    id: int
    request_id: int
    financing_amount: float
    interest_rate: float

# In-memory data store (replace with a database in production)
import_export_requests = [
    ImportExportRequest(id=1, customer_name="John Doe", shipment_type="import", status="pending"),
    ImportExportRequest(id=2, customer_name="Jane Doe", shipment_type="export", status="in_transit")
]

pre_financing_options = [
    PreFinancingOption(id=1, request_id=1, financing_amount=1000.0, interest_rate=0.05),
    PreFinancingOption(id=2, request_id=2, financing_amount=500.0, interest_rate=0.03)
]

# Endpoints
@app.get("/import-export-requests/", response_model=List[ImportExportRequest])
def read_import_export_requests():
    """Retrieve a list of all import/export requests"""
    return import_export_requests

@app.get("/import-export-requests/{request_id}", response_model=ImportExportRequest)
def read_import_export_request(request_id: int):
    """Retrieve a specific import/export request by ID"""
    for request in import_export_requests:
        if request.id == request_id:
            return request
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

@app.post("/import-export-requests/", response_model=ImportExportRequest, status_code=status.HTTP_201_CREATED)
def create_import_export_request(request: ImportExportRequest):
    """Create a new import/export request"""
    import_export_requests.append(request)
    return request

@app.put("/import-export-requests/{request_id}", response_model=ImportExportRequest)
def update_import_export_request(request_id: int, request: ImportExportRequest):
    """Update an existing import/export request"""
    for i, existing_request in enumerate(import_export_requests):
        if existing_request.id == request_id:
            import_export_requests[i] = request
            return request
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

@app.delete("/import-export-requests/{request_id}")
def delete_import_export_request(request_id: int):
    """Delete an import/export request"""
    for i, request in enumerate(import_export_requests):
        if request.id == request_id:
            del import_export_requests[i]
            return {"message": "Request deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request not found")

@app.get("/pre-financing-options/", response_model=List[PreFinancingOption])
def read_pre_financing_options():
    """Retrieve a list of all pre-financing options"""
    return pre_financing_options

@app.get("/pre-financing-options/{option_id}", response_model=PreFinancingOption)
def read_pre_financing_option(option_id: int):
    """Retrieve a specific pre-financing option by ID"""
    for option in pre_financing_options:
        if option.id == option_id:
            return option
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")

@app.post("/pre-financing-options/", response_model=PreFinancingOption, status_code=status.HTTP_201_CREATED)
def create_pre_financing_option(option: PreFinancingOption):
    """Create a new pre-financing option"""
    pre_financing_options.append(option)
    return option

@app.put("/pre-financing-options/{option_id}", response_model=PreFinancingOption)
def update_pre_financing_option(option_id: int, option: PreFinancingOption):
    """Update an existing pre-financing option"""
    for i, existing_option in enumerate(pre_financing_options):
        if existing_option.id == option_id:
            pre_financing_options[i] = option
            return option
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")

@app.delete("/pre-financing-options/{option_id}")
def delete_pre_financing_option(option_id: int):
    """Delete a pre-financing option"""
    for i, option in enumerate(pre_financing_options):
        if option.id == option_id:
            del pre_financing_options[i]
            return {"message": "Option deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
