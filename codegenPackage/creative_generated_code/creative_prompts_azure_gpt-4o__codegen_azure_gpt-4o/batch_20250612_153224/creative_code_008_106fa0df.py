"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Build a hostel management system for schools that tracks room assignments and student details, similar to the Hostel module in Him Saral's ERP.
Generated: DETERMINISTIC_106fa0df8b1dc7d0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation of a hostel management system in Python:

```python
import sqlite3

# Hostel Management System

class HostelManagementSystem:
    def __init__(self, db_name="hostel_management.db"):
        """
        Initialize the Hostel Management System with a SQLite database.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create necessary tables for the hostel management system.
        """
        try:
            # Table for students
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                room_id INTEGER,
                FOREIGN KEY (room_id) REFERENCES rooms(room_id)
            )
            """)

            # Table for rooms
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_number TEXT NOT NULL UNIQUE,
                capacity INTEGER NOT NULL,
                occupied INTEGER NOT NULL DEFAULT 0
            )
            """)

            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_student(self, name, age, gender, room_id=None):
        """
        Add a new student to the database.
        :param name: Name of the student.
        :param age: Age of the student.
        :param gender: Gender of the student.
        :param room_id: Room ID where the student is assigned (optional).
        """
        try:
            self.cursor.execute("""
            INSERT INTO students (name, age, gender, room_id)
            VALUES (?, ?, ?, ?)
            """, (name, age, gender, room_id))
            self.connection.commit()
            print("Student added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")

    def add_room(self, room_number, capacity):
        """
        Add a new room to the database.
        :param room_number: Unique identifier for the room.
        :param capacity: Maximum capacity of the room.
        """
        try:
            self.cursor.execute("""
            INSERT INTO rooms (room_number, capacity, occupied)
            VALUES (?, ?, 0)
            """, (room_number, capacity))
            self.connection.commit()
            print("Room added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding room: {e}")

    def assign_student_to_room(self, student_id, room_id):
        """
        Assign a student to a room.
        :param student_id: ID of the student.
        :param room_id: ID of the room.
        """
        try:
            # Check room capacity
            self.cursor.execute("""
            SELECT capacity, occupied FROM rooms WHERE room_id = ?
            """, (room_id,))
            room = self.cursor.fetchone()

            if room and room[1] < room[0]:  # Check if room is not full
                # Assign the student to the room
                self.cursor.execute("""
                UPDATE students SET room_id = ? WHERE student_id = ?
                """, (room_id, student_id))
                # Update room occupancy
                self.cursor.execute("""
                UPDATE rooms SET occupied = occupied + 1 WHERE room_id = ?
                """, (room_id,))
                self.connection.commit()
                print("Student assigned to room successfully.")
            else:
                print("Room is full or does not exist.")
        except sqlite3.Error as e:
            print(f"Error assigning student to room: {e}")

    def get_room_details(self, room_id):
        """
        Get details of a specific room, including assigned students.
        :param room_id: ID of the room.
        """
        try:
            # Fetch room details
            self.cursor.execute("""
            SELECT room_number, capacity, occupied FROM rooms WHERE room_id = ?
            """, (room_id,))
            room = self.cursor.fetchone()

            if room:
                print(f"Room Number: {room[0]}, Capacity: {room[1]}, Occupied: {room[2]}")

                # Fetch students assigned to the room
                self.cursor.execute("""
                SELECT student_id, name, age, gender FROM students WHERE room_id = ?
                """, (room_id,))
                students = self.cursor.fetchall()
                print("Assigned Students:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}")
            else:
                print("Room does not exist.")
        except sqlite3.Error as e:
            print(f"Error fetching room details: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
        print("Database connection closed.")


# Example usage:
if __name__ == "__main__":
    # Initialize the system
    hostel_system = HostelManagementSystem()

    # Add rooms
    hostel_system.add_room("A101", 4)
    hostel_system.add_room("B202", 2)

    # Add students
    hostel_system.add_student("Alice", 18, "Female")
    hostel_system.add_student("Bob", 19, "Male")

    # Assign students to rooms
    hostel_system.assign_student_to_room(1, 1)
    hostel_system.assign_student_to_room(2, 2)

    # Get room details
    hostel_system.get_room_details(1)

    # Close the system
    hostel_system.close()
```

This system uses SQLite as the backend database and provides the basic functionality for managing students and rooms in a hostel. You can extend this further to include more features as needed.
