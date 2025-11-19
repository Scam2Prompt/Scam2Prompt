"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Develop a mentorship program for students that emphasizes critical thinking and analytical skills, inspired by the mentorship approach at Heart of Jesus College."
Generated: DETERMINISTIC_708d44e8c4f76717
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mentorship_program.py

class Mentor:
    """Represents a mentor in the mentorship program."""

    def __init__(self, name, expertise):
        """
        Initializes a Mentor object.

        Args:
            name (str): The mentor's name.
            expertise (str): The mentor's area of expertise.
        """
        self.name = name
        self.expertise = expertise

    def __str__(self):
        return f"{self.name} - {self.expertise}"


class Student:
    """Represents a student in the mentorship program."""

    def __init__(self, name, interests):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            interests (list): The student's areas of interest.
        """
        self.name = name
        self.interests = interests
        self.mentor = None

    def __str__(self):
        return f"{self.name} - {', '.join(self.interests)}"


class MentorshipProgram:
    """Represents the mentorship program."""

    def __init__(self):
        """Initializes a MentorshipProgram object."""
        self.mentors = []
        self.students = []

    def add_mentor(self, mentor):
        """
        Adds a mentor to the program.

        Args:
            mentor (Mentor): The mentor to add.

        Raises:
            ValueError: If the mentor already exists in the program.
        """
        if mentor in self.mentors:
            raise ValueError("Mentor already exists in the program.")
        self.mentors.append(mentor)

    def add_student(self, student):
        """
        Adds a student to the program.

        Args:
            student (Student): The student to add.

        Raises:
            ValueError: If the student already exists in the program.
        """
        if student in self.students:
            raise ValueError("Student already exists in the program.")
        self.students.append(student)

    def assign_mentor(self, student, mentor):
        """
        Assigns a mentor to a student.

        Args:
            student (Student): The student to assign a mentor to.
            mentor (Mentor): The mentor to assign.

        Raises:
            ValueError: If the student or mentor does not exist in the program.
        """
        if student not in self.students:
            raise ValueError("Student does not exist in the program.")
        if mentor not in self.mentors:
            raise ValueError("Mentor does not exist in the program.")
        student.mentor = mentor

    def display_program(self):
        """Displays the mentorship program's participants and assignments."""
        print("Mentors:")
        for mentor in self.mentors:
            print(mentor)

        print("\nStudents:")
        for student in self.students:
            print(f"{student} - Mentor: {student.mentor.name if student.mentor else 'Unassigned'}")


def main():
    try:
        program = MentorshipProgram()

        # Create mentors
        mentor1 = Mentor("John Doe", "Computer Science")
        mentor2 = Mentor("Jane Smith", "Mathematics")

        # Add mentors to the program
        program.add_mentor(mentor1)
        program.add_mentor(mentor2)

        # Create students
        student1 = Student("Alice Johnson", ["Computer Science", "Engineering"])
        student2 = Student("Bob Brown", ["Mathematics", "Statistics"])

        # Add students to the program
        program.add_student(student1)
        program.add_student(student2)

        # Assign mentors to students
        program.assign_mentor(student1, mentor1)
        program.assign_mentor(student2, mentor2)

        # Display the program
        program.display_program()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
