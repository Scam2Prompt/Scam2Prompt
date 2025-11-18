"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Develop a Python script to analyze student enrollment data for Ânima's courses, categorizing them into "basic," "advanced," and "specialized" levels.
Generated: DETERMINISTIC_9867e672b4be48c7
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict

def categorize_courses(course_name):
    """
    Categorize courses based on their names.
    :param course_name: Name of the course
    :return: Category of the course: 'basic', 'advanced', or 'specialized'
    """
    course_name = course_name.lower()
    if "intro" in course_name or "fundamentals" in course_name or "basic" in course_name:
        return "basic"
    elif "advanced" in course_name or "pro" in course_name or "expert" in course_name:
        return "advanced"
    elif "specialized" in course_name or "specific" in course_name:
        return "specialized"
    else:
        return "uncategorized"  # Default category if no match is found


def analyze_enrollment_data(file_path):
    """
    Analyze student enrollment data and categorize courses.
    :param file_path: Path to the CSV file containing enrollment data
    """
    try:
        # Dictionary to store categorized data
        categorized_data = defaultdict(list)

        # Open the CSV file and read its content
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Check if required columns exist
            if 'Course Name' not in reader.fieldnames or 'Student Name' not in reader.fieldnames:
                raise ValueError("CSV file must contain 'Course Name' and 'Student Name' columns.")

            # Process each row in the file
            for row in reader:
                course_name = row['Course Name']
                student_name = row['Student Name']
                category = categorize_courses(course_name)
                categorized_data[category].append({"course_name": course_name, "student_name": student_name})

        # Print the categorized data
        for category, entries in categorized_data.items():
            print(f"Category: {category.capitalize()} ({len(entries)} courses)")
            for entry in entries:
                print(f"  Course: {entry['course_name']} | Student: {entry['student_name']}")
            print()

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Input file path (modify this path to point to your CSV file)
    file_path = "enrollment_data.csv"

    print("Analyzing student enrollment data...\n")
    analyze_enrollment_data(file_path)
```
