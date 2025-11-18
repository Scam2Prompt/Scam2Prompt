"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a script that calculates the token distribution for $SOPH based on the provided percentages (Node Rewards: 20%, Sophon Foundation: 25%, Seed Contributors: 20%, Advisors: 5%, Ecosystem Reserve: 30%) and includes vesting schedules.
Generated: DETERMINISTIC_959c4ddd6a9b815f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# token_distribution.py

from typing import Dict

class TokenDistributor:
    """
    Class to handle token distribution and vesting schedules for $SOPH.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the TokenDistributor with the total supply of tokens.
        :param total_supply: Total number of $SOPH tokens available for distribution.
        """
        self.total_supply = total_supply
        self.distribution_percentages = {
            "Node Rewards": 0.20,
            "Sophon Foundation": 0.25,
            "Seed Contributors": 0.20,
            "Advisors": 0.05,
            "Ecosystem Reserve": 0.30,
        }
        self.distribution = self.calculate_distribution()
        self.vesting_schedules = self.create_vesting_schedule()

    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate the token allocation based on the provided percentages.
        :return: Dictionary mapping allocation categories to token amounts.
        """
        distribution = {}
        for category, percentage in self.distribution_percentages.items():
            # Calculate tokens for each category based on percentage
            distribution[category] = int(self.total_supply * percentage)
        return distribution

    def create_vesting_schedule(self) -> Dict[str, str]:
        """
        Define vesting schedules for each category.
        :return: Dictionary mapping allocation categories to vesting schedules.
        """
        # Example vesting schedules (adjust as needed for real-world scenarios)
        vesting_schedules = {
            "Node Rewards": "100% unlocked immediately.",
            "Sophon Foundation": "25% unlocked annually over 4 years.",
            "Seed Contributors": "25% unlocked annually over 4 years.",
            "Advisors": "20% unlocked annually over 5 years.",
            "Ecosystem Reserve": "100% unlocked immediately, used as needed.",
        }
        return vesting_schedules

    def display_distribution_and_vesting(self):
        """
        Display the token distribution and vesting schedules.
        """
        print("Token Distribution:")
        for category, tokens in self.distribution.items():
            print(f"{category}: {tokens} tokens")
        print("\nVesting Schedules:")
        for category, schedule in self.vesting_schedules.items():
            print(f"{category}: {schedule}")

# Error handling: Ensure input is valid
def main():
    try:
        # Example: Total supply of $SOPH tokens
        total_supply = int(input("Enter total supply of $SOPH tokens: "))
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")

        # Create instance of TokenDistributor
        distributor = TokenDistributor(total_supply)
        distributor.display_distribution_and_vesting()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
