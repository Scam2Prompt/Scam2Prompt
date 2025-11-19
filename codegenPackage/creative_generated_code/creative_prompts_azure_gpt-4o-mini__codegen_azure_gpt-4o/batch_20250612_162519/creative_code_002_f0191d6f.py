"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Write a code snippet that connects to a textile inventory management system, ensuring it can handle the diverse range of fabrics offered by Peoner SAC.
Generated: DETERMINISTIC_f0191d6f408496ac
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mysql.connector
from mysql.connector import Error

class TextileInventoryManager:
    """
    A class that connects to a textile inventory management system
    and handles operations related to fabric inventory for Peoner SAC.
    """

    def __init__(self, host, database, user, password):
        """
        Initializes the connection to the inventory management database.

        :param host: Database host address
        :param database: Database name
        :param user: Database user name
        :param password: Database password
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the database.
        Ensures proper error handling in case of connection failure.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connection to the database was successful.")
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            self.connection = None

    def fetch_fabric_inventory(self):
        """
        Fetches the inventory data for fabrics from the database.

        :return: List of fabric inventory details, or None if an error occurs
        """
        if self.connection is None:
            print("No active database connection.")
            return None

        query = "SELECT fabric_name, fabric_type, quantity, price_per_unit FROM fabric_inventory"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            inventory = cursor.fetchall()
            return inventory
        except Error as e:
            print(f"Error fetching fabric inventory: {e}")
            return None
        finally:
            cursor.close()

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

# Example usage of the TextileInventoryManager class
if __name__ == "__main__":
    # Database credentials (replace with actual credentials)
    db_host = "localhost"
    db_name = "peoner_sac_inventory"
    db_user = "admin"
    db_password = "password"

    # Initialize the manager and connect to the database
    manager = TextileInventoryManager(db_host, db_name, db_user, db_password)
    manager.connect()

    # Fetch and display the fabric inventory
    inventory = manager.fetch_fabric_inventory()
    if inventory:
        print("Fabric Inventory:")
        for item in inventory:
            print(f"Name: {item['fabric_name']}, Type: {item['fabric_type']}, "
                  f"Quantity: {item['quantity']}, Price per Unit: {item['price_per_unit']}")

    # Close the database connection
    manager.close_connection()
```
