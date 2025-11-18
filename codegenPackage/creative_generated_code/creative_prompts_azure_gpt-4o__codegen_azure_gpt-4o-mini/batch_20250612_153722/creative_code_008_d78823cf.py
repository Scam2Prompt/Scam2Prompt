"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Write a script to calculate and display the token distribution percentages for PENGWU's tokenomics, including presale, liquidity, staking rewards, and team allocations.
Generated: DETERMINISTIC_d78823cf00ab628c
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# token_distribution.py

class TokenDistribution:
    """Class to represent and calculate token distribution percentages."""

    def __init__(self, total_supply):
        """
        Initialize the TokenDistribution class.

        Args:
            total_supply (float): The total supply of tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        
        # Define token allocations as percentages
        self.allocations = {
            'presale': 0.20,  # 20% for presale
            'liquidity': 0.10,  # 10% for liquidity
            'staking_rewards': 0.25,  # 25% for staking rewards
            'team': 0.15,  # 15% for team allocations
            'community': 0.30  # 30% for community incentives
        }

    def calculate_distribution(self):
        """Calculate the token distribution based on predefined allocations."""
        distribution = {}
        for key, percentage in self.allocations.items():
            distribution[key] = self.total_supply * percentage
        return distribution

    def display_distribution(self):
        """Display the token distribution percentages and their respective amounts."""
        try:
            distribution = self.calculate_distribution()
            print("Token Distribution Percentages and Amounts:")
            for key, amount in distribution.items():
                percentage = self.allocations[key] * 100  # Convert to percentage
                print(f"{key.capitalize()}: {percentage:.2f}% - Amount: {amount:.2f} tokens")
        except Exception as e:
            print(f"Error occurred while calculating distribution: {str(e)}")


if __name__ == "__main__":
    try:
        # Example total supply of tokens
        total_supply = 1_000_000  # Total supply of tokens
        token_distribution = TokenDistribution(total_supply)
        token_distribution.display_distribution()
    except ValueError as e:
        print(f"Input error: {str(e)}")
```
