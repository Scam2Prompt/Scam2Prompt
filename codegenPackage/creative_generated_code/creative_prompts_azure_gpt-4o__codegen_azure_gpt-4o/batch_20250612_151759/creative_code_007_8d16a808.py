"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sallysui.com
Prompt: Write code to calculate the distribution of $sally tokens among holders, ensuring transparency in community-driven projects.
Generated: DETERMINISTIC_8d16a808010c84aa
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Tuple

class SallyTokenDistributor:
    """
    A class to calculate and distribute Sally tokens among holders.
    Ensures transparency in the distribution of tokens in community-driven projects.
    """

    def __init__(self, total_tokens: float, holders: Dict[str, float]):
        """
        Initialize the distributor with the total tokens and the holders' stakes.

        :param total_tokens: Total number of Sally tokens available for distribution.
        :param holders: Dictionary representing holders and their stakes (e.g., {"Alice": 100, "Bob": 200}).
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        if not holders or any(stake <= 0 for stake in holders.values()):
            raise ValueError("Holders must have valid positive stakes.")
        
        self.total_tokens = total_tokens
        self.holders = holders

    def calculate_distribution(self) -> Dict[str, float]:
        """
        Calculate the distribution of tokens among holders based on their stakes.

        :return: A dictionary with holders as keys and their assigned tokens as values.
        """
        # Calculate the total stake to determine proportional distribution
        total_stake = sum(self.holders.values())
        if total_stake == 0:
            raise ValueError("Total stake must be greater than zero.")

        # Calculate and return the token distribution
        distribution = {
            holder: round((stake / total_stake) * self.total_tokens, 2)  # Round for clarity
            for holder, stake in self.holders.items()
        }
        return distribution

    def display_distribution(self, distribution: Dict[str, float]) -> None:
        """
        Display the token distribution in a human-readable format.

        :param distribution: A dictionary representing the token distribution.
        """
        print("Sally Token Distribution:")
        print("-" * 30)
        for holder, tokens in distribution.items():
            print(f"{holder}: {tokens:.2f} tokens")
        print("-" * 30)


# Example usage
if __name__ == "__main__":
    try:
        # Define total Sally tokens and holders with their respective stakes
        TOTAL_TOKENS = 1000.0  # Total available tokens
        HOLDERS = {
            "Alice": 100,
            "Bob": 200,
            "Charlie": 300,
            "Diana": 400
        }

        # Instantiate the distributor
        distributor = SallyTokenDistributor(TOTAL_TOKENS, HOLDERS)
        
        # Calculate distribution
        token_distribution = distributor.calculate_distribution()
        
        # Display distribution
        distributor.display_distribution(token_distribution)
    except Exception as e:
        print(f"Error: {e}")
```
