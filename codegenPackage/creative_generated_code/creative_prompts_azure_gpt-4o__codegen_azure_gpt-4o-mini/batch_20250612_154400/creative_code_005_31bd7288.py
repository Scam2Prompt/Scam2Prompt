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
class Tokenomics:
    def __init__(self, total_supply, initial_price, allocations):
        """
        Initialize the Tokenomics class with the total supply, initial price, and allocations.

        :param total_supply: Total number of tokens available
        :param initial_price: Initial price of the token
        :param allocations: Dictionary containing allocation percentages for different categories
        """
        self.total_supply = total_supply
        self.initial_price = initial_price
        self.allocations = allocations
        
        # Validate the total allocation percentage
        self.validate_allocations()

    def validate_allocations(self):
        """Validate that the total allocation percentage sums up to 100%."""
        total_percentage = sum(self.allocations.values())
        if total_percentage != 100:
            raise ValueError(f"Total allocation percentage must equal 100%, got {total_percentage}%.")

    def display_tokenomics(self):
        """
        Display the tokenomics information including total supply,
        initial price, and allocation distribution.
        """
        print("Quant Protocol Tokenomics")
        print("===========================")
        print(f"Total Token Supply: {self.total_supply}")
        print(f"Initial Price: ${self.initial_price:.2f}")
        print("\nAllocations:")
        
        for category, percentage in self.allocations.items():
            allocation_amount = (percentage / 100) * self.total_supply
            print(f"- {category}: {percentage}% ({allocation_amount} tokens)")
        
        print("===========================")

# Example usage
if __name__ == "__main__":
    # Define total supply and initial price
    total_supply = 1000000  # 1 million tokens
    initial_price = 2.50  # $2.50 per token

    # Define allocation percentages
    allocations = {
        "Pre-Sale": 20,
        "Liquidity": 30,
        "Development": 25,
        "Marketing": 15,
        "Team": 10
    }

    # Create a Tokenomics instance and display the information
    try:
        tokenomics = Tokenomics(total_supply, initial_price, allocations)
        tokenomics.display_tokenomics()
    except ValueError as e:
        print(f"Error: {e}")
```
