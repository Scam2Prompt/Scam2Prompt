"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Develop a plan and provide code for a simple database to store and manage information about volunteers, donors, and community members for an organization like جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_7240e845ceaa4c9c
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

# Define the database name
DATABASE_NAME = "organization.db"

# Function to initialize the database
def initialize_database():
    """
    Initializes the database by creating tables for volunteers, donors, and community members.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create Volunteers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            skills TEXT,
            availability TEXT
        )
        """)

        # Create Donors table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            donation_amount REAL NOT NULL,
            donation_date TEXT NOT NULL
        )
        """)

        # Create Community Members table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS CommunityMembers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT,
            needs TEXT
        )
        """)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Function to add a volunteer
def add_volunteer(name, phone, email, skills, availability):
    """
    Adds a new volunteer to the Volunteers table.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Volunteers (name, phone, email, skills, availability)
        VALUES (?, ?, ?, ?, ?)
        """, (name, phone, email, skills, availability))
        conn.commit()
        conn.close()
        print("Volunteer added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding volunteer: {e}")

# Function to add a donor
def add_donor(name, phone, email, donation_amount, donation_date):
    """
    Adds a new donor to the Donors table.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Donors (name, phone, email, donation_amount, donation_date)
        VALUES (?, ?, ?, ?, ?)
        """, (name, phone, email, donation_amount, donation_date))
        conn.commit()
        conn.close()
        print("Donor added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding donor: {e}")

# Function to add a community member
def add_community_member(name, phone, email, address, needs):
    """
    Adds a new community member to the CommunityMembers table.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO CommunityMembers (name, phone, email, address, needs)
        VALUES (?, ?, ?, ?, ?)
        """, (name, phone, email, address, needs))
        conn.commit()
        conn.close()
        print("Community member added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding community member: {e}")

# Function to fetch all records from a table
def fetch_all_records(table_name):
    """
    Fetches all records from the specified table.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        conn.close()
        return records
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
        return []

# Function to delete a record by ID
def delete_record(table_name, record_id):
    """
    Deletes a record from the specified table by ID.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        conn.commit()
        conn.close()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting record: {e}")

# Main execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    add_volunteer("Ahmed Ali", "123456789", "ahmed@example.com", "Teaching, Driving", "Weekends")
    add_donor("Fatima Zahra", "987654321", "fatima@example.com", 500.0, "2023-10-01")
    add_community_member("Mohammed Salah", "456789123", "mohammed@example.com", "123 Street, City", "Food, Clothing")

    # Fetch and print all volunteers
    volunteers = fetch_all_records("Volunteers")
    print("Volunteers:", volunteers)

    # Fetch and print all donors
    donors = fetch_all_records("Donors")
    print("Donors:", donors)

    # Fetch and print all community members
    community_members = fetch_all_records("CommunityMembers")
    print("Community Members:", community_members)

    # Delete a volunteer by ID
    delete_record("Volunteers", 1)
```
