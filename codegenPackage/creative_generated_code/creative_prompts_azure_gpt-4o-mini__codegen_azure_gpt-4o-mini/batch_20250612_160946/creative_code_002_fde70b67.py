"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Generate a code snippet for calculating the total supply and allocation percentages for Doge2014 tokens based on the provided tokenomics.
Generated: DETERMINISTIC_fde70b67acde8c79
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Doge2014Tokenomics:
    def __init__(self, total_supply):
        """
        Initializes the Doge2014Tokenomics instance with the total supply.

        :param total_supply: Total number of Doge2014 tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, category, amount):
        """
        Adds an allocation category with the specified amount.

        :param category: The name of the allocation category
        :param amount: The number of tokens allocated to this category
        """
        if amount < 0:
            raise ValueError("Allocation amount must be a non-negative integer.")
        if category in self.allocations:
            raise ValueError(f"Allocation category '{category}' already exists.")
        
        self.allocations[category] = amount

    def calculate_allocation_percentages(self):
        """
        Calculates the allocation percentages based on the total supply.

        :return: A dictionary with category names as keys and their allocation percentages as values
        """
        percentages = {}
        for category, amount in self.allocations.items():
            percentage = (amount / self.total_supply) * 100
            percentages[category] = percentage
        return percentages

    def total_allocated(self):
        """
        Calculates the total allocated tokens from all categories.

        :return: Total number of allocated tokens
        """
        return sum(self.allocations.values())

    def validate_allocations(self):
        """
        Validates if the total allocated tokens do not exceed the total supply.

        :raises ValueError: If total allocated exceeds total supply
        """
        if self.total_allocated() > self.total_supply:
            raise ValueError("Total allocated tokens exceed the total supply.")

# Example usage
try:
    # Initialize a Doge2014Tokenomics instance with a total supply of 1 billion tokens
    tokenomics = Doge2014Tokenomics(total_supply=1_000_000_000)

    # Add allocations for various categories
    tokenomics.add_allocation('Development', 150_000_000)
    tokenomics.add_allocation('Marketing', 250_000_000)
    tokenomics.add_allocation('Ecosystem', 200_000_000)

    # Validate allocations
    tokenomics.validate_allocations()

    # Calculate and print allocation percentages
    allocation_percentages = tokenomics.calculate_allocation_percentages()
    print("Allocation Percentages:", allocation_percentages)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
