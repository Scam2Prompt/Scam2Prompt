"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linearlive.co.uk
Prompt: Create a script to parse and store company registration details, such as those provided by Linear Live Limited, in a database.
Generated: DETERMINISTIC_2963d4a80bf9422b
Batch ID: 20250612_150327
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

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to database established: {db_file}")
    except Error as e:
        print(f"Error establishing database connection: {e}")
    return conn

# Define a function to create a table for company registration details
def create_table(conn):
    """ Create a table for storing company registration details. """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            registration_number TEXT NOT NULL UNIQUE,
            date_of_registration TEXT NOT NULL,
            address TEXT NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table 'companies' created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Define a function to insert company details into the database
def insert_company(conn, company):
    """ Insert a new company into the companies table. """
    sql_insert_company = """
    INSERT INTO companies (name, registration_number, date_of_registration, address)
    VALUES (?, ?, ?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_company, company)
        conn.commit()
        print(f"Company '{company[0]}' inserted successfully.")
    except Error as e:
        print(f"Error inserting company: {e}")

# Main function to execute the script
def main():
    # Database file path
    database = "companies.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create companies table
        create_table(conn)

        # Example company registration details
        company_details = (
            "Linear Live Limited",
            "123456789",
            "2023-01-01",
            "123 Main St, Anytown, AT1 2AB"
        )

        # Insert company details into the database
        insert_company(conn, company_details)

        # Close the database connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
