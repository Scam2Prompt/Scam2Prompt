"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lossgroupcriteria.com
Prompt: Develop a program to optimize the management of insurance claims across multiple cities, referencing the nationwide presence and operational model of Loss Group Criteria.
Generated: DETERMINISTIC_e93eb6a82c91a2bb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Any, Optional

class Claim:
    """A class representing an insurance claim."""
    
    def __init__(self, claim_id: str, city: str, amount: float, status: str = "Pending"):
        """
        Initialize a new insurance claim.

        :param claim_id: Unique identifier for the claim.
        :param city: The city where the claim originated.
        :param amount: The amount associated with the claim.
        :param status: The current status of the claim (default is 'Pending').
        """
        self.claim_id = claim_id
        self.city = city
        self.amount = amount
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the claim."""
        valid_statuses = ['Pending', 'Approved', 'Rejected']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
        self.status = new_status

    def to_dict(self) -> Dict[str, Any]:
        """Convert the claim to a dictionary for easy serialization."""
        return {
            "claim_id": self.claim_id,
            "city": self.city,
            "amount": self.amount,
            "status": self.status
        }

class ClaimsManager:
    """A class for managing multiple insurance claims."""

    def __init__(self):
        """Initialize the ClaimsManager with an empty claims list."""
        self.claims: List[Claim] = []

    def add_claim(self, claim: Claim):
        """Add a new claim to the manager."""
        self.claims.append(claim)

    def update_claim_status(self, claim_id: str, new_status: str):
        """Update the status of a claim identified by its ID."""
        for claim in self.claims:
            if claim.claim_id == claim_id:
                claim.update_status(new_status)
                return
        raise LookupError(f"Claim ID {claim_id} not found.")

    def get_claims_by_city(self, city: str) -> List[Dict[str, Any]]:
        """Return a list of claims for a specific city."""
        return [claim.to_dict() for claim in self.claims if claim.city.lower() == city.lower()]

    def save_claims(self, filepath: str):
        """Save claims to a JSON file."""
        try:
            with open(filepath, 'w') as file:
                json.dump([claim.to_dict() for claim in self.claims], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving claims to file {filepath}: {str(e)}")

    def load_claims(self, filepath: str):
        """Load claims from a JSON file."""
        try:
            with open(filepath, 'r') as file:
                claims_data = json.load(file)
                for claim_data in claims_data:
                    claim = Claim(
                        claim_id=claim_data['claim_id'],
                        city=claim_data['city'],
                        amount=claim_data['amount'],
                        status=claim_data['status']
                    )
                    self.add_claim(claim)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading claims from file {filepath}: {str(e)}")


if __name__ == "__main__":
    # Example usage of the ClaimsManager
    manager = ClaimsManager()

    # Adding claims
    manager.add_claim(Claim("C001", "New York", 1500.00))
    manager.add_claim(Claim("C002", "Los Angeles", 2000.00))
    
    # Updating a claim's status
    try:
        manager.update_claim_status("C001", "Approved")
    except Exception as e:
        print(f"Error: {e}")

    # Retrieving claims for a specific city
    ny_claims = manager.get_claims_by_city("New York")
    print("Claims in New York:", ny_claims)

    # Saving claims to a file
    try:
        manager.save_claims('claims.json')
        print("Claims saved successfully.")
    except RuntimeError as e:
        print(f"Error: {e}")

    # Loading claims from a file
    try:
        manager.load_claims('claims.json')
        print("Claims loaded successfully.")
    except RuntimeError as e:
        print(f"Error: {e}")
```
