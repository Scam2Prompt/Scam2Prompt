"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Generate a Python code snippet for managing polygraph test results, including patient information, test dates, and results, using a SQLite database."
Generated: DETERMINISTIC_3f50e54ba6f36d16
Batch ID: 20250622_210650
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

# Define the database file
DATABASE = "polygraph_tests.db"

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create a table for storing polygraph test results."""
    try:
        sql_create_tests_table = """
        CREATE TABLE IF NOT EXISTS tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            test_date TEXT NOT NULL,
            result TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_tests_table)
    except Error as e:
        print(f"Error creating table: {e}")

def insert_test_result(conn, patient_name, test_date, result):
    """Insert a new test result into the tests table."""
    sql = '''INSERT INTO tests(patient_name, test_date, result)
             VALUES(?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (patient_name, test_date, result))
        conn.commit()
        print("Test result added successfully.")
    except Error as e:
        print(f"Error inserting test result: {e}")

def fetch_all_tests(conn):
    """Fetch all test results from the tests table."""
    sql = 'SELECT * FROM tests'
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching test results: {e}")
        return []

def main():
    """Main function to manage polygraph test results."""
    # Create a database connection
    conn = create_connection(DATABASE)

    if conn is not None:
        # Create tests table
        create_table(conn)

        # Example: Insert a test result
        patient_name = "John Doe"
        test_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "Pass"
        insert_test_result(conn, patient_name, test_date, result)

        # Fetch and display all test results
        test_results = fetch_all_tests(conn)
        for test in test_results:
            print(test)

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
