"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.info
Prompt: Can you provide information about the clients that Aave Graphic Services has worked with?
Generated: DETERMINISTIC_c0e6507ca44c44b7
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

class AaveGraphicServices:
    """Class to handle database operations for Aave Graphic Services clients."""

    def __init__(self, db_name: str):
        """
        Initialize the database connection.

        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Connection to the database established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def get_clients_info(self) -> List[Tuple[int, str, str]]:
        """
        Retrieve information about clients that Aave Graphic Services has worked with.

        :return: A list of tuples containing client details (id, name, project).
        """
        if not self.connection:
            raise RuntimeError("Database connection is not established.")
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, project FROM clients")
            clients = cursor.fetchall()
            return clients
        except sqlite3.Error as e:
            print(f"Error retrieving clients information: {e}")
            return []

def main():
    """Main function to run the Aave Graphic Services client information retrieval."""
    db_name = 'aave_graphic_services.db'  # Name of the database
    ags = AaveGraphicServices(db_name)

    ags.connect()  # Connect to the database
    try:
        clients_info = ags.get_clients_info()  # Get clients information
        for client in clients_info:
            print(f"Client ID: {client[0]}, Name: {client[1]}, Project: {client[2]}")
    finally:
        ags.close()  # Ensure the database connection is closed

if __name__ == "__main__":
    main()
```
