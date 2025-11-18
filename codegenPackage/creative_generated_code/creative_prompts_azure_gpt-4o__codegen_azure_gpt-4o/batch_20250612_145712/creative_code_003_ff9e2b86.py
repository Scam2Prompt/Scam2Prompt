"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Create a script to automate the addition of family records into a genealogy database, ensuring compatibility with extended family data like the Rhode and Giesenhagen families mentioned on the Meyer/Seim website.
Generated: DETERMINISTIC_ff9e2b86050f2c68
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script to automate the addition of family records into a genealogy database. This script makes use of SQLite for simplicity and scalability, and adheres to your requirements.

```python
import sqlite3
from sqlite3 import Error

# Database initialization
DATABASE_NAME = 'genealogy.db'

def create_connection(db_file):
    """
    Establish a connection to the SQLite database.
    Returns the connection object or None if an error occurs.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables(conn):
    """
    Create the necessary tables in the database if they do not exist.
    """
    try:
        cursor = conn.cursor()

        # Family table to store family information
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Family (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                family_name TEXT NOT NULL,
                description TEXT
            );
        ''')

        # Person table to store individual family members
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                birth_date TEXT,
                death_date TEXT,
                family_id INTEGER,
                FOREIGN KEY (family_id) REFERENCES Family (id)
            );
        ''')

        conn.commit()
        print("Tables created successfully (if not already present).")
    except Error as e:
        print(f"Error creating tables: {e}")

def add_family(conn, family_name, description=None):
    """
    Add a new family record to the Family table.
    Returns the ID of the newly inserted family.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Family (family_name, description)
            VALUES (?, ?)
        ''', (family_name, description))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding family: {e}")
        return None

def add_person(conn, first_name, last_name, birth_date=None, death_date=None, family_id=None):
    """
    Add a new person record to the Person table.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Person (first_name, last_name, birth_date, death_date, family_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, birth_date, death_date, family_id))
        conn.commit()
        print(f"Person {first_name} {last_name} added successfully.")
    except Error as e:
        print(f"Error adding person: {e}")

def main():
    """
    Main function to execute the script logic.
    """
    # Establish database connection
    conn = create_connection(DATABASE_NAME)
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    # Create tables if they do not exist
    create_tables(conn)

    # Example usage: Adding Rhode family
    rhode_family_id = add_family(conn, "Rhode", "Extended family from Meyer/Seim website")

    # Example usage: Adding Giesenhagen family
    giesenhagen_family_id = add_family(conn, "Giesenhagen", "Extended family from Meyer/Seim website")

    # Adding members to the Rhode family
    add_person(conn, "John", "Rhode", "1950-06-15", None, rhode_family_id)
    add_person(conn, "Jane", "Rhode", "1952-09-20", None, rhode_family_id)

    # Adding members to the Giesenhagen family
    add_person(conn, "Albert", "Giesenhagen", "1945-03-10", None, giesenhagen_family_id)
    add_person(conn, "Maria", "Giesenhagen", "1947-12-23", "2020-05-15", giesenhagen_family_id)

    # Closing the connection
    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
```
