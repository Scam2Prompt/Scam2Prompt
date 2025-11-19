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

class Claim:
    """
    Represents an insurance claim.
    """
    def __init__(self, policy_number, claimant_name, claim_amount, claim_reason):
        """
        Initializes a new claim instance.

        :param policy_number: The policy number associated with the claim.
        :param claimant_name: Name of the person filing the claim.
        :param claim_amount: Amount being claimed.
        :param claim_reason: Reason for the claim.
        """
        self.claim_id = str(uuid.uuid4())  # Generate a unique claim ID
        self.policy_number = policy_number
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount
        self.claim_reason = claim_reason
        self.status = "Pending"  # Initial status of the claim
        self.created_at = datetime.now()  # Timestamp of claim creation

    def update_status(self, new_status):
        """
        Updates the status of the claim.

        :param new_status: The new status to set for the claim.
        """
        valid_statuses = ["Pending", "Approved", "Rejected", "Settled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status


class ClaimsManager:
    """
    Manages claims registration and processing.
    """
    def __init__(self):
        """
        Initializes the ClaimsManager with an empty list of claims.
        """
        self.claims = []

    def register_claim(self, policy_number, claimant_name, claim_amount, claim_reason):
        """
        Registers a new claim.

        :param policy_number: The policy number associated with the claim.
        :param claimant_name: Name of the person filing the claim.
        :param claim_amount: Amount being claimed.
        :param claim_reason: Reason for the claim.
        :return: The newly created Claim object.
        """
        if claim_amount <= 0:
            raise ValueError("Claim amount must be greater than zero.")
        new_claim = Claim(policy_number, claimant_name, claim_amount, claim_reason)
        self.claims.append(new_claim)
        return new_claim

    def get_claim_by_id(self, claim_id):
        """
        Retrieves a claim by its ID.

        :param claim_id: The ID of the claim to retrieve.
        :return: The Claim object if found, None otherwise.
        """
        for claim in self.claims:
            if claim.claim_id == claim_id:
                return claim
        return None

    def update_claim_status(self, claim_id, new_status):
        """
        Updates the status of a claim.

        :param claim_id: The ID of the claim to update.
        :param new_status: The new status to set for the claim.
        :return: True if the update was successful, False otherwise.
        """
        claim = self.get_claim_by_id(claim_id)
        if not claim:
            raise ValueError(f"No claim found with ID: {claim_id}")
        claim.update_status(new_status)
        return True

    def list_claims(self):
        """
        Lists all registered claims.

        :return: A list of all Claim objects.
        """
        return self.claims


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the ClaimsManager
        manager = ClaimsManager()

        # Register a new claim
        claim = manager.register_claim(
            policy_number="POL12345",
            claimant_name="John Doe",
            claim_amount=5000.00,
            claim_reason="Car accident"
        )
        print(f"Claim registered successfully: {claim.claim_id}")

        # Update claim status
        manager.update_claim_status(claim.claim_id, "Approved")
        print(f"Claim status updated to: {claim.status}")

        # List all claims
        claims = manager.list_claims()
        for c in claims:
            print(f"Claim ID: {c.claim_id}, Status: {c.status}, Amount: {c.claim_amount}")

    except Exception as e:
        print(f"Error: {e}")
```
