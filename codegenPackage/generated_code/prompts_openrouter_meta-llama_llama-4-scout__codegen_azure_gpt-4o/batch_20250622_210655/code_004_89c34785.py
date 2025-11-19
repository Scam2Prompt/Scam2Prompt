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
# Import necessary libraries
import sqlite3

# Database schema creation and interaction script for Jiyo Jaago Foundation

# Function to create tables
def create_tables():
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("jiyo_jaago.db")
        cursor = conn.cursor()

        # Create Initiatives table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Initiatives (
            initiative_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date DATE NOT NULL,
            end_date DATE,
            budget REAL NOT NULL
        );
        """)

        # Create TeamMembers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TeamMembers (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            initiative_id INTEGER,
            FOREIGN KEY (initiative_id) REFERENCES Initiatives (initiative_id)
        );
        """)

        # Create Donors table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Donors (
            donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            amount_donated REAL NOT NULL,
            donation_date DATE NOT NULL,
            initiative_id INTEGER,
            FOREIGN KEY (initiative_id) REFERENCES Initiatives (initiative_id)
        );
        """)

        # Commit changes and close connection
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

# Function to insert data into Initiatives table
def add_initiative(name, description, start_date, end_date, budget):
    try:
        conn = sqlite3.connect("jiyo_jaago.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Initiatives (name, description, start_date, end_date, budget)
        VALUES (?, ?, ?, ?, ?);
        """, (name, description, start_date, end_date, budget))

        conn.commit()
        print("Initiative added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding initiative: {e}")
    finally:
        conn.close()

# Function to insert data into TeamMembers table
def add_team_member(name, role, email, phone, initiative_id):
    try:
        conn = sqlite3.connect("jiyo_jaago.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO TeamMembers (name, role, email, phone, initiative_id)
        VALUES (?, ?, ?, ?, ?);
        """, (name, role, email, phone, initiative_id))

        conn.commit()
        print("Team member added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding team member: {e}")
    finally:
        conn.close()

# Function to insert data into Donors table
def add_donor(name, email, phone, amount_donated, donation_date, initiative_id):
    try:
        conn = sqlite3.connect("jiyo_jaago.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Donors (name, email, phone, amount_donated, donation_date, initiative_id)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (name, email, phone, amount_donated, donation_date, initiative_id))

        conn.commit()
        print("Donor added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding donor: {e}")
    finally:
        conn.close()

# Function to fetch all initiatives
def fetch_initiatives():
    try:
        conn = sqlite3.connect("jiyo_jaago.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Initiatives;")
        initiatives = cursor.fetchall()

        for initiative in initiatives:
            print(initiative)
    except sqlite3.Error as e:
        print(f"Error fetching initiatives: {e}")
    finally:
        conn.close()

# Main script execution
if __name__ == "__main__":
    # Create tables
    create_tables()

    # Example data insertion
    add_initiative("Clean Water Project", "Providing clean drinking water to rural areas", "2023-01-01", "2023-12-31", 50000.00)
    add_team_member("Alice Johnson", "Project Manager", "alice@example.com", "1234567890", 1)
    add_donor("John Doe", "john@example.com", "0987654321", 1000.00, "2023-02-15", 1)

    # Fetch and display all initiatives
    fetch_initiatives()
```
