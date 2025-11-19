"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Generate code using a database management system to store and retrieve occupational health examination records, including tests like electrocardiograms and radiology results, as outlined on Medicid IPS's services page.
Generated: DETERMINISTIC_ad492c79a2b284b5
Batch ID: 20250612_150902
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

# Database connection function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database successful.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables
def create_tables(conn):
    """Create tables for storing occupational health examination records."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS examinations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                examination_date TEXT NOT NULL,
                test_type TEXT NOT NULL,
                result TEXT NOT NULL
            );
        ''')
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to insert examination record
def insert_examination(conn, patient_name, examination_date, test_type, result):
    """Insert a new examination record into the examinations table."""
    sql = '''INSERT INTO examinations(patient_name, examination_date, test_type, result)
             VALUES(?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (patient_name, examination_date, test_type, result))
        conn.commit()
        print("Examination record inserted successfully.")
    except Error as e:
        print(f"Error inserting record: {e}")

# Function to retrieve examination records
def retrieve_examinations(conn):
    """Retrieve all examination records from the examinations table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM examinations")
        records = cursor.fetchall()
        return records
    except Error as e:
        print(f"Error retrieving records: {e}")
        return []

# Main function to demonstrate functionality
def main():
    database = "occupational_health.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tables if connection is successful
    if conn:
        create_tables(conn)

        # Example data insertion
        insert_examination(conn, "John Doe", "2023-10-01", "Electrocardiogram", "Normal")
        insert_examination(conn, "Jane Smith", "2023-10-02", "Radiology", "No abnormalities")

        # Retrieve and print all examination records
        records = retrieve_examinations(conn)
        for record in records:
            print(record)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
