"""
Generated Code Metadata:
========================
Original URL: https://pulse.claims
Prompt: "Design a data model for storing and retrieving insurance claims information, including claimant details and claim status."
Generated: DETERMINISTIC_91c643aedb054342
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum, auto
from typing import Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4


class ClaimStatus(Enum):
    """Enum representing possible claim statuses."""
    SUBMITTED = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    DENIED = auto()
    PAID = auto()


class Claimant(BaseModel):
    """Data model for claimant information."""
    id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    phone: str = Field(..., min_length=10, max_length=15)
    address: str = Field(..., min_length=5, max_length=200)

    @validator('phone')
    def validate_phone(cls, v):
        """Validate phone number contains only digits."""
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        return v


class Claim(BaseModel):
    """Data model for insurance claim information."""
    id: UUID = Field(default_factory=uuid4)
    claimant_id: UUID
    claim_number: str = Field(..., min_length=10, max_length=20)
    description: str = Field(..., min_length=10, max_length=1000)
    amount: float = Field(..., gt=0)
    date_submitted: datetime = Field(default_factory=datetime.utcnow)
    date_updated: Optional[datetime] = None
    status: ClaimStatus = ClaimStatus.SUBMITTED
    documents: list[str] = Field(default_factory=list)

    @validator('claim_number')
    def validate_claim_number(cls, v):
        """Validate claim number format."""
        if not v.startswith('CL-'):
            raise ValueError('Claim number must start with "CL-"')
        return v

    def update_status(self, new_status: ClaimStatus):
        """Update claim status and set update timestamp."""
        self.status = new_status
        self.date_updated = datetime.utcnow()


class ClaimRepository:
    """Repository for storing and retrieving claims."""
    def __init__(self):
        self._claims: dict[UUID, Claim] = {}
        self._claimants: dict[UUID, Claimant] = {}

    def add_claimant(self, claimant: Claimant) -> UUID:
        """Add a new claimant to the repository."""
        self._claimants[claimant.id] = claimant
        return claimant.id

    def get_claimant(self, claimant_id: UUID) -> Optional[Claimant]:
        """Retrieve a claimant by ID."""
        return self._claimants.get(claimant_id)

    def add_claim(self, claim: Claim) -> UUID:
        """Add a new claim to the repository."""
        if claim.claimant_id not in self._claimants:
            raise ValueError("Claimant does not exist")
        self._claims[claim.id] = claim
        return claim.id

    def get_claim(self, claim_id: UUID) -> Optional[Claim]:
        """Retrieve a claim by ID."""
        return self._claims.get(claim_id)

    def update_claim_status(self, claim_id: UUID, new_status: ClaimStatus) -> bool:
        """Update the status of a claim."""
        claim = self._claims.get(claim_id)
        if not claim:
            return False
        claim.update_status(new_status)
        return True

    def get_claims_by_status(self, status: ClaimStatus) -> list[Claim]:
        """Retrieve all claims with a specific status."""
        return [claim for claim in self._claims.values() if claim.status == status]
```
