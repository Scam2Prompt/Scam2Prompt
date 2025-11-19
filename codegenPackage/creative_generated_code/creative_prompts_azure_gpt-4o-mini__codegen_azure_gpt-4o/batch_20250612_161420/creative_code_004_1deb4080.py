"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Outline the annual examination schedule for the 2023-2024 academic year for the 11th grade at Nazirpur Degree College, based on the provided content.
Generated: DETERMINISTIC_1deb4080577f7eb0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_exam_schedule():
    """
    Generate the annual examination schedule for the 2023-2024 academic year for 11th grade at Nazirpur Degree College.
    
    Returns:
        dict: A dictionary containing exam names as keys and their respective dates as values.
    """
    try:
        # Define the academic year start and end dates
        academic_year_start = datetime.date(2023, 6, 1)  # June 1, 2023
        academic_year_end = datetime.date(2024, 5, 31)   # May 31, 2024

        # Define examination names and their tentative months
        examinations = {
            "Midterm Examination": datetime.date(2023, 9, 15),  # Mid-September
            "Annual Examination": datetime.date(2024, 4, 10),  # Early April
            "Pre-Test Examination": datetime.date(2024, 2, 15),  # Mid-February
        }

        # Validate exam dates to ensure they fit within the academic year
        for exam_name, exam_date in examinations.items():
            if not (academic_year_start <= exam_date <= academic_year_end):
                raise ValueError(f"The date for {exam_name} ({exam_date}) is outside the academic year range.")

        return examinations

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"Error generating exam schedule: {e}")
        return None


def display_exam_schedule(schedule):
    """
    Display the exam schedule in a user-friendly format.

    Args:
        schedule (dict): The exam schedule to display.
    """
    if not schedule:
        print("No exam schedule available.")
        return

    print("Nazirpur Degree College - 11th Grade Examination Schedule (2023-2024):")
    print("-------------------------------------------------------------")
    for exam_name, exam_date in schedule.items():
        print(f"{exam_name}: {exam_date.strftime('%B %d, %Y')}")  # Format date for better readability


# Main execution
if __name__ == "__main__":
    # Generate the exam schedule
    exam_schedule = generate_exam_schedule()
    
    # Display the exam schedule if successfully generated
    display_exam_schedule(exam_schedule)
```
