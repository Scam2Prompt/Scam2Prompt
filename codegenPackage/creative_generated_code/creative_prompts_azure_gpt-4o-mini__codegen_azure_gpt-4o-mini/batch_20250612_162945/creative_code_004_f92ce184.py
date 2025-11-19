"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: What is the best way to structure a database for storing information about peptides and bioregulators, based on the product details from BioLongevity Labs?
Generated: DETERMINISTIC_f92ce184518e5cc7
Batch ID: 20250612_162945
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

class Database:
    """Database class to manage Peptides and Bioregulators data."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error while connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create tables for storing peptides and bioregulators."""
        try:
            cursor = self.connection.cursor()

            # SQL command to create Peptides table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Peptides (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sequence TEXT NOT NULL,
                    molecular_weight REAL NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # SQL command to create Bioregulators table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Bioregulators (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    mechanism_of_action TEXT,
                    dosage TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            self.connection.commit()
        except Error as e:
            print(f"Error while creating tables: {e}")

    def insert_peptide(self, name, sequence, molecular_weight, description=''):
        """Insert a new peptide into the Peptides table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO Peptides (name, sequence, molecular_weight, description)
                VALUES (?, ?, ?, ?)
            ''', (name, sequence, molecular_weight, description))
            self.connection.commit()
        except Error as e:
            print(f"Error inserting peptide: {e}")

    def insert_bioregulator(self, name, type_, mechanism_of_action, dosage):
        """Insert a new bioregulator into the Bioregulators table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO Bioregulators (name, type, mechanism_of_action, dosage)
                VALUES (?, ?, ?, ?)
            ''', (name, type_, mechanism_of_action, dosage))
            self.connection.commit()
        except Error as e:
            print(f"Error inserting bioregulator: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    db = Database("bioregulators_peptides.db")
    db.create_tables()
    db.insert_peptide("Insulin", "FVNQHLCGSHLVEALYLVCGERGFFYTPKA", 5808.6)
    db.insert_bioregulator("Melatonin", "Hormone", "Regulates sleep-wake cycle", "0.5-5 mg")
    db.close_connection()
```
