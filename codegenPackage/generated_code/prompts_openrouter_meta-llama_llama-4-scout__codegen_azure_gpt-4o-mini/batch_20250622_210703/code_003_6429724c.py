"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Develop a basic data model for storing and managing client information, cases, and investigations for a law firm like Grupo Legal Corporativo, using a database management system.
Generated: DETERMINISTIC_6429724c94cccd80
Batch ID: 20250622_210703
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

class Database:
    """Class to manage the SQLite database connection and operations."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

class Client:
    """Class to represent a client in the law firm."""
    
    def __init__(self, name, email, phone):
        """Initialize a client with name, email, and phone."""
        self.name = name
        self.email = email
        self.phone = phone

class Case:
    """Class to represent a legal case."""
    
    def __init__(self, client_id, case_number, description):
        """Initialize a case with client ID, case number, and description."""
        self.client_id = client_id
        self.case_number = case_number
        self.description = description

class Investigation:
    """Class to represent an investigation related to a case."""
    
    def __init__(self, case_id, investigator_name, findings):
        """Initialize an investigation with case ID, investigator name, and findings."""
        self.case_id = case_id
        self.investigator_name = investigator_name
        self.findings = findings

class LawFirmDB:
    """Class to manage the law firm's database operations."""
    
    def __init__(self, db_file):
        """Initialize the database and create tables if they do not exist."""
        self.database = Database(db_file)
        self.create_tables()

    def create_tables(self):
        """Create tables for clients, cases, and investigations."""
        try:
            cursor = self.database.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    case_number TEXT NOT NULL UNIQUE,
                    description TEXT,
                    FOREIGN KEY (client_id) REFERENCES clients (id)
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS investigations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_id INTEGER NOT NULL,
                    investigator_name TEXT NOT NULL,
                    findings TEXT,
                    FOREIGN KEY (case_id) REFERENCES cases (id)
                );
            ''')
            self.database.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_client(self, client):
        """Add a new client to the database."""
        try:
            cursor = self.database.connection.cursor()
            cursor.execute('''
                INSERT INTO clients (name, email, phone)
                VALUES (?, ?, ?);
            ''', (client.name, client.email, client.phone))
            self.database.connection.commit()
            print(f"Client {client.name} added successfully.")
        except Error as e:
            print(f"Error adding client: {e}")

    def add_case(self, case):
        """Add a new case to the database."""
        try:
            cursor = self.database.connection.cursor()
            cursor.execute('''
                INSERT INTO cases (client_id, case_number, description)
                VALUES (?, ?, ?);
            ''', (case.client_id, case.case_number, case.description))
            self.database.connection.commit()
            print(f"Case {case.case_number} added successfully.")
        except Error as e:
            print(f"Error adding case: {e}")

    def add_investigation(self, investigation):
        """Add a new investigation to the database."""
        try:
            cursor = self.database.connection.cursor()
            cursor.execute('''
                INSERT INTO investigations (case_id, investigator_name, findings)
                VALUES (?, ?, ?);
            ''', (investigation.case_id, investigation.investigator_name, investigation.findings))
            self.database.connection.commit()
            print(f"Investigation by {investigation.investigator_name} added successfully.")
        except Error as e:
            print(f"Error adding investigation: {e}")

# Example usage
if __name__ == "__main__":
    db_file = "law_firm.db"
    law_firm_db = LawFirmDB(db_file)

    # Adding a client
    client = Client(name="John Doe", email="john.doe@example.com", phone="123-456-7890")
    law_firm_db.add_client(client)

    # Adding a case for the client
    case = Case(client_id=1, case_number="C12345", description="Contract dispute")
    law_firm_db.add_case(case)

    # Adding an investigation for the case
    investigation = Investigation(case_id=1, investigator_name="Jane Smith", findings="Evidence collected.")
    law_firm_db.add_investigation(investigation)

    # Close the database connection
    law_firm_db.database.close_connection()
```
