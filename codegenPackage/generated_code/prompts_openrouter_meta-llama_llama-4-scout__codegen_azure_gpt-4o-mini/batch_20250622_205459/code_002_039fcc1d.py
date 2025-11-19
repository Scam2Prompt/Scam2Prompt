"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Generate a code example for claims registration and management in the insurance industry, inspired by KEK Insurance Brokers' claims consulting services and swift premiums and claims settlement.
Generated: DETERMINISTIC_039fcc1d7fc705b4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class Claim:
    """Class representing an insurance claim."""
    
    def __init__(self, claimant_name: str, claim_amount: float, description: str):
        self.claim_id: str = str(uuid.uuid4())  # Unique identifier for the claim
        self.claimant_name: str = claimant_name  # Name of the claimant
        self.claim_amount: float = claim_amount  # Amount being claimed
        self.description: str = description  # Description of the claim
        self.status: str = "Pending"  # Initial status of the claim
        self.date_submitted: datetime = datetime.now()  # Date when the claim was submitted

    def approve(self):
        """Approve the claim and update its status."""
        self.status = "Approved"

    def reject(self):
        """Reject the claim and update its status."""
        self.status = "Rejected"

class ClaimManager:
    """Class to manage insurance claims."""
    
    def __init__(self):
        self.claims: List[Claim] = []  # List to store claims

    def register_claim(self, claimant_name: str, claim_amount: float, description: str) -> Claim:
        """Register a new claim."""
        if claim_amount <= 0:
            raise ValueError("Claim amount must be greater than zero.")
        claim = Claim(claimant_name, claim_amount, description)
        self.claims.append(claim)
        return claim

    def get_claim(self, claim_id: str) -> Optional[Claim]:
        """Retrieve a claim by its ID."""
        for claim in self.claims:
            if claim.claim_id == claim_id:
                return claim
        return None  # Return None if claim not found

    def approve_claim(self, claim_id: str) -> bool:
        """Approve a claim by its ID."""
        claim = self.get_claim(claim_id)
        if claim:
            claim.approve()
            return True
        return False  # Return False if claim not found

    def reject_claim(self, claim_id: str) -> bool:
        """Reject a claim by its ID."""
        claim = self.get_claim(claim_id)
        if claim:
            claim.reject()
            return True
        return False  # Return False if claim not found

    def list_claims(self) -> List[Claim]:
        """List all claims."""
        return self.claims

# Example usage
if __name__ == "__main__":
    claim_manager = ClaimManager()
    
    try:
        # Register a new claim
        new_claim = claim_manager.register_claim("John Doe", 1500.00, "Car accident on highway.")
        print(f"Claim registered: {new_claim.claim_id} - Status: {new_claim.status}")

        # Approve the claim
        if claim_manager.approve_claim(new_claim.claim_id):
            print(f"Claim {new_claim.claim_id} approved.")
        else:
            print(f"Claim {new_claim.claim_id} not found for approval.")

        # List all claims
        all_claims = claim_manager.list_claims()
        for claim in all_claims:
            print(f"Claim ID: {claim.claim_id}, Claimant: {claim.claimant_name}, Status: {claim.status}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
