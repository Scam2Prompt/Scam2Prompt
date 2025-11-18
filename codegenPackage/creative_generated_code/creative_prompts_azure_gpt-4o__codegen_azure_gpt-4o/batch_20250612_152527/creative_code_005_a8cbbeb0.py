"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Provide an example of a tokenomics calculator in Python that computes the total supply and distribution percentages of $MANIA tokens based on ScapesMania's business model.
Generated: DETERMINISTIC_a8cbbeb0ca06423c
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tokenomics_calculator.py

class TokenomicsCalculator:
    """
    A class to calculate tokenomics for ScapesMania's $MANIA tokens.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenomicsCalculator with the total supply of tokens.

        Args:
        total_supply (float): The total supply of $MANIA tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0.")
        self.total_supply = total_supply
        self.token_distribution = {
            "Team": 0.25,         # 25% allocated to the team
            "Development": 0.15,  # 15% allocated to development
            "Marketing": 0.10,    # 10% allocated to marketing
            "Reserve": 0.20,      # 20% allocated to reserve
            "Community Rewards": 0.30  # 30% allocated to community rewards
        }

    def calculate_distribution(self):
        """
        Calculates the distribution of tokens based on the percentages allocated.

        Returns:
        dict: A dictionary with the token allocations in absolute amounts.
        """
        distribution = {}
        for category, percentage in self.token_distribution.items():
            distribution[category] = self.total_supply * percentage
        return distribution

    def print_distribution(self):
        """
        Prints the token distribution in a user-friendly format.
        """
        distribution = self.calculate_distribution()
        print("\nTokenomics Distribution of $MANIA Tokens:")
        print("-" * 40)
        for category, amount in distribution.items():
            print(f"{category}: {amount:.2f} tokens ({self.token_distribution[category] * 100:.2f}%)")
        print("\nTotal Supply:", self.total_supply, "tokens")
        print("-" * 40)


def main():
    """
    Main function to run the tokenomics calculator.
    """
    try:
        # Assume the total supply is input by the user
        total_supply = float(input("Enter the Total Supply of $MANIA tokens: "))
        calculator = TokenomicsCalculator(total_supply)
        calculator.print_distribution()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
