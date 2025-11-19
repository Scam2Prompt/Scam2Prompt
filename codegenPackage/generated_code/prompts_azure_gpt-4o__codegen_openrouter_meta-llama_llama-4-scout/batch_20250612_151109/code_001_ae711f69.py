"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Generate Python code for managing an inventory of advertising products such as billboards, neon boxes, and banners, with functionality for tracking availability and client bookings.
Generated: DETERMINISTIC_ae711f69082290d1
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from typing import Dict, List
from datetime import datetime, timedelta

class AdvertisingProduct:
    """Represents an advertising product."""

    def __init__(self, product_id: int, name: str, description: str, quantity: int):
        """
        Initializes an AdvertisingProduct.

        Args:
        - product_id (int): Unique identifier for the product.
        - name (str): Name of the product (e.g., billboard, neon box, banner).
        - description (str): Brief description of the product.
        - quantity (int): Initial quantity of the product available.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.bookings: List[Booking] = []

    def book(self, client_name: str, start_date: datetime, end_date: datetime):
        """
        Books a product for a client.

        Args:
        - client_name (str): Name of the client booking the product.
        - start_date (datetime): Start date of the booking.
        - end_date (datetime): End date of the booking.

        Raises:
        - ValueError: If the product is not available for the requested dates.
        """
        if self.quantity <= 0:
            raise ValueError("Product is not available.")

        for booking in self.bookings:
            if start_date < booking.end_date and end_date > booking.start_date:
                raise ValueError("Product is already booked for these dates.")

        self.quantity -= 1
        self.bookings.append(Booking(client_name, start_date, end_date))

    def cancel_booking(self, booking_id: int):
        """
        Cancels a booking by ID.

        Args:
        - booking_id (int): ID of the booking to cancel.

        Raises:
        - ValueError: If the booking ID is not found.
        """
        for i, booking in enumerate(self.bookings):
            if i == booking_id:
                self.quantity += 1
                del self.bookings[i]
                return
        raise ValueError("Booking ID not found.")

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Quantity: {self.quantity}"


class Booking:
    """Represents a booking."""

    id_counter = 0

    def __init__(self, client_name: str, start_date: datetime, end_date: datetime):
        """
        Initializes a Booking.

        Args:
        - client_name (str): Name of the client.
        - start_date (datetime): Start date of the booking.
        - end_date (datetime): End date of the booking.
        """
        self.id = Booking.id_counter
        Booking.id_counter += 1
        self.client_name = client_name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Booking {self.id} for {self.client_name} from {self.start_date} to {self.end_date}"


class Inventory:
    """Manages an inventory of advertising products."""

    def __init__(self):
        self.products: Dict[int, AdvertisingProduct] = {}

    def add_product(self, product: AdvertisingProduct):
        """
        Adds a product to the inventory.

        Args:
        - product (AdvertisingProduct): Product to add.
        """
        self.products[product.product_id] = product

    def get_product(self, product_id: int) -> AdvertisingProduct:
        """
        Retrieves a product by ID.

        Args:
        - product_id (int): ID of the product to retrieve.

        Returns:
        - AdvertisingProduct: The product with the given ID.

        Raises:
        - ValueError: If the product ID is not found.
        """
        try:
            return self.products[product_id]
        except KeyError:
            raise ValueError("Product ID not found.")

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    billboard = AdvertisingProduct(1, "Billboard", "Large billboard", 5)
    neon_box = AdvertisingProduct(2, "Neon Box", "Colorful neon box", 3)
    banner = AdvertisingProduct(3, "Banner", "Large banner", 10)

    # Add products to the inventory
    inventory.add_product(billboard)
    inventory.add_product(neon_box)
    inventory.add_product(banner)

    # Print initial inventory
    print(inventory)

    # Book a product
    try:
        billboard.book("Client1", datetime.now(), datetime.now() + timedelta(days=7))
        print(billboard.bookings[0])
    except ValueError as e:
        print(e)

    # Cancel a booking
    try:
        billboard.cancel_booking(0)
        print("Booking cancelled successfully.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
