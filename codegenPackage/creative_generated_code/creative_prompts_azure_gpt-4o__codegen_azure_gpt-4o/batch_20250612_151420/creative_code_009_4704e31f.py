"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Create a script to calculate scholarship eligibility for SC/ST/OBC students enrolling in physiotherapy courses, referencing the scholarship schemes mentioned on Ayushman College's website.
Generated: DETERMINISTIC_4704e31fe6b06f14
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

# Define the scholarship criteria
SCHOLARSHIP_CRITERIA = {
    "SC": {"min_grade": 60, "max_income": 250000},
    "ST": {"min_grade": 55, "max_income": 250000},
    "OBC": {"min_grade": 65, "max_income": 300000}
}

def load_student_data(file_path):
    """
    Load student data from a JSON file.
    :param file_path: Path to the JSON file containing student data.
    :return: List of student records.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {file_path}")
        sys.exit(1)

def is_eligible_for_scholarship(category, grade, family_income):
    """
    Check if a student is eligible for a scholarship.
    :param category: Student's category (SC, ST, OBC).
    :param grade: Student's grade percentage.
    :param family_income: Student's family annual income.
    :return: Boolean indicating eligibility.
    """
    criteria = SCHOLARSHIP_CRITERIA.get(category.upper())
    if not criteria:
        return False

    # Check grade and income against criteria
    return grade >= criteria["min_grade"] and family_income <= criteria["max_income"]

def calculate_scholarship_eligibility(student_data):
    """
    Calculate scholarship eligibility for a list of students.
    :param student_data: List of student records.
    :return: A list of results indicating scholarship eligibility for each student.
    """
    eligibility_results = []

    for student in student_data:
        try:
            name = student["name"]
            category = student["category"]
            grade = student["grade"]
            family_income = student["family_income"]

            if not isinstance(grade, (int, float)) or not isinstance(family_income, (int, float)):
                raise ValueError("Grade and family income must be numeric.")

            eligibility = is_eligible_for_scholarship(category, grade, family_income)
            eligibility_results.append({"name": name, "eligible": eligibility})
        except KeyError as e:
            print(f"Error: Missing required field {e} in student record.")
        except ValueError as e:
            print(f"Error: {e} for student {student.get('name', 'Unknown')}.")

    return eligibility_results

def main():
    # Path to the JSON file containing student data
    student_data_file = "students.json"

    # Load student data
    students = load_student_data(student_data_file)

    # Calculate eligibility
    results = calculate_scholarship_eligibility(students)

    # Print results
    print("Scholarship Eligibility Results:")
    for result in results:
        name = result["name"]
        eligible = "Eligible" if result["eligible"] else "Not Eligible"
        print(f"{name}: {eligible}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure the JSON file (`students.json`) is properly formatted and contains an array of student records, e.g.:
   ```json
   [
       {"name": "Alice", "category": "SC", "grade": 62, "family_income": 240000},
       {"name": "Bob", "category": "OBC", "grade": 70, "family_income": 310000}
   ]
   ```
2. Update the file path (`student_data_file`) in the script if needed.
