"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Develop a program to track sales performance and generate reports for e-commerce stores, referencing the rapid sales results highlighted by FinishDrop.
Generated: DETERMINISTIC_7ebb2b939aece678
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
from typing import List, Tuple

# Database handler class
class SalesDatabase:
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_sales_table()

    def create_sales_table(self):
        """Create sales table if it does not exist."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    sale_date TEXT NOT NULL,
                    total_amount REAL NOT NULL
                )
            ''')

    def add_sale(self, product_name: str, quantity: int, total_amount: float):
        """Insert a new sale record into the database."""
        sale_date = datetime.now().isoformat()
        with self.connection:
            self.connection.execute('''
                INSERT INTO sales (product_name, quantity, sale_date, total_amount)
                VALUES (?, ?, ?, ?)
            ''', (product_name, quantity, sale_date, total_amount))

    def get_sales_report(self) -> List[Tuple]:
        """Retrieve a report of all sales."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM sales')
        return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Report generator class
class SalesReport:
    def __init__(self, db: SalesDatabase):
        """Initialize the sales report generator with a database instance."""
        self.db = db

    def generate_report(self) -> str:
        """Generate a simple sales report."""
        sales_data = self.db.get_sales_report()
        report_lines = ["Sales Report:"]
        report_lines.append(f"{'ID':<5} {'Product Name':<20} {'Quantity':<10} {'Sale Date':<25} {'Total Amount':<15}")
        report_lines.append("=" * 75)

        for sale in sales_data:
            report_lines.append(f"{sale[0]:<5} {sale[1]:<20} {sale[2]:<10} {sale[3]:<25} ${sale[4]:<15.2f}")

        return "\n".join(report_lines)

def main():
    """Main program execution."""
    try:
        # Initialize the database
        db = SalesDatabase('sales_data.db')

        # Example sales data (in a real scenario, this would come from user input or an API)
        sales = [
            ("Product A", 2, 29.99),
            ("Product B", 1, 19.99),
            ("Product C", 5, 99.95)
        ]

        # Add sales to the database
        for product_name, quantity, total_amount in sales:
            db.add_sale(product_name, quantity, total_amount)

        # Generate and print the sales report
        report_generator = SalesReport(db)
        print(report_generator.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the database connection is closed
        db.close()

if __name__ == "__main__":
    main()
```
