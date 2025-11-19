"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Provide an example of using a database to store and retrieve pricing information for various glass products and services, including balcony glass, shower cabins, and automatic glass doors, as detailed on the website.
Generated: DETERMINISTIC_072334f98ef652da
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# database.py

import sqlite3
from typing import Dict, List

class GlassPricingDatabase:
    def __init__(self, db_name: str):
        """
        Initialize a connection to the SQLite database.

        Args:
        db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create a table to store pricing information for glass products and services.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS glass_pricing
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             product_name TEXT NOT NULL,
             price REAL NOT NULL,
             description TEXT)
        ''')
        self.conn.commit()

    def insert_pricing_info(self, product_name: str, price: float, description: str = None):
        """
        Insert pricing information for a glass product or service.

        Args:
        product_name (str): The name of the product or service.
        price (float): The price of the product or service.
        description (str, optional): A brief description of the product or service. Defaults to None.
        """
        try:
            self.cursor.execute('''
                INSERT INTO glass_pricing (product_name, price, description)
                VALUES (?, ?, ?)
            ''', (product_name, price, description))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting pricing info: {e}")

    def get_all_pricing_info(self) -> List[Dict]:
        """
        Retrieve all pricing information from the database.

        Returns:
        List[Dict]: A list of dictionaries containing pricing information.
        """
        try:
            self.cursor.execute('SELECT * FROM glass_pricing')
            rows = self.cursor.fetchall()
            return [
                {
                    'id': row[0],
                    'product_name': row[1],
                    'price': row[2],
                    'description': row[3]
                } for row in rows
            ]
        except sqlite3.Error as e:
            print(f"Error retrieving pricing info: {e}")
            return []

    def get_pricing_info_by_product(self, product_name: str) -> Dict:
        """
        Retrieve pricing information for a specific glass product or service.

        Args:
        product_name (str): The name of the product or service.

        Returns:
        Dict: A dictionary containing pricing information for the specified product or service.
        """
        try:
            self.cursor.execute('''
                SELECT * FROM glass_pricing
                WHERE product_name = ?
            ''', (product_name,))
            row = self.cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'product_name': row[1],
                    'price': row[2],
                    'description': row[3]
                }
            else:
                return {}
        except sqlite3.Error as e:
            print(f"Error retrieving pricing info: {e}")
            return {}

    def update_pricing_info(self, product_name: str, price: float, description: str = None):
        """
        Update pricing information for a glass product or service.

        Args:
        product_name (str): The name of the product or service.
        price (float): The updated price of the product or service.
        description (str, optional): The updated description of the product or service. Defaults to None.
        """
        try:
            self.cursor.execute('''
                UPDATE glass_pricing
                SET price = ?, description = ?
                WHERE product_name = ?
            ''', (price, description, product_name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating pricing info: {e}")

    def delete_pricing_info(self, product_name: str):
        """
        Delete pricing information for a glass product or service.

        Args:
        product_name (str): The name of the product or service.
        """
        try:
            self.cursor.execute('''
                DELETE FROM glass_pricing
                WHERE product_name = ?
            ''', (product_name,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting pricing info: {e}")

    def close_connection(self):
        """
        Close the connection to the database.
        """
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    db = GlassPricingDatabase('glass_pricing.db')

    # Insert pricing information
    db.insert_pricing_info('Balcony Glass', 500.0, 'Per square meter')
    db.insert_pricing_info('Shower Cabin', 2000.0, 'Standard size')
    db.insert_pricing_info('Automatic Glass Door', 1500.0, 'Per unit')

    # Retrieve all pricing information
    pricing_info = db.get_all_pricing_info()
    print("All Pricing Information:")
    for info in pricing_info:
        print(info)

    # Retrieve pricing information by product
    balcony_glass_info = db.get_pricing_info_by_product('Balcony Glass')
    print("\nBalcony Glass Pricing Information:")
    print(balcony_glass_info)

    # Update pricing information
    db.update_pricing_info('Balcony Glass', 550.0)

    # Retrieve updated pricing information
    updated_balcony_glass_info = db.get_pricing_info_by_product('Balcony Glass')
    print("\nUpdated Balcony Glass Pricing Information:")
    print(updated_balcony_glass_info)

    # Delete pricing information
    db.delete_pricing_info('Shower Cabin')

    # Close the database connection
    db.close_connection()
```
