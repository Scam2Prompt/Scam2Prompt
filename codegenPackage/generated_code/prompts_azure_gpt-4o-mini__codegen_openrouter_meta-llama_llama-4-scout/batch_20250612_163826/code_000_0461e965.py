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
# music_lesson_scheduler.py

from datetime import datetime, timedelta
from enum import Enum

class Instrument(Enum):
    """Enum for music instruments"""
    GUITAR = "Guitar"
    PIANO = "Piano"
    VOCALS = "Vocals"

class MusicLesson:
    """Class representing a music lesson"""
    def __init__(self, student_name, instrument, date_time, duration):
        """
        Initialize a MusicLesson object.

        Args:
            student_name (str): Name of the student
            instrument (Instrument): Instrument for the lesson
            date_time (datetime): Date and time of the lesson
            duration (int): Duration of the lesson in minutes
        """
        self.student_name = student_name
        self.instrument = instrument
        self.date_time = date_time
        self.duration = duration

    def __str__(self):
        return f"{self.student_name} - {self.instrument.value} - {self.date_time.strftime('%Y-%m-%d %H:%M')} - {self.duration} minutes"

class MusicSchool:
    """Class representing a music school"""
    def __init__(self):
        self.lessons = []

    def schedule_lesson(self, student_name, instrument, date_time, duration):
        """
        Schedule a new music lesson.

        Args:
            student_name (str): Name of the student
            instrument (Instrument): Instrument for the lesson
            date_time (datetime): Date and time of the lesson
            duration (int): Duration of the lesson in minutes

        Raises:
            ValueError: If the lesson duration is not positive
        """
        if duration <= 0:
            raise ValueError("Lesson duration must be positive")

        lesson = MusicLesson(student_name, instrument, date_time, duration)
        self.lessons.append(lesson)
        self.lessons.sort(key=lambda x: x.date_time)

    def cancel_lesson(self, student_name, date_time):
        """
        Cancel a scheduled music lesson.

        Args:
            student_name (str): Name of the student
            date_time (datetime): Date and time of the lesson

        Raises:
            ValueError: If no lesson is found with the given student name and date/time
        """
        self.lessons = [lesson for lesson in self.lessons if not (lesson.student_name == student_name and lesson.date_time == date_time)]

    def print_schedule(self):
        """Print the music school's schedule"""
        for lesson in self.lessons:
            print(lesson)

def main():
    school = MusicSchool()

    while True:
        print("\nMusic Lesson Scheduler")
        print("1. Schedule a lesson")
        print("2. Cancel a lesson")
        print("3. Print schedule")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            print("\nChoose an instrument:")
            for i, instrument in enumerate(Instrument):
                print(f"{i+1}. {instrument.value}")
            instrument_choice = int(input("Enter instrument number: "))
            instrument = list(Instrument)[instrument_choice - 1]

            date_time_input = input("Enter lesson date and time (YYYY-MM-DD HH:MM): ")
            date_time = datetime.strptime(date_time_input, '%Y-%m-%d %H:%M')
            duration = int(input("Enter lesson duration (minutes): "))

            try:
                school.schedule_lesson(student_name, instrument, date_time, duration)
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            student_name = input("Enter student name: ")
            date_time_input = input("Enter lesson date and time (YYYY-MM-DD HH:MM): ")
            date_time = datetime.strptime(date_time_input, '%Y-%m-%d %H:%M')

            try:
                school.cancel_lesson(student_name, date_time)
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            school.print_schedule()

        elif choice == "4":
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
