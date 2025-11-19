"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ch9.pages.dev
Prompt: Explain the tokenomics of $ROOST, including the breakdown of total supply and distribution for presale participants.
Generated: DETERMINISTIC_96f0b6e823379572
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

class Tokenomics:
    """
    A class to represent the tokenomics of $ROOST.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the Tokenomics class with total supply of tokens.

        :param total_supply: Total supply of $ROOST tokens
        """
        self.total_supply = total_supply
        self.distribution = {}

    def add_distribution(self, category: str, percentage: float):
        """
        Add a category to the distribution and its respective percentage.

        :param category: Name of the distribution category
        :param percentage: Percentage of total supply allocated to the category (0-100)
        :raises ValueError: If percentage is not between 0 and 100, or if total exceeds 100%
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        if sum(self.distribution.values()) + percentage > 100:
            raise ValueError("Total percentage allocation exceeds 100%.")
        self.distribution[category] = percentage

    def calculate_allocation(self) -> dict:
        """
        Calculate the token allocation for each category based on the total supply.

        :return: Dictionary with category names and token amounts
        """
        allocation = {
            category: round((percentage / 100) * self.total_supply)
            for category, percentage in self.distribution.items()
        }
        return allocation

    def to_json(self) -> str:
        """
        Generate a JSON representation of the tokenomics.

        :return: JSON string containing the total supply and distribution breakdown
        """
        data = {
            "total_supply": self.total_supply,
            "distribution": self.calculate_allocation()
        }
        return json.dumps(data, indent=4)


# Usage example
try:
    # Instantiate the Tokenomics class with total supply of $ROOST tokens
    roost_tokenomics = Tokenomics(total_supply=1000000)  # Total supply is 1,000,000 tokens

    # Add distribution categories and their allocation percentages
    roost_tokenomics.add_distribution("Presale Participants", 30.0)  # 30% allocated for presale
    roost_tokenomics.add_distribution("Team and Advisors", 20.0)     # 20% allocated for team
    roost_tokenomics.add_distribution("Marketing and Partnerships", 25.0)  # 25% allocated for marketing
    roost_tokenomics.add_distribution("Reserve Fund", 25.0)          # 25% allocated for reserve fund

    # Print the tokenomics in JSON format
    print(roost_tokenomics.to_json())

except ValueError as e:
    # Handle allocation errors
    print(f"Error: {e}")
```
