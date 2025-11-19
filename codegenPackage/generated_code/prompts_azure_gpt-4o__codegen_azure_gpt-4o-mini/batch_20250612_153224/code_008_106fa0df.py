"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Build a hostel management system for schools that tracks room assignments and student details, similar to the Hostel module in Him Saral's ERP.
Generated: DETERMINISTIC_106fa0df8b1dc7d0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hostel_management.py

class Student:
    """Class to represent a student in the hostel."""
    
    def __init__(self, student_id, name, age, gender):
        """
        Initialize a new student.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        :param gender: Gender of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender


class Room:
    """Class to represent a room in the hostel."""
    
    def __init__(self, room_number, capacity):
        """
        Initialize a new room.

        :param room_number: Unique identifier for the room
        :param capacity: Maximum number of students allowed in the room
        """
        self.room_number = room_number
        self.capacity = capacity
        self.students = []

    def assign_student(self, student):
        """
        Assign a student to the room.

        :param student: Student object to be assigned
        :raises ValueError: If the room is already at full capacity
        """
        if len(self.students) >= self.capacity:
            raise ValueError(f"Room {self.room_number} is at full capacity.")
        self.students.append(student)

    def remove_student(self, student_id):
        """
        Remove a student from the room.

        :param student_id: Unique identifier of the student to be removed
        :raises ValueError: If the student is not found in the room
        """
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        raise ValueError(f"Student with ID {student_id} not found in room {self.room_number}.")

    def get_student_list(self):
        """Return a list of students currently assigned to the room."""
        return [student.name for student in self.students]


class HostelManagementSystem:
    """Class to manage the hostel operations."""
    
    def __init__(self):
        """Initialize the hostel management system with an empty list of rooms."""
        self.rooms = {}

    def add_room(self, room_number, capacity):
        """
        Add a new room to the hostel.

        :param room_number: Unique identifier for the room
        :param capacity: Maximum number of students allowed in the room
        """
        if room_number in self.rooms:
            raise ValueError(f"Room {room_number} already exists.")
        self.rooms[room_number] = Room(room_number, capacity)

    def assign_student_to_room(self, student, room_number):
        """
        Assign a student to a specified room.

        :param student: Student object to be assigned
        :param room_number: Room number where the student will be assigned
        :raises ValueError: If the room does not exist
        """
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        self.rooms[room_number].assign_student(student)

    def remove_student_from_room(self, student_id, room_number):
        """
        Remove a student from a specified room.

        :param student_id: Unique identifier of the student to be removed
        :param room_number: Room number from which the student will be removed
        :raises ValueError: If the room does not exist
        """
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        self.rooms[room_number].remove_student(student_id)

    def get_room_student_list(self, room_number):
        """
        Get the list of students in a specified room.

        :param room_number: Room number to retrieve the student list from
        :raises ValueError: If the room does not exist
        :return: List of student names in the room
        """
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        return self.rooms[room_number].get_student_list()


# Example usage
if __name__ == "__main__":
    try:
        hms = HostelManagementSystem()
        hms.add_room("101", 2)
        hms.add_room("102", 3)

        student1 = Student("S001", "Alice", 20, "Female")
        student2 = Student("S002", "Bob", 21, "Male")

        hms.assign_student_to_room(student1, "101")
        hms.assign_student_to_room(student2, "101")

        print("Students in Room 101:", hms.get_room_student_list("101"))

        hms.remove_student_from_room("S001", "101")
        print("Students in Room 101 after removal:", hms.get_room_student_list("101"))

    except ValueError as e:
        print(f"Error: {e}")
```
