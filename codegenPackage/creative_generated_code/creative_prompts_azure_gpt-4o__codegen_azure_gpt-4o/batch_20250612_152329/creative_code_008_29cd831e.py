"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Create a function to calculate the total $Jelly tokens claimed and update the percentage dynamically, based on the data structure described on the website.
Generated: DETERMINISTIC_29cd831e002d77e0
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict


class JellyTokenManager:
    """
    Class to manage Jelly Token calculations and update claims dynamically.
    """

    def __init__(self, total_tokens: int):
        """
        Initialize the JellyTokenManager with total tokens available.

        :param total_tokens: Total number of Jelly tokens available for claiming.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        self.total_tokens = total_tokens
        self.claimed_tokens = 0

    def calculate_total_claimed(self, claims: List[Dict[str, int]]) -> int:
        """
        Calculate the total Jelly tokens claimed based on the claims data.

        :param claims: List of claim records where each record is a dictionary 
                       with keys 'user_id' and 'tokens_claimed'.
                       Example: [{'user_id': 1, 'tokens_claimed': 50}, ...]
        :return: Total tokens claimed.
        """
        total_claimed = 0
        for claim in claims:
            try:
                tokens_claimed = claim.get('tokens_claimed', 0)
                if tokens_claimed < 0:
                    raise ValueError("Tokens claimed cannot be negative.")
                total_claimed += tokens_claimed
            except Exception as e:
                print(f"Error processing claim record {claim}: {e}")
        return total_claimed

    def update_claim_percentage(self, total_claimed: int) -> float:
        """
        Update the percentage of Jelly tokens claimed dynamically.

        :param total_claimed: Total tokens claimed so far.
        :return: Percentage of tokens claimed.
        """
        if total_claimed < 0:
            raise ValueError("Total claimed tokens cannot be negative.")
        if total_claimed > self.total_tokens:
            raise ValueError("Total claimed tokens cannot exceed total available tokens.")
        
        self.claimed_tokens = total_claimed
        return (self.claimed_tokens / self.total_tokens) * 100


# Example usage
if __name__ == "__main__":
    # Initialize the JellyTokenManager with a total of 1000 tokens
    manager = JellyTokenManager(total_tokens=1000)

    # Sample claims data
    claims_data = [
        {'user_id': 1, 'tokens_claimed': 50},
        {'user_id': 2, 'tokens_claimed': 150},
        {'user_id': 3, 'tokens_claimed': 200},
    ]

    # Calculate total tokens claimed
    total_claimed = manager.calculate_total_claimed(claims_data)
    print(f"Total Tokens Claimed: {total_claimed}")

    # Update and display the percentage of tokens claimed
    percentage_claimed = manager.update_claim_percentage(total_claimed)
    print(f"Percentage of Tokens Claimed: {percentage_claimed:.2f}%")
```
