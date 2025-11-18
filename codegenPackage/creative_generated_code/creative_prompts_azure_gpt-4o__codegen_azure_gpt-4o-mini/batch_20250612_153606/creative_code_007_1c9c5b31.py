"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverse-com.pages.dev
Prompt: Write code to implement a token allocation tracker for $DOGEVERSE, showing percentages allocated to presale, staking, liquidity, marketing, ecosystem funds, and exchanges.
Generated: DETERMINISTIC_1c9c5b31d645bd57
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenAllocationTracker:
    """
    A class to track the allocation of $DOGEVERSE tokens.
    
    Attributes:
        total_supply (float): The total supply of $DOGEVERSE tokens.
        allocations (dict): A dictionary containing the allocation percentages for different categories.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenAllocationTracker with total supply and predefined allocations.
        
        Args:
            total_supply (float): The total supply of $DOGEVERSE tokens.
        
        Raises:
            ValueError: If total_supply is not a positive number.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        self.total_supply = total_supply
        self.allocations = {
            'presale': 0.0,
            'staking': 0.0,
            'liquidity': 0.0,
            'marketing': 0.0,
            'ecosystem_funds': 0.0,
            'exchanges': 0.0
        }

    def set_allocation(self, category, percentage):
        """
        Sets the allocation percentage for a specific category.
        
        Args:
            category (str): The category for which to set the allocation.
            percentage (float): The allocation percentage to set.
        
        Raises:
            ValueError: If the percentage is not between 0 and 100 or if the category is not valid.
        """
        if category not in self.allocations:
            raise ValueError("Invalid category. Valid categories are: {}".format(', '.join(self.allocations.keys())))
        
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        self.allocations[category] = percentage

    def get_allocation(self):
        """
        Returns the current allocations in percentage and token amount.
        
        Returns:
            dict: A dictionary containing the allocations with both percentage and amount in tokens.
        """
        allocation_summary = {}
        for category, percentage in self.allocations.items():
            allocation_amount = (percentage / 100) * self.total_supply
            allocation_summary[category] = {
                'percentage': percentage,
                'amount': allocation_amount
            }
        return allocation_summary

    def validate_total_allocation(self):
        """
        Validates that the total allocation percentages do not exceed 100%.
        
        Raises:
            ValueError: If the total allocation exceeds 100%.
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage > 100:
            raise ValueError("Total allocation exceeds 100%: {}".format(total_percentage))

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the tracker with a total supply of 1 million tokens
        tracker = TokenAllocationTracker(total_supply=1_000_000)
        
        # Set allocations
        tracker.set_allocation('presale', 25)
        tracker.set_allocation('staking', 20)
        tracker.set_allocation('liquidity', 15)
        tracker.set_allocation('marketing', 10)
        tracker.set_allocation('ecosystem_funds', 10)
        tracker.set_allocation('exchanges', 20)

        # Validate total allocation
        tracker.validate_total_allocation()

        # Get and print allocation details
        allocations = tracker.get_allocation()
        for category, details in allocations.items():
            print(f"{category.capitalize()}: {details['percentage']}% ({details['amount']} tokens)")

    except ValueError as e:
        print(f"Error: {e}")
```
