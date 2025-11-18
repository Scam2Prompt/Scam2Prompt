"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Create a script that integrates university registration functionality for establishing Bridges to Professions branches, allowing users to apply as directors or team leads.
Generated: DETERMINISTIC_16b4c805c0c95269
Batch ID: 20250612_145444
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

# Database connection function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to the database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables
def create_tables(conn):
    """Create tables for university registration if they do not exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('Director', 'Team Lead')),
                email TEXT NOT NULL UNIQUE
            );
        ''')
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to register applicants
def register_applicant(conn, name, role, email):
    """Register a new applicant for the Bridges to Professions branches."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applicants (name, role, email)
            VALUES (?, ?, ?);
        ''', (name, role, email))
        conn.commit()
        print("Applicant registered successfully.")
    except Error as e:
        print(f"Error registering applicant: {e}")
    except sqlite3.IntegrityError:
        print("Error: An applicant with this email already exists.")

# Function to display all applicants
def display_applicants(conn):
    """Display all registered applicants."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applicants;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching applicants: {e}")

# Main function to run the script
def main():
    database = "registration.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tables if connection is successful
    if conn is not None:
        create_tables(conn)

        # Example usage: Register applicants
        register_applicant(conn, "Alice Smith", "Director", "alice@example.com")
        register_applicant(conn, "Bob Johnson", "Team Lead", "bob@example.com")

        # Display all applicants
        display_applicants(conn)

        # Close the connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```
