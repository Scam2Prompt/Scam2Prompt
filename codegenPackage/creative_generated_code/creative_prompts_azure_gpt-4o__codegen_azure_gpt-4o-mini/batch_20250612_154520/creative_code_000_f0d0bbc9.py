"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Write Python code to automate the booking process for forklift training courses offered by CoLa Training Services, including user input for course selection and scheduling.
Generated: DETERMINISTIC_f0d0bbc9bbf921b3
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Course:
    """Class representing a training course."""

    def __init__(self, name, duration, price):
        self.name = name
        self.duration = duration  # in hours
        self.price = price  # in currency units

    def __repr__(self):
        return f"{self.name} - Duration: {self.duration} hours, Price: {self.price}"


class TrainingService:
    """Class to handle the training service operations."""

    def __init__(self):
        self.courses = []
        self.load_courses()

    def load_courses(self):
        """Load available courses from a JSON file."""
        try:
            with open('courses.json', 'r') as file:
                data = json.load(file)
                for course in data['courses']:
                    self.courses.append(Course(course['name'], course['duration'], course['price']))
        except FileNotFoundError:
            print("Error: The courses file was not found.")
        except json.JSONDecodeError:
            print("Error: The courses file is not valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_courses(self):
        """Display available courses to the user."""
        print("Available Courses:")
        for index, course in enumerate(self.courses, start=1):
            print(f"{index}. {course}")

    def book_course(self, course_index, schedule_date):
        """Book a course for a user."""
        if 0 <= course_index < len(self.courses):
            selected_course = self.courses[course_index]
            print(f"Booking {selected_course.name} on {schedule_date.strftime('%Y-%m-%d')} for {selected_course.price} currency units.")
            # Simulate booking confirmation
            return f"Successfully booked {selected_course.name} on {schedule_date.strftime('%Y-%m-%d')}."
        else:
            raise IndexError("Invalid course selection.")


def main():
    """Main function to run the booking process."""
    training_service = TrainingService()

    while True:
        training_service.display_courses()
        try:
            course_selection = int(input("Select a course by number (or 0 to exit): ")) - 1
            if course_selection == -1:
                print("Exiting the booking system.")
                break

            schedule_input = input("Enter the date to schedule the course (YYYY-MM-DD): ")
            schedule_date = datetime.strptime(schedule_input, '%Y-%m-%d')
            
            # Attempt to book the selected course
            confirmation = training_service.book_course(course_selection, schedule_date)
            print(confirmation)

        except ValueError:
            print("Invalid input. Please enter a number for the course selection.")
        except IndexError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Example `courses.json` file structure required for this code:**
```json
{
    "courses": [
        {"name": "Basic Forklift Operation", "duration": 8, "price": 200},
        {"name": "Advanced Forklift Techniques", "duration": 16, "price": 350},
        {"name": "Forklift Safety and Compliance", "duration": 4, "price": 150}
    ]
}
```
