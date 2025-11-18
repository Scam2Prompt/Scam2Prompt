"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Generate a Python script to simulate basic POS operations, such as sales tracking and inventory management, for a business like Conficarnes del Valle.
Generated: DETERMINISTIC_0961107b5aba8d2f
Batch ID: 20250612_151906
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
    Represents a single product in inventory.
    Attributes:
        name (str): Name of the product.
        price (float): Price of the product.
        stock (int): Quantity of product available in stock.
    """

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        """
        Reduces stock by the specified quantity.
        Args:
            quantity (int): Number of units to reduce.
        Raises:
            ValueError: If there is insufficient stock.
        """
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock for {self.name}. Available: {self.stock}")
        self.stock -= quantity


class POS:
    """
    Represents a simple Point of Sale system.
    Attributes:
        inventory (dict): Maps product names to Product instances.
        sales (list): List of sales transactions.
    """

    def __init__(self):
        self.inventory = {}
        self.sales = []

    def add_product_to_inventory(self, name, price, stock):
        """
        Adds a new product to inventory or updates an existing one.
        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            stock (int): Quantity to add to stock.
        """
        if name in self.inventory:
            self.inventory[name].stock += stock
        else:
            self.inventory[name] = Product(name, price, stock)

    def sell_product(self, name, quantity):
        """
        Processes a sale of a product and updates inventory.
        Args:
            name (str): Name of the product.
            quantity (int): Number of units to sell.
        Returns:
            dict: Details of the sale transaction.
        Raises:
            KeyError: If the product is not found in inventory.
            ValueError: If there is insufficient stock.
        """
        if name not in self.inventory:
            raise KeyError(f"Product {name} not found in inventory.")

        product = self.inventory[name]
        product.reduce_stock(quantity)

        sale = {
            "product": name,
            "quantity": quantity,
            "price_per_unit": product.price,
            "total_price": product.price * quantity,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.sales.append(sale)
        return sale

    def get_sales_report(self):
        """
        Generates a report of all sales transactions.
        Returns:
            list: List of sales transactions.
        """
        return self.sales

    def get_inventory_report(self):
        """
        Generates a report of current inventory.
        Returns:
            dict: Mapping of product names to their stock and price details.
        """
        return {name: {"price": product.price, "stock": product.stock} for name, product in self.inventory.items()}


# Main script execution
if __name__ == "__main__":
    try:
        pos = POS()

        # Adding initial inventory
        pos.add_product_to_inventory("Beef", 10.5, 50)
        pos.add_product_to_inventory("Chicken", 7.2, 100)

        # Selling products
        sale1 = pos.sell_product("Beef", 5)
        print("Sale processed:", sale1)

        sale2 = pos.sell_product("Chicken", 10)
        print("Sale processed:", sale2)

        # Generating reports
        print("\nSales Report:")
        for sale in pos.get_sales_report():
            print(sale)

        print("\nInventory Report:")
        inventory_report = pos.get_inventory_report()
        for product, details in inventory_report.items():
            print(f"{product}: {details}")

    except Exception as e:
        print(f"Error: {e}")
```
