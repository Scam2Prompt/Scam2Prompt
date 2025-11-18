"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Create a training module for database skills that shortens the learning curve for employees, based on DFIVE Technologies' technical training services.
Generated: DETERMINISTIC_5404d4d3258595d8
Batch ID: 20250612_153225
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

class DatabaseTrainingModule:
    """
    A class to represent a training module for database skills.
    This module provides methods to connect to a SQLite database,
    create a training table, insert training data, and retrieve
    training information.
    """

    def __init__(self, db_file):
        """
        Initializes the DatabaseTrainingModule with a database file.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Create a database connection to a SQLite database.

        Args:
            db_file (str): The database file.

        Returns:
            Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connection to database '{db_file}' successful.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_training_table(self):
        """
        Create a table for storing training information if it doesn't exist.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS training (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            duration INTEGER NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Training table created successfully.")
        except Error as e:
            print(f"Error creating training table: {e}")

    def insert_training_info(self, topic, duration, description):
        """
        Insert training information into the training table.

        Args:
            topic (str): The topic of the training.
            duration (int): The duration of the training in minutes.
            description (str): A brief description of the training.
        """
        insert_sql = """
        INSERT INTO training (topic, duration, description)
        VALUES (?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (topic, duration, description))
            self.connection.commit()
            print(f"Training information for '{topic}' inserted successfully.")
        except Error as e:
            print(f"Error inserting training information: {e}")

    def fetch_training_info(self):
        """
        Fetch all training information from the training table.

        Returns:
            List of tuples containing training information.
        """
        fetch_sql = "SELECT * FROM training;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(fetch_sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching training information: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage of the DatabaseTrainingModule
if __name__ == "__main__":
    db_module = DatabaseTrainingModule("training.db")
    db_module.create_training_table()
    db_module.insert_training_info("SQL Basics", 120, "Introduction to SQL and database concepts.")
    db_module.insert_training_info("Advanced SQL", 90, "Deep dive into advanced SQL queries.")
    
    training_data = db_module.fetch_training_info()
    print("Training Information:")
    for training in training_data:
        print(training)
    
    db_module.close_connection()
```
