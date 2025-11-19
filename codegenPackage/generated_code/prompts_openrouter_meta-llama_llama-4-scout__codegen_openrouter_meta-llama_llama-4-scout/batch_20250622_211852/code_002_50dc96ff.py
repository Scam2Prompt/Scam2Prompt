"""
Generated Code Metadata:
========================
Original URL: https://www.suezlng.com
Prompt: "Write a Python script to calculate the total cost of oil trading based on the prices of different oil products, such as JetA1, Mogas, and LPG."
Generated: DETERMINISTIC_50dc96ff98e16764
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# oil_trading_cost_calculator.py

class OilProduct:
    """Represents an oil product with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes an OilProduct instance.

        Args:
            name (str): The name of the oil product.
            price (float): The price of the oil product per unit.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        return f"OilProduct(name='{self.name}', price={self.price})"


class OilTradingCostCalculator:
    """Calculates the total cost of oil trading based on oil product prices."""

    def __init__(self):
        """Initializes an OilTradingCostCalculator instance."""
        self.oil_products = {}

    def add_oil_product(self, product: OilProduct, quantity: float):
        """
        Adds an oil product to the calculator.

        Args:
            product (OilProduct): The oil product to add.
            quantity (float): The quantity of the oil product.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.oil_products[product.name] = (product, quantity)

    def remove_oil_product(self, product_name: str):
        """
        Removes an oil product from the calculator.

        Args:
            product_name (str): The name of the oil product to remove.

        Raises:
            KeyError: If the product is not found.
        """
        if product_name not in self.oil_products:
            raise KeyError(f"Product '{product_name}' not found")

        del self.oil_products[product_name]

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of oil trading.

        Returns:
            float: The total cost.

        Raises:
            Exception: If an error occurs during calculation.
        """
        try:
            total_cost = sum(product.price * quantity for product, quantity in self.oil_products.values())
            return total_cost
        except Exception as e:
            raise Exception("Failed to calculate total cost") from e


def main():
    calculator = OilTradingCostCalculator()

    # Define oil products
    jet_a1 = OilProduct("JetA1", 100.0)
    mogas = OilProduct("Mogas", 80.0)
    lpg = OilProduct("LPG", 50.0)

    # Add oil products to the calculator
    calculator.add_oil_product(jet_a1, 1000.0)
    calculator.add_oil_product(mogas, 500.0)
    calculator.add_oil_product(lpg, 2000.0)

    # Calculate total cost
    try:
        total_cost = calculator.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")

    # Remove an oil product
    calculator.remove_oil_product("Mogas")

    # Calculate total cost again
    try:
        total_cost = calculator.calculate_total_cost()
        print(f"Updated total cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
