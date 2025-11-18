"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Generate code to calculate the distribution of $INIT tokens across different categories (Community Reserve, Investors, Treasury, etc.) based on the tokenomics provided on the Initia website.
Generated: DETERMINISTIC_a987ecbdb837dbbd
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDistribution:
    """
    A class to calculate the distribution of INIT tokens across different categories 
    based on predefined tokenomics percentages.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the TokenDistribution with a total supply of INIT tokens.

        :param total_supply: Total number of INIT tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution = {
            "Community Reserve": 0.20,
            "Investors": 0.25,
            "Treasury": 0.15,
            "Team": 0.20,
            "Development": 0.10,
            "Marketing": 0.10
        }

    def calculate_distribution(self):
        """
        Calculates the distribution of INIT tokens across different categories.

        :return: A dictionary with the number of tokens allocated to each category
        """
        allocations = {}
        for category, percentage in self.distribution.items():
            allocations[category] = self.total_supply * percentage
        return allocations

    def display_distribution(self):
        """
        Displays the token distribution in a readable format.
        """
        try:
            distribution = self.calculate_distribution()
            print("INIT Token Distribution:")
            for category, amount in distribution.items():
                print(f"{category}: {amount:.2f} tokens")
        except Exception as e:
            print(f"Error calculating distribution: {e}")

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply of INIT tokens
        token_distribution = TokenDistribution(total_supply)
        token_distribution.display_distribution()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
