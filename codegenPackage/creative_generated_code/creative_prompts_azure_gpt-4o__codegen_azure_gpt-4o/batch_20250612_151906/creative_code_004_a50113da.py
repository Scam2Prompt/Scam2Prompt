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
from typing import List, Tuple, Dict

# Database configuration
DB_NAME = "consumer_debt_portfolio.db"

def create_database():
    """
    Creates a database and the necessary table for managing consumer debt portfolios.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create the debt portfolio table if it doesn't already exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS debt_portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            consumer_name TEXT NOT NULL,
            debt_amount REAL NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending'
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def add_debt(consumer_name: str, debt_amount: float, due_date: str) -> bool:
    """
    Adds a new debt entry to the database.

    :param consumer_name: Name of the consumer.
    :param debt_amount: Amount of debt.
    :param due_date: Due date for the debt.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO debt_portfolio (consumer_name, debt_amount, due_date)
        VALUES (?, ?, ?)
        """, (consumer_name, debt_amount, due_date))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def update_debt_status(debt_id: int, status: str) -> bool:
    """
    Updates the status of a debt entry in the database.

    :param debt_id: ID of the debt entry.
    :param status: New status, e.g. "paid", "overdue".
    :return: True if the operation is successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        UPDATE debt_portfolio
        SET status = ?
        WHERE id = ?
        """, (status, debt_id))
        
        conn.commit()
        return cursor.rowcount > 0  # Returns True if any row was updated
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def fetch_all_debts() -> List[Dict]:
    """
    Fetches all debt entries from the database.

    :return: A list of dictionaries containing debt portfolio data.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM debt_portfolio")
        rows = cursor.fetchall()
        
        # Convert the rows to a list of dictionaries
        debts = [
            {"id": row[0], "consumer_name": row[1], "debt_amount": row[2], "due_date": row[3], "status": row[4]}
            for row in rows
        ]
        
        return debts
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def delete_debt(debt_id: int) -> bool:
    """
    Deletes a debt entry from the database.

    :param debt_id: ID of the debt entry to delete.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        DELETE FROM debt_portfolio
        WHERE id = ?
        """, (debt_id,))
        
        conn.commit()
        return cursor.rowcount > 0  # Returns True if any row was deleted
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Initialize the database
    create_database()
    
    # Example operations
    add_debt("John Doe", 1500.50, "2023-12-15")
    add_debt("Jane Smith", 500.00, "2023-11-01")
    print(fetch_all_debts())
    update_debt_status(1, "paid")
    print(fetch_all_debts())
    delete_debt(2)
    print(fetch_all_debts())
```
