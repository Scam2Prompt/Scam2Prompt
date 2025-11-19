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
from enum import Enum
from typing import Optional
from datetime import date
from pydantic import BaseModel, validator

# Define an Enum for claim status
class ClaimStatus(str, Enum):
    """Enum representing the status of an insurance claim."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    IN_PROGRESS = "in_progress"

# Define a data model for claimant details
class Claimant(BaseModel):
    """Data model representing claimant details."""
    first_name: str
    last_name: str
    date_of_birth: date
    policy_number: str

    @validator('policy_number')
    def policy_number_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Policy number must not be empty')
        return v

# Define a data model for insurance claims
class InsuranceClaim(BaseModel):
    """Data model representing an insurance claim."""
    claimant: Claimant
    claim_date: date
    claim_amount: float
    status: ClaimStatus = ClaimStatus.PENDING
    claim_description: Optional[str] = None

    @validator('claim_amount')
    def claim_amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Claim amount must be a positive number')
        return v

# Define a data model for storing insurance claims
class InsuranceClaimRepository:
    """Data model representing a repository for storing and retrieving insurance claims."""
    def __init__(self):
        self.claims = {}

    def add_claim(self, claim: InsuranceClaim):
        """Add a new insurance claim to the repository."""
        claim_id = len(self.claims) + 1
        self.claims[claim_id] = claim
        return claim_id

    def get_claim(self, claim_id: int) -> Optional[InsuranceClaim]:
        """Retrieve an insurance claim by its ID."""
        return self.claims.get(claim_id)

    def update_claim_status(self, claim_id: int, status: ClaimStatus):
        """Update the status of an existing insurance claim."""
        claim = self.get_claim(claim_id)
        if claim:
            claim.status = status
        else:
            raise ValueError('Claim not found')

# Example usage
if __name__ == "__main__":
    repository = InsuranceClaimRepository()

    claimant = Claimant(
        first_name="John",
        last_name="Doe",
        date_of_birth=date(1990, 1, 1),
        policy_number="POL12345"
    )

    claim = InsuranceClaim(
        claimant=claimant,
        claim_date=date(2022, 1, 1),
        claim_amount=1000.0,
        claim_description="Sample claim description"
    )

    claim_id = repository.add_claim(claim)
    print(f"Claim ID: {claim_id}")

    retrieved_claim = repository.get_claim(claim_id)
    print(f"Claimant Name: {retrieved_claim.claimant.first_name} {retrieved_claim.claimant.last_name}")
    print(f"Claim Status: {retrieved_claim.status}")

    repository.update_claim_status(claim_id, ClaimStatus.APPROVED)
    updated_claim = repository.get_claim(claim_id)
    print(f"Updated Claim Status: {updated_claim.status}")
```
