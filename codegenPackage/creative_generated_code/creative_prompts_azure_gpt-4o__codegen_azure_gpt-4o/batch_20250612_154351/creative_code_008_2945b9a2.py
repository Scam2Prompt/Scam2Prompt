"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finflix.me
Prompt: Generate code for a system that matches users with tailored smartphone contracts based on their creditworthiness, as mentioned in the Handyvermittlung service on flix-fin.me.
Generated: DETERMINISTIC_2945b9a2b6fdffdb
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class User:
    """
    Represents a user with basic details and creditworthiness.
    """
    def __init__(self, user_id, name, credit_score):
        self.user_id = user_id
        self.name = name
        self.credit_score = credit_score


class SmartphoneContract:
    """
    Represents a smartphone contract with tailored offers.
    """
    def __init__(self, contract_id, name, min_credit_score, monthly_cost):
        self.contract_id = contract_id
        self.name = name
        self.min_credit_score = min_credit_score
        self.monthly_cost = monthly_cost


class HandyvermittlungService:
    """
    Service for matching users with tailored smartphone contracts based on their creditworthiness.
    """
    def __init__(self):
        self.users = []  # List of registered users
        self.contracts = []  # List of available smartphone contracts

    def add_user(self, user):
        """
        Adds a new user to the service.
        :param user: User object to add.
        """
        if not isinstance(user, User):
            raise TypeError("Invalid user type. Expected 'User'.")
        self.users.append(user)

    def add_contract(self, contract):
        """
        Adds a new contract to the service.
        :param contract: SmartphoneContract object to add.
        """
        if not isinstance(contract, SmartphoneContract):
            raise TypeError("Invalid contract type. Expected 'SmartphoneContract'.")
        self.contracts.append(contract)

    def match_user_with_contract(self, user_id):
        """
        Matches a user with tailored smartphone contracts based on their creditworthiness.
        :param user_id: Unique ID of the user to match.
        :return: List of matched contracts or an error message.
        """
        # Find the user by ID
        user = next((user for user in self.users if user.user_id == user_id), None)
        if not user:
            return {"error": "User not found."}

        # Filter contracts based on the user's credit score
        matched_contracts = [
            contract for contract in self.contracts if user.credit_score >= contract.min_credit_score
        ]

        if not matched_contracts:
            return {"message": f"No contracts available for user '{user.name}' with credit score {user.credit_score}."}

        # Return matched contracts as a JSON response
        result = {
            "user": {"user_id": user.user_id, "name": user.name, "credit_score": user.credit_score},
            "matched_contracts": [
                {
                    "contract_id": contract.contract_id,
                    "name": contract.name,
                    "monthly_cost": contract.monthly_cost,
                    "min_credit_score": contract.min_credit_score
                }
                for contract in matched_contracts
            ]
        }
        return json.dumps(result, indent=4)

# Example usage:
if __name__ == "__main__":
    try:
        # Create a Handyvermittlung service instance
        service = HandyvermittlungService()

        # Add sample users
        service.add_user(User(user_id=1, name="Alice", credit_score=700))
        service.add_user(User(user_id=2, name="Bob", credit_score=500))

        # Add sample contracts
        service.add_contract(SmartphoneContract(contract_id=101, name="Premium Plan", min_credit_score=650, monthly_cost=50))
        service.add_contract(SmartphoneContract(contract_id=102, name="Basic Plan", min_credit_score=400, monthly_cost=20))
        service.add_contract(SmartphoneContract(contract_id=103, name="Standard Plan", min_credit_score=550, monthly_cost=35))

        # Match users with contracts
        print(service.match_user_with_contract(user_id=1))  # Matches Alice
        print(service.match_user_with_contract(user_id=2))  # Matches Bob

    except Exception as e:
        print(f"An error occurred: {e}")
```
