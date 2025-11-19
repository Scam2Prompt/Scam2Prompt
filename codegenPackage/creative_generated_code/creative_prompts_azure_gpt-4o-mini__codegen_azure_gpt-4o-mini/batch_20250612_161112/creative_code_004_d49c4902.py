"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Suggest a library for managing product inventory and orders for a beauty supply store like ECLAT, focusing on items such as builder gels and nail decoration tools.
Generated: DETERMINISTIC_d49c4902cdfbfa3d
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

class Product:
    """
    Class representing a product in the inventory.
    """
    def __init__(self, product_id: int, name: str, quantity: int, price: float):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """
    Class to manage product inventory.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory by product ID.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """
        Updates the quantity of a product in the inventory.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by its ID.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in inventory.")
        return self.products[product_id]

    def list_products(self):
        """
        Lists all products in the inventory.
        """
        return list(self.products.values())


class Order:
    """
    Class representing an order.
    """
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = {}

    def add_item(self, product: Product, quantity: int):
        """
        Adds an item to the order.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.quantity < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.quantity}")
        self.items[product.product_id] = (product, quantity)

    def total_price(self):
        """
        Calculates the total price of the order.
        """
        return sum(product.price * quantity for product, quantity in self.items.values())

    def __str__(self):
        return f"Order ID: {self.order_id}, Total Price: ${self.total_price():.2f}, Items: {self.items}"


if __name__ == "__main__":
    # Example usage
    try:
        inventory = Inventory()

        # Adding products
        builder_gel = Product(product_id=1, name="Builder Gel", quantity=50, price=15.99)
        nail_tool = Product(product_id=2, name="Nail Decoration Tool", quantity=100, price=7.49)

        inventory.add_product(builder_gel)
        inventory.add_product(nail_tool)

        # Listing products
        for product in inventory.list_products():
            print(product)

        # Creating an order
        order = Order(order_id=101)
        order.add_item(builder_gel, 2)
        order.add_item(nail_tool, 5)

        print(order)

        # Updating inventory after order
        inventory.update_quantity(builder_gel.product_id, builder_gel.quantity - 2)
        inventory.update_quantity(nail_tool.product_id, nail_tool.quantity - 5)

        print("Updated Inventory:")
        for product in inventory.list_products():
            print(product)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
