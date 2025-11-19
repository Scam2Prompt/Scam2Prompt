"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Create a script that integrates university registration functionality for establishing Bridges to Professions branches, allowing users to apply as directors or team leads.
Generated: DETERMINISTIC_16b4c805c0c95269
Batch ID: 20250612_145444
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

# Database configuration
DATABASE = "university_registration.db"

# Create a connection to the SQLite database
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database established.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables for the registration system
def create_tables(conn):
    """Create tables for storing user applications."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                role TEXT NOT NULL CHECK(role IN ('Director', 'Team Lead')),
                status TEXT NOT NULL DEFAULT 'Pending'
            );
        ''')
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to apply for a position
def apply_for_position(conn, name, email, role):
    """Insert a new application into the applications table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applications (name, email, role)
            VALUES (?, ?, ?);
        ''', (name, email, role))
        conn.commit()
        print(f"Application submitted successfully for {name} as {role}.")
    except Error as e:
        print(f"Error submitting application: {e}")

# Function to view all applications
def view_applications(conn):
    """Fetch and display all applications from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM applications;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching applications: {e}")

# Main function to run the application
def main():
    """Main function to run the university registration script."""
    conn = create_connection(DATABASE)
    if conn is not None:
        create_tables(conn)

        # Example usage
        apply_for_position(conn, "Alice Smith", "alice@example.com", "Director")
        apply_for_position(conn, "Bob Johnson", "bob@example.com", "Team Lead")

        print("\nCurrent Applications:")
        view_applications(conn)

        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```
