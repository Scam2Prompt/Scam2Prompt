"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Write code to simulate a laboratory management system for "Laboratorio de Microbiología" and "Laboratorio de Control de Calidad," as featured in the Trentino facilities.
Generated: DETERMINISTIC_55c45cc8fede6467
Batch ID: 20250612_151445
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

class LaboratoryManagementSystem:
    def __init__(self, db_file):
        """Initialize the laboratory management system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for laboratories if they do not exist."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS laboratories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS samples (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lab_id INTEGER,
                    sample_name TEXT NOT NULL,
                    date_collected TEXT NOT NULL,
                    FOREIGN KEY (lab_id) REFERENCES laboratories (id)
                )
            ''')
            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_laboratory(self, name, lab_type):
        """Add a new laboratory to the system."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO laboratories (name, type) VALUES (?, ?)', (name, lab_type))
            self.connection.commit()
            print(f"Laboratory '{name}' added successfully.")
        except Error as e:
            print(f"Error adding laboratory: {e}")

    def add_sample(self, lab_id, sample_name, date_collected):
        """Add a new sample to a specified laboratory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO samples (lab_id, sample_name, date_collected) VALUES (?, ?, ?)', 
                           (lab_id, sample_name, date_collected))
            self.connection.commit()
            print(f"Sample '{sample_name}' added to laboratory ID {lab_id}.")
        except Error as e:
            print(f"Error adding sample: {e}")

    def get_laboratories(self):
        """Retrieve all laboratories from the system."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM laboratories')
            labs = cursor.fetchall()
            return labs
        except Error as e:
            print(f"Error retrieving laboratories: {e}")
            return []

    def get_samples(self, lab_id):
        """Retrieve all samples for a specified laboratory."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM samples WHERE lab_id = ?', (lab_id,))
            samples = cursor.fetchall()
            return samples
        except Error as e:
            print(f"Error retrieving samples: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db_path = "laboratory_management.db"
    lms = LaboratoryManagementSystem(db_path)

    # Adding laboratories
    lms.add_laboratory("Laboratorio de Microbiología", "Microbiology")
    lms.add_laboratory("Laboratorio de Control de Calidad", "Quality Control")

    # Adding samples
    lms.add_sample(1, "Sample A", "2023-10-01")
    lms.add_sample(2, "Sample B", "2023-10-02")

    # Retrieving laboratories and samples
    print("Laboratories:", lms.get_laboratories())
    print("Samples in Lab 1:", lms.get_samples(1))

    # Closing the connection
    lms.close_connection()
```
