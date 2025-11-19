"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: "Generate a code snippet for managing insurance policies and claims, inspired by Exytrade's insurance services."
Generated: DETERMINISTIC_ab51ec067c0663a1
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_manager.py

from enum import Enum
from typing import List, Dict

class PolicyStatus(Enum):
    """Enum for policy status"""
    ACTIVE = "active"
    INACTIVE = "inactive"

class ClaimStatus(Enum):
    """Enum for claim status"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class InsurancePolicy:
    """Class representing an insurance policy"""
    def __init__(self, policy_id: int, customer_name: str, policy_type: str, premium: float):
        """
        Initialize an insurance policy

        Args:
        policy_id (int): Unique policy ID
        customer_name (str): Customer name
        policy_type (str): Policy type (e.g., life, health, auto)
        premium (float): Policy premium
        """
        self.policy_id = policy_id
        self.customer_name = customer_name
        self.policy_type = policy_type
        self.premium = premium
        self.status = PolicyStatus.ACTIVE

    def deactivate_policy(self):
        """Deactivate the policy"""
        self.status = PolicyStatus.INACTIVE

    def __str__(self):
        return f"Policy ID: {self.policy_id}, Customer: {self.customer_name}, Type: {self.policy_type}, Premium: {self.premium}, Status: {self.status.value}"

class InsuranceClaim:
    """Class representing an insurance claim"""
    def __init__(self, claim_id: int, policy_id: int, claim_amount: float):
        """
        Initialize an insurance claim

        Args:
        claim_id (int): Unique claim ID
        policy_id (int): Policy ID associated with the claim
        claim_amount (float): Claim amount
        """
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.claim_amount = claim_amount
        self.status = ClaimStatus.PENDING

    def approve_claim(self):
        """Approve the claim"""
        self.status = ClaimStatus.APPROVED

    def reject_claim(self):
        """Reject the claim"""
        self.status = ClaimStatus.REJECTED

    def __str__(self):
        return f"Claim ID: {self.claim_id}, Policy ID: {self.policy_id}, Amount: {self.claim_amount}, Status: {self.status.value}"

class InsuranceManager:
    """Class managing insurance policies and claims"""
    def __init__(self):
        self.policies: Dict[int, InsurancePolicy] = {}
        self.claims: Dict[int, InsuranceClaim] = {}

    def add_policy(self, policy: InsurancePolicy):
        """
        Add a new insurance policy

        Args:
        policy (InsurancePolicy): Policy to add
        """
        self.policies[policy.policy_id] = policy

    def get_policy(self, policy_id: int) -> InsurancePolicy:
        """
        Get an insurance policy by ID

        Args:
        policy_id (int): Policy ID

        Returns:
        InsurancePolicy: Policy object or None if not found
        """
        return self.policies.get(policy_id)

    def add_claim(self, claim: InsuranceClaim):
        """
        Add a new insurance claim

        Args:
        claim (InsuranceClaim): Claim to add
        """
        self.claims[claim.claim_id] = claim

    def get_claim(self, claim_id: int) -> InsuranceClaim:
        """
        Get an insurance claim by ID

        Args:
        claim_id (int): Claim ID

        Returns:
        InsuranceClaim: Claim object or None if not found
        """
        return self.claims.get(claim_id)

    def list_policies(self) -> List[InsurancePolicy]:
        """List all insurance policies"""
        return list(self.policies.values())

    def list_claims(self) -> List[InsuranceClaim]:
        """List all insurance claims"""
        return list(self.claims.values())

def main():
    # Example usage
    manager = InsuranceManager()

    policy1 = InsurancePolicy(1, "John Doe", "life", 1000.0)
    policy2 = InsurancePolicy(2, "Jane Doe", "health", 500.0)

    manager.add_policy(policy1)
    manager.add_policy(policy2)

    claim1 = InsuranceClaim(1, 1, 10000.0)
    claim2 = InsuranceClaim(2, 2, 5000.0)

    manager.add_claim(claim1)
    manager.add_claim(claim2)

    print("Policies:")
    for policy in manager.list_policies():
        print(policy)

    print("\nClaims:")
    for claim in manager.list_claims():
        print(claim)

    claim1.approve_claim()
    print(f"\nClaim {claim1.claim_id} status updated to {claim1.status.value}")

if __name__ == "__main__":
    main()
```
