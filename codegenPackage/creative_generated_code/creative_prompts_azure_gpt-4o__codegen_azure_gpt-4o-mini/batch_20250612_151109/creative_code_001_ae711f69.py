"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Generate Python code for managing an inventory of advertising products such as billboards, neon boxes, and banners, with functionality for tracking availability and client bookings.
Generated: DETERMINISTIC_ae711f69082290d1
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AdvertisingProduct:
    """
    Represents an advertising product in the inventory.
    """
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.booked = 0

    def is_available(self):
        """
        Checks if the product is available for booking.
        """
        return self.quantity - self.booked > 0

    def book(self, number):
        """
        Books a specified number of products.

        Args:
            number (int): The number of products to book.

        Raises:
            ValueError: If the requested number exceeds available quantity.
        """
        if number < 1:
            raise ValueError("Number of products to book must be at least 1.")
        if self.booked + number > self.quantity:
            raise ValueError("Not enough products available to book.")
        
        self.booked += number

    def cancel_booking(self, number):
        """
        Cancels a specified number of booked products.

        Args:
            number (int): The number of products to cancel.

        Raises:
            ValueError: If the requested number of bookings to cancel is invalid.
        """
        if number < 1:
            raise ValueError("Number of products to cancel must be at least 1.")
        if number > self.booked:
            raise ValueError("Cannot cancel more products than booked.")
        
        self.booked -= number


class Inventory:
    """
    Manages a collection of advertising products.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity):
        """
        Adds a new advertising product to the inventory.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            quantity (int): Number of available units.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product_id in self.products:
            raise ValueError("Product with this ID already exists.")
        
        self.products[product_id] = AdvertisingProduct(product_id, name, quantity)

    def book_product(self, product_id, number):
        """
        Books a specified number of a product.

        Args:
            product_id (str): Unique identifier for the product.
            number (int): Number of products to book.

        Raises:
            KeyError: If the product ID does not exist in the inventory.
            ValueError: If the booking request is invalid.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in inventory.")
        
        product = self.products[product_id]
        product.book(number)

    def cancel_booking(self, product_id, number):
        """
        Cancels a specified number of booked products.

        Args:
            product_id (str): Unique identifier for the product.
            number (int): Number of products to cancel.

        Raises:
            KeyError: If the product ID does not exist in the inventory.
            ValueError: If the cancellation request is invalid.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in inventory.")
        
        product = self.products[product_id]
        product.cancel_booking(number)

    def get_product_availability(self, product_id):
        """
        Returns the availability status of a product.

        Args:
            product_id (str): Unique identifier for the product.

        Raises:
            KeyError: If the product ID does not exist in the inventory.

        Returns:
            bool: True if available, False otherwise.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in inventory.")
        
        return self.products[product_id].is_available()


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Add products to inventory
    inventory.add_product("001", "Billboard", 10)
    inventory.add_product("002", "Neon Box", 5)
    
    # Book some products
    try:
        inventory.book_product("001", 3)
        print("3 Billboards booked successfully.")
    except (KeyError, ValueError) as e:
        print(f"Booking failed: {e}")
    
    # Check availability
    print("Billboard available:", inventory.get_product_availability("001"))
    
    # Cancel a booking
    try:
        inventory.cancel_booking("001", 1)
        print("1 Billboard booking cancelled successfully.")
    except (KeyError, ValueError) as e:
        print(f"Cancellation failed: {e}")

    # Check availability after cancellation
    print("Billboard available:", inventory.get_product_availability("001"))
```
