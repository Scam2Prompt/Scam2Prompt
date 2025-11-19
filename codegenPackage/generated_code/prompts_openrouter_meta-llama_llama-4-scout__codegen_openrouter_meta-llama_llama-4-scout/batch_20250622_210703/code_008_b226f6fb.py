"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Create a simple chatbot script to provide information about Nzotho FET College's courses and programs to prospective students.
Generated: DETERMINISTIC_b226f6fb35f6497b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Nzotho FET College Chatbot Script

class Course:
    """Represents a course offered by Nzotho FET College."""

    def __init__(self, name, description):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
        """
        self.name = name
        self.description = description

class Chatbot:
    """Provides information about Nzotho FET College's courses and programs."""

    def __init__(self):
        """
        Initializes a Chatbot object with a list of courses.
        """
        self.courses = [
            Course("National Certificate (Vocational) - NCV", "A 3-year programme that provides students with a broad range of skills and knowledge."),
            Course("FET Certificate in Business Administration", "A 1-year programme that provides students with skills and knowledge in business administration."),
            Course("FET Certificate in Information Technology", "A 1-year programme that provides students with skills and knowledge in information technology."),
        ]

    def get_courses(self):
        """
        Returns a list of courses offered by Nzotho FET College.

        Returns:
            list: A list of Course objects.
        """
        return self.courses

    def get_course_info(self, course_name):
        """
        Returns information about a specific course.

        Args:
            course_name (str): The name of the course.

        Returns:
            Course: A Course object if found, otherwise None.
        """
        for course in self.courses:
            if course.name.lower() == course_name.lower():
                return course
        return None

def main():
    chatbot = Chatbot()

    print("Welcome to Nzotho FET College Chatbot!")
    print("----------------------------------------")

    while True:
        print("\nOptions:")
        print("1. View all courses")
        print("2. Search for a course")
        print("3. Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option. Please choose a valid option.")
            continue

        if option == 1:
            courses = chatbot.get_courses()
            for course in courses:
                print(f"\nCourse: {course.name}")
                print(f"Description: {course.description}")
        elif option == 2:
            course_name = input("Enter the course name: ")
            course = chatbot.get_course_info(course_name)
            if course:
                print(f"\nCourse: {course.name}")
                print(f"Description: {course.description}")
            else:
                print("Course not found.")
        elif option == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
