"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Design a simple database schema to store information about students, teachers, and activities offered by a play school like Kiddoo Playway, and write a Python script to interact with this database.
Generated: DETERMINISTIC_0e9174fcc45b4e07
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

# Database schema creation and interaction script
def initialize_database():
    """
    Initializes the database and creates tables for students, teachers, and activities.
    """
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        # Create Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            parent_contact TEXT NOT NULL
        );
        """)

        # Create Teachers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            contact TEXT NOT NULL
        );
        """)

        # Create Activities table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Activities (
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teachers (teacher_id)
        );
        """)

        # Commit changes and close connection
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()


def add_student(name, age, parent_contact):
    """
    Adds a new student to the Students table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Students (name, age, parent_contact)
        VALUES (?, ?, ?);
        """, (name, age, parent_contact))

        conn.commit()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()


def add_teacher(name, subject, contact):
    """
    Adds a new teacher to the Teachers table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Teachers (name, subject, contact)
        VALUES (?, ?, ?);
        """, (name, subject, contact))

        conn.commit()
        print("Teacher added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding teacher: {e}")
    finally:
        conn.close()


def add_activity(name, description, teacher_id):
    """
    Adds a new activity to the Activities table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Activities (name, description, teacher_id)
        VALUES (?, ?, ?);
        """, (name, description, teacher_id))

        conn.commit()
        print("Activity added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding activity: {e}")
    finally:
        conn.close()


def fetch_all_students():
    """
    Fetches all students from the Students table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Students;")
        students = cursor.fetchall()

        for student in students:
            print(student)
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
    finally:
        conn.close()


def fetch_all_teachers():
    """
    Fetches all teachers from the Teachers table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Teachers;")
        teachers = cursor.fetchall()

        for teacher in teachers:
            print(teacher)
    except sqlite3.Error as e:
        print(f"Error fetching teachers: {e}")
    finally:
        conn.close()


def fetch_all_activities():
    """
    Fetches all activities from the Activities table.
    """
    try:
        conn = sqlite3.connect("play_school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Activities;")
        activities = cursor.fetchall()

        for activity in activities:
            print(activity)
    except sqlite3.Error as e:
        print(f"Error fetching activities: {e}")
    finally:
        conn.close()


# Main script execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    add_student("Alice", 5, "123-456-7890")
    add_teacher("Mr. Smith", "Art", "987-654-3210")
    add_activity("Painting", "Learn to paint with watercolors", 1)

    print("\nStudents:")
    fetch_all_students()

    print("\nTeachers:")
    fetch_all_teachers()

    print("\nActivities:")
    fetch_all_activities()
```
