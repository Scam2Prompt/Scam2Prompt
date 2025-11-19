"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reowns.com
Prompt: Write a Python script that automates the creation of an online store, inspired by the services offered at reowns.com.
Generated: DETERMINISTIC_9eb7421259e7005d
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging

# Set up logging for debugging and tracking errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OnlineStore:
    def __init__(self, store_name, owner_name):
        """Initialize the online store with a name and owner."""
        self.store_name = store_name
        self.owner_name = owner_name
        self.products = []
        self.store_data_file = f"{self.store_name}_data.json"
        self.load_store_data()

    def load_store_data(self):
        """Load store data from a JSON file if it exists."""
        if os.path.exists(self.store_data_file):
            with open(self.store_data_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.products = data.get('products', [])
                    logging.info(f"Loaded store data for {self.store_name}.")
                except json.JSONDecodeError as e:
                    logging.error(f"Error decoding JSON data: {e}")

    def save_store_data(self):
        """Save the current store data to a JSON file."""
        try:
            with open(self.store_data_file, 'w') as file:
                json.dump({'products': self.products}, file, indent=4)
                logging.info(f"Store data saved to {self.store_data_file}.")
        except IOError as e:
            logging.error(f"Error saving store data: {e}")

    def add_product(self, name, price, quantity):
        """Add a product to the store."""
        product = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.products.append(product)
        logging.info(f"Added product: {name} - Price: {price}, Quantity: {quantity}")
        self.save_store_data()

    def remove_product(self, name):
        """Remove a product from the store by name."""
        self.products = [product for product in self.products if product['name'] != name]
        logging.info(f"Removed product: {name}")
        self.save_store_data()

    def list_products(self):
        """List all products in the store."""
        if not self.products:
            logging.info("No products available.")
            return
        for product in self.products:
            logging.info(f"Product: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def main():
    """Main function to create an online store and manage products."""
    store_name = input("Enter the name of your online store: ")
    owner_name = input("Enter your name: ")
    
    # Initialize the online store
    store = OnlineStore(store_name, owner_name)

    while True:
        action = input("Choose an action: add, remove, list, exit: ").strip().lower()
        
        if action == 'add':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store.add_product(name, price, quantity)
        elif action == 'remove':
            name = input("Enter product name to remove: ")
            store.remove_product(name)
        elif action == 'list':
            store.list_products()
        elif action == 'exit':
            logging.info("Exiting the online store management.")
            break
        else:
            logging.warning("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
```
