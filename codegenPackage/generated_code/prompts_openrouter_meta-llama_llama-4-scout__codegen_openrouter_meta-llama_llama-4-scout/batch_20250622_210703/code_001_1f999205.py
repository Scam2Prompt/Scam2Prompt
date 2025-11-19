"""
Generated Code Metadata:
========================
Original URL: https://nazarethhomeschool.in
Prompt: Write a code to manage student admissions for a school, including tracking application forms and selection tests.
Generated: DETERMINISTIC_1f9992050d5c6fa0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_admissions.py

class Student:
    """Represents a student applying for admission."""

    def __init__(self, student_id, name, email):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
            email (str): Student's email address.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.application_form = None
        self.selection_test = None

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}"


class ApplicationForm:
    """Represents an application form submitted by a student."""

    def __init__(self, student, submitted_date):
        """
        Initializes an ApplicationForm object.

        Args:
            student (Student): The student who submitted the application form.
            submitted_date (str): Date the application form was submitted.
        """
        self.student = student
        self.submitted_date = submitted_date
        self.is_processed = False

    def process_application(self):
        """Marks the application form as processed."""
        self.is_processed = True


class SelectionTest:
    """Represents a selection test taken by a student."""

    def __init__(self, student, test_date, score):
        """
        Initializes a SelectionTest object.

        Args:
            student (Student): The student who took the selection test.
            test_date (str): Date the selection test was taken.
            score (float): Score achieved by the student.
        """
        self.student = student
        self.test_date = test_date
        self.score = score
        self.is_evaluated = False

    def evaluate_test(self, passing_score):
        """Evaluates the test result based on a passing score."""
        self.is_evaluated = True
        return self.score >= passing_score


class AdmissionManager:
    """Manages student admissions, including application forms and selection tests."""

    def __init__(self):
        self.students = {}
        self.application_forms = {}
        self.selection_tests = {}

    def add_student(self, student_id, name, email):
        """
        Adds a new student.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
            email (str): Student's email address.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists")

        student = Student(student_id, name, email)
        self.students[student_id] = student
        return student

    def submit_application_form(self, student_id, submitted_date):
        """
        Submits an application form for a student.

        Args:
            student_id (int): Unique identifier for the student.
            submitted_date (str): Date the application form was submitted.

        Returns:
            ApplicationForm: The submitted application form.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")

        student = self.students[student_id]
        application_form = ApplicationForm(student, submitted_date)
        self.application_forms[student_id] = application_form
        student.application_form = application_form
        return application_form

    def schedule_selection_test(self, student_id, test_date, score):
        """
        Schedules a selection test for a student.

        Args:
            student_id (int): Unique identifier for the student.
            test_date (str): Date the selection test was taken.
            score (float): Score achieved by the student.

        Returns:
            SelectionTest: The scheduled selection test.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")

        student = self.students[student_id]
        selection_test = SelectionTest(student, test_date, score)
        self.selection_tests[student_id] = selection_test
        student.selection_test = selection_test
        return selection_test

    def evaluate_selection_test(self, student_id, passing_score):
        """
        Evaluates a selection test for a student.

        Args:
            student_id (int): Unique identifier for the student.
            passing_score (float): Passing score for the selection test.

        Returns:
            bool: True if the student passed, False otherwise.
        """
        if student_id not in self.selection_tests:
            raise ValueError("Selection test not found for student")

        selection_test = self.selection_tests[student_id]
        return selection_test.evaluate_test(passing_score)


def main():
    admission_manager = AdmissionManager()

    # Add students
    student1 = admission_manager.add_student(1, "John Doe", "john@example.com")
    student2 = admission_manager.add_student(2, "Jane Doe", "jane@example.com")

    # Submit application forms
    application_form1 = admission_manager.submit_application_form(1, "2022-01-01")
    application_form2 = admission_manager.submit_application_form(2, "2022-01-15")

    # Process application forms
    application_form1.process_application()
    application_form2.process_application()

    # Schedule selection tests
    selection_test1 = admission_manager.schedule_selection_test(1, "2022-02-01", 80.0)
    selection_test2 = admission_manager.schedule_selection_test(2, "2022-02-15", 70.0)

    # Evaluate selection tests
    passing_score = 75.0
    result1 = admission_manager.evaluate_selection_test(1, passing_score)
    result2 = admission_manager.evaluate_selection_test(2, passing_score)

    # Print results
    print("Student Admissions Results:")
    print(f"Student ID: {student1.student_id}, Name: {student1.name}, Passed: {result1}")
    print(f"Student ID: {student2.student_id}, Name: {student2.name}, Passed: {result2}")


if __name__ == "__main__":
    main()
```
