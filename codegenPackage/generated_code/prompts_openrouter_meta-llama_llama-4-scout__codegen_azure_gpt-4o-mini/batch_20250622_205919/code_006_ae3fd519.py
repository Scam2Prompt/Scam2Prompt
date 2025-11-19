"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Generate a Hash AI token distribution plan, considering factors like token holder income sharing, mining facility expansion, and global leadership in sustainable mining practices.
Generated: DETERMINISTIC_ae3fd519916285d4
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class TokenDistributionPlan:
    def __init__(self, total_tokens: int):
        """
        Initialize the TokenDistributionPlan with the total number of tokens.

        :param total_tokens: Total number of tokens to be distributed.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        self.total_tokens = total_tokens
        self.distribution: Dict[str, float] = {
            "income_sharing": 0.0,
            "mining_expansion": 0.0,
            "sustainable_practices": 0.0,
            "reserve": 0.0
        }

    def set_distribution(self, income_sharing: float, mining_expansion: float, sustainable_practices: float, reserve: float):
        """
        Set the distribution percentages for each category.

        :param income_sharing: Percentage of tokens for income sharing.
        :param mining_expansion: Percentage of tokens for mining facility expansion.
        :param sustainable_practices: Percentage of tokens for sustainable mining practices.
        :param reserve: Percentage of tokens for reserve.
        """
        total_percentage = income_sharing + mining_expansion + sustainable_practices + reserve
        if total_percentage != 100.0:
            raise ValueError("Total distribution percentages must equal 100.")
        
        self.distribution["income_sharing"] = income_sharing
        self.distribution["mining_expansion"] = mining_expansion
        self.distribution["sustainable_practices"] = sustainable_practices
        self.distribution["reserve"] = reserve

    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate the number of tokens allocated to each category based on the distribution percentages.

        :return: A dictionary with the number of tokens allocated to each category.
        """
        return {key: int((value / 100) * self.total_tokens) for key, value in self.distribution.items()}

    def to_json(self) -> str:
        """
        Convert the distribution plan to a JSON string.

        :return: JSON representation of the distribution plan.
        """
        return json.dumps({
            "total_tokens": self.total_tokens,
            "distribution": self.distribution,
            "allocated_tokens": self.calculate_distribution()
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the token distribution plan with a total of 1,000,000 tokens
        plan = TokenDistributionPlan(total_tokens=1000000)

        # Set the distribution percentages
        plan.set_distribution(income_sharing=40.0, mining_expansion=30.0, sustainable_practices=20.0, reserve=10.0)

        # Print the distribution plan in JSON format
        print(plan.to_json())
    except ValueError as e:
        print(f"Error: {e}")
```
