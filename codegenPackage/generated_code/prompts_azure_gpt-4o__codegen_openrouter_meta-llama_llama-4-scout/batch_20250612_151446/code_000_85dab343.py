"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a Python script to generate a table of vocational and technical school courses for the academic year 1400-1401, using data structures to organize course names, descriptions, and associated fields of study.
Generated: DETERMINISTIC_85dab3433ad2661c
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vocational_courses.py

class Course:
    """Represents a vocational or technical school course."""

    def __init__(self, name, description, field_of_study):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
            field_of_study (str): The field of study associated with the course.
        """
        self.name = name
        self.description = description
        self.field_of_study = field_of_study

    def __str__(self):
        return f"{self.name}: {self.description} ({self.field_of_study})"


class CourseCatalog:
    """Represents a catalog of vocational or technical school courses."""

    def __init__(self):
        self.courses = []

    def add_course(self, course):
        """
        Adds a course to the catalog.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)

    def generate_table(self):
        """
        Generates a table of courses.

        Returns:
            str: A formatted table of courses.
        """
        table = "| Course Name | Description | Field of Study |\n"
        table += "|-------------|-------------|-----------------|\n"
        for course in self.courses:
            table += f"| {course.name} | {course.description} | {course.field_of_study} |\n"
        return table


def main():
    try:
        catalog = CourseCatalog()

        # Add courses to the catalog
        catalog.add_course(Course("HVAC Technician", "Heating, ventilation, and air conditioning training", "Construction"))
        catalog.add_course(Course("Web Development", "Design and development of web applications", "Computer Science"))
        catalog.add_course(Course("Culinary Arts", "Food preparation and cooking techniques", "Hospitality"))
        catalog.add_course(Course("Automotive Repair", "Diagnosis and repair of vehicles", "Transportation"))
        catalog.add_course(Course("Cybersecurity", "Protection of computer systems from cyber threats", "Computer Science"))

        # Generate and print the course table
        print("# Vocational and Technical School Courses for Academic Year 1400-1401")
        print(catalog.generate_table())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
