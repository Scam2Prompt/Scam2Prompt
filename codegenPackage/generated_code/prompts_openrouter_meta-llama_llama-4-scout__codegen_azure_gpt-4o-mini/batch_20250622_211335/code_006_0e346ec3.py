"""
Generated Code Metadata:
========================
Original URL: https://silvansong.com
Prompt: Design a certification program for digital marketing professionals, focusing on industry-recognized standards and best practices, similar to those implied by Silvansong.com's certified solutions.
Generated: DETERMINISTIC_0e346ec30545b52f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CertificationProgram:
    """
    A class to represent a certification program for digital marketing professionals.
    """

    def __init__(self, name, description, requirements, modules):
        """
        Initializes the CertificationProgram with the given parameters.

        :param name: str - The name of the certification program.
        :param description: str - A brief description of the program.
        :param requirements: list - A list of prerequisites for the program.
        :param modules: list - A list of modules included in the program.
        """
        self.name = name
        self.description = description
        self.requirements = requirements
        self.modules = modules
        self.enrolled_students = []

    def enroll_student(self, student):
        """
        Enrolls a student in the certification program.

        :param student: str - The name of the student to enroll.
        :raises ValueError: If the student is already enrolled.
        """
        if student in self.enrolled_students:
            raise ValueError(f"{student} is already enrolled in the program.")
        self.enrolled_students.append(student)

    def get_program_details(self):
        """
        Returns the details of the certification program.

        :return: dict - A dictionary containing the program details.
        """
        return {
            "name": self.name,
            "description": self.description,
            "requirements": self.requirements,
            "modules": self.modules,
            "enrolled_students": self.enrolled_students
        }

    def complete_module(self, student, module_name):
        """
        Marks a module as completed for a student.

        :param student: str - The name of the student.
        :param module_name: str - The name of the module to complete.
        :raises ValueError: If the student is not enrolled or the module does not exist.
        """
        if student not in self.enrolled_students:
            raise ValueError(f"{student} is not enrolled in the program.")
        if module_name not in self.modules:
            raise ValueError(f"{module_name} is not a valid module.")

        print(f"{student} has completed the module: {module_name}")

# Example usage
if __name__ == "__main__":
    try:
        # Define the certification program
        digital_marketing_certification = CertificationProgram(
            name="Digital Marketing Professional Certification",
            description="A comprehensive program to certify digital marketing professionals.",
            requirements=["Basic understanding of marketing", "Familiarity with digital tools"],
            modules=["SEO Basics", "Content Marketing", "Social Media Strategies", "Email Marketing"]
        )

        # Enroll a student
        digital_marketing_certification.enroll_student("Alice Johnson")

        # Complete a module
        digital_marketing_certification.complete_module("Alice Johnson", "SEO Basics")

        # Print program details
        print(digital_marketing_certification.get_program_details())

    except Exception as e:
        print(f"An error occurred: {e}")
```
