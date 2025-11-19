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
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, constr

# Enum for policy status
class PolicyStatus(str):
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

# Model for a party involved in the title insurance policy
class Party(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[constr(regex=r'^\+?\d{10,15}$')] = None  # Optional phone number with regex validation

# Model for earnest money transfer details
class EarnestMoneyTransfer(BaseModel):
    amount: float = Field(..., gt=0)  # Amount must be greater than 0
    transfer_date: datetime
    sender: Party
    receiver: Party

# Model for online notary service details
class NotaryService(BaseModel):
    notary_name: str
    notary_email: EmailStr
    appointment_date: datetime
    location: str

# Main model for Title Insurance Policy
class TitleInsurancePolicy(BaseModel):
    policy_id: str
    property_address: str
    insured_amount: float = Field(..., gt=0)  # Insured amount must be greater than 0
    policy_holder: Party
    status: PolicyStatus
    issue_date: datetime
    expiration_date: datetime
    earnest_money_transfer: Optional[EarnestMoneyTransfer] = None
    notary_service: Optional[NotaryService] = None

    # Method to check if the policy is active
    def is_active(self) -> bool:
        return self.status == PolicyStatus.ACTIVE and self.expiration_date > datetime.now()

    # Method to cancel the policy
    def cancel_policy(self) -> None:
        if self.status == PolicyStatus.ACTIVE:
            self.status = PolicyStatus.CANCELLED
        else:
            raise ValueError("Cannot cancel a policy that is not active.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a policy holder
        policy_holder = Party(
            name="John Doe",
            email="john.doe@example.com",
            phone="+12345678901"
        )

        # Create a title insurance policy
        policy = TitleInsurancePolicy(
            policy_id="POL123456",
            property_address="123 Main St, Anytown, MT",
            insured_amount=250000.00,
            policy_holder=policy_holder,
            status=PolicyStatus.ACTIVE,
            issue_date=datetime.now(),
            expiration_date=datetime(2025, 1, 1)
        )

        # Print policy details
        print(policy.json(indent=4))

        # Check if the policy is active
        print("Is policy active?", policy.is_active())

    except Exception as e:
        print(f"An error occurred: {e}")
```
