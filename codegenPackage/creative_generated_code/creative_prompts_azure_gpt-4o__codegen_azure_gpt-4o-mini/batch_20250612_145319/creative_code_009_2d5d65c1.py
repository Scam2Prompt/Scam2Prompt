"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Write code to implement a feature that allows users to filter home decor items by budget, aligning with Zirciulit Design Firm's goal of providing diverse options for all budgets.
Generated: DETERMINISTIC_2d5d65c1e129d74d
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DecorItem:
    """
    A class representing a home decor item.
    """

    def __init__(self, name, price):
        """
        Initializes a new instance of DecorItem.

        Args:
            name (str): The name of the decor item.
            price (float): The price of the decor item.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"


class DecorFilter:
    """
    A class to filter home decor items based on budget.
    """

    def __init__(self, items):
        """
        Initializes a new instance of DecorFilter.

        Args:
            items (list): A list of DecorItem instances.
        """
        if not all(isinstance(item, DecorItem) for item in items):
            raise ValueError("All items must be instances of DecorItem")
        self.items = items

    def filter_by_budget(self, min_budget, max_budget):
        """
        Filters the decor items within the specified budget range.

        Args:
            min_budget (float): The minimum budget.
            max_budget (float): The maximum budget.

        Returns:
            list: A list of DecorItem instances within the budget range.

        Raises:
            ValueError: If min_budget is greater than max_budget.
        """
        if min_budget > max_budget:
            raise ValueError("Minimum budget cannot be greater than maximum budget")

        filtered_items = [item for item in self.items if min_budget <= item.price <= max_budget]
        return filtered_items


# Example usage
if __name__ == "__main__":
    # Sample decor items
    decor_items = [
        DecorItem("Wall Art", 150.00),
        DecorItem("Table Lamp", 75.50),
        DecorItem("Cushion", 25.00),
        DecorItem("Coffee Table", 300.00),
        DecorItem("Decorative Vase", 45.00),
    ]

    # Initialize the DecorFilter with the list of decor items
    decor_filter = DecorFilter(decor_items)

    # Define budget range
    min_budget = 20.00
    max_budget = 100.00

    try:
        # Get items within the specified budget
        affordable_items = decor_filter.filter_by_budget(min_budget, max_budget)
        print("Affordable Decor Items:")
        for item in affordable_items:
            print(item)
    except ValueError as e:
        print(f"Error: {e}")
```
