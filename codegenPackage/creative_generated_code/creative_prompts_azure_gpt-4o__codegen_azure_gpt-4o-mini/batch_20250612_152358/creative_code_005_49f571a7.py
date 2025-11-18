"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Provide code to calculate and display the allocation percentages for $CHOC tokenomics (presale, project funds, liquidity, marketing).
Generated: DETERMINISTIC_49f571a7984baf64
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """Class to represent the token allocation of a cryptocurrency."""

    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class with the total supply of tokens.

        Args:
            total_supply (float): The total supply of the $CHOC token.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.0,
            "project_funds": 0.0,
            "liquidity": 0.0,
            "marketing": 0.0
        }

    def set_allocation(self, category, amount):
        """
        Set the allocation for a specified category.

        Args:
            category (str): The category for the allocation (presale, project_funds, liquidity, marketing).
            amount (float): The amount allocated to the specified category.

        Raises:
            ValueError: If the category is invalid or the amount is negative.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category '{category}'. Valid categories are {list(self.allocations.keys())}.")
        if amount < 0:
            raise ValueError("Allocation amount must be non-negative.")
        
        self.allocations[category] = amount

    def calculate_percentages(self):
        """
        Calculate the allocation percentages for each category.

        Returns:
            dict: A dictionary containing the allocation percentages for each category.
        
        Raises:
            ZeroDivisionError: If the total supply is zero when calculating percentages.
        """
        if self.total_supply == 0:
            raise ZeroDivisionError("Total supply cannot be zero when calculating percentages.")

        percentages = {}
        for category, amount in self.allocations.items():
            percentages[category] = (amount / self.total_supply) * 100
        
        return percentages

    def display_allocations(self):
        """Display the allocation percentages for each category."""
        try:
            percentages = self.calculate_percentages()
            print("Token Allocation Percentages:")
            for category, percentage in percentages.items():
                print(f"{category.capitalize()}: {percentage:.2f}%")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage of the Tokenomics class
    try:
        total_supply = 1000000.0  # Set total supply of $CHOC tokens
        tokenomics = Tokenomics(total_supply)
        
        # Set allocations for various categories
        tokenomics.set_allocation("presale", 200000)
        tokenomics.set_allocation("project_funds", 300000)
        tokenomics.set_allocation("liquidity", 400000)
        tokenomics.set_allocation("marketing", 100000)

        # Display the allocation percentages
        tokenomics.display_allocations()

    except ValueError as e:
        print(f"Initialization Error: {e}")
```
