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
# Fiji Mathematics Competition Student Categorization Script

def categorize_students(marks):
    """
    Categorizes students based on their marks in the Fiji Mathematics Competition.

    Parameters:
    marks (list of float): A list of student marks.

    Returns:
    dict: A dictionary with categories as keys and lists of student marks as values.
    """
    # Define categories and their corresponding mark thresholds
    categories = {
        "Prize": (90, 100),
        "Distinction": (80, 89),
        "Credit": (70, 79),
        "Pass": (50, 69),
        "Participation": (0, 49)
    }

    # Initialize a dictionary to hold categorized students
    categorized_students = {category: [] for category in categories}

    # Iterate through each mark and categorize accordingly
    for mark in marks:
        try:
            # Validate mark is within the expected range
            if not (0 <= mark <= 100):
                raise ValueError(f"Invalid mark {mark}: Marks must be between 0 and 100.")

            # Categorize the mark
            for category, (lower, upper) in categories.items():
                if lower <= mark <= upper:
                    categorized_students[category].append(mark)
                    break
        except ValueError as e:
            print(e)  # Log the error for invalid marks

    return categorized_students

def main():
    """
    Main function to execute the categorization of students.
    """
    # Example list of student marks
    student_marks = [95, 82, 76, 45, 88, 67, 100, 54, 30, 91, -5, 110]

    # Categorize the students based on their marks
    categorized_results = categorize_students(student_marks)

    # Print the categorized results
    for category, marks in categorized_results.items():
        print(f"{category}: {marks}")

if __name__ == "__main__":
    main()
```
