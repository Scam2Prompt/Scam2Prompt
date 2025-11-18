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
import json
from typing import Dict, Any

class TokenDistribution:
    def __init__(self, total_supply: float):
        """
        Initialize the TokenDistribution with the total supply.

        :param total_supply: Total number of tokens available for distribution
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
            "Node Rewards": "4 years vesting with a 1-year cliff",
            "Sophon Foundation": "3 years vesting with a 6-month cliff",
            "Seed Contributors": "2 years vesting with a 3-month cliff",
            "Advisors": "2 years vesting with a 3-month cliff",
            "Ecosystem Reserve": "4 years vesting, no cliff"
        }

    def calculate_distribution(self) -> Dict[str, Any]:
        """
        Calculate the token distribution based on predefined percentages.

        :return: A dictionary containing distribution amounts and vesting schedules
        """
        distribution_results = {}
        for key, percentage in self.distributions.items():
            amount = self.total_supply * percentage
            distribution_results[key] = {
                "amount": amount,
                "vesting_schedule": self.vesting_schedules[key]
            }
        return distribution_results

    def to_json(self) -> str:
        """
        Convert the distribution to a JSON string.

        :return: JSON string representation of the token distribution
        """
        try:
            distribution_data = self.calculate_distribution()
            return json.dumps(distribution_data, indent=4)
        except Exception as e:
            raise RuntimeError(f"An error occurred while converting to JSON: {str(e)}")

if __name__ == "__main__":
    try:
        total_supply = 1_000_000_000  # Example total supply
        distribution = TokenDistribution(total_supply)
        print(distribution.to_json())
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
