"""
Generated Code Metadata:
========================
Original URL: https://bossasopetroleum.com
Prompt: Write a script that automates the delivery information process for a petrol station, taking cues from the operational details provided by Bosasa Petroleum.
Generated: DETERMINISTIC_83d5380494e58b3d
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# delivery_automation.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryInfo:
    def __init__(self, delivery_id, product_type, quantity, delivery_date, supplier):
        """
        Initialize a DeliveryInfo object.

        Args:
            delivery_id (int): Unique identifier for the delivery.
            product_type (str): Type of petroleum product (e.g., petrol, diesel).
            quantity (float): Quantity of product delivered in liters.
            delivery_date (str): Date of delivery in YYYY-MM-DD format.
            supplier (str): Name of the supplier.
        """
        self.delivery_id = delivery_id
        self.product_type = product_type
        self.quantity = quantity
        self.delivery_date = delivery_date
        self.supplier = supplier

class PetrolStation:
    def __init__(self, name, location):
        """
        Initialize a PetrolStation object.

        Args:
            name (str): Name of the petrol station.
            location (str): Location of the petrol station.
        """
        self.name = name
        self.location = location
        self.deliveries = []

    def add_delivery(self, delivery_info):
        """
        Add a delivery to the petrol station's records.

        Args:
            delivery_info (DeliveryInfo): Delivery information to add.
        """
        self.deliveries.append(delivery_info)

    def get_deliveries(self):
        """
        Retrieve a list of all deliveries.

        Returns:
            list[DeliveryInfo]: List of DeliveryInfo objects.
        """
        return self.deliveries

def validate_delivery_info(delivery_id, product_type, quantity, delivery_date, supplier):
    """
    Validate delivery information.

    Args:
        delivery_id (int): Unique identifier for the delivery.
        product_type (str): Type of petroleum product.
        quantity (float): Quantity of product delivered in liters.
        delivery_date (str): Date of delivery in YYYY-MM-DD format.
        supplier (str): Name of the supplier.

    Raises:
        ValueError: If any of the input values are invalid.
    """
    if not isinstance(delivery_id, int) or delivery_id <= 0:
        raise ValueError("Invalid delivery ID")
    if not product_type or not isinstance(product_type, str):
        raise ValueError("Invalid product type")
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Invalid quantity")
    try:
        datetime.datetime.strptime(delivery_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid delivery date")
    if not supplier or not isinstance(supplier, str):
        raise ValueError("Invalid supplier")

def create_delivery_info(delivery_id, product_type, quantity, delivery_date, supplier):
    """
    Create a DeliveryInfo object.

    Args:
        delivery_id (int): Unique identifier for the delivery.
        product_type (str): Type of petroleum product.
        quantity (float): Quantity of product delivered in liters.
        delivery_date (str): Date of delivery in YYYY-MM-DD format.
        supplier (str): Name of the supplier.

    Returns:
        DeliveryInfo: DeliveryInfo object.

    Raises:
        ValueError: If any of the input values are invalid.
    """
    validate_delivery_info(delivery_id, product_type, quantity, delivery_date, supplier)
    return DeliveryInfo(delivery_id, product_type, quantity, delivery_date, supplier)

def main():
    # Create a petrol station
    station = PetrolStation("Bosasa Petroleum", "Kampala")

    # Create delivery information
    delivery1 = create_delivery_info(1, "Petrol", 10000, "2024-09-16", "Supplier X")
    delivery2 = create_delivery_info(2, "Diesel", 5000, "2024-09-17", "Supplier Y")

    # Add deliveries to the petrol station
    station.add_delivery(delivery1)
    station.add_delivery(delivery2)

    # Log deliveries
    logging.info("Deliveries:")
    for delivery in station.get_deliveries():
        logging.info(f"ID: {delivery.delivery_id}, Product: {delivery.product_type}, Quantity: {delivery.quantity}L, Date: {delivery.delivery_date}, Supplier: {delivery.supplier}")

if __name__ == "__main__":
    main()
```
