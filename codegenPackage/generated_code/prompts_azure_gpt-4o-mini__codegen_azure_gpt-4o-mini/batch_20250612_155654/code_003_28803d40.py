"""
Generated Code Metadata:
========================
Original URL: https://rabbi-apps.teachable.com
Prompt: What are the best practices for designing an online course on rabbi-apps?
Generated: DETERMINISTIC_28803d40bae112de
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OnlineCourse:
    """
    A class to represent an online course for rabbi-apps.

    Attributes:
        title (str): The title of the course.
        description (str): A brief description of the course.
        modules (list): A list of modules in the course.
        enrolled_students (list): A list of students enrolled in the course.
    """

    def __init__(self, title, description):
        """
        Initializes the OnlineCourse with a title and description.

        Args:
            title (str): The title of the course.
            description (str): A brief description of the course.
        """
        self.title = title
        self.description = description
        self.modules = []
        self.enrolled_students = []

    def add_module(self, module_title, module_content):
        """
        Adds a module to the course.

        Args:
            module_title (str): The title of the module.
            module_content (str): The content of the module.

        Raises:
            ValueError: If the module title is empty.
        """
        if not module_title:
            raise ValueError("Module title cannot be empty.")
        
        module = {
            'title': module_title,
            'content': module_content
        }
        self.modules.append(module)

    def enroll_student(self, student_name):
        """
        Enrolls a student in the course.

        Args:
            student_name (str): The name of the student.

        Raises:
            ValueError: If the student name is empty or already enrolled.
        """
        if not student_name:
            raise ValueError("Student name cannot be empty.")
        if student_name in self.enrolled_students:
            raise ValueError("Student is already enrolled in the course.")
        
        self.enrolled_students.append(student_name)

    def get_course_info(self):
        """
        Returns the course information including title, description, modules, and enrolled students.

        Returns:
            dict: A dictionary containing course information.
        """
        return {
            'title': self.title,
            'description': self.description,
            'modules': self.modules,
            'enrolled_students': self.enrolled_students
        }

# Example usage
if __name__ == "__main__":
    try:
        course = OnlineCourse("Rabbi-Apps Development", "Learn to develop applications for rabbi services.")
        course.add_module("Introduction to Rabbi-Apps", "Overview of rabbi-apps and their importance.")
        course.enroll_student("John Doe")
        
        # Print course information
        course_info = course.get_course_info()
        print(course_info)
    except Exception as e:
        print(f"An error occurred: {e}")
```
