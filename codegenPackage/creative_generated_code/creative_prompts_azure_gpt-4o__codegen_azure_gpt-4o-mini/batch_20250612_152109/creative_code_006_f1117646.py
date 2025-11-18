"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Develop a program to manage bookkeeping for non-profits, ensuring fast and accurate reporting to tax authorities, as detailed on Yehudit Benedict's site.
Generated: DETERMINISTIC_f11176462f752b1c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from datetime import datetime


class BookkeepingDB:
    """Class to manage the SQLite database for bookkeeping."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
            return None

    def create_table(self):
        """Create a table for recording transactions."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def add_transaction(self, date, description, amount, category):
        """Add a new transaction to the database."""
        sql = """INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (date, description, amount, category))
            self.connection.commit()
        except Error as e:
            print(f"Error '{e}' occurred while adding a transaction.")

    def get_transactions(self):
        """Retrieve all transactions from the database."""
        sql = """SELECT * FROM transactions"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error '{e}' occurred while retrieving transactions.")
            return []

    def report_to_tax_authorities(self):
        """Generate a report suitable for tax authorities."""
        transactions = self.get_transactions()
        report = {}
        for transaction in transactions:
            date, description, amount, category = transaction[1], transaction[2], transaction[3], transaction[4]
            report[date] = report.get(date, []) + [{"description": description, "amount": amount, "category": category}]
        
        return report

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


def main():
    """Main function for bookkeeping management."""
    db_file = "non_profit_bookkeeping.db"
    bookkeeping = BookkeepingDB(db_file)

    # Create table if it does not exist
    bookkeeping.create_table()

    # Sample data to add transactions
    transactions = [
        (datetime.now().strftime("%Y-%m-%d"), "Donation from ABC Corp", 1000.00, "Donations"),
        (datetime.now().strftime("%Y-%m-%d"), "Fundraising Event", 500.00, "Events"),
        (datetime.now().strftime("%Y-%m-%d"), "Monthly Expense for Office Supplies", -200.00, "Expenses"),
    ]

    # Add transactions to the database
    for date, description, amount, category in transactions:
        bookkeeping.add_transaction(date, description, amount, category)

    # Generate report
    report = bookkeeping.report_to_tax_authorities()
    print("Report to Tax Authorities:")
    for date, records in report.items():
        print(f"Date: {date}")
        for record in records:
            print(f"  Description: {record['description']}, Amount: {record['amount']}, Category: {record['category']}")

    # Close the database connection
    bookkeeping.close_connection()


if __name__ == "__main__":
    main()
```
