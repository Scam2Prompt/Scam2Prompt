"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Develop a Python script to manage enrollment forms for various music programs, including individual lessons and group classes, as detailed by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_f46f0ebd80c19290
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_program_enrollment.py

class MusicProgram:
    """Base class for music programs."""

    def __init__(self, name, description):
        """
        Initialize a music program.

        Args:
            name (str): Program name.
            description (str): Program description.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class IndividualLesson(MusicProgram):
    """Individual music lesson program."""

    def __init__(self, name, description, instrument, duration):
        """
        Initialize an individual lesson program.

        Args:
            name (str): Program name.
            description (str): Program description.
            instrument (str): Instrument for the lesson.
            duration (int): Lesson duration in minutes.
        """
        super().__init__(name, description)
        self.instrument = instrument
        self.duration = duration

    def __str__(self):
        return f"Individual Lesson: {super().__str__()} - {self.instrument}, {self.duration} minutes"


class GroupClass(MusicProgram):
    """Group music class program."""

    def __init__(self, name, description, instrument, max_students):
        """
        Initialize a group class program.

        Args:
            name (str): Program name.
            description (str): Program description.
            instrument (str): Instrument for the class.
            max_students (int): Maximum number of students in the class.
        """
        super().__init__(name, description)
        self.instrument = instrument
        self.max_students = max_students
        self.enrolled_students = []

    def enroll_student(self, student_name):
        """
        Enroll a student in the group class.

        Args:
            student_name (str): Name of the student.

        Raises:
            ValueError: If the class is full.
        """
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student_name)
        else:
            raise ValueError("Class is full.")

    def __str__(self):
        return f"Group Class: {super().__str__()} - {self.instrument}, Max Students: {self.max_students}"


class EnrollmentForm:
    """Enrollment form for music programs."""

    def __init__(self):
        self.programs = []

    def add_program(self, program):
        """
        Add a music program to the enrollment form.

        Args:
            program (MusicProgram): Music program to add.
        """
        self.programs.append(program)

    def display_programs(self):
        """Display all music programs."""
        for i, program in enumerate(self.programs, start=1):
            print(f"{i}. {program}")

    def get_program(self, index):
        """
        Get a music program by index.

        Args:
            index (int): Index of the program.

        Returns:
            MusicProgram: Music program at the given index.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            return self.programs[index - 1]
        except IndexError:
            raise IndexError("Invalid program index.")


def main():
    # Create music programs
    lesson_program = IndividualLesson("Piano Lesson", "Private piano lesson.", "Piano", 60)
    group_class_program = GroupClass("Guitar Class", "Group guitar class.", "Guitar", 10)

    # Create enrollment form
    enrollment_form = EnrollmentForm()
    enrollment_form.add_program(lesson_program)
    enrollment_form.add_program(group_class_program)

    # Display music programs
    print("Music Programs:")
    enrollment_form.display_programs()

    # Get a program and enroll a student
    program_index = 2
    program = enrollment_form.get_program(program_index)
    print(f"\nSelected Program: {program}")

    if isinstance(program, GroupClass):
        student_name = "John Doe"
        try:
            program.enroll_student(student_name)
            print(f"Student '{student_name}' enrolled successfully.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
