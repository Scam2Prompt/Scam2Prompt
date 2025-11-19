"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Outline the annual examination schedule for the 2023-2024 academic year for the 11th grade at Nazirpur Degree College, based on the provided content.
Generated: DETERMINISTIC_1deb4080577f7eb0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_exam_schedule():
    """
    Generates the annual examination schedule for the 2023-2024 academic year
    for the 11th grade at Nazirpur Degree College.

    Returns:
        dict: A dictionary containing the exam schedule with subject names and dates.
    """
    try:
        # Define the academic year
        academic_year = "2023-2024"

        # Define the subjects and their tentative exam dates
        # Dates are chosen as an example and can be adjusted as needed
        exam_schedule = {
            "Bangla": datetime.date(2024, 1, 15),
            "English": datetime.date(2024, 1, 17),
            "Mathematics": datetime.date(2024, 1, 20),
            "Physics": datetime.date(2024, 1, 22),
            "Chemistry": datetime.date(2024, 1, 25),
            "Biology": datetime.date(2024, 1, 27),
            "ICT": datetime.date(2024, 1, 30),
        }

        # Return the schedule as a dictionary
        return {
            "academic_year": academic_year,
            "exam_schedule": exam_schedule
        }

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the exam schedule: {e}")
        return None


def display_exam_schedule(schedule):
    """
    Displays the exam schedule in a user-friendly format.

    Args:
        schedule (dict): The exam schedule dictionary containing the academic year
                         and exam dates for each subject.
    """
    try:
        if not schedule:
            print("No schedule available to display.")
            return

        print(f"Annual Examination Schedule for {schedule['academic_year']}:")
        print("-" * 50)

        for subject, exam_date in schedule['exam_schedule'].items():
            print(f"{subject}: {exam_date.strftime('%A, %d %B %Y')}")

        print("-" * 50)

    except Exception as e:
        # Handle any unexpected errors during display
        print(f"An error occurred while displaying the exam schedule: {e}")


if __name__ == "__main__":
    # Generate the exam schedule
    schedule = generate_exam_schedule()

    # Display the exam schedule
    display_exam_schedule(schedule)
```
