"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Generate code for a registration system that allows students to enroll in programs like JEE, NEET, CUET, and Foundation, with options for offline learning and online testing, as detailed by Potencia Academy.
Generated: DETERMINISTIC_6613424b0afc9c02
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Program:
    """Class representing a study program offered by the academy."""
    
    def __init__(self, name, mode):
        """
        Initialize a Program instance.

        Args:
            name (str): The name of the program (e.g., JEE, NEET).
            mode (str): The mode of learning (e.g., online, offline).
        """
        self.name = name
        self.mode = mode

    def __str__(self):
        """Return a string representation of the program."""
        return f"{self.name} ({self.mode})"


class Student:
    """Class representing a student who can enroll in programs."""
    
    def __init__(self, name, email):
        """
        Initialize a Student instance.

        Args:
            name (str): The name of the student.
            email (str): The email of the student. Must be valid.
        """
        self.name = name
        self.email = email
        self.enrolled_programs = []

    def enroll(self, program):
        """
        Enroll the student in a program.

        Args:
            program (Program): The program to enroll in.
        """
        if program not in self.enrolled_programs:
            self.enrolled_programs.append(program)
            print(f"{self.name} has been enrolled in {program}.")
        else:
            print(f"{self.name} is already enrolled in {program}.")

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student: {self.name}, Email: {self.email}"


class RegistrationSystem:
    """Class representing the registration system for students."""
    
    def __init__(self):
        """Initialize the registration system with available programs."""
        self.programs = [
            Program('JEE', 'Offline'),
            Program('NEET', 'Offline'),
            Program('CUET', 'Online'),
            Program('Foundation', 'Online'),
        ]
        self.students = []

    def register_student(self, name, email):
        """
        Register a new student in the system.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            Student: The registered student instance.
        """
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")
        
        student = Student(name, email)
        self.students.append(student)
        print(f"Registered new student: {student}")
        return student

    def validate_email(self, email):
        """
        Validate the email format.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def list_programs(self):
        """List all available programs in the system."""
        for program in self.programs:
            print(program)

    def enroll_student_in_program(self, student, program_name):
        """
        Enroll a given student in a specified program.

        Args:
            student (Student): The student to enroll.
            program_name (str): The name of the program to enroll in.

        Raises:
            ValueError: If the program name is not found.
        """
        program = self.find_program_by_name(program_name)
        if program:
            student.enroll(program)
        else:
            raise ValueError(f"Program '{program_name}' not found.")

    def find_program_by_name(self, name):
        """
        Find a program by its name.

        Args:
            name (str): The name of the program to find.

        Returns:
            Program: The matching program or None if not found.
        """
        for program in self.programs:
            if program.name == name:
                return program
        return None


# Example usage
if __name__ == "__main__":
    system = RegistrationSystem()
    
    # List all programs
    system.list_programs()
    
    # Register a student
    try:
        student1 = system.register_student("Alice Smith", "alice@example.com")
        
        # Enroll the student in a program
        system.enroll_student_in_program(student1, "JEE")
        system.enroll_student_in_program(student1, "NEET")
        
        # Attempt to enroll in a non-existing program to trigger error
        system.enroll_student_in_program(student1, "XYZ")
    
    except ValueError as e:
        print(f"Error: {e}")
```
