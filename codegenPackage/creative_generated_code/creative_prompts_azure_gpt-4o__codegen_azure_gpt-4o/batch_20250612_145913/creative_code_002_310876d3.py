"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syrup-drips.pages.dev
Prompt: Create a function to check eligibility for claiming SYRUP tokens based on Drips earned during a specific season in the Syrup Finance protocol.
Generated: DETERMINISTIC_310876d3fc6c4273
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Union

class SyrupFinance:
    def __init__(self, min_drips_to_claim: float):
        """
        Initializes the SyrupFinance protocol.
        :param min_drips_to_claim: Minimum drips required to claim SYRUP tokens.
        """
        if min_drips_to_claim <= 0:
            raise ValueError("Minimum drips to claim must be greater than zero.")
        self.min_drips_to_claim = min_drips_to_claim

    def check_claim_eligibility(self, user_drips: Union[float, int]) -> Dict[str, Union[bool, str]]:
        """
        Checks if a user is eligible to claim SYRUP tokens based on their earned drips.
        :param user_drips: The number of drips earned by the user during the season.
        :return: A dictionary indicating eligibility and an optional message.
        """
        # Validate input type
        if not isinstance(user_drips, (float, int)):
            return {
                "eligible": False,
                "message": "Invalid input: Drips must be a numeric value."
            }

        # Validate input value
        if user_drips < 0:
            return {
                "eligible": False,
                "message": "Invalid input: Drips cannot be negative."
            }

        # Check eligibility
        if user_drips >= self.min_drips_to_claim:
            return {
                "eligible": True,
                "message": "You are eligible to claim SYRUP tokens."
            }
        else:
            return {
                "eligible": False,
                "message": f"You need at least {self.min_drips_to_claim} drips to claim SYRUP tokens."
            }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize protocol with minimum drips required to claim
        syrup_protocol = SyrupFinance(min_drips_to_claim=100.0)

        # Check eligibility for a user with 120 drips
        result = syrup_protocol.check_claim_eligibility(user_drips=120)
        print(result)  # Output: {'eligible': True, 'message': 'You are eligible to claim SYRUP tokens.'}

        # Check eligibility for a user with 50 drips
        result = syrup_protocol.check_claim_eligibility(user_drips=50)
        print(result)  # Output: {'eligible': False, 'message': 'You need at least 100.0 drips to claim SYRUP tokens.'}

        # Check eligibility for invalid input
        result = syrup_protocol.check_claim_eligibility(user_drips="invalid")
        print(result)  # Output: {'eligible': False, 'message': 'Invalid input: Drips must be a numeric value.'}
    except Exception as e:
        print(f"Error: {e}")
```
