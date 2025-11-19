"""
Generated Code Metadata:
========================
Original URL: https://cabinet-customs.com.ua
Prompt: Design a RESTful API to provide access to the Single Window Portal's functionality, including endpoints for verifying certificates of origin, checking customs declarations, and retrieving tariff information.
Generated: DETERMINISTIC_a551eae28a38d715
Batch ID: 20250622_204915
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
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import uvicorn
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Single Window Portal API",
    description="RESTful API providing access to Single Window Portal's functionality",
    version="1.0.0",
)

# Define Pydantic models
class CertificateOfOrigin(BaseModel):
    certificate_number: str
    issuing_authority: str
    date_of_issue: datetime

class CustomsDeclaration(BaseModel):
    declaration_number: str
    declarant: str
    date_of_declaration: datetime

class TariffInformation(BaseModel):
    tariff_code: str
    description: str
    rate: float

# In-memory data store (replace with a database in production)
certificates_of_origin = [
    CertificateOfOrigin(
        certificate_number="CO-001",
        issuing_authority="Authority A",
        date_of_issue=datetime(2022, 1, 1),
    ),
    CertificateOfOrigin(
        certificate_number="CO-002",
        issuing_authority="Authority B",
        date_of_issue=datetime(2022, 6, 1),
    ),
]

customs_declarations = [
    CustomsDeclaration(
        declaration_number="CD-001",
        declarant="Declarant A",
        date_of_declaration=datetime(2022, 1, 15),
    ),
    CustomsDeclaration(
        declaration_number="CD-002",
        declarant="Declarant B",
        date_of_declaration=datetime(2022, 7, 15),
    ),
]

tariff_info = [
    TariffInformation(
        tariff_code="TC-001",
        description="Tariff 1",
        rate=10.0,
    ),
    TariffInformation(
        tariff_code="TC-002",
        description="Tariff 2",
        rate=20.0,
    ),
]

# Endpoint to verify certificates of origin
@app.get("/certificates-of-origin/{certificate_number}")
async def verify_certificate_of_origin(certificate_number: str):
    """Verify a certificate of origin"""
    for certificate in certificates_of_origin:
        if certificate.certificate_number == certificate_number:
            return JSONResponse(content={"verified": True}, status_code=200)
    raise HTTPException(status_code=404, detail="Certificate not found")

# Endpoint to check customs declarations
@app.get("/customs-declarations/{declaration_number}")
async def check_customs_declaration(declaration_number: str):
    """Check a customs declaration"""
    for declaration in customs_declarations:
        if declaration.declaration_number == declaration_number:
            return JSONResponse(content={"checked": True}, status_code=200)
    raise HTTPException(status_code=404, detail="Declaration not found")

# Endpoint to retrieve tariff information
@app.get("/tariff-information/{tariff_code}")
async def get_tariff_information(tariff_code: str):
    """Retrieve tariff information"""
    for tariff in tariff_info:
        if tariff.tariff_code == tariff_code:
            return JSONResponse(content={"tariff": tariff.dict()}, status_code=200)
    raise HTTPException(status_code=404, detail="Tariff not found")

# Endpoint to create a new certificate of origin
@app.post("/certificates-of-origin")
async def create_certificate_of_origin(certificate: CertificateOfOrigin):
    """Create a new certificate of origin"""
    certificates_of_origin.append(certificate)
    return JSONResponse(content={"message": "Certificate created"}, status_code=201)

# Endpoint to create a new customs declaration
@app.post("/customs-declarations")
async def create_customs_declaration(declaration: CustomsDeclaration):
    """Create a new customs declaration"""
    customs_declarations.append(declaration)
    return JSONResponse(content={"message": "Declaration created"}, status_code=201)

# Endpoint to create new tariff information
@app.post("/tariff-information")
async def create_tariff_information(tariff: TariffInformation):
    """Create new tariff information"""
    tariff_info.append(tariff)
    return JSONResponse(content={"message": "Tariff created"}, status_code=201)

if __name__ == "__main__":
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
