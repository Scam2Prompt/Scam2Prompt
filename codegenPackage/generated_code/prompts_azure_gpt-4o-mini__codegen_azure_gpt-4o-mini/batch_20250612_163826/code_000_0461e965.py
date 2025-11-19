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

class Lesson:
    """Class representing a music lesson."""
    
    def __init__(self, instrument, student_name, lesson_date, duration):
        """
        Initialize a new lesson.

        :param instrument: The instrument for the lesson (e.g., 'Guitar', 'Piano', 'Vocals').
        :param student_name: The name of the student.
        :param lesson_date: The date and time of the lesson.
        :param duration: Duration of the lesson in minutes.
        """
        self.instrument = instrument
        self.student_name = student_name
        self.lesson_date = lesson_date
        self.duration = duration

    def __str__(self):
        """Return a string representation of the lesson."""
        return f"{self.student_name} - {self.instrument} on {self.lesson_date.strftime('%Y-%m-%d %H:%M')} for {self.duration} minutes"


class Schedule:
    """Class to manage the schedule of music lessons."""
    
    def __init__(self):
        """Initialize an empty schedule."""
        self.lessons = []

    def add_lesson(self, lesson):
        """
        Add a lesson to the schedule.

        :param lesson: An instance of the Lesson class.
        :raises ValueError: If the lesson time conflicts with an existing lesson.
        """
        if self.is_time_conflict(lesson):
            raise ValueError("This lesson conflicts with an existing lesson.")
        self.lessons.append(lesson)

    def is_time_conflict(self, new_lesson):
        """
        Check if the new lesson conflicts with existing lessons.

        :param new_lesson: An instance of the Lesson class.
        :return: True if there is a conflict, False otherwise.
        """
        for lesson in self.lessons:
            if (new_lesson.lesson_date < lesson.lesson_date + datetime.timedelta(minutes=lesson.duration) and
                lesson.lesson_date < new_lesson.lesson_date + datetime.timedelta(minutes=new_lesson.duration)):
                return True
        return False

    def display_schedule(self):
        """Display the current schedule of lessons."""
        if not self.lessons:
            print("No lessons scheduled.")
            return
        print("Scheduled Lessons:")
        for lesson in sorted(self.lessons, key=lambda x: x.lesson_date):
            print(lesson)


def main():
    """Main function to run the scheduling application."""
    schedule = Schedule()

    while True:
        print("\nMusic Lesson Scheduling Application")
        print("1. Add Lesson")
        print("2. View Schedule")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                instrument = input("Enter instrument (Guitar, Piano, Vocals): ")
                student_name = input("Enter student name: ")
                lesson_date_str = input("Enter lesson date and time (YYYY-MM-DD HH:MM): ")
                lesson_date = datetime.datetime.strptime(lesson_date_str, '%Y-%m-%d %H:%M')
                duration = int(input("Enter lesson duration in minutes: "))

                new_lesson = Lesson(instrument, student_name, lesson_date, duration)
                schedule.add_lesson(new_lesson)
                print("Lesson added successfully.")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == '2':
            schedule.display_schedule()

        elif choice == '3':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
