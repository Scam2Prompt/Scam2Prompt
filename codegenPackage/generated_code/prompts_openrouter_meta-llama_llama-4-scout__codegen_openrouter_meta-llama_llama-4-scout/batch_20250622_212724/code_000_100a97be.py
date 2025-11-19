"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write a Python code snippet to calculate the total cost of purchasing solar batteries, including a 40A 12V/24V AM MPPT Solar charge controller and a 2000 Lithium Portable Power Pack, considering a 10% discount on the total price.
Generated: DETERMINISTIC_100a97bef233b0c8
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for solar products
class SolarProduct:
    def __init__(self, name, price):
        """
        Initialize a solar product.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        self.name = name
        self.price = price

# Define a class for the solar charge controller
class SolarChargeController(SolarProduct):
    def __init__(self, name, price, specs):
        """
        Initialize a solar charge controller.

        Args:
            name (str): Product name.
            price (float): Product price.
            specs (str): Product specifications.
        """
        super().__init__(name, price)
        self.specs = specs

# Define a class for the lithium portable power pack
class LithiumPortablePowerPack(SolarProduct):
    def __init__(self, name, price, capacity):
        """
        Initialize a lithium portable power pack.

        Args:
            name (str): Product name.
            price (float): Product price.
            capacity (int): Power pack capacity.
        """
        super().__init__(name, price)
        self.capacity = capacity

# Define a function to calculate the total cost
def calculate_total_cost(products, discount_rate):
    """
    Calculate the total cost of purchasing solar products.

    Args:
        products (list): List of solar products.
        discount_rate (float): Discount rate.

    Returns:
        float: Total cost after discount.
    """
    try:
        # Check if products is a list
        if not isinstance(products, list):
            raise TypeError("Products must be a list")

        # Check if discount rate is within valid range
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1")

        # Calculate subtotal
        subtotal = sum(product.price for product in products)

        # Apply discount
        discount = subtotal * discount_rate
        total_cost = subtotal - discount

        return total_cost

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define main function
def main():
    # Create solar products
    charge_controller = SolarChargeController("40A 12V/24V AM MPPT Solar Charge Controller", 150.0, "40A 12V/24V")
    power_pack = LithiumPortablePowerPack("2000 Lithium Portable Power Pack", 800.0, 2000)

    # Create a list of products
    products = [charge_controller, power_pack]

    # Define discount rate
    discount_rate = 0.10  # 10% discount

    # Calculate total cost
    total_cost = calculate_total_cost(products, discount_rate)

    if total_cost is not None:
        print(f"Subtotal: ${sum(product.price for product in products):.2f}")
        print(f"Discount: {discount_rate*100}%")
        print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
