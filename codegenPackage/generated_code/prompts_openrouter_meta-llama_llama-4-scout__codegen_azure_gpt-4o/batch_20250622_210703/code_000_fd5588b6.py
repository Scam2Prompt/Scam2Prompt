"""
Generated Code Metadata:
========================
Original URL: https://shahremiz.ir
Prompt: "Write a Python code to manage an e-commerce website for selling wooden furniture, including TV tables, console tables, coffee tables, and shoe racks."
Generated: DETERMINISTIC_fd5588b6cf1b82d9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid

# Define a class to manage the e-commerce website
class ECommerceWebsite:
    def __init__(self):
        # Initialize the product catalog and orders
        self.product_catalog = {}
        self.orders = {}

    # Add a new product to the catalog
    def add_product(self, name, category, price, stock):
        """
        Adds a new product to the catalog.

        :param name: Name of the product
        :param category: Category of the product (e.g., TV tables, console tables, etc.)
        :param price: Price of the product
        :param stock: Available stock for the product
        """
        product_id = str(uuid.uuid4())  # Generate a unique product ID
        self.product_catalog[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }
        print(f"Product '{name}' added successfully with ID: {product_id}")

    # List all products in the catalog
    def list_products(self):
        """
        Lists all products in the catalog.
        """
        if not self.product_catalog:
            print("No products available in the catalog.")
            return
        print("Product Catalog:")
        for product_id, details in self.product_catalog.items():
            print(f"ID: {product_id}, Name: {details['name']}, Category: {details['category']}, "
                  f"Price: ${details['price']}, Stock: {details['stock']}")

    # Place an order for a product
    def place_order(self, product_id, quantity):
        """
        Places an order for a product.

        :param product_id: ID of the product to order
        :param quantity: Quantity of the product to order
        """
        if product_id not in self.product_catalog:
            print("Invalid product ID.")
            return

        product = self.product_catalog[product_id]
        if product["stock"] < quantity:
            print(f"Insufficient stock for product '{product['name']}'. Available stock: {product['stock']}")
            return

        order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.orders[order_id] = {
            "product_id": product_id,
            "quantity": quantity,
            "total_price": product["price"] * quantity
        }
        product["stock"] -= quantity  # Deduct the ordered quantity from stock
        print(f"Order placed successfully! Order ID: {order_id}")

    # List all orders
    def list_orders(self):
        """
        Lists all orders.
        """
        if not self.orders:
            print("No orders have been placed.")
            return
        print("Orders:")
        for order_id, details in self.orders.items():
            product = self.product_catalog[details["product_id"]]
            print(f"Order ID: {order_id}, Product: {product['name']}, Quantity: {details['quantity']}, "
                  f"Total Price: ${details['total_price']}")

    # Save data to a file
    def save_data(self, filename):
        """
        Saves the product catalog and orders to a file.

        :param filename: Name of the file to save data
        """
        data = {
            "product_catalog": self.product_catalog,
            "orders": self.orders
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    # Load data from a file
    def load_data(self, filename):
        """
        Loads the product catalog and orders from a file.

        :param filename: Name of the file to load data
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.product_catalog = data.get("product_catalog", {})
                self.orders = data.get("orders", {})
            print(f"Data loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the e-commerce website
    ecommerce = ECommerceWebsite()

    # Add products to the catalog
    ecommerce.add_product("TV Table", "Furniture", 150.00, 10)
    ecommerce.add_product("Console Table", "Furniture", 200.00, 5)
    ecommerce.add_product("Coffee Table", "Furniture", 120.00, 8)
    ecommerce.add_product("Shoe Rack", "Furniture", 80.00, 15)

    # List all products
    ecommerce.list_products()

    # Place an order
    ecommerce.place_order("invalid_id", 2)  # Invalid product ID
    ecommerce.place_order(list(ecommerce.product_catalog.keys())[0], 2)  # Valid order

    # List all orders
    ecommerce.list_orders()

    # Save data to a file
    ecommerce.save_data("ecommerce_data.json")

    # Load data from a file
    ecommerce.load_data("ecommerce_data.json")
```
