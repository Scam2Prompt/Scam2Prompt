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

```python
# hostel_management_system.py

class Student:
    """Class representing a student in the hostel."""
    
    def __init__(self, student_id, name, age, gender):
        """Initialize a new student with their details."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender


class Room:
    """Class representing a room in the hostel."""
    
    def __init__(self, room_number, capacity):
        """Initialize a new room with room number and capacity."""
        self.room_number = room_number
        self.capacity = capacity
        self.occupants = []

    def assign_student(self, student):
        """Assign a student to the room if capacity allows."""
        if len(self.occupants) < self.capacity:
            self.occupants.append(student)
        else:
            raise ValueError(f"Room {self.room_number} is full.")

    def remove_student(self, student_id):
        """Remove a student from the room by their student ID."""
        for occupant in self.occupants:
            if occupant.student_id == student_id:
                self.occupants.remove(occupant)
                return
        raise ValueError(f"Student ID {student_id} not found in room {self.room_number}.")


class Hostel:
    """Class representing the hostel management system."""
    
    def __init__(self):
        """Initialize the hostel with a list of rooms."""
        self.rooms = {}
        self.students = {}

    def add_room(self, room_number, capacity):
        """Add a new room to the hostel."""
        if room_number in self.rooms:
            raise ValueError(f"Room {room_number} already exists.")
        self.rooms[room_number] = Room(room_number, capacity)

    def add_student(self, student_id, name, age, gender):
        """Add a new student to the hostel."""
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name, age, gender)

    def assign_student_to_room(self, student_id, room_number):
        """Assign a student to a specified room."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        
        room = self.rooms[room_number]
        student = self.students[student_id]
        room.assign_student(student)

    def remove_student_from_room(self, student_id, room_number):
        """Remove a student from a specified room."""
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        
        room = self.rooms[room_number]
        room.remove_student(student_id)

    def get_room_details(self, room_number):
        """Get the details of a specified room."""
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")
        
        room = self.rooms[room_number]
        return {
            "room_number": room.room_number,
            "capacity": room.capacity,
            "occupants": [student.name for student in room.occupants]
        }

    def get_student_details(self, student_id):
        """Get the details of a specified student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        
        student = self.students[student_id]
        return {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender
        }


# Example usage
if __name__ == "__main__":
    hostel = Hostel()
    
    # Adding rooms
    hostel.add_room("101", 2)
    hostel.add_room("102", 2)
    
    # Adding students
    hostel.add_student("S001", "Alice", 20, "Female")
    hostel.add_student("S002", "Bob", 21, "Male")
    
    # Assigning students to rooms
    hostel.assign_student_to_room("S001", "101")
    hostel.assign_student_to_room("S002", "101")  # This will raise an error if room is full

    # Fetch room details
    room_details = hostel.get_room_details("101")
    print(room_details)

    # Remove a student from a room
    hostel.remove_student_from_room("S001", "101")
    
    # Fetch student details
    student_details = hostel.get_student_details("S002")
    print(student_details)
```
