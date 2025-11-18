"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Write Python code to simulate inventory management for a supplier of aromatic essential oils like Karnataka Aromas, including tracking stock levels, dispatch schedules, and order processing.
Generated: DETERMINISTIC_fdbc771d4cb403a3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Product:
    """
    Represents a product in the inventory.
    """
    def __init__(self, product_id, name, stock_level):
        """
        Initialize a Product object.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param stock_level: Current stock level of the product
        """
        self.product_id = product_id
        self.name = name
        self.stock_level = stock_level


class Order:
    """
    Represents a customer order.
    """
    def __init__(self, order_id, product_id, quantity, dispatch_date):
        """
        Initialize an Order object.

        :param order_id: Unique identifier for the order
        :param product_id: ID of the product being ordered
        :param quantity: Quantity of the product requested
        :param dispatch_date: Scheduled dispatch date
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.dispatch_date = dispatch_date


class InventoryManagement:
    """
    Manages inventory for a supplier of aromatic essential oils.
    """
    def __init__(self):
        """
        Initialize the inventory management system with an empty inventory and orders.
        """
        self.products = {}  # Stores products by product_id
        self.orders = {}    # Stores orders by order_id

    def add_product(self, product_id, name, stock_level):
        """
        Add a new product to the inventory.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param stock_level: Initial stock level
        """
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        self.products[product_id] = Product(product_id, name, stock_level)

    def update_stock(self, product_id, new_stock_level):
        """
        Update the stock level for a product.

        :param product_id: ID of the product to update
        :param new_stock_level: New stock level
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' not found.")
        self.products[product_id].stock_level = new_stock_level

    def place_order(self, order_id, product_id, quantity, dispatch_date):
        """
        Place a new order for a product.

        :param order_id: Unique identifier for the order
        :param product_id: ID of the product being ordered
        :param quantity: Quantity of the product requested
        :param dispatch_date: Scheduled dispatch date
        """
        if order_id in self.orders:
            raise ValueError(f"Order ID '{order_id}' already exists.")
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' not found.")
        if self.products[product_id].stock_level < quantity:
            raise ValueError("Insufficient stock to fulfill the order.")
        
        self.orders[order_id] = Order(order_id, product_id, quantity, dispatch_date)
        self.products[product_id].stock_level -= quantity  # Deduct stock

    def get_product_info(self, product_id):
        """
        Retrieve information for a specific product.

        :param product_id: ID of the product
        :return: Product object
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' not found.")
        return self.products[product_id]

    def get_order_info(self, order_id):
        """
        Retrieve information for a specific order.

        :param order_id: ID of the order
        :return: Order object
        """
        if order_id not in self.orders:
            raise ValueError(f"Order ID '{order_id}' not found.")
        return self.orders[order_id]

    def list_products(self):
        """
        List all products in the inventory.

        :return: List of Product objects
        """
        return list(self.products.values())

    def list_orders(self):
        """
        List all orders.

        :return: List of Order objects
        """
        return list(self.orders.values())


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize inventory management system
        inventory = InventoryManagement()

        # Add products to inventory
        inventory.add_product("P001", "Lavender Oil", 100)
        inventory.add_product("P002", "Rosemary Oil", 50)

        # Update product stock
        inventory.update_stock("P001", 120)

        # Place orders
        inventory.place_order("O001", "P001", 20, datetime.date(2023, 10, 15))
        inventory.place_order("O002", "P002", 10, datetime.date(2023, 10, 20))

        # Retrieve product and order information
        print("Product Info:", vars(inventory.get_product_info("P001")))
        print("Order Info:", vars(inventory.get_order_info("O001")))

        # List all products and orders
        print("All Products:", [vars(product) for product in inventory.list_products()])
        print("All Orders:", [vars(order) for order in inventory.list_orders()])
    except Exception as e:
        print(f"Error: {e}")
```
