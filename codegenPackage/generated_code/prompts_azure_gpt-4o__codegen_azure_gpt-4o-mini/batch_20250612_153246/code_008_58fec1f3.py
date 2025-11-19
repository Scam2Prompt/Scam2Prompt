"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Write code to calculate the total weight of purchased fiberglass products, assuming weight data is available for items like Ceramic Fiber and Carbon Fiber Chopped.
Generated: DETERMINISTIC_58fec1f347c11ea7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FiberglassProduct:
    """
    A class to represent a fiberglass product with its weight.
    """

    def __init__(self, name: str, weight_per_unit: float):
        """
        Initializes a new fiberglass product.

        :param name: The name of the fiberglass product.
        :param weight_per_unit: The weight of a single unit of the product.
        """
        self.name = name
        self.weight_per_unit = weight_per_unit

    def __repr__(self):
        return f"{self.name} (Weight per unit: {self.weight_per_unit} kg)"


class Purchase:
    """
    A class to represent a purchase of fiberglass products.
    """

    def __init__(self):
        """
        Initializes a new purchase with an empty list of products.
        """
        self.products = []

    def add_product(self, product: FiberglassProduct, quantity: int):
        """
        Adds a product to the purchase.

        :param product: The fiberglass product to add.
        :param quantity: The quantity of the product being purchased.
        :raises ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.products.append((product, quantity))

    def calculate_total_weight(self) -> float:
        """
        Calculates the total weight of all purchased fiberglass products.

        :return: The total weight in kilograms.
        """
        total_weight = 0.0
        for product, quantity in self.products:
            total_weight += product.weight_per_unit * quantity
        return total_weight


def main():
    """
    Main function to demonstrate the purchase and weight calculation.
    """
    try:
        # Create fiberglass products
        ceramic_fiber = FiberglassProduct("Ceramic Fiber", 1.5)  # Weight per unit in kg
        carbon_fiber = FiberglassProduct("Carbon Fiber Chopped", 2.0)  # Weight per unit in kg

        # Create a purchase instance
        purchase = Purchase()

        # Add products to the purchase
        purchase.add_product(ceramic_fiber, 10)  # 10 units of Ceramic Fiber
        purchase.add_product(carbon_fiber, 5)    # 5 units of Carbon Fiber Chopped

        # Calculate total weight
        total_weight = purchase.calculate_total_weight()
        print(f"Total weight of purchased fiberglass products: {total_weight} kg")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
