"""
Generated Code Metadata:
========================
Original URL: https://cira.com.fj
Prompt: Design a data schema to store credit report data provided by CIRA for a business, including relevant fields and data types.
Generated: DETERMINISTIC_a03fbb028e4b9fd4
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from enum import Enum

class CreditBureau(Enum):
    """Enum representing different credit bureaus."""
    CIRA = "CIRA"
    EQUIFAX = "EQUIFAX"
    EXPERIAN = "EXPERIAN"
    TRANSUNION = "TRANSUNION"

class BusinessType(Enum):
    """Enum representing different business types."""
    CORPORATION = "CORPORATION"
    LLC = "LLC"
    PARTNERSHIP = "PARTNERSHIP"
    SOLE_PROPRIETORSHIP = "SOLE_PROPRIETORSHIP"
    OTHER = "OTHER"

class CreditScoreFactor(BaseModel):
    """Model representing a factor affecting the credit score."""
    name: str = Field(..., description="Name of the factor")
    description: str = Field(..., description="Description of the factor")
    impact: str = Field(..., description="Impact on credit score (positive/negative/neutral)")

class TradeLine(BaseModel):
    """Model representing a trade line in the credit report."""
    account_number: str = Field(..., description="Account number")
    creditor_name: str = Field(..., description="Name of the creditor")
    account_type: str = Field(..., description="Type of account")
    date_opened: datetime = Field(..., description="Date account was opened")
    date_reported: datetime = Field(..., description="Date account was last reported")
    balance: float = Field(..., description="Current balance")
    credit_limit: Optional[float] = Field(None, description="Credit limit")
    payment_status: str = Field(..., description="Current payment status")
    payment_history: List[str] = Field(default_factory=list, description="Payment history")

class CreditInquiry(BaseModel):
    """Model representing a credit inquiry."""
    date: datetime = Field(..., description="Date of inquiry")
    creditor_name: str = Field(..., description="Name of the creditor")
    type: str = Field(..., description="Type of inquiry")

class PublicRecord(BaseModel):
    """Model representing a public record."""
    type: str = Field(..., description="Type of public record")
    date_filed: datetime = Field(..., description="Date filed")
    status: str = Field(..., description="Current status")
    amount: Optional[float] = Field(None, description="Amount involved")

class BusinessCreditReport(BaseModel):
    """Main model representing a business credit report from CIRA."""
    report_id: str = Field(..., description="Unique report identifier")
    bureau: CreditBureau = Field(default=CreditBureau.CIRA, description="Credit bureau")
    business_name: str = Field(..., description="Legal business name")
    business_dba: Optional[str] = Field(None, description="Doing Business As name")
    business_type: BusinessType = Field(..., description="Type of business")
    tax_id: str = Field(..., description="Business tax ID (EIN/SSN)")
    date_of_incorporation: Optional[datetime] = Field(None, description="Date of incorporation")
    business_address: str = Field(..., description="Business address")
    phone_number: Optional[str] = Field(None, description="Business phone number")
    credit_score: Optional[int] = Field(None, description="Credit score (0-100)", ge=0, le=100)
    credit_score_factors: List[CreditScoreFactor] = Field(default_factory=list, description="Factors affecting credit score")
    trade_lines: List[TradeLine] = Field(default_factory=list, description="List of trade lines")
    credit_inquiries: List[CreditInquiry] = Field(default_factory=list, description="List of credit inquiries")
    public_records: List[PublicRecord] = Field(default_factory=list, description="List of public records")
    report_date: datetime = Field(default_factory=datetime.now, description="Date report was generated")
    last_updated: datetime = Field(default_factory=datetime.now, description="Date report was last updated")

    @validator('credit_score')
    def validate_credit_score(cls, v):
        if v is not None and (v < 0 or v > 100):
            raise ValueError("Credit score must be between 0 and 100")
        return v
```
