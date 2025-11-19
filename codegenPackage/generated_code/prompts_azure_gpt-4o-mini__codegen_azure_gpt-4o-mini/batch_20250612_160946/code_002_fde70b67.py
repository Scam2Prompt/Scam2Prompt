"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Generate a code snippet for calculating the total supply and allocation percentages for Doge2014 tokens based on the provided tokenomics.
Generated: DETERMINISTIC_fde70b67acde8c79
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Doge2014Tokenomics:
    def __init__(self, total_supply: int):
        """
        Initializes the Doge2014Tokenomics with the total supply of tokens.

        :param total_supply: Total supply of Doge2014 tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, name: str, amount: int):
        """
        Adds an allocation to the tokenomics.

        :param name: Name of the allocation
        :param amount: Amount allocated
        :raises ValueError: If the amount is non-positive or exceeds the remaining supply
        """
        if amount <= 0:
            raise ValueError("Allocation amount must be a positive integer.")
        if name in self.allocations:
            raise ValueError(f"Allocation '{name}' already exists.")
        
        remaining_supply = self.total_supply - sum(self.allocations.values())
        if amount > remaining_supply:
            raise ValueError("Allocation exceeds remaining supply.")

        self.allocations[name] = amount

    def calculate_allocation_percentages(self):
        """
        Calculates the allocation percentages for each category.

        :return: A dictionary with allocation names as keys and their percentages as values
        """
        percentages = {}
        for name, amount in self.allocations.items():
            percentages[name] = (amount / self.total_supply) * 100
        return percentages

    def get_total_allocated(self):
        """
        Returns the total amount allocated.

        :return: Total allocated amount
        """
        return sum(self.allocations.values())

    def get_remaining_supply(self):
        """
        Returns the remaining supply of tokens after allocations.

        :return: Remaining supply
        """
        return self.total_supply - self.get_total_allocated()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tokenomics with a total supply of 1,000,000 tokens
        tokenomics = Doge2014Tokenomics(total_supply=1_000_000)

        # Add allocations
        tokenomics.add_allocation("Development", 200_000)
        tokenomics.add_allocation("Marketing", 150_000)
        tokenomics.add_allocation("Community Rewards", 100_000)

        # Calculate and print allocation percentages
        allocation_percentages = tokenomics.calculate_allocation_percentages()
        print("Allocation Percentages:", allocation_percentages)

        # Print total allocated and remaining supply
        print("Total Allocated:", tokenomics.get_total_allocated())
        print("Remaining Supply:", tokenomics.get_remaining_supply())

    except ValueError as e:
        print(f"Error: {e}")
```
