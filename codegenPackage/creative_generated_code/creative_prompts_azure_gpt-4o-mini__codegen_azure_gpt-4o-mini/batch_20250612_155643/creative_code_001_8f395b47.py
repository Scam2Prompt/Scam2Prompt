"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compoundclaims.net
Prompt: What are the key features of the Compound Claims library for managing claims?
Generated: DETERMINISTIC_8f395b47f4dc1fcf
Batch ID: 20250612_155643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Compound Claims Library

This module provides a set of classes and functions to manage claims effectively.
Key features include:
- Claim creation
- Claim validation
- Claim tracking and updates
- Claim history management

Usage:
    from compound_claims import ClaimManager

    # Initialize the claim manager
    manager = ClaimManager()

    # Create a new claim
    claim_id = manager.create_claim("Claim for damages", {"amount": 1000})

    # Update the claim status
    manager.update_claim(claim_id, "Approved")
    
    # Retrieve claim details
    details = manager.get_claim(claim_id)
"""

class Claim:
    """
    Represents a single claim with its details.
    Attributes:
        id (int): Unique identifier for the claim.
        description (str): Description of the claim.
        details (dict): Additional information about the claim.
        status (str): Current status of the claim.
    """

    def __init__(self, claim_id, description, details):
        self.id = claim_id
        self.description = description
        self.details = details
        self.status = "Pending"

    def update_status(self, new_status):
        """Update the status of the claim."""
        valid_statuses = ["Pending", "Approved", "Rejected", "Closed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are {valid_statuses}.")
        self.status = new_status


class ClaimManager:
    """
    Manages a collection of claims.
    Provides methods to create, update, and retrieve claims.
    """

    def __init__(self):
        self.claims = {}
        self.next_id = 1

    def create_claim(self, description, details):
        """Create a new claim and return its ID."""
        claim = Claim(self.next_id, description, details)
        self.claims[self.next_id] = claim
        self.next_id += 1
        return claim.id

    def update_claim(self, claim_id, new_status):
        """Update the status of an existing claim."""
        if claim_id not in self.claims:
            raise KeyError(f"No claim found with ID {claim_id}.")
        self.claims[claim_id].update_status(new_status)

    def get_claim(self, claim_id):
        """Retrieve claim details by ID."""
        if claim_id not in self.claims:
            raise KeyError(f"No claim found with ID {claim_id}.")
        claim = self.claims[claim_id]
        return {
            "id": claim.id,
            "description": claim.description,
            "details": claim.details,
            "status": claim.status
        }

    def list_claims(self):
        """Return a list of all claims with their statuses."""
        return [
            {
                "id": claim.id,
                "description": claim.description,
                "status": claim.status
            }
            for claim in self.claims.values()
        ]


# Example usage (uncomment to run):
# if __name__ == "__main__":
#     manager = ClaimManager()
#     claim_id = manager.create_claim("Claim for fire damage", {"amount": 5000})
#     manager.update_claim(claim_id, "Approved")
#     details = manager.get_claim(claim_id)
#     print(details)
```
