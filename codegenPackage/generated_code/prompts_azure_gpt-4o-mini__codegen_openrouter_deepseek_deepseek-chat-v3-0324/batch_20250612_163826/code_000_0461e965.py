"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Generate a Python script to create a simple music lesson scheduling application for a music school, incorporating features like individual lessons for guitar, piano, and vocals.
Generated: DETERMINISTIC_0461e965d4bce539
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from enum import Enum
import os

class Instrument(Enum):
    """Enum representing available instruments for lessons."""
    GUITAR = "Guitar"
    PIANO = "Piano"
    VOCALS = "Vocals"

class Lesson:
    """Represents a music lesson with student, instrument, and time details."""
    
    def __init__(self, student_name: str, instrument: Instrument, start_time: datetime, duration: int):
        """
        Initialize a Lesson object.
        
        Args:
            student_name: Name of the student.
            instrument: Instrument for the lesson.
            start_time: Start time of the lesson.
            duration: Duration of the lesson in minutes.
        """
        self.student_name = student_name
        self.instrument = instrument
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + timedelta(minutes=duration)
    
    def to_dict(self) -> dict:
        """Convert Lesson object to dictionary for serialization."""
        return {
            "student_name": self.student_name,
            "instrument": self.instrument.value,
            "start_time": self.start_time.isoformat(),
            "duration": self.duration
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Lesson':
        """Create Lesson object from dictionary."""
        return cls(
            student_name=data["student_name"],
            instrument=Instrument(data["instrument"]),
            start_time=datetime.fromisoformat(data["start_time"]),
            duration=data["duration"]
        )

class MusicSchoolScheduler:
    """Handles scheduling and management of music lessons."""
    
    def __init__(self, storage_file: str = "lessons.json"):
        """
        Initialize the scheduler.
        
        Args:
            storage_file: JSON file to store lessons data.
        """
        self.storage_file = storage_file
        self.lessons = []
        self._load_lessons()
    
    def _load_lessons(self):
        """Load lessons from the storage file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.lessons = [Lesson.from_dict(item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading lessons: {e}")
            self.lessons = []
    
    def _save_lessons(self):
        """Save lessons to the storage file."""
        try:
            with open(self.storage_file, "w") as f:
                json.dump([lesson.to_dict() for lesson in self.lessons], f, indent=2)
        except IOError as e:
            print(f"Error saving lessons: {e}")
    
    def add_lesson(self, student_name: str, instrument: Instrument, 
                   start_time: datetime, duration: int) -> bool:
        """
        Add a new lesson to the schedule.
        
        Args:
            student_name: Name of the student.
            instrument: Instrument for the lesson.
            start_time: Start time of the lesson.
            duration: Duration in minutes.
            
        Returns:
            bool: True if lesson was added successfully, False otherwise.
        """
        new_lesson = Lesson(student_name, instrument, start_time, duration)
        
        # Check for scheduling conflicts
        for lesson in self.lessons:
            if (new_lesson.start_time < lesson.end_time and 
                new_lesson.end_time > lesson.start_time):
                print("Error: Schedule conflict detected.")
                return False
        
        self.lessons.append(new_lesson)
        self._save_lessons()
        return True
    
    def get_lessons_by_student(self, student_name: str) -> list[Lesson]:
        """Return all lessons for a given student."""
        return [lesson for lesson in self.lessons if lesson.student_name == student_name]
    
    def get_lessons_by_instrument(self, instrument: Instrument) -> list[Lesson]:
        """Return all lessons for a given instrument."""
        return [lesson for lesson in self.lessons if lesson.instrument == instrument]
    
    def get_upcoming_lessons(self, days: int = 7) -> list[Lesson]:
        """Return lessons scheduled within the next X days."""
        now = datetime.now()
        end_date = now + timedelta(days=days)
        return [lesson for lesson in self.lessons 
                if now <= lesson.start_time <= end_date]
    
    def cancel_lesson(self, student_name: str, start_time: datetime) -> bool:
        """
        Cancel a lesson.
        
        Args:
            student_name: Name of the student.
            start_time: Start time of the lesson to cancel.
            
        Returns:
            bool: True if lesson was canceled, False if not found.
        """
        for i, lesson in enumerate(self.lessons):
            if (lesson.student_name == student_name and 
                lesson.start_time == start_time):
                del self.lessons[i]
                self._save_lessons()
                return True
        return False
    
    def display_schedule(self):
        """Print the current schedule."""
        if not self.lessons:
            print("No lessons scheduled.")
            return
        
        print("\nMusic School Schedule:")
        print("-" * 40)
        for lesson in sorted(self.lessons, key=lambda x: x.start_time):
            print(f"Student: {lesson.student_name}")
            print(f"Instrument: {lesson.instrument.value}")
            print(f"Time: {lesson.start_time.strftime('%Y-%m-%d %I:%M %p')} "
                  f"to {lesson.end_time.strftime('%I:%M %p')}")
            print(f"Duration: {lesson.duration} minutes")
            print("-" * 40)

def main():
    """Main entry point for the music school scheduler."""
    scheduler = MusicSchoolScheduler()
    
    while True:
        print("\nMusic School Lesson Scheduler")
        print("1. Schedule a new lesson")
        print("2. View upcoming lessons")
        print("3. View student lessons")
        print("4. View lessons by instrument")
        print("5. Cancel a lesson")
        print("6. Display full schedule")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            try:
                student = input("Student name: ").strip()
                print("\nAvailable Instruments:")
                for i, instrument in enumerate(Instrument, 1):
                    print(f"{i}. {instrument.value}")
                instr_choice = int(input("Select instrument (1-3): ")) - 1
                instrument = list(Instrument)[instr_choice]
                
                date_str = input("Lesson date (YYYY-MM-DD): ").strip()
                time_str = input("Lesson time (HH:MM): ").strip()
                start_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
                
                duration = int(input("Duration in minutes: ").strip())
                
                if scheduler.add_lesson(student, instrument, start_time, duration):
                    print("Lesson scheduled successfully!")
                else:
                    print("Failed to schedule lesson.")
            except (ValueError, IndexError) as e:
                print(f"Invalid input: {e}")
        
        elif choice == "2":
            days = input("Show lessons for next how many days? (default 7): ").strip()
            days = int(days) if days.isdigit() else 7
            upcoming = scheduler.get_upcoming_lessons(days)
            if upcoming:
                print(f"\nUpcoming lessons (next {days} days):")
                for lesson in upcoming:
                    print(f"{lesson.student_name}: {lesson.instrument.value} "
                          f"at {lesson.start_time.strftime('%Y-%m-%d %I:%M %p')}")
            else:
                print(f"No lessons scheduled for the next {days} days.")
        
        elif choice == "3":
            student = input("Student name: ").strip()
            lessons = scheduler.get_lessons_by_student(student)
            if lessons:
                print(f"\nLessons for {student}:")
                for lesson in lessons:
                    print(f"{lesson.instrument.value}: {lesson.start_time.strftime('%Y-%m-%d %I:%M %p')}")
            else:
                print(f"No lessons found for {student}.")
        
        elif choice == "4":
            print("\nAvailable Instruments:")
            for i, instrument in enumerate(Instrument, 1):
                print(f"{i}. {instrument.value}")
            try:
                instr_choice = int(input("Select instrument (1-3): ")) - 1
                instrument = list(Instrument)[instr_choice]
                lessons = scheduler.get_lessons_by_instrument(instrument)
                if lessons:
                    print(f"\n{instrument.value} Lessons:")
                    for lesson in lessons:
                        print(f"{lesson.student_name}: {lesson.start_time.strftime('%Y-%m-%d %I:%M %p')}")
                else:
                    print(f"No {instrument.value} lessons scheduled.")
            except (ValueError, IndexError):
                print("Invalid instrument selection
