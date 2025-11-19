"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a Python script that connects a community organization with local schools to enhance literacy programs, inspired by the NICER Foundation's approach to education.
Generated: DETERMINISTIC_8d0461ff958906d3
Batch ID: 20250612_160507
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

# Define a class for the Literacy Program
class LiteracyProgram:
    def __init__(self, db_file):
        """Initialize the LiteracyProgram with a database file."""
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

    def create_table(self):
        """Create tables for schools and programs in the database."""
        try:
            sql_create_schools_table = """ 
            CREATE TABLE IF NOT EXISTS schools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            );"""
            
            sql_create_programs_table = """ 
            CREATE TABLE IF NOT EXISTS programs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                school_id INTEGER NOT NULL,
                program_name TEXT NOT NULL,
                description TEXT,
                FOREIGN KEY (school_id) REFERENCES schools (id)
            );"""
            
            cursor = self.connection.cursor()
            cursor.execute(sql_create_schools_table)
            cursor.execute(sql_create_programs_table)
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def add_school(self, name, address):
        """Add a new school to the database."""
        sql = ''' INSERT INTO schools(name, address) VALUES(?, ?) '''
        cur = self.connection.cursor()
        cur.execute(sql, (name, address))
        self.connection.commit()
        print(f"School added: {name}")

    def add_program(self, school_id, program_name, description):
        """Add a new literacy program for a specific school."""
        sql = ''' INSERT INTO programs(school_id, program_name, description) VALUES(?, ?, ?) '''
        cur = self.connection.cursor()
        cur.execute(sql, (school_id, program_name, description))
        self.connection.commit()
        print(f"Program added: {program_name}")

    def list_schools(self):
        """List all schools in the database."""
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM schools")
        rows = cur.fetchall()
        for row in rows:
            print(f"School ID: {row[0]}, Name: {row[1]}, Address: {row[2]}")

    def list_programs(self):
        """List all programs in the database."""
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM programs")
        rows = cur.fetchall()
        for row in rows:
            print(f"Program ID: {row[0]}, School ID: {row[1]}, Name: {row[2]}, Description: {row[3]}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Main function to demonstrate the functionality
def main():
    database = "literacy_programs.db"
    
    # Create a LiteracyProgram instance
    program = LiteracyProgram(database)
    
    # Create tables
    program.create_table()

    # Add sample schools
    program.add_school("Greenwood High", "123 Main St, Springfield")
    program.add_school("Lincoln Elementary", "456 Elm St, Springfield")

    # Add sample programs
    program.add_program(1, "Reading Club", "A club focused on reading books and discussing them.")
    program.add_program(2, "Writing Workshop", "A workshop to improve writing skills among students.")

    # List schools and programs
    print("\nList of Schools:")
    program.list_schools()
    
    print("\nList of Programs:")
    program.list_programs()

    # Close the database connection
    program.close_connection()

if __name__ == '__main__':
    main()
```
