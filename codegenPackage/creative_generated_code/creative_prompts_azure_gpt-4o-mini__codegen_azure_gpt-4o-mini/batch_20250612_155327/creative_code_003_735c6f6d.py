"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Develop a checkout process that includes options for both single and bulk purchases of coat racks, inspired by the purchasing model of Shahkar Industry.
Generated: DETERMINISTIC_735c6f6d896148ae
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoatRack:
    def __init__(self, name, price):
        """
        Initializes a CoatRack instance with a name and a price.

        :param name: str - The name of the coat rack.
        :param price: float - The price of the coat rack.
        """
        self.name = name
        self.price = price

class Checkout:
    def __init__(self):
        """
        Initializes the Checkout process with an empty cart.
        """
        self.cart = []

    def add_to_cart(self, coat_rack, quantity):
        """
        Adds a coat rack to the cart with the specified quantity.

        :param coat_rack: CoatRack - The coat rack to add.
        :param quantity: int - The number of coat racks to add.
        :raises ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.cart.append((coat_rack, quantity))

    def calculate_total(self):
        """
        Calculates the total price of items in the cart.

        :return: float - The total cost of the items in the cart.
        """
        total = sum(coat_rack.price * quantity for coat_rack, quantity in self.cart)
        return total

    def checkout(self):
        """
        Processes the checkout, returning the total amount due.

        :return: float - The total cost of the items in the cart.
        """
        if not self.cart:
            raise ValueError("Cart is empty. Cannot proceed to checkout.")
        
        total = self.calculate_total()
        self.cart.clear()  # Clear the cart after checkout
        return total

def main():
    """
    Main function to simulate the checkout process.
    """
    try:
        # Create some coat racks
        rack1 = CoatRack("Wooden Coat Rack", 49.99)
        rack2 = CoatRack("Metal Coat Rack", 39.99)

        # Create a checkout instance
        checkout = Checkout()

        # Add items to the cart (single and bulk)
        checkout.add_to_cart(rack1, 2)  # Adding 2 Wooden Coat Racks
        checkout.add_to_cart(rack2, 5)  # Adding 5 Metal Coat Racks

        # Calculate total and proceed to checkout
        total_amount = checkout.checkout()
        print(f"Total amount due: ${total_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
