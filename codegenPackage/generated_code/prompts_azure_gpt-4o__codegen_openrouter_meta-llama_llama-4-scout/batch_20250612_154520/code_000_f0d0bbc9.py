"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write Python code to automate the booking process for forklift training courses offered by CoLa Training Services, including user input for course selection and scheduling.
Generated: DETERMINISTIC_f0d0bbc9bbf921b3
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class Course:
    """Represents a forklift training course."""
    def __init__(self, name, duration, dates):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            duration (int): The duration of the course in days.
            dates (list): A list of available dates for the course.
        """
        self.name = name
        self.duration = duration
        self.dates = dates

class BookingSystem:
    """Manages course bookings for CoLa Training Services."""
    def __init__(self):
        """Initializes the booking system with available courses."""
        self.courses = {
            "1": Course("Forklift Operator Training", 1, ["2024-09-16", "2024-09-23", "2024-09-30"]),
            "2": Course("Forklift Safety and Operations", 2, ["2024-09-17", "2024-09-24", "2024-10-01"]),
            "3": Course("Advanced Forklift Training", 3, ["2024-09-18", "2024-09-25", "2024-10-02"]),
        }

    def display_courses(self):
        """Displays available courses."""
        print("Available Courses:")
        for key, course in self.courses.items():
            print(f"{key}. {course.name} ({course.duration} day(s))")

    def get_user_course_choice(self):
        """Gets the user's course choice."""
        while True:
            self.display_courses()
            choice = input("Please select a course (enter the course number): ")
            if choice in self.courses:
                return self.courses[choice]
            else:
                print("Invalid course choice. Please try again.")

    def get_user_schedule_choice(self, course):
        """Gets the user's schedule choice for the selected course."""
        print(f"\nAvailable dates for {course.name}:")
        for i, date in enumerate(course.dates):
            print(f"{i + 1}. {date}")

        while True:
            try:
                choice = int(input("Please select a date (enter the date number): "))
                if 1 <= choice <= len(course.dates):
                    return course.dates[choice - 1]
                else:
                    print("Invalid date choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def book_course(self):
        """Books a course for the user."""
        try:
            course = self.get_user_course_choice()
            date = self.get_user_schedule_choice(course)
            print(f"\nYou have booked {course.name} on {date}.")
            confirmation = input("Is this correct? (yes/no): ")
            if confirmation.lower() == "yes":
                print("Booking confirmed.")
            else:
                print("Booking cancelled.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    booking_system = BookingSystem()
    while True:
        booking_system.book_course()
        cont = input("\nDo you want to book another course? (yes/no): ")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    main()
```
