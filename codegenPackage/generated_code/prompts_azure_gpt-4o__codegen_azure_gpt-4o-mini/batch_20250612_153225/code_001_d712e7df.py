"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Generate a script that uses the SDS (Safety Data Sheet) information to create a database for tracking chemical properties, hazards, and storage guidelines, referencing Kimia Shimi's emphasis on SDS documentation.
Generated: DETERMINISTIC_d712e7dfc4e9b97f
Batch ID: 20250612_153225
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

# Define the database file
DATABASE_FILE = 'chemical_sds.db'

# SQL commands to create the necessary tables
CREATE_CHEMICALS_TABLE = """
CREATE TABLE IF NOT EXISTS Chemicals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    formula TEXT,
    properties TEXT,
    hazards TEXT,
    storage_guidelines TEXT
);
"""

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the Chemicals table in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_CHEMICALS_TABLE)
        print("Chemicals table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_chemical(conn, chemical):
    """Insert a new chemical record into the Chemicals table."""
    sql = '''INSERT INTO Chemicals(name, formula, properties, hazards, storage_guidelines)
             VALUES(?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, chemical)
        conn.commit()
        print(f"Chemical '{chemical[0]}' added successfully.")
    except Error as e:
        print(f"Error inserting chemical: {e}")

def main():
    """Main function to set up the database and insert sample data."""
    # Create a database connection
    conn = create_connection(DATABASE_FILE)

    if conn is not None:
        # Create Chemicals table
        create_table(conn)

        # Sample chemical data to insert
        sample_chemicals = [
            ('Acetone', 'C3H6O', 'Colorless liquid, volatile', 'Flammable, irritant', 'Store in a cool, well-ventilated area.'),
            ('Benzene', 'C6H6', 'Colorless liquid, sweet odor', 'Carcinogenic, flammable', 'Store away from heat and ignition sources.'),
            ('Ethanol', 'C2H5OH', 'Colorless liquid, alcoholic odor', 'Flammable, irritant', 'Store in a cool, dry place.'),
        ]

        # Insert sample chemicals into the database
        for chemical in sample_chemicals:
            insert_chemical(conn, chemical)

        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
