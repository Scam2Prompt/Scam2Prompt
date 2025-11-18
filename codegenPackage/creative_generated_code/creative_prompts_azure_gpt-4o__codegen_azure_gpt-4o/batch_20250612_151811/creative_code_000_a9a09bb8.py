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
import json
import uuid

class ClaimsRegistrationSystem:
    """
    A class to simulate a claims registration system for KEK Insurance Brokers.
    """

    def __init__(self):
        # Initialize an empty list to store claims
        self.claims = []

    def register_claim(self, customer_name, customer_email, policy_type, claim_description):
        """
        Registers a new insurance claim.

        Parameters:
            customer_name (str): Name of the customer.
            customer_email (str): Email of the customer.
            policy_type (str): Type of insurance policy (e.g., Motor Insurance, Life Assurance).
            claim_description (str): Description of the claim.

        Returns:
            dict: Details of the registered claim.
        """
        try:
            # Validate inputs
            if not customer_name or not customer_email or not policy_type or not claim_description:
                raise ValueError("All fields are required.")
            
            # Create a unique claim ID
            claim_id = str(uuid.uuid4())

            # Create the claim record
            claim = {
                "claim_id": claim_id,
                "customer_name": customer_name,
                "customer_email": customer_email,
                "policy_type": policy_type,
                "claim_description": claim_description,
            }
            
            # Add the claim record to the list of claims
            self.claims.append(claim)
            
            # Return the claim details
            return claim

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def list_claims(self):
        """
        Lists all registered claims.

        Returns:
            list: A list of all registered claims.
        """
        return self.claims

    def save_claims_to_file(self, filename):
        """
        Saves all registered claims to a JSON file.

        Parameters:
            filename (str): Name of the file to save the claims.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.claims, file, indent=4)
            print(f"Claims successfully saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving claims to file: {e}")

    def load_claims_from_file(self, filename):
        """
        Loads claims from a JSON file.

        Parameters:
            filename (str): Name of the file to load the claims.

        Returns:
            list: A list of claims loaded from the file.
        """
        try:
            with open(filename, 'r') as file:
                self.claims = json.load(file)
            print(f"Claims successfully loaded from {filename}.")
            return self.claims
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading claims from file: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Instantiate the claims registration system
    kek_insurance = ClaimsRegistrationSystem()

    # Register a new claim
    claim = kek_insurance.register_claim(
        customer_name="John Doe",
        customer_email="johndoe@example.com",
        policy_type="Motor Insurance",
        claim_description="Car accident on Highway 50."
    )
    if claim:
        print("Registered Claim:", claim)

    # List all claims
    print("All Claims:", kek_insurance.list_claims())

    # Save claims to a file
    kek_insurance.save_claims_to_file("claims.json")

    # Load claims from a file
    loaded_claims = kek_insurance.load_claims_from_file("claims.json")
    print("Loaded Claims:", loaded_claims)
```
