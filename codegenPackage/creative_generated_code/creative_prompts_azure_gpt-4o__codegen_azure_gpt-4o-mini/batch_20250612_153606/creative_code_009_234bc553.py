"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Develop a tokenomics optimization tool for Web3 startups, incorporating features like those mentioned in the mentorship and workshop sessions of the Proof of Pitch competition.
Generated: DETERMINISTIC_234bc553569851b3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class TokenomicsOptimizer:
    """
    A class to model a tokenomics optimization tool for Web3 startups.
    It provides methods to calculate token distribution, inflation rates, and vesting schedules.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the TokenomicsOptimizer with a total token supply.

        Args:
            total_supply (float): The total number of tokens available for distribution.
        """
        self.total_supply = total_supply
        self.distribution: Dict[str, float] = {}
        self.vesting_schedule: Dict[str, List[Dict[str, float]]] = {}

    def add_distribution(self, category: str, amount: float) -> None:
        """
        Adds a distribution category and its corresponding token amount.

        Args:
            category (str): The category for the token distribution (e.g., Team, Advisors, Marketing).
            amount (float): The amount of tokens allocated to this category.
        
        Raises:
            ValueError: If the amount exceeds the remaining supply or is negative.
        """
        if amount < 0:
            raise ValueError("Distribution amount cannot be negative.")
        if sum(self.distribution.values()) + amount > self.total_supply:
            raise ValueError("Total distribution exceeds the total supply.")
        
        self.distribution[category] = self.distribution.get(category, 0) + amount

    def calculate_inflation_rate(self, current_supply: float, target_supply: float, years: int) -> float:
        """
        Calculates the annual inflation rate required to reach a target supply.

        Args:
            current_supply (float): The current number of tokens in circulation.
            target_supply (float): The target number of tokens to reach.
            years (int): The number of years over which the inflation will occur.
        
        Returns:
            float: The annual inflation rate as a percentage.
        """
        if current_supply <= 0 or years <= 0:
            raise ValueError("Current supply and years must be positive.")
        return ((target_supply / current_supply) ** (1 / years) - 1) * 100

    def add_vesting_schedule(self, category: str, schedule: List[Dict[str, float]]) -> None:
        """
        Adds a vesting schedule for a distribution category.

        Args:
            category (str): The category associated with the vesting schedule.
            schedule (List[Dict[str, float]]): A list of vesting milestones, where each milestone has a date and amount.
        
        Raises:
            ValueError: If any milestone has a negative amount.
        """
        for milestone in schedule:
            if milestone['amount'] < 0:
                raise ValueError("Vesting amounts cannot be negative.")
        
        self.vesting_schedule[category] = schedule

    def export_to_json(self, filename: str) -> None:
        """
        Exports the current tokenomics data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "total_supply": self.total_supply,
                    "distribution": self.distribution,
                    "vesting_schedule": self.vesting_schedule
                }, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        optimizer = TokenomicsOptimizer(total_supply=1_000_000_000)
        optimizer.add_distribution("Team", 200_000_000)
        optimizer.add_distribution("Advisors", 100_000_000)
        optimizer.add_distribution("Marketing", 50_000_000)
        
        inflation_rate = optimizer.calculate_inflation_rate(current_supply=100_000_000, target_supply=1_000_000_000, years=5)
        print(f"Required annual inflation rate: {inflation_rate:.2f}%")
        
        vesting_schedule = [
            {"date": "2024-01-01", "amount": 50000000},
            {"date": "2025-01-01", "amount": 50000000}
        ]
        optimizer.add_vesting_schedule("Team", vesting_schedule)
        
        optimizer.export_to_json("tokenomics.json")
        print("Tokenomics data exported successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
