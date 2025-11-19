"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vejanoticiabrasil.online
Prompt: Write a Python script that calculates the total cost of an imported item, including customs taxes and postal fees, based on the new regulations mentioned in the article.
Generated: DETERMINISTIC_4865a081c5bb6efc
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ItemImportCalculator:
    """A class to calculate the total cost of an imported item, including customs taxes and postal fees."""

    def __init__(self, item_cost, customs_rate, postal_fee):
        """
        Initializes the calculator with the item cost, customs tax rate, and postal fee.
        
        :param item_cost: float, cost of the item
        :param customs_rate: float, customs tax rate as a percentage (e.g., 20 for 20%)
        :param postal_fee: float, fixed postal fee
        """
        if item_cost < 0 or customs_rate < 0 or postal_fee < 0:
            raise ValueError("Item cost, customs rate, and postal fee must be non-negative.")

        self.item_cost = item_cost
        self.customs_rate = customs_rate
        self.postal_fee = postal_fee

    def calculate_customs_tax(self):
        """Calculates the customs tax based on the item cost and customs rate."""
        customs_tax = (self.item_cost * self.customs_rate) / 100
        return customs_tax

    def calculate_total_cost(self):
        """Calculates the total cost including item cost, customs tax, and postal fee."""
        customs_tax = self.calculate_customs_tax()
        total_cost = self.item_cost + customs_tax + self.postal_fee
        return total_cost


def main():
    """Main function to execute the calculator."""
    try:
        # Sample input values
        item_cost = float(input("Enter the cost of the item: "))
        customs_rate = float(input("Enter the customs tax rate (in %): "))
        postal_fee = float(input("Enter the postal fee: "))

        # Create an instance of the calculator
        calculator = ItemImportCalculator(item_cost, customs_rate, postal_fee)

        # Calculate total cost
        total_cost = calculator.calculate_total_cost()

        # Output the total cost
        print(f"The total cost of the imported item is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
