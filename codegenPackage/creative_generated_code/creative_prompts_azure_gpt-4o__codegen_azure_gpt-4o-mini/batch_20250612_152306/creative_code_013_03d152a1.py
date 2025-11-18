"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write a program to manage franchise applications and offline/online course registrations for vocational training centers, referencing the features on the RSP Bharat website.
Generated: DETERMINISTIC_03d152a1c90e5c77
Batch ID: 20250612_152306
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

# Database class to handle SQLite operations
class Database:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error creating connection: {e}")
            return None

    def execute_query(self, query, params=()):
        """Execute a query against the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=()):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

# Franchise application manager
class FranchiseApplicationManager:
    def __init__(self, db):
        """Initialize the franchise application manager with a database instance."""
        self.db = db

    def create_franchise_application_table(self):
        """Create the table for franchise applications."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS franchise_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
        );
        """
        self.db.execute_query(create_table_query)

    def add_application(self, name, email, phone):
        """Add a new franchise application."""
        insert_query = """INSERT INTO franchise_applications (name, email, phone) VALUES (?, ?, ?)"""
        return self.db.execute_query(insert_query, (name, email, phone))

    def get_applications(self):
        """Retrieve all franchise applications."""
        select_query = "SELECT * FROM franchise_applications"
        return self.db.fetch_all(select_query)

# Course registration manager
class CourseRegistrationManager:
    def __init__(self, db):
        """Initialize the course registration manager with a database instance."""
        self.db = db

    def create_course_registration_table(self):
        """Create the table for course registrations."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS course_registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            course_name TEXT NOT NULL,
            registration_type TEXT NOT NULL CHECK(registration_type IN ('Online', 'Offline')),
            date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.db.execute_query(create_table_query)

    def register_course(self, student_name, course_name, registration_type):
        """Register a student for a course."""
        if registration_type not in ('Online', 'Offline'):
            raise ValueError("Registration type must be 'Online' or 'Offline'")
        
        insert_query = """INSERT INTO course_registrations (student_name, course_name, registration_type) VALUES (?, ?, ?)"""
        return self.db.execute_query(insert_query, (student_name, course_name, registration_type))

    def get_registrations(self):
        """Retrieve all course registrations."""
        select_query = "SELECT * FROM course_registrations"
        return self.db.fetch_all(select_query)

# Main application logic
def main():
    # Initialize the database
    db = Database("vocational_training_centers.db")

    # Create tables
    franchise_manager = FranchiseApplicationManager(db)
    franchise_manager.create_franchise_application_table()

    course_manager = CourseRegistrationManager(db)
    course_manager.create_course_registration_table()

    # Example usage: Adding a franchise application
    try:
        franchise_manager.add_application("John Doe", "john@example.com", "123-456-7890")
        print("Franchise application added successfully.")
    except Exception as e:
        print(f"Failed to add franchise application: {e}")

    # Example usage: Registering a course
    try:
        course_manager.register_course("Alice Smith", "Python Programming", "Online")
        print("Course registration completed successfully.")
    except ValueError as ve:
        print(f"Error in registration: {ve}")
    except Exception as e:
        print(f"Failed to register course: {e}")

    # Fetch and display applications and registrations
    print("Franchise Applications:", franchise_manager.get_applications())
    print("Course Registrations:", course_manager.get_registrations())

if __name__ == "__main__":
    main()
```
