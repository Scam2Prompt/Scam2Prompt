"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quantprotocol.xyz
Prompt: Generate code to display the tokenomics of Quant Protocol, including percentages for pre-sale, liquidity, development, marketing, and team allocation, along with the total token supply and initial price.
Generated: DETERMINISTIC_31bd7288f530f121
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to display the tokenomics of Quant Protocol

class Tokenomics:
    """
    A class to represent the tokenomics of Quant Protocol.
    Attributes:
        total_supply (int): Total token supply.
        initial_price (float): Initial price per token in USD.
        allocations (dict): Dictionary representing the token allocation breakdown.
    Methods:
        display_tokenomics(): Prints the tokenomics information.
    """

    def __init__(self, total_supply, initial_price, allocations):
        """
        Initializes the Tokenomics object with total supply, initial price, and allocations.
        Args:
            total_supply (int): Total token supply.
            initial_price (float): Initial price per token in USD.
            allocations (dict): Allocation percentages for each category.
        """
        self.total_supply = total_supply
        self.initial_price = initial_price
        self.allocations = allocations

    def display_tokenomics(self):
        """
        Prints the tokenomics information in a readable format.
        """
        print("Quant Protocol Tokenomics:")
        print(f"Total Token Supply: {self.total_supply:,} tokens")
        print(f"Initial Price per Token: ${self.initial_price:.2f}\n")
        print("Allocations:")
        for category, percentage in self.allocations.items():
            print(f"  {category}: {percentage:.2f}%")

# Error handling for invalid tokenomics configuration
def validate_allocations(allocations):
    """
    Validates that the allocation percentages add up to 100.
    Args:
        allocations (dict): Allocation percentages for each category.
    Returns:
        bool: True if allocations are valid, raises ValueError otherwise.
    """
    total_percentage = sum(allocations.values())
    if abs(total_percentage - 100.0) > 1e-6:  # Allowing for minor floating-point inaccuracies
        raise ValueError(f"Allocation percentages do not add up to 100 (total: {total_percentage:.2f}%).")
    return True


def main():
    # Tokenomics configuration
    total_supply = 100_000_000  # 100 million tokens
    initial_price = 0.05  # Initial price per token in USD
    allocations = {
        "Pre-sale": 20.0,
        "Liquidity": 25.0,
        "Development": 30.0,
        "Marketing": 15.0,
        "Team Allocation": 10.0,
    }

    try:
        # Validate allocations before proceeding
        validate_allocations(allocations)

        # Create the Tokenomics object and display details
        quant_protocol_tokenomics = Tokenomics(total_supply, initial_price, allocations)
        quant_protocol_tokenomics.display_tokenomics()
    except ValueError as e:
        # Handle allocation validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
