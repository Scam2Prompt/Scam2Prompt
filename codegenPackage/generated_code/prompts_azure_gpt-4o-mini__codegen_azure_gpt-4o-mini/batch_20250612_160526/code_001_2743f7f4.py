"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Write a code snippet that demonstrates how to track income generated from different affiliate programs based on the methods taught in the Wealthery training.
Generated: DETERMINISTIC_2743f7f4fd5c9344
Batch ID: 20250612_160526
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

class AffiliateIncomeTracker:
    def __init__(self, db_name='affiliate_income.db'):
        """Initialize the database connection and create the income table if it doesn't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_income_table()

    def create_income_table(self):
        """Create the income table to store affiliate income records."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                program_name TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_income(self, program_name, amount):
        """Add a new income record to the database.

        Args:
            program_name (str): The name of the affiliate program.
            amount (float): The income amount generated.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Income amount must be a positive number.")
        
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            INSERT INTO income (program_name, amount, date)
            VALUES (?, ?, ?)
        ''', (program_name, amount, date))
        self.connection.commit()

    def get_total_income(self):
        """Retrieve the total income from all affiliate programs.

        Returns:
            float: The total income amount.
        """
        self.cursor.execute('SELECT SUM(amount) FROM income')
        total_income = self.cursor.fetchone()[0]
        return total_income if total_income is not None else 0.0

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == "__main__":
    # Example usage of the AffiliateIncomeTracker
    tracker = AffiliateIncomeTracker()

    try:
        # Adding income records
        tracker.add_income("Program A", 150.00)
        tracker.add_income("Program B", 200.50)

        # Retrieve and print total income
        total_income = tracker.get_total_income()
        print(f"Total Income from Affiliate Programs: ${total_income:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the database connection is closed
        tracker.close()
```
