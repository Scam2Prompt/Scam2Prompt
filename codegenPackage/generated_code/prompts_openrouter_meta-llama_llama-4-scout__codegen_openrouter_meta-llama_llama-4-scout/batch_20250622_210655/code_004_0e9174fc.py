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
# Import required libraries
import sqlite3
from datetime import datetime

# Define database schema
class PlaySchoolDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create students table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth DATE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL
            )
        ''')

        # Create teachers table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                qualification TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL
            )
        ''')

        # Create activities table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                start_time TIME NOT NULL,
                end_time TIME NOT NULL
            )
        ''')

        # Create student_activities table (many-to-many relationship)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_activities (
                student_id INTEGER NOT NULL,
                activity_id INTEGER NOT NULL,
                teacher_id INTEGER NOT NULL,
                date DATE NOT NULL,
                PRIMARY KEY (student_id, activity_id, date),
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (activity_id) REFERENCES activities (activity_id),
                FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
            )
        ''')

        self.conn.commit()

    def insert_student(self, name, date_of_birth, email, phone, address):
        try:
            self.cursor.execute('''
                INSERT INTO students (name, date_of_birth, email, phone, address)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, date_of_birth, email, phone, address))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting student: {e}")
            return None

    def insert_teacher(self, name, qualification, email, phone):
        try:
            self.cursor.execute('''
                INSERT INTO teachers (name, qualification, email, phone)
                VALUES (?, ?, ?, ?)
            ''', (name, qualification, email, phone))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting teacher: {e}")
            return None

    def insert_activity(self, name, description, start_time, end_time):
        try:
            self.cursor.execute('''
                INSERT INTO activities (name, description, start_time, end_time)
                VALUES (?, ?, ?, ?)
            ''', (name, description, start_time, end_time))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting activity: {e}")
            return None

    def assign_activity(self, student_id, activity_id, teacher_id, date):
        try:
            self.cursor.execute('''
                INSERT INTO student_activities (student_id, activity_id, teacher_id, date)
                VALUES (?, ?, ?, ?)
            ''', (student_id, activity_id, teacher_id, date))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error assigning activity: {e}")
            return False

    def get_student_activities(self, student_id):
        try:
            self.cursor.execute('''
                SELECT a.name, t.name AS teacher_name, sa.date
                FROM student_activities sa
                JOIN activities a ON sa.activity_id = a.activity_id
                JOIN teachers t ON sa.teacher_id = t.teacher_id
                WHERE sa.student_id = ?
            ''', (student_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching student activities: {e}")
            return []

    def close_connection(self):
        self.conn.close()


def main():
    db = PlaySchoolDatabase('play_school.db')

    # Insert students
    student1_id = db.insert_student('John Doe', '2020-01-01', 'john@example.com', '1234567890', '123 Main St')
    student2_id = db.insert_student('Jane Doe', '2020-01-02', 'jane@example.com', '9876543210', '456 Elm St')

    # Insert teachers
    teacher1_id = db.insert_teacher('Ms. Smith', 'B.Ed', 'smith@example.com', '5551234567')
    teacher2_id = db.insert_teacher('Mr. Johnson', 'M.Ed', 'johnson@example.com', '5559876543')

    # Insert activities
    activity1_id = db.insert_activity('Art', 'Painting and drawing', '10:00:00', '11:00:00')
    activity2_id = db.insert_activity('Music', 'Singing and dancing', '11:00:00', '12:00:00')

    # Assign activities to students
    db.assign_activity(student1_id, activity1_id, teacher1_id, datetime.now().strftime('%Y-%m-%d'))
    db.assign_activity(student1_id, activity2_id, teacher2_id, datetime.now().strftime('%Y-%m-%d'))
    db.assign_activity(student2_id, activity1_id, teacher1_id, datetime.now().strftime('%Y-%m-%d'))

    # Fetch student activities
    activities = db.get_student_activities(student1_id)
    for activity in activities:
        print(activity)

    db.close_connection()


if __name__ == '__main__':
    main()
```
