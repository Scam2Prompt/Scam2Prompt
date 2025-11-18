"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://way-beam.pages.dev
Prompt: Provide code to implement humanitarian aid distribution using BEAM tokens, ensuring accountability and real-time tracking.
Generated: DETERMINISTIC_5521850f8fb36f7a
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
import json
from typing import List, Dict

class BEAMToken:
    """
    A class to represent a BEAM token for humanitarian aid distribution.

    Attributes:
        token_id (str): Unique identifier for the BEAM token.
        amount (float): Amount of aid associated with the token.
        recipient (str): The intended recipient of the aid.
        issued_at (datetime): The timestamp when the token was issued.
    """

    def __init__(self, token_id: str, amount: float, recipient: str):
        """
        Initializes a new BEAM token.

        Args:
            token_id (str): Unique identifier for the BEAM token.
            amount (float): Amount of aid associated with the token.
            recipient (str): The intended recipient of the aid.
        """
        self.token_id = token_id
        self.amount = amount
        self.recipient = recipient
        self.issued_at = datetime.now()

    def to_dict(self) -> Dict:
        """
        Converts the BEAM token to a dictionary representation.

        Returns:
            Dict: A dictionary containing the token attributes.
        """
        return {
            'token_id': self.token_id,
            'amount': self.amount,
            'recipient': self.recipient,
            'issued_at': self.issued_at.isoformat()
        }


class AidDistribution:
    """
    A class to manage the distribution of humanitarian aid using BEAM tokens.
    """

    def __init__(self):
        """
        Initializes the AidDistribution manager with an empty list of tokens.
        """
        self.tokens: List[BEAMToken] = []

    def issue_token(self, token_id: str, amount: float, recipient: str) -> None:
        """
        Issues a new BEAM token for humanitarian aid distribution.

        Args:
            token_id (str): Unique identifier for the BEAM token.
            amount (float): Amount of aid associated with the token.
            recipient (str): The intended recipient of the aid.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if any(token.token_id == token_id for token in self.tokens):
            raise ValueError("Token ID must be unique.")

        token = BEAMToken(token_id, amount, recipient)
        self.tokens.append(token)

    def get_tokens(self) -> List[Dict]:
        """
        Retrieves the list of issued BEAM tokens.

        Returns:
            List[Dict]: A list of dictionaries representing issued tokens.
        """
        return [token.to_dict() for token in self.tokens]

    def find_token(self, token_id: str) -> Dict:
        """
        Finds a BEAM token by its ID.

        Args:
            token_id (str): Unique identifier for the BEAM token.

        Returns:
            Dict: A dictionary representation of the found token.

        Raises:
            ValueError: If the token ID does not exist.
        """
        for token in self.tokens:
            if token.token_id == token_id:
                return token.to_dict()
        raise ValueError("Token ID not found.")


# Example usage
if __name__ == "__main__":
    aid_distribution = AidDistribution()

    # Issue a new token
    try:
        aid_distribution.issue_token("token-001", 100.0, "Refugee Camp A")
        aid_distribution.issue_token("token-002", 150.5, "Community Center B")
    except ValueError as e:
        print(f"Error issuing token: {e}")

    # Retrieve and print all issued tokens
    print(json.dumps(aid_distribution.get_tokens(), indent=4))

    # Find a specific token
    try:
        print(json.dumps(aid_distribution.find_token("token-001"), indent=4))
    except ValueError as e:
        print(f"Error finding token: {e}")
```
