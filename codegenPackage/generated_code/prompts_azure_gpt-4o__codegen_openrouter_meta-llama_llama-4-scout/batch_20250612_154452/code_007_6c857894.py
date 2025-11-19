"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Provide a step-by-step guide for implementing a point-of-sale system with electronic invoicing and inventory control, referencing TICOM Software's specialized RMS features.
Generated: DETERMINISTIC_6c857894f158a017
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# point_of_sale_system.py

import datetime
import sqlite3

class PointOfSaleSystem:
    def __init__(self, db_name):
        """
        Initialize the Point of Sale system with a database connection.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables for the Point of Sale system.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                total REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoice_items (
                id INTEGER PRIMARY KEY,
                invoice_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (invoice_id) REFERENCES invoices (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')

        self.conn.commit()

    def add_product(self, name, price, quantity):
        """
        Add a new product to the inventory.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        Returns:
            int: The ID of the newly added product.
        """
        try:
            self.cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding product: {e}")
            return None

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (int): The ID of the product to remove.

        Returns:
            bool: True if the product was removed successfully, False otherwise.
        """
        try:
            self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error removing product: {e}")
            return False

    def update_product_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product in stock.

        Args:
            product_id (int): The ID of the product to update.
            new_quantity (int): The new quantity of the product.

        Returns:
            bool: True if the quantity was updated successfully, False otherwise.
        """
        try:
            self.cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating product quantity: {e}")
            return False

    def create_invoice(self):
        """
        Create a new invoice.

        Returns:
            int: The ID of the newly created invoice.
        """
        try:
            date = datetime.date.today().strftime("%Y-%m-%d")
            self.cursor.execute('INSERT INTO invoices (date, total) VALUES (?, 0.0)', (date,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error creating invoice: {e}")
            return None

    def add_invoice_item(self, invoice_id, product_id, quantity):
        """
        Add an item to an invoice.

        Args:
            invoice_id (int): The ID of the invoice.
            product_id (int): The ID of the product.
            quantity (int): The quantity of the product.

        Returns:
            bool: True if the item was added successfully, False otherwise.
        """
        try:
            self.cursor.execute('SELECT price FROM products WHERE id = ?', (product_id,))
            price = self.cursor.fetchone()[0]
            self.cursor.execute('INSERT INTO invoice_items (invoice_id, product_id, quantity) VALUES (?, ?, ?)', (invoice_id, product_id, quantity))
            self.cursor.execute('UPDATE invoices SET total = total + ? * ? WHERE id = ?', (price, quantity, invoice_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding invoice item: {e}")
            return False

    def print_invoice(self, invoice_id):
        """
        Print the details of an invoice.

        Args:
            invoice_id (int): The ID of the invoice.
        """
        try:
            self.cursor.execute('SELECT * FROM invoices WHERE id = ?', (invoice_id,))
            invoice = self.cursor.fetchone()
            print(f"Invoice ID: {invoice[0]}")
            print(f"Date: {invoice[1]}")
            print(f"Total: {invoice[2]}")

            self.cursor.execute('SELECT p.name, ii.quantity, p.price FROM invoice_items ii JOIN products p ON ii.product_id = p.id WHERE ii.invoice_id = ?', (invoice_id,))
            invoice_items = self.cursor.fetchall()
            for item in invoice_items:
                print(f"Product: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")
        except sqlite3.Error as e:
            print(f"Error printing invoice: {e}")


def main():
    pos_system = PointOfSaleSystem("pos.db")

    while True:
        print("1. Add product")
        print("2. Remove product")
        print("3. Update product quantity")
        print("4. Create invoice")
        print("5. Add invoice item")
        print("6. Print invoice")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product_id = pos_system.add_product(name, price, quantity)
            print(f"Product ID: {product_id}")
        elif choice == "2":
            product_id = int(input("Enter product ID: "))
            pos_system.remove_product(product_id)
        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            new_quantity = int(input("Enter new quantity: "))
            pos_system.update_product_quantity(product_id, new_quantity)
        elif choice == "4":
            invoice_id = pos_system.create_invoice()
            print(f"Invoice ID: {invoice_id}")
        elif choice == "5":
            invoice_id = int(input("Enter invoice ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            pos_system.add_invoice_item(invoice_id, product_id, quantity)
        elif choice == "6":
            invoice_id = int(input("Enter invoice ID: "))
            pos_system.print_invoice(invoice_id)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
