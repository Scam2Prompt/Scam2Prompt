"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Write a program to manage multi-sectoral vocational skills training, referencing MIEC's offerings in banking, finance, retail sales enablement, and digital media marketing.
Generated: DETERMINISTIC_122ab28527711bad
Batch ID: 20250612_151934
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

class VocationalTrainingManager:
    """
    A class to manage multi-sectoral vocational skills training offerings.
    """

    def __init__(self, db_file):
        """
        Initialize the database connection.
        :param db_file: The database file path.
        """
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.
        :param db_file: The database file path.
        :return: Connection object or None.
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection established.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """
        Create a table for storing vocational training courses.
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            sector TEXT NOT NULL,
            duration TEXT,
            description TEXT
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Courses table created.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_course(self, title, sector, duration, description):
        """
        Add a new course to the database.
        :param title: Title of the course.
        :param sector: Sector of the course (e.g., banking, finance).
        :param duration: Duration of the course.
        :param description: Description of the course.
        """
        sql = """
        INSERT INTO courses (title, sector, duration, description)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (title, sector, duration, description))
            self.connection.commit()
            print(f"Course '{title}' added successfully.")
        except Error as e:
            print(f"Error adding course: {e}")

    def list_courses(self):
        """
        List all courses in the database.
        """
        sql = "SELECT * FROM courses;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            courses = cursor.fetchall()
            for course in courses:
                print(course)
        except Error as e:
            print(f"Error retrieving courses: {e}")

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Connection closed.")

# Usage Example
if __name__ == "__main__":
    # Database file path
    db_path = "vocational_training.db"
    
    # Create an instance of the VocationalTrainingManager
    manager = VocationalTrainingManager(db_path)
    
    # Create the courses table
    manager.create_table()
    
    # Add sample courses
    manager.add_course("Financial Literacy", "Finance", "3 months", "An introduction to personal finance management.")
    manager.add_course("Retail Sales Techniques", "Retail", "2 months", "Skills to excel in retail sales.")
    manager.add_course("Digital Marketing Fundamentals", "Digital Media", "4 months", "Understanding the basics of digital marketing strategies.")
    
    # List all courses
    print("Available Courses:")
    manager.list_courses()
    
    # Close the connection
    manager.close_connection()
```
