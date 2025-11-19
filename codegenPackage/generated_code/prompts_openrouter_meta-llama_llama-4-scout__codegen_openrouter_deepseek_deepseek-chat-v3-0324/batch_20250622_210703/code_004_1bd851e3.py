"""
Generated Code Metadata:
========================
Original URL: https://karnafoundation.org.in
Prompt: Create a data model for tracking donations, volunteers, and beneficiaries for an organization like Karna Foundation, which supports multiple causes such as child education, healthcare, and food distribution.
Generated: DETERMINISTIC_1bd851e3589f099b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, validator

class Cause(str, Enum):
    CHILD_EDUCATION = "Child Education"
    HEALTHCARE = "Healthcare"
    FOOD_DISTRIBUTION = "Food Distribution"
    OTHER = "Other"

class DonationType(str, Enum):
    CASH = "Cash"
    IN_KIND = "In-Kind"
    STOCK = "Stock"
    OTHER = "Other"

class VolunteerStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PROSPECTIVE = "Prospective"

class BeneficiaryType(str, Enum):
    INDIVIDUAL = "Individual"
    FAMILY = "Family"
    COMMUNITY = "Community"
    ORGANIZATION = "Organization"

class Address(BaseModel):
    street: str = Field(..., max_length=100)
    city: str = Field(..., max_length=50)
    state: str = Field(..., max_length=50)
    postal_code: str = Field(..., max_length=20)
    country: str = Field(..., max_length=50)

class ContactInfo(BaseModel):
    phone: str = Field(..., max_length=20)
    email: EmailStr
    alternate_phone: Optional[str] = Field(None, max_length=20)

class Donor(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(..., max_length=100)
    contact: ContactInfo
    address: Optional[Address] = None
    is_anonymous: bool = False
    tax_id: Optional[str] = Field(None, max_length=50, description="Tax ID for receipt purposes")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Donation(BaseModel):
    id: str = Field(..., alias="_id")
    donor_id: str
    amount: float = Field(..., gt=0, description="Amount in local currency")
    donation_type: DonationType
    cause: Cause
    date: datetime = Field(default_factory=datetime.utcnow)
    is_recurring: bool = False
    receipt_issued: bool = False
    notes: Optional[str] = Field(None, max_length=500)

    @validator('amount')
    def round_amount(cls, v):
        return round(v, 2)

class Volunteer(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(..., max_length=100)
    contact: ContactInfo
    address: Address
    skills: List[str] = Field(default_factory=list)
    status: VolunteerStatus = VolunteerStatus.PROSPECTIVE
    causes: List[Cause] = Field(default_factory=list)
    availability: List[str] = Field(default_factory=list)
    joined_date: datetime = Field(default_factory=datetime.utcnow)
    background_check: bool = False
    emergency_contact: Optional[str] = Field(None, max_length=100)

class Beneficiary(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(..., max_length=100)
    type: BeneficiaryType
    contact: Optional[ContactInfo] = None
    address: Optional[Address] = None
    causes: List[Cause] = Field(default_factory=list)
    needs: List[str] = Field(default_factory=list)
    registered_date: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    notes: Optional[str] = Field(None, max_length=500)

class Program(BaseModel):
    id: str = Field(..., alias="_id")
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=1000)
    cause: Cause
    start_date: datetime
    end_date: Optional[datetime] = None
    volunteers: List[str] = Field(default_factory=list)
    beneficiaries: List[str] = Field(default_factory=list)
    budget: float = 0.0
    is_active: bool = True

class OrganizationMetrics(BaseModel):
    total_donations: float = 0.0
    active_volunteers: int = 0
    beneficiaries_served: int = 0
    programs_active: int = 0
    last_updated: datetime = Field(default_factory=datetime.utcnow)
```
