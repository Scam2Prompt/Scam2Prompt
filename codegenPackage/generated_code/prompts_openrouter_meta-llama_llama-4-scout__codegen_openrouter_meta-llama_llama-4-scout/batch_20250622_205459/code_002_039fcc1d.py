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
# claims_management_system.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class ClaimStatus(Enum):
    """Enum for claim status"""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    PAID = "Paid"

class Claim:
    """Class representing an insurance claim"""
    def __init__(self, claim_id: int, policy_id: int, claim_date: datetime, claim_amount: float, status: ClaimStatus = ClaimStatus.PENDING):
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.claim_date = claim_date
        self.claim_amount = claim_amount
        self.status = status

class Policy:
    """Class representing an insurance policy"""
    def __init__(self, policy_id: int, customer_name: str, policy_date: datetime, premium: float):
        self.policy_id = policy_id
        self.customer_name = customer_name
        self.policy_date = policy_date
        self.premium = premium

class ClaimsManagementSystem:
    """Class managing insurance claims"""
    def __init__(self):
        self.claims: Dict[int, Claim] = {}
        self.policies: Dict[int, Policy] = {}

    def add_policy(self, policy: Policy):
        """Add a policy to the system"""
        self.policies[policy.policy_id] = policy

    def add_claim(self, claim: Claim):
        """Add a claim to the system"""
        if claim.policy_id not in self.policies:
            raise ValueError("Policy not found")
        self.claims[claim.claim_id] = claim

    def update_claim_status(self, claim_id: int, status: ClaimStatus):
        """Update the status of a claim"""
        if claim_id not in self.claims:
            raise ValueError("Claim not found")
        self.claims[claim_id].status = status

    def get_claim(self, claim_id: int) -> Claim:
        """Get a claim by ID"""
        return self.claims.get(claim_id)

    def get_policy(self, policy_id: int) -> Policy:
        """Get a policy by ID"""
        return self.policies.get(policy_id)

    def settle_claim(self, claim_id: int):
        """Settle a claim"""
        claim = self.get_claim(claim_id)
        if claim and claim.status == ClaimStatus.APPROVED:
            claim.status = ClaimStatus.PAID
            print(f"Claim {claim_id} settled")
        else:
            print(f"Claim {claim_id} not found or not approved")

def main():
    # Create a claims management system
    cms = ClaimsManagementSystem()

    # Create policies
    policy1 = Policy(1, "John Doe", datetime(2022, 1, 1), 1000.0)
    policy2 = Policy(2, "Jane Doe", datetime(2022, 6, 1), 2000.0)

    # Add policies to the system
    cms.add_policy(policy1)
    cms.add_policy(policy2)

    # Create claims
    claim1 = Claim(1, 1, datetime(2022, 2, 1), 500.0)
    claim2 = Claim(2, 2, datetime(2022, 7, 1), 1000.0)

    # Add claims to the system
    cms.add_claim(claim1)
    cms.add_claim(claim2)

    # Update claim status
    cms.update_claim_status(1, ClaimStatus.APPROVED)

    # Settle claim
    cms.settle_claim(1)

    # Print claim status
    claim = cms.get_claim(1)
    print(f"Claim {claim.claim_id} status: {claim.status.value}")

if __name__ == "__main__":
    main()
```
