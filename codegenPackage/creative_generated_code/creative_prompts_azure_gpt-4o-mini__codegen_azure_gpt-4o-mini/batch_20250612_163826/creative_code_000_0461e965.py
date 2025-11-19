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

class Lesson:
    """Class representing a music lesson."""
    
    def __init__(self, instrument, student_name, lesson_date, duration):
        """
        Initializes a new Lesson instance.

        Args:
            instrument (str): The instrument for the lesson (guitar, piano, vocals).
            student_name (str): The name of the student.
            lesson_date (datetime): The date and time of the lesson.
            duration (int): Duration of the lesson in minutes.
        """
        self.instrument = instrument
        self.student_name = student_name
        self.lesson_date = lesson_date
        self.duration = duration

    def __str__(self):
        """String representation of the lesson."""
        return f"{self.student_name} - {self.instrument} on {self.lesson_date.strftime('%Y-%m-%d %H:%M')} for {self.duration} minutes"


class Schedule:
    """Class to manage a schedule of music lessons."""
    
    def __init__(self):
        """Initializes an empty schedule."""
        self.lessons = []

    def add_lesson(self, lesson):
        """
        Adds a lesson to the schedule.

        Args:
            lesson (Lesson): An instance of the Lesson class.

        Raises:
            ValueError: If the lesson time conflicts with an existing lesson.
        """
        if self.is_time_conflict(lesson):
            raise ValueError("The lesson time conflicts with an existing lesson.")
        self.lessons.append(lesson)

    def is_time_conflict(self, new_lesson):
        """
        Checks if a new lesson conflicts with existing lessons.

        Args:
            new_lesson (Lesson): The new lesson to check for conflicts.

        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        for lesson in self.lessons:
            if lesson.lesson_date < (new_lesson.lesson_date + datetime.timedelta(minutes=new_lesson.duration)) and \
               (new_lesson.lesson_date < (lesson.lesson_date + datetime.timedelta(minutes=lesson.duration))):
                return True
        return False

    def show_schedule(self):
        """Displays all scheduled lessons."""
        if not self.lessons:
            print("No lessons scheduled.")
            return
        for lesson in self.lessons:
            print(lesson)


def main():
    """Main function to run the scheduling application."""
    schedule = Schedule()

    print("Welcome to the Music Lesson Scheduling Application")
    
    while True:
        try:
            instrument = input("Enter the instrument (guitar, piano, vocals) or 'exit' to quit: ").strip().lower()
            if instrument == 'exit':
                break
            if instrument not in ['guitar', 'piano', 'vocals']:
                print("Invalid instrument. Please try again.")
                continue
            
            student_name = input("Enter the student's name: ").strip()
            lesson_date_str = input("Enter the lesson date and time (YYYY-MM-DD HH:MM): ")
            lesson_date = datetime.datetime.strptime(lesson_date_str, '%Y-%m-%d %H:%M')
            duration = int(input("Enter the duration of the lesson in minutes: "))
            
            lesson = Lesson(instrument, student_name, lesson_date, duration)
            schedule.add_lesson(lesson)
            print("Lesson added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("Scheduled Lessons:")
    schedule.show_schedule()


if __name__ == "__main__":
    main()
```
