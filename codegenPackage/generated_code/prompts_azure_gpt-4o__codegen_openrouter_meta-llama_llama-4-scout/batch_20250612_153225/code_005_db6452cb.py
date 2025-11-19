"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Develop a program to organize and display the syllabus and results for MBBS and MD/MS courses at MIMSR Medical College, referencing the "Syllabus & Results" section.
Generated: DETERMINISTIC_db6452cb630dfd84
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**MIMSR Medical College Syllabus and Results Program**
======================================================

```python
# Import required libraries
import json
import os

class Course:
    """Represents a course with syllabus and results."""

    def __init__(self, name):
        """
        Initializes a Course object.

        Args:
            name (str): Name of the course.
        """
        self.name = name
        self.syllabus = {}
        self.results = {}

    def add_syllabus(self, semester, subjects):
        """
        Adds syllabus for a semester.

        Args:
            semester (str): Semester number.
            subjects (dict): Dictionary of subjects with their descriptions.
        """
        self.syllabus[semester] = subjects

    def add_results(self, semester, results):
        """
        Adds results for a semester.

        Args:
            semester (str): Semester number.
            results (dict): Dictionary of student results.
        """
        self.results[semester] = results


class MIMSRMedicalCollege:
    """Represents MIMSR Medical College with courses."""

    def __init__(self):
        """
        Initializes an MIMSRMedicalCollege object.
        """
        self.courses = {}

    def add_course(self, course):
        """
        Adds a course to the college.

        Args:
            course (Course): Course object to add.
        """
        self.courses[course.name] = course

    def display_syllabus(self, course_name, semester=None):
        """
        Displays syllabus for a course.

        Args:
            course_name (str): Name of the course.
            semester (str, optional): Semester number. Defaults to None.

        Returns:
            dict: Syllabus for the course.
        """
        if course_name not in self.courses:
            raise ValueError("Course not found")

        if semester:
            return self.courses[course_name].syllabus.get(semester, {})
        else:
            return self.courses[course_name].syllabus

    def display_results(self, course_name, semester=None):
        """
        Displays results for a course.

        Args:
            course_name (str): Name of the course.
            semester (str, optional): Semester number. Defaults to None.

        Returns:
            dict: Results for the course.
        """
        if course_name not in self.courses:
            raise ValueError("Course not found")

        if semester:
            return self.courses[course_name].results.get(semester, {})
        else:
            return self.courses[course_name].results


def main():
    # Create college object
    college = MIMSRMedicalCollege()

    # Create courses
    mbbs = Course("MBBS")
    md_ms = Course("MD/MS")

    # Add syllabus and results for MBBS
    mbbs.add_syllabus("Semester 1", {
        "Anatomy": "Human body structure",
        "Physiology": "Human body functions"
    })
    mbbs.add_results("Semester 1", {
        "Student 1": {"Anatomy": 80, "Physiology": 90},
        "Student 2": {"Anatomy": 70, "Physiology": 80}
    })

    # Add syllabus and results for MD/MS
    md_ms.add_syllabus("Semester 1", {
        "Pharmacology": "Drugs and their effects",
        "Pathology": "Disease study"
    })
    md_ms.add_results("Semester 1", {
        "Student 1": {"Pharmacology": 85, "Pathology": 95},
        "Student 2": {"Pharmacology": 75, "Pathology": 85}
    })

    # Add courses to college
    college.add_course(mbbs)
    college.add_course(md_ms)

    # Display syllabus and results
    print("MBBS Syllabus:")
    print(json.dumps(college.display_syllabus("MBBS"), indent=4))
    print("\nMBBS Results:")
    print(json.dumps(college.display_results("MBBS"), indent=4))

    print("\nMD/MS Syllabus:")
    print(json.dumps(college.display_syllabus("MD/MS"), indent=4))
    print("\nMD/MS Results:")
    print(json.dumps(college.display_results("MD/MS"), indent=4))


if __name__ == "__main__":
    main()
```
