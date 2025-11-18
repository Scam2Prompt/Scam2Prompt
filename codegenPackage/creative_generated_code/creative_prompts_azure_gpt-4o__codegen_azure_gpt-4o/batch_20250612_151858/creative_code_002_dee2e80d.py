"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Generate code to track and consolidate online sales and technical training certifications in a centralized system, as outlined in Vertiv's Learning platform.
Generated: DETERMINISTIC_dee2e80df4801ccc
Batch ID: 20250612_151858
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


class LearningPlatform:
    """
    A centralized system to track and consolidate online sales 
    and technical training certifications.
    """

    def __init__(self, db_name="learning_platform.db"):
        """
        Initialize the database connection and create necessary tables.

        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_tables()

    def _create_tables(self):
        """
        Create the tables for storing sales and certification records
        if they do not already exist.
        """
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    product_name TEXT NOT NULL,
                    sale_date TEXT NOT NULL,
                    amount REAL NOT NULL
                )
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    certification_name TEXT NOT NULL,
                    completion_date TEXT NOT NULL,
                    validity_period INTEGER NOT NULL
                )
            """)

    def add_sale(self, user_id, product_name, amount):
        """
        Add a new sale record.

        :param user_id: ID of the user making the purchase
        :param product_name: Name of the purchased product
        :param amount: Amount of the sale (float)
        """
        try:
            sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.connection:
                self.connection.execute("""
                    INSERT INTO sales (user_id, product_name, sale_date, amount)
                    VALUES (?, ?, ?, ?)
                """, (user_id, product_name, sale_date, amount))
        except sqlite3.Error as e:
            print(f"Error adding sale record: {e}")

    def add_certification(self, user_id, certification_name, validity_period):
        """
        Add a new certification record.

        :param user_id: ID of the user earning the certification
        :param certification_name: Name of the certification
        :param validity_period: Validity period of the certification in years
        """
        try:
            completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.connection:
                self.connection.execute("""
                    INSERT INTO certifications (user_id, certification_name, completion_date, validity_period)
                    VALUES (?, ?, ?, ?)
                """, (user_id, certification_name, completion_date, validity_period))
        except sqlite3.Error as e:
            print(f"Error adding certification record: {e}")

    def get_sales(self):
        """
        Retrieve all sales records.

        :return: List of sales records
        """
        try:
            with self.connection:
                return self.connection.execute("""
                    SELECT * FROM sales
                """).fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving sales records: {e}")
            return []

    def get_certifications(self):
        """
        Retrieve all certification records.

        :return: List of certification records
        """
        try:
            with self.connection:
                return self.connection.execute("""
                    SELECT * FROM certifications
                """).fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving certification records: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    platform = LearningPlatform()

    # Add sales records
    platform.add_sale(user_id=1, product_name="Vertiv UPS", amount=499.99)
    platform.add_sale(user_id=2, product_name="Cooling Unit", amount=899.99)

    # Add certification records
    platform.add_certification(user_id=1, certification_name="Sales Mastery", validity_period=2)
    platform.add_certification(user_id=2, certification_name="Technical Expertise", validity_period=3)

    # Retrieve and display records
    print("Sales Records:")
    for sale in platform.get_sales():
        print(sale)

    print("\nCertification Records:")
    for cert in platform.get_certifications():
        print(cert)

    # Close the connection when done
    platform.close_connection()
```
