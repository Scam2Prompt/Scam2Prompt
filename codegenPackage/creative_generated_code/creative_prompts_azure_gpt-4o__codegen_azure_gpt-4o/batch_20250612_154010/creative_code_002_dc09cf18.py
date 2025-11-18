"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate code to integrate a discount system for psychological tests, as mentioned in the Colegio de Psicólogos de Oruro's partnership with AMI-Bolivia, using Python and a database management system.
Generated: DETERMINISTIC_dc09cf18a56fad9e
Batch ID: 20250612_154010
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

class DiscountSystem:
    """
    A class to manage discounts for psychological tests as part of the Colegio de Psicólogos de Oruro's partnership 
    with AMI-Bolivia.
    """

    def __init__(self, db_name="discount_system.db"):
        """
        Initializes the discount system by setting up the database connection.

        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary tables if they do not exist in the database.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()

            # Create the discounts table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS discounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_name TEXT NOT NULL,
                discount_percentage REAL NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL
            )
            """)

            # Commit changes
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing the database: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def add_discount(self, test_name, discount_percentage, start_date, end_date):
        """
        Adds a new discount for a psychological test.

        :param test_name: Name of the psychological test.
        :param discount_percentage: Discount percentage (0-100).
        :param start_date: Start date of the discount (YYYY-MM-DD).
        :param end_date: End date of the discount (YYYY-MM-DD).
        :return: None
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()

            # Insert the discount into the database
            cursor.execute("""
            INSERT INTO discounts (test_name, discount_percentage, start_date, end_date)
            VALUES (?, ?, ?, ?)
            """, (test_name, discount_percentage, start_date, end_date))

            self.connection.commit()

            print("Discount added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding discount: {e}")
        finally:
            if self.connection:
                self.connection.close()

    def list_active_discounts(self):
        """
        Lists all active discounts based on the current date.

        :return: List of active discounts.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()

            today = datetime.now().strftime("%Y-%m-%d")

            # Fetch active discounts
            cursor.execute("""
            SELECT test_name, discount_percentage, start_date, end_date
            FROM discounts
            WHERE start_date <= ? AND end_date >= ?
            """, (today, today))

            active_discounts = cursor.fetchall()

            print("Active discounts:")
            for discount in active_discounts:
                print(f"Test: {discount[0]}, Discount: {discount[1]}%, Valid from {discount[2]} to {discount[3]}")

            return active_discounts
        except sqlite3.Error as e:
            print(f"Error fetching discounts: {e}")
            return []
        finally:
            if self.connection:
                self.connection.close()

    def remove_expired_discounts(self):
        """
        Removes expired discounts from the database.

        :return: None
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            cursor = self.connection.cursor()

            today = datetime.now().strftime("%Y-%m-%d")

            # Delete expired discounts
            cursor.execute("""
            DELETE FROM discounts
            WHERE end_date < ?
            """, (today,))

            self.connection.commit()

            print("Expired discounts removed successfully.")
        except sqlite3.Error as e:
            print(f"Error removing expired discounts: {e}")
        finally:
            if self.connection:
                self.connection.close()


# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()

    # Add a new discount
    discount_system.add_discount("Stress Test", 20, "2023-10-01", "2023-11-01")

    # List active discounts
    discount_system.list_active_discounts()

    # Remove expired discounts
    discount_system.remove_expired_discounts()
```
