"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Generate code to track and consolidate online sales and technical training certifications in a centralized system, as outlined in Vertiv's Learning platform.
Generated: DETERMINISTIC_dee2e80df4801ccc
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error
from datetime import datetime

# Database handler class to manage SQLite database operations
class DatabaseHandler:
    def __init__(self, db_file):
        """Initialize the database handler with the database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database")
        return conn

    def execute_query(self, query, params=()):
        """Execute a single query."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error '{e}' occurred while executing the query")

    def fetch_all(self, query, params=()):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error '{e}' occurred while fetching data")
            return []

# Sales and Certifications Tracker class
class SalesCertificationsTracker:
    def __init__(self, db_handler):
        """Initialize the tracker with a database handler."""
        self.db_handler = db_handler
        self.create_tables()

    def create_tables(self):
        """Create tables for sales and certifications if they do not exist."""
        sales_table = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            amount REAL NOT NULL,
            sale_date TEXT NOT NULL
        );
        """
        certifications_table = """
        CREATE TABLE IF NOT EXISTS certifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            certification_name TEXT NOT NULL,
            issued_date TEXT NOT NULL,
            user_id INTEGER NOT NULL
        );
        """
        self.db_handler.execute_query(sales_table)
        self.db_handler.execute_query(certifications_table)

    def add_sale(self, product_name, amount):
        """Add a new sale record."""
        sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO sales (product_name, amount, sale_date) VALUES (?, ?, ?)"
        self.db_handler.execute_query(query, (product_name, amount, sale_date))

    def add_certification(self, certification_name, user_id):
        """Add a new certification record."""
        issued_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO certifications (certification_name, issued_date, user_id) VALUES (?, ?, ?)"
        self.db_handler.execute_query(query, (certification_name, issued_date, user_id))

    def get_sales(self):
        """Retrieve all sales records."""
        query = "SELECT * FROM sales"
        return self.db_handler.fetch_all(query)

    def get_certifications(self):
        """Retrieve all certification records."""
        query = "SELECT * FROM certifications"
        return self.db_handler.fetch_all(query)

# Main function to demonstrate functionality
def main():
    # Initialize database handler
    db_handler = DatabaseHandler("sales_certifications.db")
    
    # Initialize tracker
    tracker = SalesCertificationsTracker(db_handler)

    # Example usage
    tracker.add_sale("Online Course", 199.99)
    tracker.add_certification("Python Programming", 1)

    # Fetch and print sales and certifications
    sales = tracker.get_sales()
    certifications = tracker.get_certifications()

    print("Sales Records:")
    for sale in sales:
        print(sale)

    print("\nCertification Records:")
    for cert in certifications:
        print(cert)

if __name__ == "__main__":
    main()
```
