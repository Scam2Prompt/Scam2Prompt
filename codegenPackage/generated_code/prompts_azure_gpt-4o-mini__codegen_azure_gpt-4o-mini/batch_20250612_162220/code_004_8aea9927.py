"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Suggest a framework for building a vending machine application that showcases the unique benefits of Manna Markets, such as accessibility and diverse product options.
Generated: DETERMINISTIC_8aea99270a698966
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vending_machine.py

class Product:
    """Class representing a product in the vending machine."""
    
    def __init__(self, name, price, quantity):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param price: float - The price of the product
        :param quantity: int - The quantity available in the vending machine
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self):
        """Check if the product is available."""
        return self.quantity > 0

    def dispense(self):
        """Dispense the product and reduce its quantity."""
        if self.is_available():
            self.quantity -= 1
            return True
        return False


class VendingMachine:
    """Class representing a vending machine."""

    def __init__(self):
        """Initialize the vending machine with an empty product list."""
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the vending machine.

        :param product: Product - The product to add
        """
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def get_product(self, product_name):
        """
        Retrieve a product by name.

        :param product_name: str - The name of the product
        :return: Product or None - The product if found, otherwise None
        """
        return self.products.get(product_name)

    def purchase_product(self, product_name, payment):
        """
        Purchase a product from the vending machine.

        :param product_name: str - The name of the product to purchase
        :param payment: float - The amount of money provided for the purchase
        :return: str - Result of the purchase attempt
        """
        product = self.get_product(product_name)
        if not product:
            return "Product not found."
        if not product.is_available():
            return "Product is out of stock."
        if payment < product.price:
            return "Insufficient payment."

        product.dispense()
        return f"Dispensed {product.name}. Thank you for your purchase!"


def main():
    """Main function to demonstrate the vending machine functionality."""
    # Create a vending machine instance
    vending_machine = VendingMachine()

    # Add products to the vending machine
    vending_machine.add_product(Product("Water", 1.00, 10))
    vending_machine.add_product(Product("Soda", 1.50, 5))
    vending_machine.add_product(Product("Chips", 1.25, 8))

    # Simulate a purchase
    try:
        print(vending_machine.purchase_product("Soda", 2.00))  # Successful purchase
        print(vending_machine.purchase_product("Chips", 1.00))  # Insufficient payment
        print(vending_machine.purchase_product("Juice", 1.50))  # Product not found
        print(vending_machine.purchase_product("Water", 1.00))  # Successful purchase
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
