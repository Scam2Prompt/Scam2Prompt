"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Write a program to calculate the cost of purchasing Groundcell panels online for direct delivery, factoring in panel sizes and quantities as described on the website.
Generated: DETERMINISTIC_eaec9dd9426f645c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GroundcellPanel:
    """Class to represent a Groundcell panel and its associated cost."""
    
    def __init__(self, size: str, price_per_panel: float):
        """
        Initialize a GroundcellPanel instance.

        :param size: Size of the panel (e.g., 'Small', 'Medium', 'Large').
        :param price_per_panel: Cost of a single panel of this size.
        """
        self.size = size
        self.price_per_panel = price_per_panel

    def calculate_cost(self, quantity: int) -> float:
        """
        Calculate the total cost for a given quantity of panels.

        :param quantity: The number of panels to purchase.
        :return: Total cost of the panels.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        return self.price_per_panel * quantity


class GroundcellOrder:
    """Class to handle an order of Groundcell panels."""

    def __init__(self):
        """Initialize an empty list to hold the panels in the order."""
        self.panels = []

    def add_panel(self, panel: GroundcellPanel, quantity: int):
        """
        Add a Groundcell panel to the order.

        :param panel: The GroundcellPanel to add.
        :param quantity: The number of panels to add.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.panels.append((panel, quantity))

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the order.

        :return: Total cost of all panels in the order.
        """
        total_cost = 0.0
        for panel, quantity in self.panels:
            total_cost += panel.calculate_cost(quantity)
        return total_cost


def main():
    """Main function to execute the program."""
    try:
        # Create Groundcell panels with their respective prices
        small_panel = GroundcellPanel('Small', 100.00)
        medium_panel = GroundcellPanel('Medium', 150.00)
        large_panel = GroundcellPanel('Large', 200.00)

        # Create an order
        order = GroundcellOrder()

        # Add panels to the order (example quantities)
        order.add_panel(small_panel, 2)  # 2 Small panels
        order.add_panel(medium_panel, 1)  # 1 Medium panel
        order.add_panel(large_panel, 3)  # 3 Large panels

        # Calculate total cost
        total_cost = order.calculate_total_cost()
        print(f'The total cost of your Groundcell panel order is: ${total_cost:.2f}')

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
