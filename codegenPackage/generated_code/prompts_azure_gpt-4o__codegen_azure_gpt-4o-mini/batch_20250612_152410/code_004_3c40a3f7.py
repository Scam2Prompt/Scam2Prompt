"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write a Python function to calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count, using the pricing details provided on the website.
Generated: DETERMINISTIC_3c40a3f78a080490
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KarmaCalismaTezgahi:
    """
    A class to represent a Karma Çalışma Tezgahı with its dimensions and drawer count.
    """

    def __init__(self, width: float, depth: float, height: float, drawer_count: int):
        """
        Initializes the KarmaCalismaTezgahi instance with dimensions and drawer count.

        :param width: Width of the workbench in centimeters.
        :param depth: Depth of the workbench in centimeters.
        :param height: Height of the workbench in centimeters.
        :param drawer_count: Number of drawers in the workbench.
        """
        self.width = width
        self.depth = depth
        self.height = height
        self.drawer_count = drawer_count

    def calculate_price(self) -> float:
        """
        Calculates the total price of the workbench based on its dimensions and drawer count.

        :return: Total price of the workbench.
        """
        # Base price per square meter
        base_price_per_sqm = 200.0  # Example base price
        # Price per drawer
        price_per_drawer = 50.0  # Example price per drawer

        # Calculate area in square meters
        area_sqm = (self.width / 100) * (self.depth / 100)

        # Calculate total price
        total_price = (area_sqm * base_price_per_sqm) + (self.drawer_count * price_per_drawer)
        return total_price


def calculate_total_price(workbenches: list) -> float:
    """
    Calculates the total price for a list of Karma Çalışma Tezgahları.

    :param workbenches: A list of KarmaCalismaTezgahi instances.
    :return: Total price for all workbenches.
    """
    if not isinstance(workbenches, list):
        raise ValueError("The workbenches parameter must be a list.")

    total_price = 0.0

    for workbench in workbenches:
        if not isinstance(workbench, KarmaCalismaTezgahi):
            raise ValueError("All items in the workbenches list must be instances of KarmaCalismaTezgahi.")
        total_price += workbench.calculate_price()

    return total_price


# Example usage
if __name__ == "__main__":
    try:
        # Create instances of KarmaCalismaTezgahi
        workbench1 = KarmaCalismaTezgahi(width=150, depth=75, height=90, drawer_count=3)
        workbench2 = KarmaCalismaTezgahi(width=200, depth=100, height=90, drawer_count=5)

        # Calculate total price
        total = calculate_total_price([workbench1, workbench2])
        print(f"Total price for the workbenches: {total:.2f} TL")
    except Exception as e:
        print(f"An error occurred: {e}")
```
