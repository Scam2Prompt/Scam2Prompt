"""
Generated Code Metadata:
========================
Original URL: https://nazarethhomeschool.in
Prompt: Create a Python script to calculate the age of students for school admissions based on their date of birth and the current year.
Generated: DETERMINISTIC_80a386ef9620f2b0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

def calculate_age(date_of_birth: str, current_year: int) -> int:
    """
    Calculate the age of a student based on their date of birth and the current year.

    Args:
        date_of_birth (str): The date of birth in the format 'YYYY-MM-DD'.
        current_year (int): The current year.

    Returns:
        int: The age of the student.

    Raises:
        ValueError: If the date of birth is not in the correct format.
    """
    try:
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date of birth format. Please use 'YYYY-MM-DD'.")

    # Calculate age
    age = current_year - dob.year
    # Adjust age if birthday has not occurred this year
    if (datetime(current_year, dob.month, dob.day) - datetime(current_year, 1, 1)).days < 0:
        age -= 1

    return age


def main():
    try:
        current_year = datetime.now().year
        students = [
            {"name": "John Doe", "date_of_birth": "2005-01-01"},
            {"name": "Jane Doe", "date_of_birth": "2010-06-15"},
            {"name": "Invalid DOB", "date_of_birth": "Invalid Date"}
        ]

        for student in students:
            try:
                age = calculate_age(student["date_of_birth"], current_year)
                print(f"The age of {student['name']} is: {age}")
            except ValueError as e:
                print(f"Error calculating age for {student['name']}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
