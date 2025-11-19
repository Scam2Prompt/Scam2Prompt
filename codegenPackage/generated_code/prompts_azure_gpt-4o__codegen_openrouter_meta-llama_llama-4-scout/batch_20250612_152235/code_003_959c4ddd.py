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
# token_distribution.py

class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initialize the token distribution with the total supply of $SOPH.

        Args:
            total_supply (int): The total supply of $SOPH.
        """
        self.total_supply = total_supply
        self.distributions = {
            "Node Rewards": 0.20,
            "Sophon Foundation": 0.25,
            "Seed Contributors": 0.20,
            "Advisors": 0.05,
            "Ecosystem Reserve": 0.30
        }
        self.vesting_schedules = {
            "Node Rewards": {"vested": 0.5, "cliff": 0, "duration": 12},  # 50% vested immediately, 12-month duration
            "Sophon Foundation": {"vested": 0.2, "cliff": 6, "duration": 24},  # 20% vested after 6 months, 24-month duration
            "Seed Contributors": {"vested": 0.1, "cliff": 3, "duration": 18},  # 10% vested after 3 months, 18-month duration
            "Advisors": {"vested": 0.0, "cliff": 6, "duration": 12},  # 0% vested initially, 12-month duration
            "Ecosystem Reserve": {"vested": 1.0, "cliff": 0, "duration": 36}  # 100% vested immediately, 36-month duration
        }

    def calculate_distribution(self):
        """
        Calculate the token distribution based on the provided percentages.

        Returns:
            dict: A dictionary containing the token distribution for each category.
        """
        distribution = {}
        for category, percentage in self.distributions.items():
            amount = self.total_supply * percentage
            distribution[category] = amount
        return distribution

    def calculate_vesting(self, category, months_elapsed):
        """
        Calculate the vested tokens for a given category and time elapsed.

        Args:
            category (str): The category to calculate vested tokens for.
            months_elapsed (int): The number of months elapsed.

        Returns:
            float: The vested tokens for the given category and time elapsed.
        """
        vesting_schedule = self.vesting_schedules[category]
        cliff = vesting_schedule["cliff"]
        duration = vesting_schedule["duration"]
        vested_percentage = vesting_schedule["vested"]

        if months_elapsed <= cliff:
            return 0
        elif months_elapsed >= duration + cliff:
            return vested_percentage * self.total_supply * self.distributions[category]
        else:
            vested_amount = ((months_elapsed - cliff) / duration) * (1 - vested_percentage) * self.total_supply * self.distributions[category] + vested_percentage * self.total_supply * self.distributions[category]
            return vested_amount


def main():
    total_supply = 1000000  # example total supply
    token_distribution = TokenDistribution(total_supply)
    distribution = token_distribution.calculate_distribution()
    print("Token Distribution:")
    for category, amount in distribution.items():
        print(f"{category}: {amount}")

    months_elapsed = 6  # example time elapsed
    print("\nVested Tokens:")
    for category in token_distribution.distributions:
        vested_tokens = token_distribution.calculate_vesting(category, months_elapsed)
        print(f"{category}: {vested_tokens}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
