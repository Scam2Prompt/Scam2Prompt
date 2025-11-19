"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://site-7eg.pages.dev
Prompt: Can you provide code examples for managing user claims for airdrops, referencing the HYTOPIA model?
Generated: DETERMINISTIC_8f3a378019774bf4
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Optional

class UserClaim:
    """Class to manage user claims for airdrops in the HYTOPIA model."""
    
    def __init__(self, user_id: str):
        """
        Initialize the UserClaim instance.

        :param user_id: Unique identifier for the user.
        """
        self.user_id = user_id
        self.claimed_amount = 0.0
        self.claimable_amount = 0.0

    def set_claimable_amount(self, amount: float):
        """
        Set the amount that the user can claim.

        :param amount: The amount to set as claimable.
        """
        if amount < 0:
            raise ValueError("Claimable amount cannot be negative.")
        self.claimable_amount = amount

    def claim(self, amount: float):
        """
        Allow the user to claim a certain amount of tokens.

        :param amount: The amount the user wants to claim.
        :raises ValueError: If the amount exceeds the claimable amount.
        """
        if amount > self.claimable_amount:
            raise ValueError("Claim amount exceeds claimable amount.")
        self.claimed_amount += amount
        self.claimable_amount -= amount

    def get_claim_summary(self) -> Dict[str, float]:
        """
        Get the summary of claims made by the user.

        :return: A dictionary with claimed and claimable amounts.
        """
        return {
            "user_id": self.user_id,
            "claimed_amount": self.claimed_amount,
            "claimable_amount": self.claimable_amount
        }

class AirdropManager:
    """Class to manage airdrop claims for multiple users."""
    
    def __init__(self):
        """Initialize the AirdropManager with an empty claims dictionary."""
        self.user_claims: Dict[str, UserClaim] = {}

    def add_user(self, user_id: str):
        """
        Add a new user to the airdrop manager.

        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_claims:
            raise ValueError("User already exists.")
        self.user_claims[user_id] = UserClaim(user_id)

    def set_user_claimable(self, user_id: str, amount: float):
        """
        Set the claimable amount for a specific user.

        :param user_id: Unique identifier for the user.
        :param amount: The amount to set as claimable.
        """
        if user_id not in self.user_claims:
            raise ValueError("User does not exist.")
        self.user_claims[user_id].set_claimable_amount(amount)

    def claim_tokens(self, user_id: str, amount: float):
        """
        Process a claim for tokens by a user.

        :param user_id: Unique identifier for the user.
        :param amount: The amount the user wants to claim.
        """
        if user_id not in self.user_claims:
            raise ValueError("User does not exist.")
        self.user_claims[user_id].claim(amount)

    def get_user_claim_summary(self, user_id: str) -> Optional[Dict[str, float]]:
        """
        Get the claim summary for a specific user.

        :param user_id: Unique identifier for the user.
        :return: Claim summary dictionary or None if user does not exist.
        """
        if user_id not in self.user_claims:
            return None
        return self.user_claims[user_id].get_claim_summary()

    def save_claims_to_file(self, filename: str):
        """
        Save all user claims to a JSON file.

        :param filename: The name of the file to save claims to.
        """
        claims_data = {user_id: claim.get_claim_summary() for user_id, claim in self.user_claims.items()}
        with open(filename, 'w') as file:
            json.dump(claims_data, file)

    def load_claims_from_file(self, filename: str):
        """
        Load user claims from a JSON file.

        :param filename: The name of the file to load claims from.
        :raises FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filename, 'r') as file:
                claims_data = json.load(file)
                for user_id, claim_summary in claims_data.items():
                    self.add_user(user_id)
                    self.set_user_claimable(user_id, claim_summary.get("claimable_amount", 0.0))
                    self.user_claims[user_id].claimed_amount = claim_summary.get("claimed_amount", 0.0)
        except FileNotFoundError:
            raise FileNotFoundError("The specified claims file does not exist.")

# Example usage (this should be removed or commented out in production code):
if __name__ == "__main__":
    manager = AirdropManager()
    manager.add_user("user1")
    manager.set_user_claimable("user1", 100.0)
    manager.claim_tokens("user1", 20.0)
    print(manager.get_user_claim_summary("user1"))
    manager.save_claims_to_file("claims.json")
```
