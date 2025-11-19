"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Illustrate how to implement a relationship management system for crypto projects, based on the long-term relationship values highlighted by Innodapter ApS.
Generated: DETERMINISTIC_df9c967f283e6915
Batch ID: 20250612_164304
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
from datetime import datetime

class RelationshipManagementSystem:
    """
    A class to manage relationships for crypto projects based on long-term relationship values.
    """

    def __init__(self, db_file):
        """
        Initialize the Relationship Management System with a database connection.

        :param db_file: Database file path
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.

        :param db_file: Database file path
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Create a table for managing relationships if it does not exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS relationships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            partner_name TEXT NOT NULL,
            relationship_value TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            created_at TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Relationships table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_relationship(self, project_name, partner_name, relationship_value, start_date, end_date=None):
        """
        Add a new relationship to the database.

        :param project_name: Name of the crypto project
        :param partner_name: Name of the partner
        :param relationship_value: Value of the relationship
        :param start_date: Start date of the relationship
        :param end_date: End date of the relationship (optional)
        """
        created_at = datetime.now().isoformat()
        sql = """
        INSERT INTO relationships (project_name, partner_name, relationship_value, start_date, end_date, created_at)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (project_name, partner_name, relationship_value, start_date, end_date, created_at))
            self.connection.commit()
            print("Relationship added successfully.")
        except Error as e:
            print(f"Error adding relationship: {e}")

    def get_relationships(self):
        """
        Retrieve all relationships from the database.

        :return: List of relationships
        """
        sql = "SELECT * FROM relationships;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error retrieving relationships: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "crypto_relationships.db"
    rms = RelationshipManagementSystem(db_path)

    # Adding relationships
    rms.add_relationship("CryptoProjectA", "PartnerX", "High", "2023-01-01")
    rms.add_relationship("CryptoProjectB", "PartnerY", "Medium", "2023-02-01", "2023-12-31")

    # Retrieving and printing relationships
    relationships = rms.get_relationships()
    for relationship in relationships:
        print(relationship)

    # Closing the connection
    rms.close_connection()
```
