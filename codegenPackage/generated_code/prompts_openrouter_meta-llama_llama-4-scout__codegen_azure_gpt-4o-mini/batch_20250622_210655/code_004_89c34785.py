"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Design a database schema to store information about the initiatives, team members, and donors of the Jiyo Jaago Foundation, and provide a Python script to interact with the database.
Generated: DETERMINISTIC_89c34785fc74ccd2
Batch ID: 20250622_210655
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
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables
def create_tables(conn):
    """Create tables for initiatives, team members, and donors."""
    try:
        cursor = conn.cursor()
        
        # Create initiatives table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS initiatives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT,
                end_date TEXT
            );
        ''')
        
        # Create team members table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS team_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT,
                initiative_id INTEGER,
                FOREIGN KEY (initiative_id) REFERENCES initiatives (id)
            );
        ''')
        
        # Create donors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount REAL NOT NULL,
                initiative_id INTEGER,
                FOREIGN KEY (initiative_id) REFERENCES initiatives (id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to insert an initiative
def insert_initiative(conn, name, description, start_date, end_date):
    """Insert a new initiative into the initiatives table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO initiatives (name, description, start_date, end_date)
            VALUES (?, ?, ?, ?);
        ''', (name, description, start_date, end_date))
        conn.commit()
        print("Initiative added successfully.")
    except Error as e:
        print(f"Error inserting initiative: {e}")

# Function to insert a team member
def insert_team_member(conn, name, role, initiative_id):
    """Insert a new team member into the team_members table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO team_members (name, role, initiative_id)
            VALUES (?, ?, ?);
        ''', (name, role, initiative_id))
        conn.commit()
        print("Team member added successfully.")
    except Error as e:
        print(f"Error inserting team member: {e}")

# Function to insert a donor
def insert_donor(conn, name, amount, initiative_id):
    """Insert a new donor into the donors table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO donors (name, amount, initiative_id)
            VALUES (?, ?, ?);
        ''', (name, amount, initiative_id))
        conn.commit()
        print("Donor added successfully.")
    except Error as e:
        print(f"Error inserting donor: {e}")

# Main function to run the script
def main():
    database = "jiyo_jaago_foundation.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example data insertion
        insert_initiative(conn, "Clean Water Initiative", "Providing clean water to rural areas.", "2023-01-01", "2023-12-31")
        insert_team_member(conn, "Alice Smith", "Project Manager", 1)
        insert_donor(conn, "John Doe", 5000.00, 1)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
