"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy-b3j.pages.dev
Prompt: Write a program to simulate the distribution of "$Gummy" tokens based on the tokenomics percentages provided (e.g., 30% LP burnt, 10% CEX liquidity, 20% market makers, 40% marketing).
Generated: DETERMINISTIC_3bfa5fee68788e5f
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GummyTokenDistribution:
    """
    A class to simulate the distribution of Gummy tokens based on predefined tokenomics percentages.
    """

    def __init__(self, total_tokens):
        """
        Initializes the GummyTokenDistribution with a total number of tokens.

        Args:
            total_tokens (int): The total number of Gummy tokens to distribute.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        self.total_tokens = total_tokens
        self.distribution = {
            "LP_burnt": 0.30,
            "CEX_liquidity": 0.10,
            "market_makers": 0.20,
            "marketing": 0.40
        }

    def distribute_tokens(self):
        """
        Distributes the tokens according to the defined tokenomics percentages.

        Returns:
            dict: A dictionary containing the allocated tokens for each category.
        """
        allocated_tokens = {}
        for category, percentage in self.distribution.items():
            allocated_tokens[category] = self._allocate_tokens(percentage)
        return allocated_tokens

    def _allocate_tokens(self, percentage):
        """
        Allocates tokens based on a given percentage.

        Args:
            percentage (float): The percentage of total tokens to allocate.

        Returns:
            int: The number of tokens allocated to the category.
        """
        if not 0 <= percentage <= 1:
            raise ValueError("Percentage must be between 0 and 1.")
        return int(self.total_tokens * percentage)

    def print_distribution(self):
        """
        Prints the distribution of Gummy tokens in a readable format.
        """
        try:
            distribution = self.distribute_tokens()
            print("Gummy Token Distribution:")
            for category, amount in distribution.items():
                print(f"{category.replace('_', ' ').title()}: {amount} tokens")
        except Exception as e:
            print(f"An error occurred during distribution: {e}")


if __name__ == "__main__":
    try:
        # Example usage:
        total_tokens = 1000000  # Total Gummy tokens to distribute
        distribution_simulator = GummyTokenDistribution(total_tokens)
        distribution_simulator.print_distribution()
    except Exception as e:
        print(f"Initialization failed: {e}")
```
