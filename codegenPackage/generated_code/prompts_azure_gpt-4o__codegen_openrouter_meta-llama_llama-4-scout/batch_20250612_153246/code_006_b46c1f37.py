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
# Import required libraries
import sqlite3
from datetime import datetime

class HardwareStore:
    def __init__(self, db_name):
        """
        Initialize the HardwareStore class.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products
            (id INTEGER PRIMARY KEY, barcode TEXT, name TEXT, price REAL, stock INTEGER)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales
            (id INTEGER PRIMARY KEY, product_id INTEGER, sale_date TEXT, quantity INTEGER, total_price REAL,
            FOREIGN KEY (product_id) REFERENCES products (id))
        ''')

        self.conn.commit()

    def add_product(self, barcode, name, price, stock):
        """
        Add a new product to the database.

        Args:
            barcode (str): The barcode of the product.
            name (str): The name of the product.
            price (float): The price of the product.
            stock (int): The initial stock of the product.
        """
        try:
            self.cursor.execute('INSERT INTO products (barcode, name, price, stock) VALUES (?, ?, ?, ?)',
                                (barcode, name, price, stock))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")

    def update_product_stock(self, barcode, new_stock):
        """
        Update the stock of a product.

        Args:
            barcode (str): The barcode of the product.
            new_stock (int): The new stock of the product.
        """
        try:
            self.cursor.execute('SELECT id FROM products WHERE barcode = ?', (barcode,))
            product_id = self.cursor.fetchone()
            if product_id:
                self.cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (new_stock, product_id[0]))
                self.conn.commit()
            else:
                print("Product not found.")
        except sqlite3.Error as e:
            print(f"Error updating product stock: {e}")

    def add_sale(self, barcode, quantity):
        """
        Add a new sale to the database.

        Args:
            barcode (str): The barcode of the product.
            quantity (int): The quantity of the product sold.
        """
        try:
            self.cursor.execute('SELECT id, price, stock FROM products WHERE barcode = ?', (barcode,))
            product = self.cursor.fetchone()
            if product:
                product_id, price, stock = product
                if stock >= quantity:
                    total_price = price * quantity
                    self.cursor.execute('INSERT INTO sales (product_id, sale_date, quantity, total_price) VALUES (?, ?, ?, ?)',
                                        (product_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), quantity, total_price))
                    self.cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (stock - quantity, product_id))
                    self.conn.commit()
                else:
                    print("Insufficient stock.")
            else:
                print("Product not found.")
        except sqlite3.Error as e:
            print(f"Error adding sale: {e}")

    def get_product_info(self, barcode):
        """
        Get the information of a product.

        Args:
            barcode (str): The barcode of the product.

        Returns:
            dict: The product information.
        """
        try:
            self.cursor.execute('SELECT * FROM products WHERE barcode = ?', (barcode,))
            product = self.cursor.fetchone()
            if product:
                return {
                    "id": product[0],
                    "barcode": product[1],
                    "name": product[2],
                    "price": product[3],
                    "stock": product[4]
                }
            else:
                print("Product not found.")
                return None
        except sqlite3.Error as e:
            print(f"Error getting product info: {e}")
            return None

    def get_sales_info(self):
        """
        Get all sales information.

        Returns:
            list: A list of sales information.
        """
        try:
            self.cursor.execute('SELECT * FROM sales')
            sales = self.cursor.fetchall()
            return [
                {
                    "id": sale[0],
                    "product_id": sale[1],
                    "sale_date": sale[2],
                    "quantity": sale[3],
                    "total_price": sale[4]
                } for sale in sales
            ]
        except sqlite3.Error as e:
            print(f"Error getting sales info: {e}")
            return []

def main():
    store = HardwareStore("hardware_store.db")

    while True:
        print("1. Add product")
        print("2. Update product stock")
        print("3. Add sale")
        print("4. Get product info")
        print("5. Get sales info")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            barcode = input("Enter barcode: ")
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            store.add_product(barcode, name, price, stock)
        elif choice == "2":
            barcode = input("Enter barcode: ")
            new_stock = int(input("Enter new stock: "))
            store.update_product_stock(barcode, new_stock)
        elif choice == "3":
            barcode = input("Enter barcode: ")
            quantity = int(input("Enter quantity: "))
            store.add_sale(barcode, quantity)
        elif choice == "4":
            barcode = input("Enter barcode: ")
            product_info = store.get_product_info(barcode)
            if product_info:
                print(product_info)
        elif choice == "5":
            sales_info = store.get_sales_info()
            if sales_info:
                for sale in sales_info:
                    print(sale)
        elif choice == "6":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
