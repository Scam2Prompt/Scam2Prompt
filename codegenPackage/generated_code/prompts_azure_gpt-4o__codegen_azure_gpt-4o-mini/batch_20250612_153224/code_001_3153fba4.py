"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Develop a module for automated timetable generation for schools, incorporating the functionality outlined in Him Saral's Time-Table Management System.
Generated: DETERMINISTIC_3153fba40ce8a57b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class TimetableGenerator:
    def __init__(self, subjects: List[str], teachers: List[str], rooms: List[str], time_slots: List[str]):
        """
        Initializes the TimetableGenerator with subjects, teachers, rooms, and time slots.

        :param subjects: List of subjects to be scheduled.
        :param teachers: List of teachers available for the subjects.
        :param rooms: List of rooms available for classes.
        :param time_slots: List of time slots for scheduling classes.
        """
        self.subjects = subjects
        self.teachers = teachers
        self.rooms = rooms
        self.time_slots = time_slots
        self.timetable = {}

    def generate_timetable(self) -> Dict[str, List[Tuple[str, str, str]]]:
        """
        Generates a timetable by randomly assigning subjects to time slots, teachers, and rooms.

        :return: A dictionary representing the timetable.
        """
        for time_slot in self.time_slots:
            self.timetable[time_slot] = []
            for subject in self.subjects:
                teacher = self.assign_teacher(subject)
                room = self.assign_room()
                self.timetable[time_slot].append((subject, teacher, room))
        return self.timetable

    def assign_teacher(self, subject: str) -> str:
        """
        Assigns a teacher to a subject randomly.

        :param subject: The subject for which a teacher is to be assigned.
        :return: A randomly selected teacher for the subject.
        """
        if not self.teachers:
            raise ValueError("No teachers available to assign.")
        return random.choice(self.teachers)

    def assign_room(self) -> str:
        """
        Assigns a room randomly.

        :return: A randomly selected room.
        """
        if not self.rooms:
            raise ValueError("No rooms available to assign.")
        return random.choice(self.rooms)

    def display_timetable(self) -> None:
        """
        Displays the generated timetable in a readable format.
        """
        for time_slot, classes in self.timetable.items():
            print(f"{time_slot}:")
            for subject, teacher, room in classes:
                print(f"  Subject: {subject}, Teacher: {teacher}, Room: {room}")
            print()

# Example usage
if __name__ == "__main__":
    subjects = ["Math", "Science", "History", "Art"]
    teachers = ["Mr. Smith", "Ms. Johnson", "Mrs. Brown"]
    rooms = ["Room 101", "Room 102", "Room 103"]
    time_slots = ["9:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM"]

    try:
        timetable_generator = TimetableGenerator(subjects, teachers, rooms, time_slots)
        timetable = timetable_generator.generate_timetable()
        timetable_generator.display_timetable()
    except ValueError as e:
        print(f"Error: {e}")
```
