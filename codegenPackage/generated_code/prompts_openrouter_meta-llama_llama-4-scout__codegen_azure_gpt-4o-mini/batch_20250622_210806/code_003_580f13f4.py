"""
Generated Code Metadata:
========================
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Generate a code snippet to calculate the $Gummy token distribution based on the provided percentages for airdrop, CEX liquidity, marketing, LP, and team.
Generated: DETERMINISTIC_580f13f4762f57ae
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GummyTokenDistribution:
    def __init__(self, total_supply):
        """
        Initialize the GummyTokenDistribution with the total supply of tokens.

        :param total_supply: Total number of Gummy tokens to distribute
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution = {
            "airdrop": 0,
            "CEX_liquidity": 0,
            "marketing": 0,
            "LP": 0,
            "team": 0
        }

    def calculate_distribution(self, percentages):
        """
        Calculate the token distribution based on provided percentages.

        :param percentages: Dictionary containing the distribution percentages
        :raises ValueError: If the total percentage does not equal 100
        """
        total_percentage = sum(percentages.values())
        
        if total_percentage != 100:
            raise ValueError("Total percentage must equal 100.")

        for key in self.distribution.keys():
            if key not in percentages:
                raise KeyError(f"Missing distribution percentage for: {key}")
            self.distribution[key] = (percentages[key] / 100) * self.total_supply

    def get_distribution(self):
        """
        Get the calculated token distribution.

        :return: Dictionary containing the token distribution
        """
        return self.distribution


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Total Gummy tokens
        percentages = {
            "airdrop": 20,
            "CEX_liquidity": 30,
            "marketing": 25,
            "LP": 15,
            "team": 10
        }

        gummy_distribution = GummyTokenDistribution(total_supply)
        gummy_distribution.calculate_distribution(percentages)
        print("Gummy Token Distribution:", gummy_distribution.get_distribution())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
