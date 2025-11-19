"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "Write a basic Python script to create a database for storing and querying user traits, akin to what Trait Sniper might use."
Generated: DETERMINISTIC_1fdfa0a5562f9fe8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

# Define a class to handle database operations
class UserTraitsDatabase:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for storing user traits."""
        try:
            sql_create_traits_table = """
            CREATE TABLE IF NOT EXISTS user_traits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                trait_name TEXT NOT NULL,
                trait_value TEXT NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_traits_table)
            print("User traits table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_trait(self, username, trait_name, trait_value):
        """Insert a new user trait into the database."""
        sql_insert_trait = """
        INSERT INTO user_traits (username, trait_name, trait_value)
        VALUES (?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_trait, (username, trait_name, trait_value))
            self.connection.commit()
            print("Trait inserted successfully.")
        except Error as e:
            print(f"Error inserting trait: {e}")

    def query_traits(self, username):
        """Query traits for a specific user."""
        sql_query_traits = """
        SELECT trait_name, trait_value FROM user_traits
        WHERE username = ?;
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query_traits, (username,))
            traits = cursor.fetchall()
            return traits
        except Error as e:
            print(f"Error querying traits: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main execution
if __name__ == "__main__":
    # Database file path
    database_path = "user_traits.db"

    # Create a database instance
    db = UserTraitsDatabase(database_path)

    # Create the user traits table
    db.create_table()

    # Example usage: Insert traits
    db.insert_trait("john_doe", "height", "6ft")
    db.insert_trait("john_doe", "eye_color", "blue")

    # Query traits for a user
    traits = db.query_traits("john_doe")
    print("Traits for john_doe:", traits)

    # Close the database connection
    db.close_connection()
```
