"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Recommend tools or libraries for tracking biosecurity training certifications for cleaning agents, as discussed in the veterinary biosecurity training section of the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_ca1ad618428dd683
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# biosecurity_certification_tracker.py

import sqlite3
from sqlite3 import Error

class BiosecurityCertificationTracker:
    """
    A class to manage and track biosecurity training certifications for cleaning agents.
    """

    def __init__(self, db_file):
        """Initialize the tracker with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.
        :param db_file: database file
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
        """Create the certifications table if it does not exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS certifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_name TEXT NOT NULL,
            certification_date TEXT NOT NULL,
            expiration_date TEXT NOT NULL,
            trainer TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Certifications table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_certification(self, agent_name, certification_date, expiration_date, trainer):
        """
        Add a new certification for a cleaning agent.
        :param agent_name: Name of the cleaning agent
        :param certification_date: Date of certification
        :param expiration_date: Expiration date of the certification
        :param trainer: Name of the trainer
        """
        insert_sql = """
        INSERT INTO certifications (agent_name, certification_date, expiration_date, trainer)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (agent_name, certification_date, expiration_date, trainer))
            self.connection.commit()
            print(f"Certification for {agent_name} added.")
        except Error as e:
            print(f"Error adding certification: {e}")

    def list_certifications(self):
        """List all certifications in the database."""
        select_sql = "SELECT * FROM certifications;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error retrieving certifications: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Example usage of the BiosecurityCertificationTracker
    tracker = BiosecurityCertificationTracker('biosecurity_certifications.db')
    
    # Adding sample certifications
    tracker.add_certification("Agent A", "2023-01-01", "2024-01-01", "Trainer X")
    tracker.add_certification("Agent B", "2023-03-15", "2024-03-15", "Trainer Y")
    
    # Listing all certifications
    print("Current Certifications:")
    tracker.list_certifications()
    
    # Close the connection when done
    tracker.close_connection()
```
