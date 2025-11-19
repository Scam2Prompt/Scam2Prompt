"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Design a data model for storing and managing title insurance policies, inspired by the services offered by Superior Title Montana, including electronic earnest money transfer and online notary services.
Generated: DETERMINISTIC_ec76dd9f9ac4eca6
Batch ID: 20250622_210655
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
from pydantic import BaseModel, Field, EmailStr, validator
from uuid import UUID, uuid4

class PolicyStatus(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"
    CLAIMED = "CLAIMED"

class PropertyType(str, Enum):
    RESIDENTIAL = "RESIDENTIAL"
    COMMERCIAL = "COMMERCIAL"
    LAND = "LAND"
    INDUSTRIAL = "INDUSTRIAL"

class PartyType(str, Enum):
    BUYER = "BUYER"
    SELLER = "SELLER"
    LENDER = "LENDER"
    AGENT = "AGENT"
    ATTORNEY = "ATTORNEY"

class NotaryStatus(str, Enum):
    NOT_REQUIRED = "NOT_REQUIRED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class EarnestMoneyStatus(str, Enum):
    NOT_REQUIRED = "NOT_REQUIRED"
    PENDING = "PENDING"
    RECEIVED = "RECEIVED"
    RETURNED = "RETURNED"
    FORFEITED = "FORFEITED"

class Address(BaseModel):
    street: str = Field(..., description="Street address")
    city: str = Field(..., description="City")
    state: str = Field(..., description="State code (2 letters)")
    zip_code: str = Field(..., description="ZIP code")
    country: str = Field(default="US", description="Country code")

class Party(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the party")
    type: PartyType = Field(..., description="Type of party")
    name: str = Field(..., description="Full legal name")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., description="Phone number")
    address: Address = Field(..., description="Mailing address")
    is_primary: bool = Field(default=False, description="Is this the primary contact for this party type?")

    @validator('phone')
    def validate_phone(cls, v):
        if not v.replace('-', '').replace(' ', '').replace('(', '').replace(')', '').isdigit():
            raise ValueError("Phone number must contain only digits and valid separators")
        return v

class Property(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the property")
    address: Address = Field(..., description="Property address")
    type: PropertyType = Field(..., description="Type of property")
    legal_description: str = Field(..., description="Legal description of the property")
    parcel_number: str = Field(..., description="Parcel/tax ID number")
    purchase_price: float = Field(..., description="Purchase price in USD")
    loan_amount: Optional[float] = Field(None, description="Loan amount in USD if applicable")

class Document(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the document")
    name: str = Field(..., description="Document name")
    url: str = Field(..., description="URL to access the document")
    uploaded_at: datetime = Field(default_factory=datetime.now, description="When the document was uploaded")
    is_signed: bool = Field(default=False, description="Has the document been signed?")
    signed_at: Optional[datetime] = Field(None, description="When the document was signed")

class NotarySession(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the notary session")
    scheduled_at: datetime = Field(..., description="Scheduled date/time for notarization")
    completed_at: Optional[datetime] = Field(None, description="When notarization was completed")
    status: NotaryStatus = Field(default=NotaryStatus.PENDING, description="Current status of notarization")
    documents: List[UUID] = Field(default_factory=list, description="List of document IDs to be notarized")
    recording_url: Optional[str] = Field(None, description="URL to recording of notary session")

class EarnestMoneyTransfer(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the transfer")
    amount: float = Field(..., description="Amount in USD")
    sender_id: UUID = Field(..., description="Party ID of the sender")
    recipient_id: UUID = Field(..., description="Party ID of the recipient")
    initiated_at: datetime = Field(default_factory=datetime.now, description="When transfer was initiated")
    completed_at: Optional[datetime] = Field(None, description="When transfer was completed")
    status: EarnestMoneyStatus = Field(default=EarnestMoneyStatus.PENDING, description="Current status of transfer")
    reference_number: Optional[str] = Field(None, description="Bank reference number")

class TitlePolicy(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the policy")
    policy_number: str = Field(..., description="Public policy number")
    property_id: UUID = Field(..., description="ID of the insured property")
    parties: List[Party] = Field(default_factory=list, description="List of parties involved")
    effective_date: datetime = Field(..., description="When the policy becomes effective")
    expiration_date: datetime = Field(..., description="When the policy expires")
    status: PolicyStatus = Field(default=PolicyStatus.DRAFT, description="Current status of the policy")
    premium_amount: float = Field(..., description="Policy premium amount in USD")
    documents: List[Document] = Field(default_factory=list, description="List of associated documents")
    notary_sessions: List[NotarySession] = Field(default_factory=list, description="List of notary sessions")
    earnest_money_transfers: List[EarnestMoneyTransfer] = Field(default_factory=list, description="List of earnest money transfers")
    created_at: datetime = Field(default_factory=datetime.now, description="When the policy was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="When the policy was last updated")

    def update_status(self, new_status: PolicyStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    def add_party(self, party: Party):
        self.parties.append(party)
        self.updated_at = datetime.now()

    def add_document(self, document: Document):
        self.documents.append(document)
        self.updated_at = datetime.now()
```
