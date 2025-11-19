"""
Generated Code Metadata:
========================
Original URL: https://canguldemir.com.tr
Prompt: Write a Python script to calculate the total cost of purchasing different sizes of construction steel bars based on the pricing information from Cangül Demir Çelik A.Ş.
Generated: DETERMINISTIC_ad40dc1d8d97a338
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_steel_bars_calculator.py

class SteelBar:
    """Represents a construction steel bar with its size and price."""

    def __init__(self, size, price_per_ton):
        """
        Initializes a SteelBar object.

        Args:
            size (str): The size of the steel bar (e.g., 8, 10, 12, etc.).
            price_per_ton (float): The price per ton of the steel bar.
        """
        self.size = size
        self.price_per_ton = price_per_ton

    def calculate_cost(self, quantity_in_tons):
        """
        Calculates the total cost of purchasing a certain quantity of steel bars.

        Args:
            quantity_in_tons (float): The quantity of steel bars to purchase in tons.

        Returns:
            float: The total cost of purchasing the steel bars.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity_in_tons < 0:
            raise ValueError("Quantity cannot be negative")

        return self.price_per_ton * quantity_in_tons


class SteelBarPricing:
    """Manages pricing information for different sizes of construction steel bars."""

    def __init__(self):
        """
        Initializes a SteelBarPricing object with an empty pricing dictionary.
        """
        self.pricing = {}

    def add_price(self, size, price_per_ton):
        """
        Adds pricing information for a specific size of steel bar.

        Args:
            size (str): The size of the steel bar (e.g., 8, 10, 12, etc.).
            price_per_ton (float): The price per ton of the steel bar.
        """
        self.pricing[size] = SteelBar(size, price_per_ton)

    def get_steel_bar(self, size):
        """
        Retrieves a SteelBar object for a specific size.

        Args:
            size (str): The size of the steel bar (e.g., 8, 10, 12, etc.).

        Returns:
            SteelBar: The SteelBar object for the specified size, or None if not found.
        """
        return self.pricing.get(size)

    def calculate_total_cost(self, orders):
        """
        Calculates the total cost of purchasing different sizes and quantities of steel bars.

        Args:
            orders (dict): A dictionary where keys are steel bar sizes and values are quantities in tons.

        Returns:
            float: The total cost of purchasing all steel bars.

        Raises:
            ValueError: If an order contains a negative quantity.
        """
        total_cost = 0.0

        for size, quantity_in_tons in orders.items():
            steel_bar = self.get_steel_bar(size)
            if steel_bar is None:
                print(f"Warning: No pricing information found for size {size}")

            try:
                cost = steel_bar.calculate_cost(quantity_in_tons) if steel_bar else 0.0
                total_cost += cost
            except ValueError as e:
                print(f"Error: {e}")

        return total_cost


def main():
    # Pricing information from Cangül Demir Çelik A.Ş. (example prices)
    pricing = SteelBarPricing()
    pricing.add_price("8", 650.0)
    pricing.add_price("10", 670.0)
    pricing.add_price("12", 690.0)
    pricing.add_price("14", 710.0)
    pricing.add_price("16", 730.0)

    # Example orders
    orders = {
        "8": 5.0,
        "10": 3.0,
        "12": 2.5,
        "14": 1.0,
        "18": 2.0  # No pricing information for this size
    }

    total_cost = pricing.calculate_total_cost(orders)
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
