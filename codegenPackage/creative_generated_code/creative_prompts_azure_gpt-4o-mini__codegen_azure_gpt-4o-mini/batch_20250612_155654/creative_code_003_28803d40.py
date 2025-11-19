"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: What are the best practices for designing an online course on rabbi-apps?
Generated: DETERMINISTIC_28803d40bae112de
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Online Course Design for Rabbi-Apps
# This module demonstrates best practices for designing an online course.

class OnlineCourse:
    """
    A class to represent an online course for rabbi-apps.
    
    Attributes
    ----------
    title : str
        Title of the online course
    description : str
        Brief description of the course
    modules : list
        List of modules included in the course
    students : list
        List of enrolled students
    """

    def __init__(self, title: str, description: str):
        """
        Initializes an OnlineCourse instance.

        Parameters
        ----------
        title : str
            Title of the online course
        description : str
            Brief description of the course
        """
        self.title = title
        self.description = description
        self.modules = []
        self.students = []

    def add_module(self, module_title: str):
        """
        Adds a module to the course.

        Parameters
        ----------
        module_title : str
            Title of the module to be added
        """
        if not module_title:
            raise ValueError("Module title must not be empty.")
        self.modules.append(module_title)
        print(f"Module '{module_title}' added to the course.")

    def enroll_student(self, student_name: str):
        """
        Enrolls a student in the course.

        Parameters
        ----------
        student_name : str
            Name of the student to enroll
        """
        if not student_name:
            raise ValueError("Student name must not be empty.")
        if student_name in self.students:
            raise ValueError("Student is already enrolled in the course.")
        self.students.append(student_name)
        print(f"Student '{student_name}' enrolled in the course.")

    def get_course_details(self):
        """
        Returns the details of the course.
        
        Returns
        -------
        dict
            A dictionary containing the course details
        """
        return {
            "Title": self.title,
            "Description": self.description,
            "Modules": self.modules,
            "Students": self.students
        }

def main():
    """
    Main function to demonstrate the usage of OnlineCourse class.
    """
    try:
        # Create an instance of the OnlineCourse
        course = OnlineCourse("Rabbi-Apps: An Introduction", "Learn how to build applications for rabbinical purposes.")

        # Add modules to the course
        course.add_module("Module 1: Understanding Rabbi-Apps")
        course.add_module("Module 2: Building Your First Rabbi-App")

        # Enroll students
        course.enroll_student("Rabbi Cohen")
        course.enroll_student("Rabbi Levy")

        # Fetch and print course details
        course_details = course.get_course_details()
        print(course_details)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
