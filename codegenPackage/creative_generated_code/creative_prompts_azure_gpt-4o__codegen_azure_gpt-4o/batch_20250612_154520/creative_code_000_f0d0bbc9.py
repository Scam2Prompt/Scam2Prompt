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
import datetime

def display_courses():
    """
    Display the list of available forklift training courses.
    """
    courses = {
        1: "Beginner Forklift Training",
        2: "Intermediate Forklift Training",
        3: "Advanced Forklift Training"
    }

    print("Available Forklift Training Courses:")
    for course_id, course_name in courses.items():
        print(f"{course_id}. {course_name}")
    
    return courses


def get_user_selection(courses):
    """
    Prompt the user to select a course.
    :param courses: Dictionary of available courses
    :return: Selected course ID and name
    """
    while True:
        try:
            course_id = int(input("Enter the course ID you want to book (e.g., 1, 2, 3): "))
            if course_id in courses:
                return course_id, courses[course_id]
            else:
                print("Invalid course ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_user_schedule():
    """
    Prompt the user to enter a preferred training date.
    :return: Validated training date
    """
    while True:
        try:
            date_input = input("Enter your preferred date for training (YYYY-MM-DD): ")
            training_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            if training_date >= datetime.date.today():
                return training_date
            else:
                print("The date must be today or in the future. Please try again.")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


def confirm_booking(course_name, training_date):
    """
    Confirm the booking details with the user.
    :param course_name: Name of the selected course
    :param training_date: Scheduled training date
    """
    print("\nBooking Confirmation:")
    print(f"Course: {course_name}")
    print(f"Date: {training_date}")
    print("Your booking has been successfully created!")


def main():
    """
    Main function to automate the booking process for forklift training courses.
    """
    print("Welcome to CoLa Training Services!")
    
    # Step 1: Display available courses
    courses = display_courses()
    
    # Step 2: Get course selection from the user
    selected_course_id, selected_course_name = get_user_selection(courses)
    
    # Step 3: Get preferred schedule from the user
    preferred_date = get_user_schedule()
    
    # Step 4: Confirm booking with the user
    confirm_booking(selected_course_name, preferred_date)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
