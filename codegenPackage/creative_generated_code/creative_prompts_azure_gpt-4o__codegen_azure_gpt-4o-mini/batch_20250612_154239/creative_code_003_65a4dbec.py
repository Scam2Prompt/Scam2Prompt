"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Write a Python script that calculates the allocation of funds raised during the Bulldogito Coin presale into categories like marketing, liquidity, dev team, and B2B Booster, based on the percentages provided.
Generated: DETERMINISTIC_65a4dbeccd70c989
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Bulldogito Coin Fund Allocation Script

class FundAllocator:
    """
    Class to handle the allocation of funds based on specified categories and percentages.
    """

    def __init__(self, total_funds, allocation_percentages):
        """
        Initializes the FundAllocator with total funds and allocation percentages.

        Args:
            total_funds (float): The total amount of funds raised.
            allocation_percentages (dict): A dictionary containing categories and their corresponding percentages.

        Raises:
            ValueError: If total funds are negative or if the percentages do not sum up to 100.
        """
        if total_funds < 0:
            raise ValueError("Total funds must be a non-negative value.")

        self.total_funds = total_funds
        self.allocation_percentages = allocation_percentages

        if not self._validate_percentages():
            raise ValueError("The percentages must sum up to 100.")

    def _validate_percentages(self):
        """
        Validates that the sum of allocation percentages equals 100.

        Returns:
            bool: True if the percentages sum to 100, False otherwise.
        """
        total_percentage = sum(self.allocation_percentages.values())
        return total_percentage == 100

    def allocate_funds(self):
        """
        Allocates the total funds according to the specified percentages.

        Returns:
            dict: A dictionary with the allocated amounts for each category.
        """
        allocations = {}
        for category, percentage in self.allocation_percentages.items():
            allocations[category] = (percentage / 100) * self.total_funds
        return allocations

def main():
    """
    Main function to execute the fund allocation process.
    """
    # Example total funds and allocation percentages
    total_funds = 100000  # Example total funds raised
    allocation_percentages = {
        'Marketing': 40,
        'Liquidity': 30,
        'Dev Team': 20,
        'B2B Booster': 10
    }

    try:
        # Creating an instance of FundAllocator
        fund_allocator = FundAllocator(total_funds, allocation_percentages)

        # Allocating funds
        allocated_funds = fund_allocator.allocate_funds()

        # Displaying the allocation results
        print("Fund Allocation Results:")
        for category, amount in allocated_funds.items():
            print(f"{category}: ${amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
