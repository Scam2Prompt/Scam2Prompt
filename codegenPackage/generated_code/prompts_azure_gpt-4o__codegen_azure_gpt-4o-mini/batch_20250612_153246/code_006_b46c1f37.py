"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Create a program to manage sales and stock data for a hardware store using DemirSoft's "Hırdavat Yapı Market Barkodlu Satış Programı."
Generated: DETERMINISTIC_b46c1f37674ef30a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class HardwareStore:
    def __init__(self, stock_file='stock.json', sales_file='sales.json'):
        """
        Initializes the HardwareStore with stock and sales data.
        Loads existing data from JSON files if they exist.
        """
        self.stock_file = stock_file
        self.sales_file = sales_file
        self.stock = self.load_data(self.stock_file)
        self.sales = self.load_data(self.sales_file)

    def load_data(self, filename):
        """
        Loads data from a JSON file.
        
        :param filename: The name of the JSON file to load data from.
        :return: A dictionary containing the data or an empty dictionary if the file does not exist.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self, filename, data):
        """
        Saves data to a JSON file.
        
        :param filename: The name of the JSON file to save data to.
        :param data: The data to save in JSON format.
        """
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_stock_item(self, barcode, name, quantity, price):
        """
        Adds a new item to the stock.
        
        :param barcode: The barcode of the item.
        :param name: The name of the item.
        :param quantity: The quantity of the item in stock.
        :param price: The price of the item.
        """
        if barcode in self.stock:
            raise ValueError("Item with this barcode already exists in stock.")
        
        self.stock[barcode] = {
            'name': name,
            'quantity': quantity,
            'price': price
        }
        self.save_data(self.stock_file, self.stock)

    def sell_item(self, barcode, quantity):
        """
        Sells an item from the stock.
        
        :param barcode: The barcode of the item to sell.
        :param quantity: The quantity of the item to sell.
        """
        if barcode not in self.stock:
            raise ValueError("Item not found in stock.")
        
        if self.stock[barcode]['quantity'] < quantity:
            raise ValueError("Not enough stock available.")
        
        # Update stock
        self.stock[barcode]['quantity'] -= quantity
        
        # Record the sale
        sale_record = {
            'barcode': barcode,
            'quantity': quantity,
            'total_price': self.stock[barcode]['price'] * quantity
        }
        self.sales.append(sale_record)
        
        # Save updated data
        self.save_data(self.stock_file, self.stock)
        self.save_data(self.sales_file, self.sales)

    def get_stock(self):
        """
        Returns the current stock data.
        
        :return: A dictionary containing the stock data.
        """
        return self.stock

    def get_sales(self):
        """
        Returns the sales data.
        
        :return: A list containing the sales records.
        """
        return self.sales

if __name__ == "__main__":
    store = HardwareStore()

    # Example usage
    try:
        store.add_stock_item('1234567890123', 'Hammer', 50, 15.99)
        store.add_stock_item('9876543210987', 'Screwdriver', 100, 7.49)
        store.sell_item('1234567890123', 2)
        
        print("Current Stock:", store.get_stock())
        print("Sales Records:", store.get_sales())
    except ValueError as e:
        print(f"Error: {e}")
```
