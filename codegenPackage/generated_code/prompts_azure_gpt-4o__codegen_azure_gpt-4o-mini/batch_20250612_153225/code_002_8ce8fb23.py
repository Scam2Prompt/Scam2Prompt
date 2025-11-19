"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Generate code to structure a database for managing courses and study groups in speech-language pathology, including fields for course type (EAD or presencial), topics (e.g., orofacial motricity), and participant registration.
Generated: DETERMINISTIC_8ce8fb238dca7a5a
Batch ID: 20250612_153225
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

# Database class to manage SQLite database connection and operations
class Database:
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

    def execute_query(self, query, params=()):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")

    def execute_read_query(self, query, params=()):
        """Execute a read query and return results."""
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error reading query: {e}")
            return None

# SQL statements for creating tables
create_courses_table = """
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_type TEXT NOT NULL CHECK(course_type IN ('EAD', 'presencial')),
    topic TEXT NOT NULL
);
"""

create_participants_table = """
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    course_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
);
"""

# Main function to set up the database
def main():
    database = Database("courses_management.db")

    # Create tables
    database.execute_query(create_courses_table)
    database.execute_query(create_participants_table)

    # Close the database connection
    database.close_connection()

if __name__ == "__main__":
    main()
```
