"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Illustrate how to implement a relationship management system for crypto projects, based on the long-term relationship values highlighted by Innodapter ApS.
Generated: DETERMINISTIC_df9c967f283e6915
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from datetime import datetime

class RelationshipManagementSystem:
    """A class to manage relationships for crypto projects."""

    def __init__(self, db_file):
        """Initialize the system with a database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_table(self):
        """Create the relationships table if it doesn't exist."""
        try:
            sql_create_relationships_table = """
            CREATE TABLE IF NOT EXISTS relationships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_name TEXT NOT NULL,
                partner_name TEXT NOT NULL,
                relationship_value INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT,
                notes TEXT
            );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_relationships_table)
        except Error as e:
            print(f"Error: {e}")

    def add_relationship(self, project_name, partner_name, relationship_value, start_date, end_date=None, notes=None):
        """Add a new relationship to the database."""
        sql = '''INSERT INTO relationships(project_name, partner_name, relationship_value, start_date, end_date, notes)
                 VALUES(?,?,?,?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (project_name, partner_name, relationship_value, start_date, end_date, notes))
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error: {e}")

    def get_relationships(self):
        """Retrieve all relationships from the database."""
        sql = 'SELECT * FROM relationships'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return []

    def update_relationship(self, relationship_id, **kwargs):
        """Update an existing relationship based on the provided kwargs."""
        updates = []
        for key, value in kwargs.items():
            updates.append(f"{key} = ?")
        update_str = ", ".join(updates)
        sql = f'UPDATE relationships SET {update_str} WHERE id = ?'
        values = list(kwargs.values()) + [relationship_id]

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, values)
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

    def delete_relationship(self, relationship_id):
        """Delete a relationship from the database."""
        sql = 'DELETE FROM relationships WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (relationship_id,))
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


# Example usage of the RelationshipManagementSystem
if __name__ == '__main__':
    db_path = 'crypto_relationships.db'
    rms = RelationshipManagementSystem(db_path)
    rms.create_table()

    # Adding a relationship example
    rms.add_relationship(
        project_name="CryptoProject",
        partner_name="PartnerA",
        relationship_value=5,
        start_date=datetime.now().strftime("%Y-%m-%d"),
        notes="Initial partnership agreement"
    )

    # Fetch and print all relationships
    relationships = rms.get_relationships()
    for relationship in relationships:
        print(relationship)

    # Update a relationship example (Assuming relationship_id is known)
    # rms.update_relationship(1, partner_name="PartnerB", relationship_value=8)

    # Delete a relationship example (Assuming relationship_id is known)
    # rms.delete_relationship(1)

    rms.close_connection()
```
