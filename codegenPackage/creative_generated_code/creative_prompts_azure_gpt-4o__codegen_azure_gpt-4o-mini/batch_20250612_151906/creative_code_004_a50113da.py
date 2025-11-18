"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Develop a Python function that integrates with a database to manage consumer debt portfolios, as described in the B2C debt collection services on Arbitrium.sk.
Generated: DETERMINISTIC_a50113da0beb1945
Batch ID: 20250612_151906
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

class DebtPortfolioManager:
    """Class to manage consumer debt portfolios in a SQLite database."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database.
        
        Args:
            db_file (str): Path to the SQLite database file.
        
        Returns:
            Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_table(self):
        """Create a table for debt portfolios."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS debt_portfolios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            consumer_name TEXT NOT NULL,
            debt_amount REAL NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Pending', 'Settled', 'Defaulted'))
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Debt portfolios table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_debt_portfolio(self, consumer_name, debt_amount, due_date, status='Pending'):
        """Add a new debt portfolio to the database.
        
        Args:
            consumer_name (str): The name of the consumer.
            debt_amount (float): The total debt amount.
            due_date (str): The due date for the debt.
            status (str): The status of the debt (default is 'Pending').
            
        Returns:
            int: The id of the newly created debt portfolio or None.
        """
        sql = """INSERT INTO debt_portfolios (consumer_name, debt_amount, due_date, status)
                 VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (consumer_name, debt_amount, due_date, status))
            self.connection.commit()
            print("Debt portfolio added successfully.")
            return cursor.lastrowid
        except Error as e:
            print(f"Error adding debt portfolio: {e}")
            return None

    def update_debt_portfolio(self, portfolio_id, **kwargs):
        """Update an existing debt portfolio in the database.
        
        Args:
            portfolio_id (int): The id of the debt portfolio to update.
            kwargs: The fields to update (e.g., consumer_name, debt_amount, due_date, status).
            
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        sql = f"UPDATE debt_portfolios SET {set_clause} WHERE id = ?"
        values = list(kwargs.values()) + [portfolio_id]

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, values)
            self.connection.commit()
            print("Debt portfolio updated successfully.")
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating debt portfolio: {e}")
            return False

    def delete_debt_portfolio(self, portfolio_id):
        """Delete a debt portfolio from the database.
        
        Args:
            portfolio_id (int): The id of the debt portfolio to delete.
            
        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        sql = "DELETE FROM debt_portfolios WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (portfolio_id,))
            self.connection.commit()
            print("Debt portfolio deleted successfully.")
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting debt portfolio: {e}")
            return False

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Usage Example
if __name__ == "__main__":
    db_file = "debt_portfolios.db"
    manager = DebtPortfolioManager(db_file)
    manager.create_table()
    portfolio_id = manager.add_debt_portfolio("John Doe", 1500.00, "2023-12-31")
    manager.update_debt_portfolio(portfolio_id, status="Settled")
    manager.delete_debt_portfolio(portfolio_id)
    manager.close_connection()
```
