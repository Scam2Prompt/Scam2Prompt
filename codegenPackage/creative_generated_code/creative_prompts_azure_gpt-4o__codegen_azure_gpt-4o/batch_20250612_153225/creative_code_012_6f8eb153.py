"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Provide a solution for creating a scalable telemarketing system to improve customer acquisition and retention, based on Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_6f8eb15340834a52
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Scalable Telemarketing System to improve customer acquisition and retention.
The system is designed with modularity and scalability in mind, leveraging Python and a database backend.
"""

import logging
import sqlite3
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TelemarketingSystem:
    """
    Telemarketing System Class to handle customer acquisition and retention tasks.

    Attributes:
        db_connection: SQLite database connection object.
    """
    def __init__(self, db_name: str = "telemarketing.db"):
        """
        Initializes the Telemarketing System and sets up the database.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.db_connection = sqlite3.connect(db_name)
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the necessary database tables if they don't already exist.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    acquisition_stage TEXT NOT NULL,
                    notes TEXT
                )
            """)
            self.db_connection.commit()
            logging.info("Database setup completed.")
        except sqlite3.Error as e:
            logging.error(f"Error setting up database: {e}")

    def add_customer(self, customer_data: Dict[str, str]) -> bool:
        """
        Adds a new customer to the database.

        Args:
            customer_data (Dict[str, str]): Dictionary containing customer details.

        Returns:
            bool: True if adding was successful, False otherwise.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                INSERT INTO customers (name, phone, email, acquisition_stage, notes)
                VALUES (:name, :phone, :email, :acquisition_stage, :notes)
            """, customer_data)
            self.db_connection.commit()
            logging.info(f"Customer {customer_data['name']} added successfully.")
            return True
        except sqlite3.IntegrityError as e:
            logging.error(f"Error adding customer (duplicate data): {e}")
            return False
        except sqlite3.Error as e:
            logging.error(f"Error adding customer: {e}")
            return False

    def update_customer_stage(self, customer_id: int, new_stage: str) -> bool:
        """
        Updates the acquisition stage of a customer.

        Args:
            customer_id (int): The ID of the customer.
            new_stage (str): The new acquisition stage.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                UPDATE customers SET acquisition_stage = ? WHERE id = ?
            """, (new_stage, customer_id))
            self.db_connection.commit()
            if cursor.rowcount > 0:
                logging.info(f"Customer ID {customer_id} stage updated to {new_stage}.")
                return True
            else:
                logging.warning(f"No customer found with ID {customer_id}.")
                return False
        except sqlite3.Error as e:
            logging.error(f"Error updating customer stage: {e}")
            return False

    def get_customer(self, customer_id: int) -> Optional[Dict[str, str]]:
        """
        Retrieves a customer's details from the database.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            Optional[Dict[str, str]]: A dictionary containing customer details if found, None otherwise.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
            row = cursor.fetchone()
            if row:
                logging.info(f"Customer ID {customer_id} retrieved successfully.")
                return {
                    "id": row[0],
                    "name": row[1],
                    "phone": row[2],
                    "email": row[3],
                    "acquisition_stage": row[4],
                    "notes": row[5]
                }
            else:
                logging.warning(f"No customer found with ID {customer_id}.")
                return None
        except sqlite3.Error as e:
            logging.error(f"Error retrieving customer: {e}")
            return None

    def list_customers(self) -> List[Dict[str, str]]:
        """
        Lists all customers in the database.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing customer details.
        """
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM customers")
            rows = cursor.fetchall()
            logging.info(f"Retrieved {len(rows)} customers from the database.")
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "phone": row[2],
                    "email": row[3],
                    "acquisition_stage": row[4],
                    "notes": row[5]
                }
                for row in rows
            ]
        except sqlite3.Error as e:
            logging.error(f"Error listing customers: {e}")
            return []

    def __del__(self):
        """
        Ensures the database connection is closed when the object is deleted.
        """
        if self.db_connection:
            self.db_connection.close()
            logging.info("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = TelemarketingSystem()

    # Add a customer
    customer_data = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john.doe@example.com",
        "acquisition_stage": "Lead",
        "notes": "Interested in product X"
    }
    system.add_customer(customer_data)

    # Get a customer
    customer = system.get_customer(1)
    if customer:
        print("Customer Details:", customer)

    # Update acquisition stage
    system.update_customer_stage(1, "Converted")

    # List all customers
    customers_list = system.list_customers()
    print("All Customers:", customers_list)
```
