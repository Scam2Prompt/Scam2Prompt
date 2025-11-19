"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a script that calculates the token distribution for $SOPH based on the provided percentages (Node Rewards: 20%, Sophon Foundation: 25%, Seed Contributors: 20%, Advisors: 5%, Ecosystem Reserve: 30%) and includes vesting schedules.
Generated: DETERMINISTIC_959c4ddd6a9b815f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initialize the TokenDistribution with the total supply of tokens.

        :param total_supply: Total number of tokens to distribute
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distributions = {
            "Node Rewards": 0.20,
            "Sophon Foundation": 0.25,
            "Seed Contributors": 0.20,
            "Advisors": 0.05,
            "Ecosystem Reserve": 0.30
        }
        self.vesting_schedules = {
            "Node Rewards": "4 years with a 1-year cliff",
            "Sophon Foundation": "3 years with a 6-month cliff",
            "Seed Contributors": "2 years with a 3-month cliff",
            "Advisors": "1 year with a 1-month cliff",
            "Ecosystem Reserve": "5 years with a 1-year cliff"
        }

    def calculate_distribution(self):
        """
        Calculate the token distribution based on the defined percentages.

        :return: A dictionary with the distribution amounts for each category
        """
        distribution_amounts = {}
        for category, percentage in self.distributions.items():
            distribution_amounts[category] = self.total_supply * percentage
        return distribution_amounts

    def get_vesting_schedule(self):
        """
        Retrieve the vesting schedules for each category.

        :return: A dictionary with the vesting schedules for each category
        """
        return self.vesting_schedules

    def display_distribution(self):
        """
        Display the token distribution and vesting schedules in a readable format.
        """
        distribution = self.calculate_distribution()
        vesting = self.get_vesting_schedule()

        print("Token Distribution for $SOPH:")
        print("-" * 30)
        for category, amount in distribution.items():
            print(f"{category}: {amount:.2f} tokens")
            print(f"  Vesting Schedule: {vesting[category]}")
        print("-" * 30)


if __name__ == "__main__":
    try:
        total_supply = 1_000_000_000  # Example total supply
        token_distribution = TokenDistribution(total_supply)
        token_distribution.display_distribution()
    except ValueError as e:
        print(f"Error: {e}")
```
