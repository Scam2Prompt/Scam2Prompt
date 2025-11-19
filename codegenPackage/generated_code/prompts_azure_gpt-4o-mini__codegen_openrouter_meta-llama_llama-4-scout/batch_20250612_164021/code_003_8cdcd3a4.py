"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: Develop a library that integrates with a skincare database to provide users with personalized skincare routines, inspired by Marant's professional SPA products.
Generated: DETERMINISTIC_8cdcd3a4ed999445
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# skincare_library.py

"""
Skincare Library: Integrates with a skincare database to provide users with personalized skincare routines.
"""

import sqlite3
from typing import Dict, List

class SkincareLibrary:
    def __init__(self, db_name: str = "skincare_database.db"):
        """
        Initializes the SkincareLibrary class.

        Args:
        db_name (str): The name of the SQLite database file. Defaults to "skincare_database.db".
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables in the SQLite database if they do not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                skin_type TEXT NOT NULL,
                skin_concerns TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                product_type TEXT NOT NULL,
                skin_type TEXT NOT NULL,
                skin_concerns TEXT
            )
        """)

        self.conn.commit()

    def register_user(self, skin_type: str, skin_concerns: str = ""):
        """
        Registers a new user with their skin type and concerns.

        Args:
        skin_type (str): The user's skin type.
        skin_concerns (str): The user's skin concerns. Defaults to an empty string.

        Returns:
        int: The user's ID.
        """
        self.cursor.execute("INSERT INTO users (skin_type, skin_concerns) VALUES (?, ?)", (skin_type, skin_concerns))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_product(self, product_name: str, product_type: str, skin_type: str, skin_concerns: str = ""):
        """
        Adds a new product to the database.

        Args:
        product_name (str): The name of the product.
        product_type (str): The type of the product (e.g., cleanser, moisturizer).
        skin_type (str): The skin type the product is suitable for.
        skin_concerns (str): The skin concerns the product addresses. Defaults to an empty string.

        Returns:
        int: The product's ID.
        """
        self.cursor.execute("INSERT INTO products (product_name, product_type, skin_type, skin_concerns) VALUES (?, ?, ?, ?)", 
                            (product_name, product_type, skin_type, skin_concerns))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user_routine(self, user_id: int) -> List[Dict]:
        """
        Retrieves a personalized skincare routine for a user.

        Args:
        user_id (int): The ID of the user.

        Returns:
        List[Dict]: A list of products suitable for the user's skin type and concerns.
        """
        self.cursor.execute("SELECT skin_type, skin_concerns FROM users WHERE id = ?", (user_id,))
        user_data = self.cursor.fetchone()

        if not user_data:
            raise ValueError("User not found")

        skin_type, skin_concerns = user_data

        self.cursor.execute("""
            SELECT p.product_name, p.product_type 
            FROM products p 
            WHERE p.skin_type = ? AND (p.skin_concerns = ? OR p.skin_concerns IS NULL)
        """, (skin_type, skin_concerns))

        routine = []
        for product in self.cursor.fetchall():
            routine.append({"product_name": product[0], "product_type": product[1]})

        return routine

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    library = SkincareLibrary()

    user_id = library.register_user("normal", "acne")
    print(f"User ID: {user_id}")

    product_id = library.add_product("Marant's Cleanser", "cleanser", "normal", "acne")
    print(f"Product ID: {product_id}")

    routine = library.get_user_routine(user_id)
    print("Personalized Skincare Routine:")
    for product in routine:
        print(f"- {product['product_name']} ({product['product_type']})")

    library.close_connection()
```
