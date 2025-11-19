"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Illustrate how to implement a pre-professional internship management system in a software application for a technical education institute, inspired by Trentino’s practices.
Generated: DETERMINISTIC_943a27aa858b0ba9
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# internship_management.py

class Internship:
    """
    Class to represent an internship.
    Attributes:
        title (str): The title of the internship.
        company (str): The company offering the internship.
        duration (int): Duration of the internship in weeks.
        description (str): A brief description of the internship.
    """

    def __init__(self, title, company, duration, description):
        self.title = title
        self.company = company
        self.duration = duration
        self.description = description

    def __str__(self):
        return f"{self.title} at {self.company} for {self.duration} weeks"


class Student:
    """
    Class to represent a student.
    Attributes:
        name (str): The name of the student.
        email (str): The email of the student.
        internships (list): A list of internships the student has applied for.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.internships = []

    def apply_for_internship(self, internship):
        """
        Method for a student to apply for an internship.
        Args:
            internship (Internship): The internship to apply for.
        """
        self.internships.append(internship)
        print(f"{self.name} has applied for {internship}")


class InternshipManager:
    """
    Class to manage internships and student applications.
    Attributes:
        internships (list): A list of available internships.
    """

    def __init__(self):
        self.internships = []

    def add_internship(self, internship):
        """
        Method to add an internship to the system.
        Args:
            internship (Internship): The internship to add.
        """
        self.internships.append(internship)
        print(f"Internship added: {internship}")

    def list_internships(self):
        """
        Method to list all available internships.
        Returns:
            list: A list of all internships.
        """
        return self.internships


def main():
    """
    Main function to demonstrate the internship management system.
    """
    # Create an instance of InternshipManager
    manager = InternshipManager()

    # Create some internships
    internship1 = Internship("Software Development Intern", "Tech Corp", 12, "Develop software solutions.")
    internship2 = Internship("Data Science Intern", "Data Inc", 8, "Analyze data and build models.")

    # Add internships to the manager
    manager.add_internship(internship1)
    manager.add_internship(internship2)

    # Create a student
    student = Student("Alice Smith", "alice.smith@example.com")

    # List available internships
    print("\nAvailable Internships:")
    for internship in manager.list_internships():
        print(internship)

    # Student applies for an internship
    student.apply_for_internship(internship1)

    # Display student's applied internships
    print("\nInternships applied by the student:")
    for internship in student.internships:
        print(internship)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
