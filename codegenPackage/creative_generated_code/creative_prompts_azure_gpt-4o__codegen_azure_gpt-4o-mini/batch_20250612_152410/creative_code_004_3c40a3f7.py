"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Write a Python function to calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count, using the pricing details provided on the website.
Generated: DETERMINISTIC_3c40a3f78a080490
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KarmaWorkBench:
    """
    A class to represent a Karma workbench with pricing details based on dimensions and drawer count.
    """

    BASE_PRICE_PER_SQUARE_METER = 150  # Base price per square meter
    DRAWER_PRICE = 50                    # Price per drawer

    def __init__(self, width: float, depth: float, drawer_count: int):
        """
        Initialize a new KarmaWorkBench instance.

        :param width: Width of the workbench in meters.
        :param depth: Depth of the workbench in meters.
        :param drawer_count: Number of drawers in the workbench.
        """
        self.width = width
        self.depth = depth
        self.drawer_count = drawer_count

    def calculate_area(self) -> float:
        """
        Calculate the area of the workbench.

        :return: Area in square meters.
        """
        return self.width * self.depth

    def calculate_price(self) -> float:
        """
        Calculate the total price of the workbench.

        :return: Total price in currency units.
        """
        area_price = self.calculate_area() * self.BASE_PRICE_PER_SQUARE_METER
        drawer_price = self.drawer_count * self.DRAWER_PRICE
        total_price = area_price + drawer_price
        return total_price


def calculate_total_price(workbenches: list) -> float:
    """
    Calculate the total price of multiple workbenches.

    :param workbenches: A list of KarmaWorkBench instances.
    :return: Total price of all workbenches.
    """
    total_price = 0.0
    for bench in workbenches:
        if not isinstance(bench, KarmaWorkBench):
            raise ValueError("All items in the list must be instances of KarmaWorkBench.")
        total_price += bench.calculate_price()
    return total_price


# Example usage
if __name__ == "__main__":
    try:
        workbench1 = KarmaWorkBench(width=2.0, depth=1.5, drawer_count=3)
        workbench2 = KarmaWorkBench(width=1.5, depth=1.0, drawer_count=2)
        
        total = calculate_total_price([workbench1, workbench2])
        print(f"Total price for the workbenches: {total:.2f} currency units")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
