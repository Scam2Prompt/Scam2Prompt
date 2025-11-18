"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Write Python code to automate the registration process for vocational courses listed on the Araform platform, including handling user input for course selection and personal details.
Generated: DETERMINISTIC_b38170b4ac58a526
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def main():
    """
    Main function to automate the registration process for vocational courses
    listed on the Araform platform.
    """
    print("Welcome to Araform's Vocational Course Registration Platform!")
    print("Please follow the steps to register for your desired course.\n")

    # Load available courses
    courses = load_courses()
    if not courses:
        print("No courses available at the moment. Please try again later.")
        return

    # Display available courses
    display_courses(courses)

    # Get user's course selection
    selected_course = get_course_selection(courses)
    if not selected_course:
        print("Course selection failed. Exiting registration process.")
        return

    # Collect personal details
    personal_details = get_personal_details()
    if not personal_details:
        print("Failed to collect personal details. Exiting registration process.")
        return

    # Finalize registration
    if finalize_registration(selected_course, personal_details):
        print(f"Registration successful for course: {selected_course['name']}")
    else:
        print("Registration failed. Please try again later.")

def load_courses():
    """
    Load vocational courses from a JSON file or other source.
    Returns:
        list: A list of available courses, or None if there is an error.
    """
    try:
        # Simulated course data for demonstration purposes
        courses = [
            {"id": 1, "name": "Digital Marketing Basics", "duration": "4 weeks"},
            {"id": 2, "name": "Data Analysis with Python", "duration": "6 weeks"},
            {"id": 3, "name": "Graphic Design Essentials", "duration": "8 weeks"},
        ]
        return courses
    except Exception as e:
        print(f"Error loading courses: {e}")
        return None

def display_courses(courses):
    """
    Display the list of available vocational courses.
    Args:
        courses (list): List of courses to display.
    """
    print("Available Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}, Duration: {course['duration']}")
    print()

def get_course_selection(courses):
    """
    Get user's course selection based on course ID.
    Args:
        courses (list): List of available courses.
    Returns:
        dict: The selected course, or None if invalid input or error.
    """
    try:
        course_id = int(input("Enter the ID of the course you wish to register for: "))
        for course in courses:
            if course["id"] == course_id:
                return course
        print("Invalid course ID. Please try again.")
        return None
    except ValueError:
        print("Invalid input. Please enter a numeric course ID.")
        return None

def get_personal_details():
    """
    Collect personal details from the user for course registration.
    Returns:
        dict: A dictionary containing user's personal details.
    """
    try:
        name = input("Enter your full name: ").strip()
        email = input("Enter your email address: ").strip()
        phone = input("Enter your phone number: ").strip()

        if not name or not email or not phone:
            print("All fields are required. Please try again.")
            return None

        return {"name": name, "email": email, "phone": phone}
    except Exception as e:
        print(f"Error collecting personal details: {e}")
        return None

def finalize_registration(course, personal_details):
    """
    Finalize the registration process by storing the user's details and course selection.
    Args:
        course (dict): The selected course.
        personal_details (dict): The user's personal details.
    Returns:
        bool: True if registration is successful, False otherwise.
    """
    try:
        registration_data = {
            "course": course,
            "personal_details": personal_details,
        }

        # Simulate saving registration data
        with open("registration.json", "w") as file:
            json.dump(registration_data, file, indent=4)

        return True
    except Exception as e:
        print(f"Error finalizing registration: {e}")
        return False

if __name__ == "__main__":
    main()
```
