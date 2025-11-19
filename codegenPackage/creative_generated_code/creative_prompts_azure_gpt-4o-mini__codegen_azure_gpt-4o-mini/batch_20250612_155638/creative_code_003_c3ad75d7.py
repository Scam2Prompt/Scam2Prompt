"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-virgocx.teachable.com
Prompt: What are the best practices for designing an online course using the platform features from portal-virgocx?
Generated: DETERMINISTIC_c3ad75d78275f6d8
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OnlineCourse:
    """
    A class to represent an online course on the portal-virgocx platform.
    """

    def __init__(self, title: str, description: str):
        """
        Initializes the OnlineCourse instance with the title and description.

        Args:
            title (str): The title of the course.
            description (str): A brief description of the course.
        """
        self.title = title
        self.description = description
        self.modules = []
        self.enrolled_students = []

    def add_module(self, module_title: str, content: str):
        """
        Adds a module to the online course.

        Args:
            module_title (str): The title of the module.
            content (str): The content of the module.
        """
        module = {'title': module_title, 'content': content}
        self.modules.append(module)

    def enroll_student(self, student_name: str):
        """
        Enrolls a student in the online course.

        Args:
            student_name (str): The name of the student to enroll.
        """
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
        else:
            raise ValueError(f"{student_name} is already enrolled in the course.")

    def get_course_details(self):
        """
        Returns the details of the course including title, description, modules, and enrolled students.

        Returns:
            dict: A dictionary containing the course details.
        """
        course_details = {
            'title': self.title,
            'description': self.description,
            'modules': self.modules,
            'enrolled_students': self.enrolled_students,
        }
        return course_details

    def remove_student(self, student_name: str):
        """
        Removes a student from the online course.

        Args:
            student_name (str): The name of the student to remove.

        Raises:
            ValueError: If the student is not enrolled in the course.
        """
        try:
            self.enrolled_students.remove(student_name)
        except ValueError:
            raise ValueError(f"{student_name} is not enrolled in this course.")

# Example usage
if __name__ == "__main__":
    try:
        # Creating an online course
        course = OnlineCourse("Python Programming", "Learn the basics of Python programming.")

        # Adding modules to the course
        course.add_module("Introduction to Python", "Content about Python basics.")
        course.add_module("Data Structures", "Content about lists, tuples, and dictionaries.")

        # Enrolling students
        course.enroll_student("Alice")
        course.enroll_student("Bob")

        # Display course details
        print(course.get_course_details())

        # Removing a student
        course.remove_student("Alice")
        print(course.get_course_details())

    except Exception as e:
        print(f"An error occurred: {e}")
```
