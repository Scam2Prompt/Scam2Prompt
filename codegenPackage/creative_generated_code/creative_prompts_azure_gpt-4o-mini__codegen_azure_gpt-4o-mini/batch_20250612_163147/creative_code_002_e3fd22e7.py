"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saldias.net
Prompt: Generate a code snippet that integrates with the Repuestos Saldias database to fetch Peugeot and Citroën spare parts information.
Generated: DETERMINISTIC_e3fd22e75f9fa71c
Batch ID: 20250612_163147
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

class SparePartsFetcher:
    """
    A class to fetch Peugeot and Citroën spare parts information from the Repuestos Saldias database.
    """

    def __init__(self, host, database, user, password):
        """
        Initializes the database connection parameters.

        :param host: Database host address
        :param database: Name of the database
        :param user: Username for database authentication
        :param password: Password for database authentication
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def create_connection(self):
        """Establishes a connection to the database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Successfully connected to the database.")
        except Error as e:
            print(f"Error while connecting to the database: {e}")
            self.connection = None

    def fetch_spare_parts(self):
        """
        Fetches spare parts information for Peugeot and Citroën from the database.

        :return: List of spare parts or None if an error occurs
        """
        if self.connection is None:
            print("No database connection established.")
            return None

        try:
            query = """
            SELECT part_id, part_name, car_model, availability 
            FROM spare_parts 
            WHERE car_brand IN ('Peugeot', 'Citroën');
            """
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching spare parts: {e}")
            return None

    def close_connection(self):
        """Closes the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    fetcher = SparePartsFetcher(
        host='localhost',
        database='repuestos_saldias',
        user='your_username',
        password='your_password'
    )
    
    fetcher.create_connection()
    spare_parts = fetcher.fetch_spare_parts()
    
    if spare_parts:
        for part in spare_parts:
            print(part)
    
    fetcher.close_connection()
```
