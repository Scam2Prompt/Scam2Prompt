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
import sqlite3
from datetime import datetime
import sys

class HardwareStoreManager:
    def __init__(self, db_name="hardware_store.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables for the hardware store management system."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                barcode TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                min_stock INTEGER DEFAULT 0,
                supplier TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                barcode TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                total_price REAL NOT NULL,
                sale_date TEXT NOT NULL,
                FOREIGN KEY (barcode) REFERENCES products (barcode)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT,
                phone TEXT,
                email TEXT
            )
        """)

        self.conn.commit()

    def add_product(self, barcode, name, price, stock, category=None, min_stock=0, supplier=None):
        """Add a new product to the inventory."""
        try:
            self.cursor.execute("""
                INSERT INTO products (barcode, name, category, price, stock, min_stock, supplier)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (barcode, name, category, price, stock, min_stock, supplier))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Product with barcode {barcode} already exists.")
            return False
        except Exception as e:
            print(f"Error adding product: {e}")
            return False

    def update_product(self, barcode, **kwargs):
        """Update product information."""
        if not kwargs:
            return False

        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values())
        values.append(barcode)

        try:
            self.cursor.execute(f"""
                UPDATE products 
                SET {set_clause}
                WHERE barcode = ?
            """, values)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating product: {e}")
            return False

    def get_product(self, barcode):
        """Retrieve product information by barcode."""
        self.cursor.execute("SELECT * FROM products WHERE barcode = ?", (barcode,))
        return self.cursor.fetchone()

    def record_sale(self, barcode, quantity):
        """Record a sale and update stock levels."""
        try:
            product = self.get_product(barcode)
            if not product:
                print(f"Product with barcode {barcode} not found.")
                return False

            if product[4] < quantity:
                print(f"Insufficient stock. Available: {product[4]}, Requested: {quantity}")
                return False

            total_price = product[3] * quantity
            sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Record the sale
            self.cursor.execute("""
                INSERT INTO sales (barcode, quantity, unit_price, total_price, sale_date)
                VALUES (?, ?, ?, ?, ?)
            """, (barcode, quantity, product[3], total_price, sale_date))

            # Update stock
            new_stock = product[4] - quantity
            self.update_product(barcode, stock=new_stock)

            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error recording sale: {e}")
            return False

    def get_sales_report(self, start_date=None, end_date=None):
        """Generate a sales report within a date range."""
        query = "SELECT * FROM sales"
        params = []

        if start_date and end_date:
            query += " WHERE sale_date BETWEEN ? AND ?"
            params.extend([start_date, end_date])
        elif start_date:
            query += " WHERE sale_date >= ?"
            params.append(start_date)
        elif end_date:
            query += " WHERE sale_date <= ?"
            params.append(end_date)

        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def check_low_stock(self):
        """Return products with stock below minimum threshold."""
        self.cursor.execute("""
            SELECT barcode, name, stock, min_stock 
            FROM products 
            WHERE stock <= min_stock
        """)
        return self.cursor.fetchall()

    def add_supplier(self, name, contact=None, phone=None, email=None):
        """Add a new supplier to the database."""
        try:
            self.cursor.execute("""
                INSERT INTO suppliers (name, contact, phone, email)
                VALUES (?, ?, ?, ?)
            """, (name, contact, phone, email))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding supplier: {e}")
            return False

    def close(self):
        """Close the database connection."""
        self.conn.close()

def main_menu():
    """Display the main menu and handle user input."""
    manager = HardwareStoreManager()

    while True:
        print("\nHardware Store Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Record Sale")
        print("4. View Sales Report")
        print("5. Check Low Stock")
        print("6. Add Supplier")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            barcode = input("Enter barcode: ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            category = input("Enter category (optional): ") or None
            min_stock = int(input("Enter minimum stock level (default 0): ") or 0)
            supplier = input("Enter supplier (optional): ") or None

            if manager.add_product(barcode, name, price, stock, category, min_stock, supplier):
                print("Product added successfully.")

        elif choice == "2":
            barcode = input("Enter barcode of product to update: ")
            product = manager.get_product(barcode)
            if not product:
                print("Product not found.")
                continue

            print("\nCurrent Product Details:")
            print(f"Name: {product[1]}")
            print(f"Category: {product[2]}")
            print(f"Price: {product[3]}")
            print(f"Stock: {product[4]}")
            print(f"Min Stock: {product[5]}")
            print(f"Supplier: {product[6]}")

            print("\nEnter new values (leave blank to keep current):")
            name = input(f"Name [{product[1]}]: ") or product[1]
            category = input(f"Category [{product[2]}]: ") or product[2]
            price = input(f"Price [{product[3]}]: ") or product[3]
            stock = input(f"Stock [{product[4]}]: ") or product[4]
            min_stock = input(f"Min Stock [{product[5]}]: ") or product[5]
            supplier = input(f"Supplier [{product[6]}]: ") or product[6]

            try:
                price = float(price)
                stock = int(stock)
                min_stock = int(min_stock)
            except ValueError:
                print("Invalid numeric input.")
                continue

            if manager.update_product(barcode, name=name, category=category, price=price, 
                                    stock=stock, min_stock=min_stock, supplier=supplier):
                print("Product updated successfully.")

        elif choice == "3":
            barcode = input("Enter product barcode: ")
            quantity = int(input("Enter quantity sold: "))
            if manager.record_sale(barcode, quantity):
                print("Sale recorded successfully.")

        elif choice == "4":
            print("\nSales Report Options:")
            print("1. All sales")
            print("2. Sales by date range")
            report_choice = input("Enter your choice (1-2): ")

            if report_choice == "1":
                sales = manager.get_sales_report()
            elif report_choice == "2":
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                sales = manager.get_sales_report(start_date, end_date)
            else:
                print("Invalid choice.")
                continue

            if not sales:
                print("No sales found.")
                continue

            print("\nSales Report:")
            print("ID | Barcode | Q
