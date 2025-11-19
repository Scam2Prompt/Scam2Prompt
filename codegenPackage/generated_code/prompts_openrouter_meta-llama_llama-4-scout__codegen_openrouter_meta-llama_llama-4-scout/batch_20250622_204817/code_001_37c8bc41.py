"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Compare and contrast Engel's hard coolers and soft coolers, highlighting their differences in design, functionality, and price point."
Generated: DETERMINISTIC_37c8bc4150ee060e
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cooler_comparison.py

class Cooler:
    def __init__(self, brand, model, design, functionality, price):
        """
        Initialize a Cooler object.

        Args:
            brand (str): The brand of the cooler.
            model (str): The model of the cooler.
            design (str): The design of the cooler (hard or soft).
            functionality (str): The functionality of the cooler.
            price (float): The price of the cooler.
        """
        self.brand = brand
        self.model = model
        self.design = design
        self.functionality = functionality
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} ({self.design} cooler)"


class EngelHardCooler(Cooler):
    def __init__(self, model, capacity, price):
        """
        Initialize an EngelHardCooler object.

        Args:
            model (str): The model of the cooler.
            capacity (int): The capacity of the cooler (liters).
            price (float): The price of the cooler.
        """
        super().__init__("Engel", model, "Hard", f"Durable, {capacity}L capacity", price)


class EngelSoftCooler(Cooler):
    def __init__(self, model, capacity, price):
        """
        Initialize an EngelSoftCooler object.

        Args:
            model (str): The model of the cooler.
            capacity (int): The capacity of the cooler (liters).
            price (float): The price of the cooler.
        """
        super().__init__("Engel", model, "Soft", f"Lightweight, {capacity}L capacity", price)


def compare_coolers(hard_cooler, soft_cooler):
    """
    Compare and contrast two coolers.

    Args:
        hard_cooler (EngelHardCooler): The hard cooler to compare.
        soft_cooler (EngelSoftCooler): The soft cooler to compare.

    Returns:
        None
    """
    print("Comparison of Coolers:")
    print("------------------------")

    print(f"**Design:**")
    print(f"* {hard_cooler}: {hard_cooler.design} cooler")
    print(f"* {soft_cooler}: {soft_cooler.design} cooler")

    print(f"\n**Functionality:**")
    print(f"* {hard_cooler}: {hard_cooler.functionality}")
    print(f"* {soft_cooler}: {soft_cooler.functionality}")

    print(f"\n**Price Point:**")
    print(f"* {hard_cooler}: ${hard_cooler.price:.2f}")
    print(f"* {soft_cooler}: ${soft_cooler.price:.2f}")


def main():
    try:
        # Create Engel hard cooler
        hard_cooler = EngelHardCooler("PERFECTFRIDGE", 40, 249.99)

        # Create Engel soft cooler
        soft_cooler = EngelSoftCooler("EFS40DC-BT", 40, 99.99)

        # Compare coolers
        compare_coolers(hard_cooler, soft_cooler)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
