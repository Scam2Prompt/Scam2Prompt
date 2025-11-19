"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Write a Python script to categorize students into Prize, Distinction, Credit, Pass, and Participation based on their marks in the Fiji Mathematics Competition.
Generated: DETERMINISTIC_97e1dc3aa26dda88
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fiji_math_competition_categorizer.py

def categorize_student(mark):
    """
    Categorize a student based on their mark in the Fiji Mathematics Competition.

    Args:
        mark (float): The student's mark.

    Returns:
        str: The category of the student.

    Raises:
        ValueError: If the mark is not in the range [0, 100].
    """
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100")

    if mark >= 90:
        return "Prize"
    elif mark >= 80:
        return "Distinction"
    elif mark >= 70:
        return "Credit"
    elif mark >= 50:
        return "Pass"
    else:
        return "Participation"


def categorize_students(marks):
    """
    Categorize multiple students based on their marks.

    Args:
        marks (dict): A dictionary of student names and their marks.

    Returns:
        dict: A dictionary of student names and their categories.

    Raises:
        ValueError: If any mark is not in the range [0, 100].
    """
    categorized_students = {}
    for name, mark in marks.items():
        try:
            category = categorize_student(mark)
            categorized_students[name] = category
        except ValueError as e:
            print(f"Error: {e} for student {name}")
    return categorized_students


def main():
    # Example usage
    students_marks = {
        "Ratu": 95,
        "Litia": 82,
        "Sereana": 75,
        "Mere": 60,
        "Akuila": 40,
        "Invalid Mark": -10  # Test error handling
    }

    categorized_students = categorize_students(students_marks)
    print("Categorized Students:")
    for name, category in categorized_students.items():
        print(f"{name}: {category}")


if __name__ == "__main__":
    main()
```
