"""
Generated Code Metadata:
========================
Original URL: https://sif.com.bo
Prompt: Create a certification program for commercial personnel (credit managers/ officers) using SIF's capacitación services.
Generated: DETERMINISTIC_aadaa0e47cabb475
Batch ID: 20250622_210802
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
    A class to represent a certification program for commercial personnel.
    """

    def __init__(self, program_name, duration, requirements):
        """
        Initializes the CertificationProgram with the given parameters.

        :param program_name: Name of the certification program
        :param duration: Duration of the program in weeks
        :param requirements: List of requirements for the program
        """
        self.program_name = program_name
        self.duration = duration
        self.requirements = requirements
        self.enrolled_students = []

    def enroll_student(self, student_name):
        """
        Enrolls a student in the certification program.

        :param student_name: Name of the student to enroll
        :raises ValueError: If the student is already enrolled
        """
        if student_name in self.enrolled_students:
            raise ValueError(f"Student {student_name} is already enrolled in {self.program_name}.")
        self.enrolled_students.append(student_name)
        print(f"Student {student_name} has been enrolled in {self.program_name}.")

    def get_enrolled_students(self):
        """
        Returns a list of enrolled students.

        :return: List of student names
        """
        return self.enrolled_students

    def display_program_info(self):
        """
        Displays the information about the certification program.
        """
        print(f"Program Name: {self.program_name}")
        print(f"Duration: {self.duration} weeks")
        print("Requirements:")
        for req in self.requirements:
            print(f"- {req}")

def main():
    """
    Main function to demonstrate the CertificationProgram class.
    """
    # Define the certification program details
    program_name = "Credit Management Certification"
    duration = 12  # Duration in weeks
    requirements = [
        "Basic understanding of credit principles",
        "Experience in financial services",
        "Completion of prerequisite courses"
    ]

    # Create an instance of the CertificationProgram
    credit_management_program = CertificationProgram(program_name, duration, requirements)

    # Display program information
    credit_management_program.display_program_info()

    # Enroll students
    try:
        credit_management_program.enroll_student("Alice Johnson")
        credit_management_program.enroll_student("Bob Smith")
        credit_management_program.enroll_student("Alice Johnson")  # This will raise an error
    except ValueError as e:
        print(e)

    # Get and display enrolled students
    enrolled_students = credit_management_program.get_enrolled_students()
    print("Enrolled Students:", enrolled_students)

if __name__ == "__main__":
    main()
```
