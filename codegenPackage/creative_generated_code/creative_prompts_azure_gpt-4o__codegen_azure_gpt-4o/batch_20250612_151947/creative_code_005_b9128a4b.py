"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Write a script to manage laptop rental inventory and customer orders, inspired by the "Sewa Laptop Surabaya" article on Azuharu.net.
Generated: DETERMINISTIC_b9128a4b9d00b31e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Class to represent a laptop in the inventory
class Laptop:
    def __init__(self, id, brand, model, price_per_day, stock):
        self.id = id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.stock = stock

# Class to represent a customer order
class RentalOrder:
    def __init__(self, order_id, customer_name, laptop_id, rental_days, order_date):
        self.order_id = order_id
        self.customer_name = customer_name
        self.laptop_id = laptop_id
        self.rental_days = rental_days
        self.order_date = order_date

# Class to manage the laptop inventory and customer orders
class LaptopRentalManager:
    def __init__(self):
        self.inventory = {}  # Dictionary to store laptops by their ID
        self.orders = []     # List to store customer orders

    # Add a laptop to the inventory
    def add_laptop_to_inventory(self, laptop):
        if laptop.id in self.inventory:
            raise ValueError("Laptop ID already exists in inventory.")
        self.inventory[laptop.id] = laptop

    # Display the current inventory
    def display_inventory(self):
        print("Laptop Inventory:")
        for laptop in self.inventory.values():
            print(f"- ID: {laptop.id}, Brand: {laptop.brand}, Model: {laptop.model}, Price/day: ${laptop.price_per_day}, Stock: {laptop.stock}")

    # Process a rental order
    def rent_laptop(self, customer_name, laptop_id, rental_days):
        if laptop_id not in self.inventory:
            raise ValueError("Laptop ID does not exist in inventory.")
        
        laptop = self.inventory[laptop_id]
        if laptop.stock <= 0:
            raise ValueError("Laptop is out of stock.")
        
        # Generate an order ID (simple sequential ID)
        order_id = len(self.orders) + 1
        order_date = datetime.datetime.now()
        
        # Create and save the order
        order = RentalOrder(order_id, customer_name, laptop_id, rental_days, order_date)
        self.orders.append(order)
        
        # Deduct stock
        laptop.stock -= 1
        print("Order successfully placed!")
        print(f"Order ID: {order.order_id}, Customer: {order.customer_name}, Laptop: {laptop.brand} {laptop.model}, Days: {order.rental_days}, Total Cost: ${laptop.price_per_day * rental_days}")

    # Display all orders
    def display_orders(self):
        print("Customer Orders:")
        for order in self.orders:
            laptop = self.inventory[order.laptop_id]
            print(f"- Order ID: {order.order_id}, Customer: {order.customer_name}, Laptop: {laptop.brand} {laptop.model}, Rental Days: {order.rental_days}, Order Date: {order.order_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Return a laptop back to inventory (cancels an order)
    def return_laptop(self, order_id):
        if order_id <= 0 or order_id > len(self.orders):
            raise ValueError("Invalid order ID.")
        
        order = self.orders[order_id - 1]
        laptop = self.inventory[order.laptop_id]
        
        # Increment stock back
        laptop.stock += 1
        print(f"Order ID {order_id} has been successfully returned.")
        
        # Remove the order
        self.orders.pop(order_id - 1)

# Example usage
if __name__ == "__main__":
    manager = LaptopRentalManager()
    
    # Add laptops to inventory
    manager.add_laptop_to_inventory(Laptop(1, "Dell", "XPS 13", 30, 5))
    manager.add_laptop_to_inventory(Laptop(2, "Apple", "MacBook Air", 40, 3))
    manager.add_laptop_to_inventory(Laptop(3, "Asus", "ZenBook", 35, 7))
    
    # Display inventory
    manager.display_inventory()
    
    # Rent laptops
    manager.rent_laptop("John Doe", 1, 4)
    manager.rent_laptop("Jane Smith", 2, 2)
    
    # Display orders
    manager.display_orders()
    
    # Return a laptop
    manager.return_laptop(1)
    
    # Display inventory after return
    manager.display_inventory()
```
