"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accounting-team.com
Prompt: How can I implement a bookkeeping system for my small startup that aligns with the services offered by The Accounting Team?
Generated: DETERMINISTIC_263aa282d35351a2
Batch ID: 20250612_155432
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

class BookkeepingSystem:
    """
    A simple bookkeeping system for managing income and expenses.
    This system uses SQLite for data persistence.
    """

    def __init__(self, db_name='bookkeeping.db'):
        """
        Initializes the bookkeeping system and creates tables if they don't exist.
        
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """
        Creates a database connection to the SQLite database.
        
        :return: SQLite database connection object.
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            print("Database connection successful.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """
        Creates the income and expenses tables if they do not exist.
        """
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY,
                        amount REAL NOT NULL,
                        source TEXT NOT NULL,
                        date TEXT NOT NULL
                    )
                ''')
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL,
                        date TEXT NOT NULL
                    )
                ''')
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_income(self, amount, source):
        """
        Adds a new income record to the database.
        
        :param amount: Amount of income.
        :param source: Source of income.
        """
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO income (amount, source, date)
                    VALUES (?, ?, ?)
                ''', (amount, source, date))
            print("Income added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding income: {e}")

    def add_expense(self, amount, category):
        """
        Adds a new expense record to the database.
        
        :param amount: Amount of expense.
        :param category: Category of expense.
        """
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO expenses (amount, category, date)
                    VALUES (?, ?, ?)
                ''', (amount, category, date))
            print("Expense added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding expense: {e}")

    def get_summary(self):
        """
        Retrieves the summary of income and expenses.
        
        :return: A dictionary containing total income, total expenses, and net profit.
        """
        try:
            total_income = self.connection.execute('SELECT SUM(amount) FROM income').fetchone()[0] or 0
            total_expenses = self.connection.execute('SELECT SUM(amount) FROM expenses').fetchone()[0] or 0
            net_profit = total_income - total_expenses

            return {
                'Total Income': total_income,
                'Total Expenses': total_expenses,
                'Net Profit': net_profit
            }
        except sqlite3.Error as e:
            print(f"Error retrieving summary: {e}")
            return {}

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
            
# Example usage
if __name__ == "__main__":
    bookkeeping = BookkeepingSystem()
    bookkeeping.add_income(1500.00, "Client Payment")
    bookkeeping.add_expense(500.00, "Office Supplies")
    summary = bookkeeping.get_summary()
    print(summary)
    bookkeeping.close_connection()
```
