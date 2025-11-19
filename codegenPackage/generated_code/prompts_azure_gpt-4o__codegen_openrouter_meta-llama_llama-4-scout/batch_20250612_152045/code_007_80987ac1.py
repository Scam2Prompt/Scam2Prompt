"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Write code to implement a multi-recharge utility software, based on the features described by MDA Tech Sys.
Generated: DETERMINISTIC_80987ac1fbe5f723
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multi_recharge_utility.py

"""
Multi-Recharge Utility Software
==============================

This software provides a utility for managing multiple recharge operations.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import sqlite3
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RechargeUtility:
    def __init__(self, db_name: str):
        """
        Initialize the RechargeUtility class.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect_to_db(self) -> None:
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            logging.info("Connected to the database successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error connecting to the database: {e}")

    def create_table(self) -> None:
        """
        Create a table for storing recharge records if it doesn't exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS recharge_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                recharge_amount REAL NOT NULL,
                recharge_date DATE NOT NULL
            )
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
            logging.info("Table created successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")

    def add_recharge_record(self, customer_name: str, recharge_amount: float, recharge_date: str) -> None:
        """
        Add a new recharge record to the database.

        Args:
        customer_name (str): The name of the customer.
        recharge_amount (float): The recharge amount.
        recharge_date (str): The recharge date in YYYY-MM-DD format.
        """
        query = """
            INSERT INTO recharge_records (customer_name, recharge_amount, recharge_date)
            VALUES (?, ?, ?)
        """
        try:
            self.cursor.execute(query, (customer_name, recharge_amount, recharge_date))
            self.conn.commit()
            logging.info("Recharge record added successfully.")
        except sqlite3.Error as e:
            logging.error(f"Error adding recharge record: {e}")

    def get_recharge_records(self) -> List[Dict]:
        """
        Retrieve all recharge records from the database.

        Returns:
        List[Dict]: A list of dictionaries containing recharge records.
        """
        query = """
            SELECT * FROM recharge_records
        """
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            recharge_records = []
            for row in rows:
                record = {
                    "id": row[0],
                    "customer_name": row[1],
                    "recharge_amount": row[2],
                    "recharge_date": row[3]
                }
                recharge_records.append(record)
            return recharge_records
        except sqlite3.Error as e:
            logging.error(f"Error retrieving recharge records: {e}")
            return []

    def close_connection(self) -> None:
        """
        Close the connection to the SQLite database.
        """
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed.")

def main():
    db_name = "recharge_utility.db"
    utility = RechargeUtility(db_name)
    utility.connect_to_db()
    utility.create_table()

    while True:
        print("\nMulti-Recharge Utility Menu:")
        print("1. Add Recharge Record")
        print("2. View Recharge Records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            recharge_amount = float(input("Enter recharge amount: "))
            recharge_date = input("Enter recharge date (YYYY-MM-DD): ")
            utility.add_recharge_record(customer_name, recharge_amount, recharge_date)
        elif choice == "2":
            recharge_records = utility.get_recharge_records()
            for record in recharge_records:
                print(record)
        elif choice == "3":
            utility.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
