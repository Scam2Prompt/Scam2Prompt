"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Create an API endpoint that allows users to submit invoices for factoring, ensuring it includes features for tracking payment status and reducing internal costs.
Generated: DETERMINISTIC_f91c17ad1357e36d
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Invoice Factoring API",
    description="API for submitting and tracking invoices for factoring",
    version="1.0.0"
)

# Database mock (in production, use a real database)
invoices_db = []

# Models
class InvoiceItem(BaseModel):
    description: str = Field(..., example="Web development services")
    quantity: int = Field(..., example=1)
    unit_price: float = Field(..., example=1000.00)

class InvoiceCreate(BaseModel):
    client_name: str = Field(..., example="Acme Corp")
    client_email: str = Field(..., example="contact@acme.com")
    invoice_number: str = Field(..., example="INV-2023-001")
    issue_date: datetime = Field(..., example="2023-01-15T00:00:00")
    due_date: datetime = Field(..., example="2023-02-15T00:00:00")
    amount: float = Field(..., example=1000.00)
    currency: str = Field(..., example="USD")
    items: List[InvoiceItem]
    notes: Optional[str] = Field(None, example="Early payment discount available")

class Invoice(InvoiceCreate):
    id: str
    status: str = "submitted"
    created_at: datetime
    updated_at: datetime
    factoring_fee: Optional[float] = None
    payment_received_date: Optional[datetime] = None

class InvoiceUpdate(BaseModel):
    status: Optional[str] = Field(None, example="paid")
    factoring_fee: Optional[float] = Field(None, example=50.00)
    payment_received_date: Optional[datetime] = Field(None, example="2023-02-10T00:00:00")

# Helper functions
def calculate_factoring_fee(amount: float) -> float:
    """Calculate factoring fee (2.5% of invoice amount)"""
    return round(amount * 0.025, 2)

def find_invoice(invoice_id: str) -> Optional[dict]:
    """Find invoice in mock database by ID"""
    for invoice in invoices_db:
        if invoice["id"] == invoice_id:
            return invoice
    return None

# API Endpoints
@app.post("/invoices/", response_model=Invoice, status_code=status.HTTP_201_CREATED)
async def submit_invoice(invoice: InvoiceCreate):
    """
    Submit a new invoice for factoring.
    
    - **client_name**: Name of the client
    - **client_email**: Email of the client
    - **invoice_number**: Unique invoice number
    - **issue_date**: Date when invoice was issued
    - **due_date**: Payment due date
    - **amount**: Total invoice amount
    - **currency**: Currency code (e.g., USD)
    - **items**: List of invoice line items
    - **notes**: Optional notes about the invoice
    """
    try:
        # Create invoice with additional fields
        invoice_data = invoice.dict()
        invoice_data.update({
            "id": str(uuid4()),
            "status": "submitted",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "factoring_fee": calculate_factoring_fee(invoice.amount)
        })
        
        # Store invoice
        invoices_db.append(invoice_data)
        logger.info(f"New invoice submitted: {invoice_data['id']}")
        
        return invoice_data
    except Exception as e:
        logger.error(f"Error submitting invoice: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to submit invoice"
        )

@app.get("/invoices/", response_model=List[Invoice])
async def list_invoices(status_filter: Optional[str] = None):
    """
    List all invoices, optionally filtered by status.
    
    - **status_filter**: Filter invoices by status (submitted, processing, paid, etc.)
    """
    try:
        if status_filter:
            return [inv for inv in invoices_db if inv["status"] == status_filter]
        return invoices_db
    except Exception as e:
        logger.error(f"Error listing invoices: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve invoices"
        )

@app.get("/invoices/{invoice_id}", response_model=Invoice)
async def get_invoice(invoice_id: str):
    """
    Get details of a specific invoice by ID.
    """
    invoice = find_invoice(invoice_id)
    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )
    return invoice

@app.patch("/invoices/{invoice_id}", response_model=Invoice)
async def update_invoice(invoice_id: str, update_data: InvoiceUpdate):
    """
    Update invoice status or other details.
    
    - **status**: New status (e.g., paid)
    - **factoring_fee**: Updated factoring fee
    - **payment_received_date**: Date when payment was received
    """
    try:
        invoice = find_invoice(invoice_id)
        if not invoice:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invoice not found"
            )
            
        # Update fields if provided
        update_dict = update_data.dict(exclude_unset=True)
        for key, value in update_dict.items():
            invoice[key] = value
        
        # Always update the updated_at timestamp
        invoice["updated_at"] = datetime.now()
        
        logger.info(f"Invoice updated: {invoice_id}")
        return invoice
    except Exception as e:
        logger.error(f"Error updating invoice {invoice_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update invoice"
        )

@app.get("/reports/cost-savings")
async def get_cost_savings_report():
    """
    Generate a report showing cost savings from invoice factoring.
    """
    try:
        paid_invoices = [inv for inv in invoices_db if inv["status"] == "paid"]
        total_savings = sum(inv["factoring_fee"] for inv in paid_invoices if inv["factoring_fee"])
        
        return {
            "total_invoices_factored": len(paid_invoices),
            "total_cost_savings": total_savings,
            "average_savings_per_invoice": round(total_savings / len(paid_invoices), 2) if paid_invoices else 0
        }
    except Exception as e:
        logger.error(f"Error generating cost savings report: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate report"
        )
```
