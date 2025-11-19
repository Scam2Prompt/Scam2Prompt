"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Develop a Python function that integrates with a database to manage consumer debt portfolios, as described in the B2C debt collection services on Arbitrium.sk.
Generated: DETERMINISTIC_a50113da0beb1945
Batch ID: 20250612_151906
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
from typing import Dict, List

class DebtPortfolioManager:
    """
    A class to manage consumer debt portfolios.

    Attributes:
    db_name (str): The name of the SQLite database file.
    """

    def __init__(self, db_name: str = "debt_portfolio.db"):
        """
        Initializes a DebtPortfolioManager instance.

        Args:
        db_name (str): The name of the SQLite database file. Defaults to "debt_portfolio.db".
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        """
        Establishes a connection to the SQLite database.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self):
        """
        Creates the debt_portfolio table if it does not exist.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        query = """
            CREATE TABLE IF NOT EXISTS debt_portfolio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                consumer_name TEXT NOT NULL,
                debt_amount REAL NOT NULL,
                debt_status TEXT NOT NULL DEFAULT 'outstanding'
            )
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_debt_portfolio(self, consumer_name: str, debt_amount: float):
        """
        Adds a new debt portfolio to the database.

        Args:
        consumer_name (str): The name of the consumer.
        debt_amount (float): The amount of debt.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        query = """
            INSERT INTO debt_portfolio (consumer_name, debt_amount)
            VALUES (?, ?)
        """
        try:
            self.cursor.execute(query, (consumer_name, debt_amount))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding debt portfolio: {e}")

    def get_debt_portfolio(self, id: int = None) -> List[Dict]:
        """
        Retrieves a debt portfolio or all debt portfolios from the database.

        Args:
        id (int): The ID of the debt portfolio to retrieve. Defaults to None.

        Returns:
        List[Dict]: A list of dictionaries containing debt portfolio information.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        if id:
            query = """
                SELECT * FROM debt_portfolio
                WHERE id = ?
            """
            try:
                self.cursor.execute(query, (id,))
                return [dict(zip([description[0] for description in self.cursor.description], self.cursor.fetchone()))]
            except sqlite3.Error as e:
                print(f"Error retrieving debt portfolio: {e}")
        else:
            query = """
                SELECT * FROM debt_portfolio
            """
            try:
                self.cursor.execute(query)
                return [dict(zip([description[0] for description in self.cursor.description], row)) for row in self.cursor.fetchall()]
            except sqlite3.Error as e:
                print(f"Error retrieving debt portfolios: {e}")

    def update_debt_portfolio(self, id: int, consumer_name: str = None, debt_amount: float = None, debt_status: str = None):
        """
        Updates a debt portfolio in the database.

        Args:
        id (int): The ID of the debt portfolio to update.
        consumer_name (str): The updated name of the consumer. Defaults to None.
        debt_amount (float): The updated amount of debt. Defaults to None.
        debt_status (str): The updated status of the debt. Defaults to None.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        query = """
            UPDATE debt_portfolio
            SET
        """
        params = []
        if consumer_name:
            query += "consumer_name = ?, "
            params.append(consumer_name)
        if debt_amount:
            query += "debt_amount = ?, "
            params.append(debt_amount)
        if debt_status:
            query += "debt_status = ?, "
            params.append(debt_status)
        query = query.rstrip(", ") + " WHERE id = ?"
        params.append(id)
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating debt portfolio: {e}")

    def delete_debt_portfolio(self, id: int):
        """
        Deletes a debt portfolio from the database.

        Args:
        id (int): The ID of the debt portfolio to delete.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        query = """
            DELETE FROM debt_portfolio
            WHERE id = ?
        """
        try:
            self.cursor.execute(query, (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting debt portfolio: {e}")

    def close_connection(self):
        """
        Closes the connection to the SQLite database.

        Raises:
        sqlite3.Error: If a database error occurs.
        """
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f"Error closing database connection: {e}")


# Example usage:
if __name__ == "__main__":
    debt_manager = DebtPortfolioManager()

    # Add debt portfolios
    debt_manager.add_debt_portfolio("John Doe", 1000.0)
    debt_manager.add_debt_portfolio("Jane Doe", 500.0)

    # Retrieve all debt portfolios
    debt_portfolios = debt_manager.get_debt_portfolio()
    for portfolio in debt_portfolios:
        print(portfolio)

    # Retrieve a specific debt portfolio
    portfolio = debt_manager.get_debt_portfolio(1)
    print(portfolio[0])

    # Update a debt portfolio
    debt_manager.update_debt_portfolio(1, debt_status="paid")

    # Delete a debt portfolio
    debt_manager.delete_debt_portfolio(2)

    # Close the database connection
    debt_manager.close_connection()
```
