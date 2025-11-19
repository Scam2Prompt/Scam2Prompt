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
import uuid

# Define the data model for Title Insurance Policies
class TitleInsurancePolicy:
    """
    Represents a title insurance policy.
    """
    def __init__(self, policy_id: str, property_address: str, insured_name: str, policy_amount: float, 
                 issue_date: datetime, expiration_date: datetime, is_active: bool):
        """
        Initialize a TitleInsurancePolicy instance.

        :param policy_id: Unique identifier for the policy
        :param property_address: Address of the insured property
        :param insured_name: Name of the insured party
        :param policy_amount: Amount covered by the policy
        :param issue_date: Date the policy was issued
        :param expiration_date: Date the policy expires
        :param is_active: Whether the policy is currently active
        """
        self.policy_id = policy_id
        self.property_address = property_address
        self.insured_name = insured_name
        self.policy_amount = policy_amount
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.is_active = is_active

    def __repr__(self):
        return f"<TitleInsurancePolicy(policy_id={self.policy_id}, insured_name={self.insured_name}, is_active={self.is_active})>"

    def deactivate_policy(self):
        """
        Deactivate the policy.
        """
        self.is_active = False

    def activate_policy(self):
        """
        Activate the policy.
        """
        self.is_active = True


class EarnestMoneyTransfer:
    """
    Represents an electronic earnest money transfer.
    """
    def __init__(self, transfer_id: str, sender_name: str, receiver_name: str, amount: float, transfer_date: datetime):
        """
        Initialize an EarnestMoneyTransfer instance.

        :param transfer_id: Unique identifier for the transfer
        :param sender_name: Name of the sender
        :param receiver_name: Name of the receiver
        :param amount: Amount of money transferred
        :param transfer_date: Date of the transfer
        """
        self.transfer_id = transfer_id
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.amount = amount
        self.transfer_date = transfer_date

    def __repr__(self):
        return f"<EarnestMoneyTransfer(transfer_id={self.transfer_id}, amount={self.amount})>"


class OnlineNotaryService:
    """
    Represents an online notary service.
    """
    def __init__(self, notary_id: str, notary_name: str, document_id: str, notarization_date: datetime):
        """
        Initialize an OnlineNotaryService instance.

        :param notary_id: Unique identifier for the notary service
        :param notary_name: Name of the notary
        :param document_id: ID of the document being notarized
        :param notarization_date: Date of notarization
        """
        self.notary_id = notary_id
        self.notary_name = notary_name
        self.document_id = document_id
        self.notarization_date = notarization_date

    def __repr__(self):
        return f"<OnlineNotaryService(notary_id={self.notary_id}, document_id={self.document_id})>"


class TitleInsuranceManagementSystem:
    """
    A system for managing title insurance policies, earnest money transfers, and online notary services.
    """
    def __init__(self):
        """
        Initialize the management system with empty lists for policies, transfers, and notary services.
        """
        self.policies: List[TitleInsurancePolicy] = []
        self.transfers: List[EarnestMoneyTransfer] = []
        self.notary_services: List[OnlineNotaryService] = []

    def add_policy(self, property_address: str, insured_name: str, policy_amount: float, 
                   issue_date: datetime, expiration_date: datetime) -> TitleInsurancePolicy:
        """
        Add a new title insurance policy to the system.

        :param property_address: Address of the insured property
        :param insured_name: Name of the insured party
        :param policy_amount: Amount covered by the policy
        :param issue_date: Date the policy was issued
        :param expiration_date: Date the policy expires
        :return: The created TitleInsurancePolicy instance
        """
        policy_id = str(uuid.uuid4())  # Generate a unique ID for the policy
        policy = TitleInsurancePolicy(policy_id, property_address, insured_name, policy_amount, issue_date, expiration_date, True)
        self.policies.append(policy)
        return policy

    def add_transfer(self, sender_name: str, receiver_name: str, amount: float, transfer_date: datetime) -> EarnestMoneyTransfer:
        """
        Add a new earnest money transfer to the system.

        :param sender_name: Name of the sender
        :param receiver_name: Name of the receiver
        :param amount: Amount of money transferred
        :param transfer_date: Date of the transfer
        :return: The created EarnestMoneyTransfer instance
        """
        transfer_id = str(uuid.uuid4())  # Generate a unique ID for the transfer
        transfer = EarnestMoneyTransfer(transfer_id, sender_name, receiver_name, amount, transfer_date)
        self.transfers.append(transfer)
        return transfer

    def add_notary_service(self, notary_name: str, document_id: str, notarization_date: datetime) -> OnlineNotaryService:
        """
        Add a new online notary service to the system.

        :param notary_name: Name of the notary
        :param document_id: ID of the document being notarized
        :param notarization_date: Date of notarization
        :return: The created OnlineNotaryService instance
        """
        notary_id = str(uuid.uuid4())  # Generate a unique ID for the notary service
        notary_service = OnlineNotaryService(notary_id, notary_name, document_id, notarization_date)
        self.notary_services.append(notary_service)
        return notary_service

    def get_active_policies(self) -> List[TitleInsurancePolicy]:
        """
        Retrieve all active title insurance policies.

        :return: List of active TitleInsurancePolicy instances
        """
        return [policy for policy in self.policies if policy.is_active]

    def deactivate_policy(self, policy_id: str) -> Optional[TitleInsurancePolicy]:
        """
        Deactivate a title insurance policy by its ID.

        :param policy_id: ID of the policy to deactivate
        :return: The deactivated TitleInsurancePolicy instance, or None if not found
        """
        for policy in self.policies:
            if policy.policy_id == policy_id:
                policy.deactivate_policy()
                return policy
        return None
```
