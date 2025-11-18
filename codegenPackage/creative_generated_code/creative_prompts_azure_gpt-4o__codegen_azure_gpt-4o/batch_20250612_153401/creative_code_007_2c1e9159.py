"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Create a Python script to calculate the total cost for a student enrolling in multiple courses at Global Healthcare Management College, factoring in course fees and durations.
Generated: DETERMINISTIC_2c1e915993eb7647
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost of enrolling in multiple courses
at Global Healthcare Management College, factoring in course fees and durations.

Author: [Your Name]
Date: [Insert Date]
"""

# Import necessary library for input validation
import sys


def calculate_total_cost(courses):
    """
    Calculate the total cost based on the selected courses.

    Parameters:
        courses (list of dict): List of courses with fee and duration details.

    Returns:
        float: Total cost for the enrolled courses.
    """
    total_cost = 0.0
    for course in courses:
        try:
            # Extract fee and duration for each course
            fee = course.get("fee", 0)
            duration = course.get("duration", 0)

            # Validate fee and duration are positive numbers
            if fee < 0 or duration < 0:
                raise ValueError("Fee and duration must be non-negative.")

            # Add course fee to total cost
            total_cost += fee

        except ValueError as ve:
            print(f"Error processing course {course.get('name', 'Unknown')}: {ve}", file=sys.stderr)

    return total_cost


def main():
    """
    Main function to calculate total course enrollment cost.
    """
    # Mock data: List of courses offered by the college
    available_courses = [
        {"name": "Healthcare Management Basics", "fee": 500, "duration": 3},
        {"name": "Advanced Patient Care", "fee": 750, "duration": 5},
        {"name": "Medical Technology Overview", "fee": 600, "duration": 4},
        {"name": "Global Health Policies", "fee": 850, "duration": 6},
    ]

    print("Welcome to Global Healthcare Management College!")
    print("Available courses:")
    for idx, course in enumerate(available_courses, start=1):
        print(f"{idx}. {course['name']} - Fee: ${course['fee']} - Duration: {course['duration']} months")

    # Prompt the user to select courses
    try:
        selected_courses = []
        while True:
            course_number = input("Enter the course number to enroll (or 'done' to finish): ").strip()

            if course_number.lower() == 'done':
                break

            if not course_number.isdigit() or int(course_number) < 1 or int(course_number) > len(available_courses):
                print("Invalid course number. Please try again.")
                continue

            selected_course = available_courses[int(course_number) - 1]
            selected_courses.append(selected_course)
            print(f"Enrolled in: {selected_course['name']}")

        if not selected_courses:
            print("No courses selected. Exiting.")
            return

        # Calculate total cost
        total_cost = calculate_total_cost(selected_courses)
        print(f"\nTotal cost for enrolled courses: ${total_cost:.2f}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
