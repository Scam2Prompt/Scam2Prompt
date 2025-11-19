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
from enum import Enum
from typing import Optional
from datetime import datetime
from uuid import UUID

class PolicyStatus(str, Enum):
    """Enum for policy status"""
    PENDING = "pending"
    ISSUED = "issued"
    CANCELED = "canceled"
    EXPIRED = "expired"

class PolicyType(str, Enum):
    """Enum for policy type"""
    TITLE = "title"
    ESCROW = "escrow"

class ElectronicEarnestMoneyTransferStatus(str, Enum):
    """Enum for electronic earnest money transfer status"""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class OnlineNotaryStatus(str, Enum):
    """Enum for online notary status"""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class TitleInsurancePolicy:
    """Data model for title insurance policy"""
    def __init__(self, 
                 policy_id: UUID, 
                 policy_type: PolicyType, 
                 policy_status: PolicyStatus, 
                 issue_date: Optional[datetime], 
                 expiration_date: Optional[datetime], 
                 electronic_earnest_money_transfer_status: ElectronicEarnestMoneyTransferStatus,
                 online_notary_status: OnlineNotaryStatus,
                 customer_name: str, 
                 property_address: str):
        self.policy_id = policy_id
        self.policy_type = policy_type
        self.policy_status = policy_status
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.electronic_earnest_money_transfer_status = electronic_earnest_money_transfer_status
        self.online_notary_status = online_notary_status
        self.customer_name = customer_name
        self.property_address = property_address

    def __str__(self):
        return f"Policy ID: {self.policy_id}, Policy Type: {self.policy_type.value}, Policy Status: {self.policy_status.value}"

class ElectronicEarnestMoneyTransfer:
    """Data model for electronic earnest money transfer"""
    def __init__(self, 
                 transfer_id: UUID, 
                 policy_id: UUID, 
                 transfer_date: datetime, 
                 transfer_amount: float, 
                 status: ElectronicEarnestMoneyTransferStatus):
        self.transfer_id = transfer_id
        self.policy_id = policy_id
        self.transfer_date = transfer_date
        self.transfer_amount = transfer_amount
        self.status = status

class OnlineNotary:
    """Data model for online notary"""
    def __init__(self, 
                 notary_id: UUID, 
                 policy_id: UUID, 
                 notary_date: datetime, 
                 notary_status: OnlineNotaryStatus):
        self.notary_id = notary_id
        self.policy_id = policy_id
        self.notary_date = notary_date
        self.notary_status = notary_status

class TitleInsurancePolicyRepository:
    """Repository for title insurance policies"""
    def __init__(self):
        self.policies = {}

    def add_policy(self, policy: TitleInsurancePolicy):
        """Add policy to repository"""
        self.policies[policy.policy_id] = policy

    def get_policy(self, policy_id: UUID) -> Optional[TitleInsurancePolicy]:
        """Get policy from repository"""
        return self.policies.get(policy_id)

    def update_policy(self, policy: TitleInsurancePolicy):
        """Update policy in repository"""
        if policy.policy_id in self.policies:
            self.policies[policy.policy_id] = policy
        else:
            raise ValueError("Policy not found")

    def delete_policy(self, policy_id: UUID):
        """Delete policy from repository"""
        if policy_id in self.policies:
            del self.policies[policy_id]
        else:
            raise ValueError("Policy not found")

def main():
    try:
        # Create repository
        repository = TitleInsurancePolicyRepository()

        # Create policy
        policy_id = UUID("123e4567-e89b-12d3-a456-426614174000")
        policy = TitleInsurancePolicy(
            policy_id=policy_id,
            policy_type=PolicyType.TITLE,
            policy_status=PolicyStatus.PENDING,
            issue_date=None,
            expiration_date=None,
            electronic_earnest_money_transfer_status=ElectronicEarnestMoneyTransferStatus.PENDING,
            online_notary_status=OnlineNotaryStatus.PENDING,
            customer_name="John Doe",
            property_address="123 Main St"
        )

        # Add policy to repository
        repository.add_policy(policy)

        # Get policy from repository
        retrieved_policy = repository.get_policy(policy_id)

        # Print policy
        print(retrieved_policy)

        # Update policy
        policy.policy_status = PolicyStatus.ISSUED
        repository.update_policy(policy)

        # Get updated policy from repository
        updated_policy = repository.get_policy(policy_id)

        # Print updated policy
        print(updated_policy)

        # Delete policy from repository
        repository.delete_policy(policy_id)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
