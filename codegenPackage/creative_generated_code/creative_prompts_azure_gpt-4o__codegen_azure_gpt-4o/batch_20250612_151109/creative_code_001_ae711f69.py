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
import datetime


class AdvertisingProduct:
    """
    Represents an advertising product such as a billboard, neon box, or banner.
    """
    def __init__(self, product_id, name, product_type, price_per_day):
        """
        Initialize an advertising product with its attributes.
        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param product_type: Type of the product (e.g., Billboard, Neon Box, Banner).
        :param price_per_day: Rental price per day.
        """
        self.product_id = product_id
        self.name = name
        self.product_type = product_type
        self.price_per_day = price_per_day
        self.is_available = True
        self.bookings = []  # List to track bookings

    def __str__(self):
        """
        String representation of the advertising product.
        """
        return f"{self.name} ({self.product_type}) - {'Available' if self.is_available else 'Booked'}"


class Booking:
    """
    Represents a booking for an advertising product.
    """
    def __init__(self, client_name, start_date, end_date):
        """
        Initialize a booking with client name, start date, and end date.
        :param client_name: Name of the client making the booking.
        :param start_date: Start date of the booking.
        :param end_date: End date of the booking.
        """
        self.client_name = client_name
        self.start_date = start_date
        self.end_date = end_date
        self.total_days = (end_date - start_date).days

    def __str__(self):
        """
        String representation of the booking.
        """
        return f"Booking by {self.client_name} from {self.start_date} to {self.end_date} ({self.total_days} days)"


class Inventory:
    """
    Manages a collection of advertising products and their bookings.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.
        :param product: AdvertisingProduct object to add.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def list_products(self):
        """
        List all products in the inventory with their status.
        """
        for product in self.products.values():
            print(product)

    def check_availability(self, product_id):
        """
        Check if a product is available for booking.
        :param product_id: Product ID to check.
        :return: True if available, False otherwise.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        return self.products[product_id].is_available

    def book_product(self, product_id, client_name, start_date, end_date):
        """
        Book a product for a client.
        :param product_id: Product ID to book.
        :param client_name: Name of the client.
        :param start_date: Start date of the booking (datetime.date).
        :param end_date: End date of the booking (datetime.date).
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        
        product = self.products[product_id]

        if not product.is_available:
            raise ValueError("Product is not available for booking.")
        
        # Validate date inputs
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            raise ValueError("Start date and end date must be of type datetime.date.")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")

        # Create and record the booking
        booking = Booking(client_name, start_date, end_date)
        product.bookings.append(booking)

        # Mark product as not available
        product.is_available = False
        print(f"Successfully booked {product.name} for {client_name}.")

    def list_bookings(self, product_id):
        """
        List all bookings for a specific product.
        :param product_id: Product ID to list bookings for.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        
        product = self.products[product_id]

        if not product.bookings:
            print(f"No bookings found for {product.name}.")
        else:
            print(f"Bookings for {product.name}:")
            for booking in product.bookings:
                print(booking)

    def mark_product_available(self, product_id):
        """
        Mark a product as available (e.g., after a booking ends).
        :param product_id: Product ID to mark as available.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        
        product = self.products[product_id]
        product.is_available = True
        print(f"{product.name} is now marked as available.")


if __name__ == "__main__":
    # Example usage of the inventory system
    inventory = Inventory()

    # Add products to inventory
    inventory.add_product(AdvertisingProduct("P001", "Billboard A", "Billboard", 200))
    inventory.add_product(AdvertisingProduct("P002", "Neon Box B", "Neon Box", 150))
    inventory.add_product(AdvertisingProduct("P003", "Banner C", "Banner", 100))

    # List available products
    print("Available products:")
    inventory.list_products()

    # Book a product
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    inventory.book_product("P001", "Client X", today, tomorrow)

    # List bookings for a product
    inventory.list_bookings("P001")

    # Mark product as available after booking
    inventory.mark_product_available("P001")

    # List products again
    print("\nUpdated product availability:")
    inventory.list_products()
```
