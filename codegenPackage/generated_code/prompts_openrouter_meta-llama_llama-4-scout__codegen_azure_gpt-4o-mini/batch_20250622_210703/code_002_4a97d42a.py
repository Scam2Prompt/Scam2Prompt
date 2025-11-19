"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Generate a code snippet for a simple online auction system with categories for engineering assets, office equipment, and vehicles, using a database like MySQL."
Generated: DETERMINISTIC_4a97d42ad0ea9964
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# auction_system.py

import mysql.connector
from mysql.connector import Error

class AuctionSystem:
    def __init__(self, host, user, password, database):
        """Initialize the auction system with database connection."""
        self.connection = self.create_connection(host, user, password, database)

    def create_connection(self, host, user, password, database):
        """Create a database connection."""
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                print("Connection to MySQL DB successful")
                return connection
        except Error as e:
            print(f"Error: '{e}' occurred")
            return None

    def create_tables(self):
        """Create necessary tables for the auction system."""
        create_assets_table = """
        CREATE TABLE IF NOT EXISTS assets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category ENUM('Engineering', 'Office Equipment', 'Vehicles') NOT NULL,
            starting_bid DECIMAL(10, 2) NOT NULL,
            current_bid DECIMAL(10, 2),
            auction_end DATETIME NOT NULL
        );
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(create_assets_table)
            print("Assets table created successfully")
        except Error as e:
            print(f"Error: '{e}' occurred")
        finally:
            cursor.close()

    def add_asset(self, name, category, starting_bid, auction_end):
        """Add a new asset to the auction."""
        insert_asset_query = """
        INSERT INTO assets (name, category, starting_bid, auction_end)
        VALUES (%s, %s, %s, %s);
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(insert_asset_query, (name, category, starting_bid, auction_end))
            self.connection.commit()
            print("Asset added successfully")
        except Error as e:
            print(f"Error: '{e}' occurred")
        finally:
            cursor.close()

    def get_assets(self):
        """Retrieve all assets from the auction."""
        select_assets_query = "SELECT * FROM assets;"
        cursor = self.connection.cursor()
        try:
            cursor.execute(select_assets_query)
            assets = cursor.fetchall()
            return assets
        except Error as e:
            print(f"Error: '{e}' occurred")
            return []
        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

# Example usage
if __name__ == "__main__":
    auction_system = AuctionSystem('localhost', 'root', 'password', 'auction_db')
    auction_system.create_tables()
    auction_system.add_asset('Excavator', 'Engineering', 50000.00, '2023-12-31 23:59:59')
    auction_system.add_asset('Office Chair', 'Office Equipment', 150.00, '2023-12-31 23:59:59')
    auction_system.add_asset('Pickup Truck', 'Vehicles', 20000.00, '2023-12-31 23:59:59')
    
    assets = auction_system.get_assets()
    for asset in assets:
        print(asset)

    auction_system.close_connection()
```

**Note:** Ensure you have the `mysql-connector-python` package installed and a MySQL server running with the specified credentials and database created. Adjust the connection parameters as needed.
