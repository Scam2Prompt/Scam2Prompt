"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Design a tokenomics structure for a new cryptocurrency token, similar to PLRT, including token allocation, total supply, and potential use cases.
Generated: DETERMINISTIC_9a88e4179538492f
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    """
    A class to represent the tokenomics structure of a cryptocurrency token.
    """

    def __init__(self, total_supply: int):
        """
        Initializes the Tokenomics with a total supply.

        :param total_supply: Total number of tokens that will ever exist.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.allocations = {
            "team": 0.15,          # 15% for the team
            "advisors": 0.05,      # 5% for advisors
            "development": 0.20,   # 20% for development
            "marketing": 0.10,     # 10% for marketing
            "community": 0.25,     # 25% for community incentives
            "liquidity": 0.10,     # 10% for liquidity
            "reserve": 0.05         # 5% for reserve
        }
        self.token_allocation = self.calculate_allocations()

    def calculate_allocations(self):
        """
        Calculates the number of tokens allocated to each category based on the total supply.

        :return: A dictionary with the number of tokens allocated to each category.
        """
        allocations = {}
        for category, percentage in self.allocations.items():
            allocations[category] = int(self.total_supply * percentage)
        return allocations

    def get_allocation(self, category: str) -> int:
        """
        Retrieves the token allocation for a specific category.

        :param category: The category for which to retrieve the allocation.
        :return: The number of tokens allocated to the specified category.
        """
        if category not in self.token_allocation:
            raise ValueError(f"Category '{category}' does not exist in allocations.")
        return self.token_allocation[category]

    def get_total_supply(self) -> int:
        """
        Retrieves the total supply of the token.

        :return: The total supply of the token.
        """
        return self.total_supply

    def get_allocations(self) -> dict:
        """
        Retrieves the complete token allocation structure.

        :return: A dictionary containing all token allocations.
        """
        return self.token_allocation


# Example usage
if __name__ == "__main__":
    try:
        # Create a new tokenomics structure with a total supply of 1,000,000 tokens
        tokenomics = Tokenomics(total_supply=1000000)

        # Print total supply
        print(f"Total Supply: {tokenomics.get_total_supply()}")

        # Print allocations
        print("Token Allocations:")
        for category, amount in tokenomics.get_allocations().items():
            print(f"{category.capitalize()}: {amount}")

    except ValueError as e:
        print(f"Error: {e}")
```
