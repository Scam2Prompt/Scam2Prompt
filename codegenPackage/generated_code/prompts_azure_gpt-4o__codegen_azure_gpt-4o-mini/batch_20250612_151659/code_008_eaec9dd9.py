"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write a program to calculate the cost of purchasing Groundcell panels online for direct delivery, factoring in panel sizes and quantities as described on the website.
Generated: DETERMINISTIC_eaec9dd9426f645c
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GroundcellPanel:
    """
    A class to represent a Groundcell panel with its size and cost.
    """

    def __init__(self, size: str, price_per_unit: float):
        """
        Initializes a Groundcell panel with a specific size and price.

        :param size: The size of the panel (e.g., 'small', 'medium', 'large').
        :param price_per_unit: The cost of one unit of the panel.
        """
        self.size = size
        self.price_per_unit = price_per_unit

    def calculate_cost(self, quantity: int) -> float:
        """
        Calculates the total cost for a given quantity of panels.

        :param quantity: The number of panels to purchase.
        :return: The total cost for the specified quantity.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        return self.price_per_unit * quantity


class GroundcellOrder:
    """
    A class to handle the order of Groundcell panels.
    """

    def __init__(self):
        """
        Initializes an empty order.
        """
        self.panels = []

    def add_panel(self, panel: GroundcellPanel, quantity: int):
        """
        Adds a panel to the order.

        :param panel: The Groundcell panel to add.
        :param quantity: The number of panels to add.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.panels.append((panel, quantity))

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the order.

        :return: The total cost of all panels in the order.
        """
        total_cost = 0.0
        for panel, quantity in self.panels:
            total_cost += panel.calculate_cost(quantity)
        return total_cost


def main():
    """
    Main function to execute the program.
    """
    # Create some Groundcell panels with their respective prices
    small_panel = GroundcellPanel(size='small', price_per_unit=50.0)
    medium_panel = GroundcellPanel(size='medium', price_per_unit=75.0)
    large_panel = GroundcellPanel(size='large', price_per_unit=100.0)

    # Create an order
    order = GroundcellOrder()

    # Add panels to the order
    try:
        order.add_panel(small_panel, 2)  # 2 small panels
        order.add_panel(medium_panel, 1)  # 1 medium panel
        order.add_panel(large_panel, 3)  # 3 large panels

        # Calculate the total cost
        total_cost = order.calculate_total_cost()
        print(f"Total cost of the order: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
