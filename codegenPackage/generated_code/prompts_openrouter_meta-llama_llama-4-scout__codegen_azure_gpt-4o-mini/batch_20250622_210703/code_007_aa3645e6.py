"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Design a library for managing essential oil inventory, including functions for tracking stock levels, orders, and shipping information for an online store like Use Essential Oils Australia.
Generated: DETERMINISTIC_aa3645e6e47c9fdc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# essential_oil_inventory.py

class EssentialOil:
    """
    Class to represent an essential oil product.
    """
    def __init__(self, name, sku, stock_level=0):
        """
        Initialize an essential oil with a name, SKU, and stock level.

        :param name: str - The name of the essential oil.
        :param sku: str - The stock keeping unit identifier.
        :param stock_level: int - The current stock level of the essential oil.
        """
        self.name = name
        self.sku = sku
        self.stock_level = stock_level

    def update_stock(self, quantity):
        """
        Update the stock level of the essential oil.

        :param quantity: int - The quantity to add (positive) or remove (negative).
        :raises ValueError: If the stock level goes negative.
        """
        if self.stock_level + quantity < 0:
            raise ValueError("Stock level cannot be negative.")
        self.stock_level += quantity


class Inventory:
    """
    Class to manage the inventory of essential oils.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.oils = {}

    def add_oil(self, oil):
        """
        Add an essential oil to the inventory.

        :param oil: EssentialOil - The essential oil to add.
        :raises ValueError: If the oil already exists in the inventory.
        """
        if oil.sku in self.oils:
            raise ValueError("Essential oil with this SKU already exists.")
        self.oils[oil.sku] = oil

    def update_stock(self, sku, quantity):
        """
        Update the stock level of an essential oil by SKU.

        :param sku: str - The SKU of the essential oil.
        :param quantity: int - The quantity to add (positive) or remove (negative).
        :raises KeyError: If the SKU does not exist in the inventory.
        """
        if sku not in self.oils:
            raise KeyError("Essential oil with this SKU does not exist.")
        self.oils[sku].update_stock(quantity)

    def get_stock_level(self, sku):
        """
        Get the current stock level of an essential oil by SKU.

        :param sku: str - The SKU of the essential oil.
        :return: int - The current stock level.
        :raises KeyError: If the SKU does not exist in the inventory.
        """
        if sku not in self.oils:
            raise KeyError("Essential oil with this SKU does not exist.")
        return self.oils[sku].stock_level

    def list_inventory(self):
        """
        List all essential oils in the inventory with their stock levels.

        :return: dict - A dictionary of SKU and stock level.
        """
        return {sku: oil.stock_level for sku, oil in self.oils.items()}


class Order:
    """
    Class to represent an order for essential oils.
    """
    def __init__(self, order_id, customer_name):
        """
        Initialize an order with an ID and customer name.

        :param order_id: str - The unique identifier for the order.
        :param customer_name: str - The name of the customer placing the order.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = {}

    def add_item(self, sku, quantity):
        """
        Add an item to the order.

        :param sku: str - The SKU of the essential oil.
        :param quantity: int - The quantity of the essential oil to order.
        :raises ValueError: If the quantity is less than or equal to zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items[sku] = self.items.get(sku, 0) + quantity

    def get_order_summary(self):
        """
        Get a summary of the order.

        :return: dict - A dictionary of SKU and quantity ordered.
        """
        return self.items


class Shipping:
    """
    Class to manage shipping information for orders.
    """
    def __init__(self):
        """
        Initialize an empty shipping records.
        """
        self.shipments = {}

    def create_shipment(self, order_id, address):
        """
        Create a shipment record for an order.

        :param order_id: str - The ID of the order being shipped.
        :param address: str - The shipping address.
        """
        self.shipments[order_id] = {
            'address': address,
            'status': 'Pending'
        }

    def update_shipment_status(self, order_id, status):
        """
        Update the shipping status of an order.

        :param order_id: str - The ID of the order.
        :param status: str - The new status of the shipment.
        :raises KeyError: If the order ID does not exist in the shipments.
        """
        if order_id not in self.shipments:
            raise KeyError("Order ID does not exist.")
        self.shipments[order_id]['status'] = status

    def get_shipment_info(self, order_id):
        """
        Get the shipping information for an order.

        :param order_id: str - The ID of the order.
        :return: dict - The shipping information.
        :raises KeyError: If the order ID does not exist in the shipments.
        """
        if order_id not in self.shipments:
            raise KeyError("Order ID does not exist.")
        return self.shipments[order_id]
```
