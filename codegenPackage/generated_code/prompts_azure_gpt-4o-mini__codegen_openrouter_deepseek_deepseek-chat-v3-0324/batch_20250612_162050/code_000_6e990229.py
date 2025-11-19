"""
Generated Code Metadata:
========================
Original URL: https://govindsweets.com
Prompt: Generate a Python script to create an online ordering system for sweets and bakery products similar to those offered by Govind Sweets, including categories like Mava Mithai and Namkeen.
Generated: DETERMINISTIC_6e990229ffc86a61
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Product:
    """
    Represents a product in the online ordering system.
    """
    def __init__(self, id: int, name: str, category: str, price: float, description: str = "", available: bool = True):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.available = available

    def to_dict(self) -> Dict:
        """Convert product to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'available': self.available
        }

class OrderItem:
    """
    Represents an item in an order with quantity.
    """
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total(self) -> float:
        """Calculate total price for this order item."""
        return self.product.price * self.quantity

    def to_dict(self) -> Dict:
        """Convert order item to dictionary for JSON serialization."""
        return {
            'product': self.product.to_dict(),
            'quantity': self.quantity,
            'total': self.get_total()
        }

class Order:
    """
    Represents a customer order.
    """
    def __init__(self, order_id: int, customer_name: str, contact: str, delivery_address: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.contact = contact
        self.delivery_address = delivery_address
        self.items: List[OrderItem] = []
        self.status = "Pending"

    def add_item(self, item: OrderItem) -> None:
        """Add an item to the order."""
        self.items.append(item)

    def remove_item(self, product_id: int) -> bool:
        """Remove an item from the order by product ID."""
        for i, item in enumerate(self.items):
            if item.product.id == product_id:
                self.items.pop(i)
                return True
        return False

    def calculate_total(self) -> float:
        """Calculate the total price of the order."""
        return sum(item.get_total() for item in self.items)

    def to_dict(self) -> Dict:
        """Convert order to dictionary for JSON serialization."""
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'contact': self.contact,
            'delivery_address': self.delivery_address,
            'items': [item.to_dict() for item in self.items],
            'total': self.calculate_total(),
            'status': self.status
        }

class SweetShop:
    """
    Main class for the online sweet shop ordering system.
    """
    def __init__(self):
        self.products: List[Product] = []
        self.orders: List[Order] = []
        self.next_order_id = 1

    def add_product(self, product: Product) -> None:
        """Add a product to the shop."""
        if any(p.id == product.id for p in self.products):
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products.append(product)

    def get_product(self, product_id: int) -> Optional[Product]:
        """Get a product by ID."""
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_products_by_category(self, category: str) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products if p.category.lower() == category.lower() and p.available]

    def create_order(self, customer_name: str, contact: str, delivery_address: str) -> Order:
        """Create a new order."""
        order = Order(self.next_order_id, customer_name, contact, delivery_address)
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def get_order(self, order_id: int) -> Optional[Order]:
        """Get an order by ID."""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def update_order_status(self, order_id: int, status: str) -> bool:
        """Update the status of an order."""
        order = self.get_order(order_id)
        if order:
            order.status = status
            return True
        return False

    def save_to_file(self, filename: str) -> None:
        """Save shop data to a JSON file."""
        data = {
            'products': [p.to_dict() for p in self.products],
            'orders': [o.to_dict() for o in self.orders],
            'next_order_id': self.next_order_id
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load shop data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = [Product(**p) for p in data['products']]
                self.orders = []
                for o in data['orders']:
                    order = Order(o['order_id'], o['customer_name'], o['contact'], o['delivery_address'])
                    order.status = o['status']
                    for item in o['items']:
                        product = Product(**item['product'])
                        order.add_item(OrderItem(product, item['quantity']))
                    self.orders.append(order)
                self.next_order_id = data['next_order_id']
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty shop.")
        except json.JSONDecodeError:
            print(f"Error decoding {filename}. Starting with empty shop.")
        except Exception as e:
            print(f"Error loading data: {str(e)}. Starting with empty shop.")

def initialize_sample_data(shop: SweetShop) -> None:
    """Initialize the shop with sample data."""
    categories = {
        "Mava Mithai": [
            ("Kaju Katli", 500, "Delicious cashew sweet"),
            ("Mava Peda", 400, "Traditional milk sweet"),
            ("Besan Ladoo", 300, "Gram flour sweet")
        ],
        "Namkeen": [
            ("Kaju Namkeen", 200, "Cashew savory snack"),
            ("Mathri", 150, "Crispy flour snack"),
            ("Chivda", 180, "Flattened rice snack")
        ],
        "Sweets": [
            ("Gulab Jamun", 250, "Deep fried milk balls in sugar syrup"),
            ("Rasgulla", 220, "Spongy cottage cheese balls in syrup"),
            ("Jalebi", 200, "Crispy swirls dipped in sugar syrup")
        ]
    }

    product_id = 1
    for category, items in categories.items():
        for name, price, description in items:
            shop.add_product(Product(product_id, name, category, price, description))
            product_id += 1

def main_menu(shop: SweetShop) -> None:
    """Display the main menu and handle user input."""
    while True:
        print("\nGovind Sweets Online Ordering System")
        print("1. Browse Products")
        print("2. Place an Order")
        print("3. View Orders")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            browse_products(shop)
        elif choice == "2":
            place_order(shop)
        elif choice == "3":
            view_orders(shop)
        elif choice == "4":
            filename = input("Enter filename to save: ")
            shop.save_to_file(filename)
            print("Data saved successfully.")
        elif choice == "5":
            filename = input("Enter filename to load: ")
            shop.load_from_file(filename)
            print("Data loaded successfully.")
        elif choice == "6":
            print("Thank you for using Govind Sweets Online Ordering System!")
            break
        else:
            print("Invalid choice. Please try again.")

def browse_products(shop: SweetShop) -> None:
    """Display product browsing menu."""
    while True:
        print("\nBrowse Products")
        print("1. View All Products")
        print("2. View by Category")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAll Products:")
            for product in shop.products:
                print(f"{product.id}. {product.name} ({product.category}) - ₹{product.price} - {product.description}")
        elif choice == "2":
            categories = set(p.category for p in shop.products)
            print("\nAvailable Categories:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            cat_choice = input("Select category (number)
