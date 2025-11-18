"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Provide a solution for tracking and managing trained labor for furniture assembly and moving services, referencing شركة الاحترافية's emphasis on skilled workers.
Generated: DETERMINISTIC_2793eba481030dcf
Batch ID: 20250612_153246
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

class LaborTracking:
    """
    A class to manage and track skilled labor for furniture assembly and moving services.
    """

    def __init__(self, db_file):
        """ Initialize the LaborTracking with a database connection. """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database. """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection established to the database.")
        except Error as e:
            print(f"Error establishing connection: {e}")
        return conn

    def create_table(self):
        """ Create a table for managing labor data if it doesn't exist. """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS labor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            skill_level TEXT NOT NULL,
            availability TEXT NOT NULL,
            contact_info TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Labor table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_worker(self, name, skill_level, availability, contact_info):
        """ Add a new skilled worker to the database. """
        sql = '''INSERT INTO labor(name, skill_level, availability, contact_info)
                  VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, skill_level, availability, contact_info))
            self.connection.commit()
            print(f"Worker {name} added successfully.")
        except Error as e:
            print(f"Error adding worker: {e}")

    def update_worker(self, worker_id, name, skill_level, availability, contact_info):
        """ Update existing worker information. """
        sql = '''UPDATE labor
                 SET name = ?, skill_level = ?, availability = ?, contact_info = ?
                 WHERE id = ?'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, skill_level, availability, contact_info, worker_id))
            self.connection.commit()
            print(f"Worker ID {worker_id} updated successfully.")
        except Error as e:
            print(f"Error updating worker: {e}")

    def delete_worker(self, worker_id):
        """ Delete a worker from the database. """
        sql = 'DELETE FROM labor WHERE id = ?'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (worker_id,))
            self.connection.commit()
            print(f"Worker ID {worker_id} deleted successfully.")
        except Error as e:
            print(f"Error deleting worker: {e}")

    def list_workers(self):
        """ List all workers in the database. """
        sql = 'SELECT * FROM labor'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            workers = cursor.fetchall()
            for worker in workers:
                print(worker)
        except Error as e:
            print(f"Error retrieving workers: {e}")

    def close_connection(self):
        """ Close the database connection. """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
if __name__ == '__main__':
    db_path = "labor_tracking.db"
    labor_tracker = LaborTracking(db_path)

    # Add workers (example data)
    labor_tracker.add_worker("Ahmed", "Expert", "Available", "123-456-7890")
    labor_tracker.add_worker("Sara", "Intermediate", "Not Available", "098-765-4321")

    # List all workers
    labor_tracker.list_workers()

    # Update a worker's information
    labor_tracker.update_worker(1, "Ahmed Ali", "Expert", "Available", "123-456-7890")

    # Delete a worker
    labor_tracker.delete_worker(2)

    # List all workers after modifications
    labor_tracker.list_workers()

    # Close database connection
    labor_tracker.close_connection()
```
