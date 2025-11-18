"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Write Python code to simulate a claims registration system for KEK Insurance Brokers, incorporating fields for policy type (e.g., motor insurance, life assurance) and customer details as described on their website.
Generated: DETERMINISTIC_a9a09bb8203ff908
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class Claim:
    """
    Class to represent a claim registered by a customer.
    """

    def __init__(self, customer_name, customer_email, policy_type, claim_details):
        """
        Initializes a new Claim instance.

        :param customer_name: Name of the customer filing the claim.
        :param customer_email: Email of the customer.
        :param policy_type: Type of insurance policy (e.g., motor insurance, life assurance).
        :param claim_details: Detailed information about the claim.
        """
        self.claim_id = str(uuid.uuid4())  # Unique identifier for the claim
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.policy_type = policy_type
        self.claim_details = claim_details
        self.date_filed = datetime.now()
        self.status = 'Pending'  # Initial status of the claim

    def __str__(self):
        """Returns a string representation of the claim."""
        return f"Claim ID: {self.claim_id}, Customer: {self.customer_name}, Policy Type: {self.policy_type}, Status: {self.status}"

class ClaimsRegistrationSystem:
    """
    Class to manage the claims registration system.
    """

    def __init__(self):
        """
        Initializes the Claims Registration System with an empty claims list.
        """
        self.claims = []

    def register_claim(self, customer_name, customer_email, policy_type, claim_details):
        """
        Registers a new claim in the system.

        :param customer_name: Name of the customer filing the claim.
        :param customer_email: Email of the customer.
        :param policy_type: Type of insurance policy.
        :param claim_details: Details of the claim.
        :raises ValueError: If any of the input parameters are invalid.
        """
        if not customer_name or not customer_email or not policy_type or not claim_details:
            raise ValueError("All fields are required to register a claim.")
        
        # Create a new Claim instance
        new_claim = Claim(customer_name, customer_email, policy_type, claim_details)
        
        # Add the claim to the claims list
        self.claims.append(new_claim)
        print(f"Claim registered successfully: {new_claim}")

    def view_claims(self):
        """Views all registered claims."""
        if not self.claims:
            print("No claims registered.")
            return
        
        print("Registered Claims:")
        for claim in self.claims:
            print(claim)
    
    def search_claim(self, claim_id):
        """
        Searches for a specific claim by its ID.

        :param claim_id: The unique ID of the claim to search for.
        :returns: The claim if found, otherwise None.
        """
        for claim in self.claims:
            if claim.claim_id == claim_id:
                return claim
        return None

# Example usage
if __name__ == "__main__":
    system = ClaimsRegistrationSystem()
    
    try:
        # Registering claims
        system.register_claim("John Doe", "john@example.com", "Motor Insurance", "Accident on highway.")
        system.register_claim("Jane Smith", "jane@example.com", "Life Assurance", "Health-related claim.")
        
        # Viewing all registered claims
        system.view_claims()

        # Searching for a specific claim (replace with a valid claim ID from output)
        claim_id_to_search = input("Enter claim ID to search: ")
        claim = system.search_claim(claim_id_to_search)
        if claim:
            print(f"Found claim: {claim}")
        else:
            print("Claim not found.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
