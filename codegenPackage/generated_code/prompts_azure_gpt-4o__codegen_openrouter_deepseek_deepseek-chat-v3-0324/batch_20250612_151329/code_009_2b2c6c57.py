"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Suggest APIs for managing quality control and compliance for suppliers of aromatic chemicals and natural essential oils, inspired by Karnataka Aromas' focus on delivering best-in-class products.
Generated: DETERMINISTIC_2b2c6c5762607d46
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="Aromatic Chemicals Quality Control API",
    description="API for managing quality control and compliance for suppliers of aromatic chemicals and natural essential oils",
    version="1.0.0"
)

# Database models (would typically be in a separate file)
class Supplier(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    contact_email: str
    location: str
    certification: str  # e.g., ISO, GMP, Organic
    registration_date: datetime = Field(default_factory=datetime.now)
    is_active: bool = True

class QualityTest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    supplier_id: str
    batch_number: str
    test_date: datetime = Field(default_factory=datetime.now)
    parameters: dict  # e.g., {"purity": 99.5, "contaminants": 0.01}
    passed: bool
    tested_by: str
    notes: Optional[str] = None

class ComplianceDocument(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    supplier_id: str
    document_type: str  # e.g., "MSDS", "Certificate of Analysis"
    issue_date: datetime
    expiry_date: Optional[datetime] = None
    file_url: str
    is_valid: bool = True

# In-memory "database" (replace with actual database in production)
suppliers_db = {}
quality_tests_db = {}
compliance_docs_db = {}

# Supplier Management Endpoints
@app.post("/suppliers/", status_code=status.HTTP_201_CREATED)
async def register_supplier(supplier: Supplier):
    """Register a new supplier of aromatic chemicals or essential oils"""
    if supplier.contact_email in [s.contact_email for s in suppliers_db.values()]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Supplier with this email already exists"
        )
    suppliers_db[supplier.id] = supplier
    return {"message": "Supplier registered successfully", "supplier_id": supplier.id}

@app.get("/suppliers/", response_model=List[Supplier])
async def get_all_suppliers(active_only: bool = True):
    """Get all suppliers, optionally filtered by active status"""
    if active_only:
        return [s for s in suppliers_db.values() if s.is_active]
    return list(suppliers_db.values())

@app.get("/suppliers/{supplier_id}", response_model=Supplier)
async def get_supplier(supplier_id: str):
    """Get details of a specific supplier"""
    if supplier_id not in suppliers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Supplier not found"
        )
    return suppliers_db[supplier_id]

# Quality Control Endpoints
@app.post("/quality-tests/", status_code=status.HTTP_201_CREATED)
async def record_quality_test(test: QualityTest):
    """Record a new quality test for a supplier's batch"""
    if test.supplier_id not in suppliers_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Supplier does not exist"
        )
    quality_tests_db[test.id] = test
    return {"message": "Quality test recorded", "test_id": test.id}

@app.get("/quality-tests/supplier/{supplier_id}", response_model=List[QualityTest])
async def get_supplier_tests(supplier_id: str, passed_only: bool = False):
    """Get all quality tests for a supplier, optionally filtered by pass/fail status"""
    if supplier_id not in suppliers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Supplier not found"
        )
    tests = [t for t in quality_tests_db.values() if t.supplier_id == supplier_id]
    if passed_only:
        tests = [t for t in tests if t.passed]
    return tests

@app.get("/quality-tests/batch/{batch_number}", response_model=List[QualityTest])
async def get_batch_tests(batch_number: str):
    """Get all quality tests for a specific batch number"""
    return [t for t in quality_tests_db.values() if t.batch_number == batch_number]

# Compliance Management Endpoints
@app.post("/compliance-documents/", status_code=status.HTTP_201_CREATED)
async def upload_compliance_document(document: ComplianceDocument):
    """Upload a new compliance document for a supplier"""
    if document.supplier_id not in suppliers_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Supplier does not exist"
        )
    compliance_docs_db[document.id] = document
    return {"message": "Compliance document uploaded", "document_id": document.id}

@app.get("/compliance-documents/supplier/{supplier_id}", response_model=List[ComplianceDocument])
async def get_supplier_documents(supplier_id: str, valid_only: bool = True):
    """Get all compliance documents for a supplier, optionally filtered by validity"""
    if supplier_id not in suppliers_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Supplier not found"
        )
    docs = [d for d in compliance_docs_db.values() if d.supplier_id == supplier_id]
    if valid_only:
        docs = [d for d in docs if d.is_valid]
    return docs

@app.put("/compliance-documents/{document_id}/validate")
async def validate_document(document_id: str, is_valid: bool):
    """Update the validation status of a compliance document"""
    if document_id not in compliance_docs_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    compliance_docs_db[document_id].is_valid = is_valid
    return {"message": "Document validation status updated"}

# Analytics Endpoint
@app.get("/suppliers/performance")
async def get_supplier_performance():
    """Get performance metrics for all suppliers"""
    performance_data = []
    for supplier in suppliers_db.values():
        tests = [t for t in quality_tests_db.values() if t.supplier_id == supplier.id]
        passed_tests = [t for t in tests if t.passed]
        pass_rate = len(passed_tests) / len(tests) * 100 if tests else 0
        
        valid_docs = [d for d in compliance_docs_db.values() 
                     if d.supplier_id == supplier.id and d.is_valid]
        
        performance_data.append({
            "supplier_id": supplier.id,
            "supplier_name": supplier.name,
            "total_tests": len(tests),
            "pass_rate": round(pass_rate, 2),
            "valid_documents": len(valid_docs),
            "last_test_date": max(t.test_date for t in tests) if tests else None
        })
    
    return sorted(performance_data, key=lambda x: x["pass_rate"], reverse=True)
```
