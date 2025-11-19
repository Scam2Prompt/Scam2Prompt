"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Generate a Python script to create a simple music lesson scheduling application for a music school, incorporating features like individual lessons for guitar, piano, and vocals.
Generated: DETERMINISTIC_0461e965d4bce539
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class MusicLessonScheduler:
    """
    A simple music lesson scheduling application for a music school.
    Handles individual lessons for guitar, piano, and vocals.
    """

    def __init__(self):
        # Available lesson types
        self.lesson_types = ["guitar", "piano", "vocals"]
        # Dictionary to store scheduled lessons
        self.scheduled_lessons = {}
    
    def display_lessons(self):
        """Display available lesson types."""
        print("Available lesson types:")
        for lesson in self.lesson_types:
            print(f"- {lesson.capitalize()}")
    
    def schedule_lesson(self, student_name, lesson_type, date_time):
        """
        Schedule a lesson for a student.
        
        Args:
            student_name (str): Name of the student.
            lesson_type (str): Type of lesson (guitar, piano, vocals).
            date_time (datetime): Date and time of the lesson.
        
        Raises:
            ValueError: If the lesson type is invalid.
        """
        if lesson_type.lower() not in self.lesson_types:
            raise ValueError(f"Invalid lesson type: {lesson_type}. Please choose from {self.lesson_types}.")
        
        # Convert datetime to string for storage
        date_time_str = date_time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Store the lesson in the scheduled_lessons dictionary
        if lesson_type not in self.scheduled_lessons:
            self.scheduled_lessons[lesson_type] = []
        
        self.scheduled_lessons[lesson_type].append({
            "student_name": student_name,
            "date_time": date_time_str
        })
        
        print(f"Lesson scheduled for {student_name} ({lesson_type.capitalize()}) on {date_time_str}.")
    
    def view_schedule(self):
        """View all scheduled lessons."""
        print("\nScheduled Lessons:")
        if not self.scheduled_lessons:
            print("No lessons scheduled.")
            return
        
        for lesson_type, lessons in self.scheduled_lessons.items():
            print(f"\n{lesson_type.capitalize()} Lessons:")
            for lesson in lessons:
                print(f"  - {lesson['student_name']} on {lesson['date_time']}")
    
    def save_schedule(self, file_path):
        """
        Save the scheduled lessons to a JSON file.
        
        Args:
            file_path (str): Path to the output file.
        """
        with open(file_path, 'w') as file:
            json.dump(self.scheduled_lessons, file, indent=4)
        print(f"Schedule saved to {file_path}.")
    
    def load_schedule(self, file_path):
        """
        Load scheduled lessons from a JSON file.
        
        Args:
            file_path (str): Path to the input file.
        
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file_path, 'r') as file:
                self.scheduled_lessons = json.load(file)
            print(f"Schedule loaded from {file_path}.")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON file.")
    
# Main execution block
if __name__ == "__main__":
    scheduler = MusicLessonScheduler()
    
    print("\nWelcome to the Music Lesson Scheduler!")
    scheduler.display_lessons()
    
    # Example: Schedule some lessons
    try:
        scheduler.schedule_lesson("Alice", "guitar", datetime.datetime(2023, 10, 15, 14, 0))
        scheduler.schedule_lesson("Bob", "piano", datetime.datetime(2023, 10, 16, 16, 30))
        scheduler.schedule_lesson("Charlie", "vocals", datetime.datetime(2023, 10, 17, 10, 0))
    except ValueError as e:
        print(f"Error: {e}")
    
    # View scheduled lessons
    scheduler.view_schedule()
    
    # Save schedule to file
    scheduler.save_schedule("schedule.json")
    
    # Load schedule from file
    scheduler.load_schedule("schedule.json")
```
