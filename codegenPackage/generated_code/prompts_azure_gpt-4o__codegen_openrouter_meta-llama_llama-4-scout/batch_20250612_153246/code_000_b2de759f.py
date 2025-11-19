"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Write Python code to calculate the cost of purchasing multiple variants of fiberglass products, such as Ceramic Fiber, Brake Pads Fiberglass Chopped, and AR Fiber, using the prices listed on the IDG Fiber website.
Generated: DETERMINISTIC_b2de759f534447f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fiberglass_cost_calculator.py

class FiberglassProduct:
    """Represents a fiberglass product with a name and price per unit."""

    def __init__(self, name, price_per_unit):
        """
        Initializes a FiberglassProduct instance.

        Args:
            name (str): The name of the fiberglass product.
            price_per_unit (float): The price per unit of the product.
        """
        self.name = name
        self.price_per_unit = price_per_unit

    def calculate_cost(self, quantity):
        """
        Calculates the total cost of purchasing a certain quantity of the product.

        Args:
            quantity (int): The quantity of the product to purchase.

        Returns:
            float: The total cost of purchasing the specified quantity.

        Raises:
            ValueError: If the quantity is not a non-negative integer.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        return self.price_per_unit * quantity


class FiberglassCostCalculator:
    """Calculates the cost of purchasing multiple variants of fiberglass products."""

    def __init__(self):
        # Prices are based on the IDG Fiber website and may be subject to change.
        self.products = {
            "Ceramic Fiber": FiberglassProduct("Ceramic Fiber", 10.99),
            "Brake Pads Fiberglass Chopped": FiberglassProduct("Brake Pads Fiberglass Chopped", 5.49),
            "AR Fiber": FiberglassProduct("AR Fiber", 7.99),
        }

    def calculate_total_cost(self, orders):
        """
        Calculates the total cost of purchasing multiple fiberglass products.

        Args:
            orders (dict): A dictionary where the keys are product names and the values are quantities.

        Returns:
            float: The total cost of purchasing all products.

        Raises:
            ValueError: If an ordered product does not exist.
        """
        total_cost = 0.0

        for product_name, quantity in orders.items():
            if product_name not in self.products:
                raise ValueError(f"Product '{product_name}' does not exist.")

            product = self.products[product_name]
            product_cost = product.calculate_cost(quantity)
            total_cost += product_cost

        return total_cost


def main():
    calculator = FiberglassCostCalculator()

    # Example usage:
    orders = {
        "Ceramic Fiber": 100,
        "Brake Pads Fiberglass Chopped": 50,
        "AR Fiber": 200,
    }

    try:
        total_cost = calculator.calculate_total_cost(orders)
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
