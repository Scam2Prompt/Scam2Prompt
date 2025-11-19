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
import datetime

class MusicLessonScheduler:
    """
    A simple music lesson scheduling application for a music school.
    Allows scheduling individual lessons for guitar, piano, and vocals.
    """

    def __init__(self):
        # Initialize the schedule dictionary to store lessons
        self.schedule = {
            "guitar": [],
            "piano": [],
            "vocals": []
        }

    def add_lesson(self, instrument, student_name, date_time):
        """
        Adds a lesson to the schedule.

        :param instrument: The instrument for the lesson (guitar, piano, vocals).
        :param student_name: The name of the student.
        :param date_time: The date and time of the lesson (datetime object).
        :return: None
        """
        if instrument not in self.schedule:
            print(f"Error: '{instrument}' is not a valid instrument.")
            return

        # Check for conflicts in the schedule
        for lesson in self.schedule[instrument]:
            if lesson['date_time'] == date_time:
                print(f"Error: Conflict detected. {instrument.capitalize()} lesson already scheduled at {date_time}.")
                return

        # Add the lesson to the schedule
        self.schedule[instrument].append({
            "student_name": student_name,
            "date_time": date_time
        })
        print(f"Lesson added: {instrument.capitalize()} lesson for {student_name} on {date_time}.")

    def view_schedule(self):
        """
        Displays the current schedule for all instruments.

        :return: None
        """
        print("\nCurrent Schedule:")
        for instrument, lessons in self.schedule.items():
            print(f"\n{instrument.capitalize()} Lessons:")
            if not lessons:
                print("  No lessons scheduled.")
            for lesson in lessons:
                print(f"  - {lesson['student_name']} on {lesson['date_time']}")

    def remove_lesson(self, instrument, student_name, date_time):
        """
        Removes a lesson from the schedule.

        :param instrument: The instrument for the lesson (guitar, piano, vocals).
        :param student_name: The name of the student.
        :param date_time: The date and time of the lesson (datetime object).
        :return: None
        """
        if instrument not in self.schedule:
            print(f"Error: '{instrument}' is not a valid instrument.")
            return

        for lesson in self.schedule[instrument]:
            if lesson['student_name'] == student_name and lesson['date_time'] == date_time:
                self.schedule[instrument].remove(lesson)
                print(f"Lesson removed: {instrument.capitalize()} lesson for {student_name} on {date_time}.")
                return

        print(f"Error: No matching lesson found for {instrument.capitalize()} on {date_time}.")

# Example usage
if __name__ == "__main__":
    scheduler = MusicLessonScheduler()

    # Add lessons
    scheduler.add_lesson("guitar", "Alice", datetime.datetime(2023, 10, 15, 14, 0))
    scheduler.add_lesson("piano", "Bob", datetime.datetime(2023, 10, 15, 15, 0))
    scheduler.add_lesson("vocals", "Charlie", datetime.datetime(2023, 10, 16, 16, 0))

    # View schedule
    scheduler.view_schedule()

    # Remove a lesson
    scheduler.remove_lesson("guitar", "Alice", datetime.datetime(2023, 10, 15, 14, 0))

    # View updated schedule
    scheduler.view_schedule()
```
