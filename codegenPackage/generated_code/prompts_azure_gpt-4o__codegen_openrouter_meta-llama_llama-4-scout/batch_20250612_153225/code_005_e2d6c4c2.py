"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Write a program to track and evaluate academic work for students, incorporating the evaluation methods described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_e2d6c4c24110cf07
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# academic_evaluator.py

class Student:
    """Represents a student with their academic work."""

    def __init__(self, name, roll_number):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            roll_number (int): The student's roll number.
        """
        self.name = name
        self.roll_number = roll_number
        self.assignments = []
        self.quizzes = []
        self.exams = []

    def add_assignment(self, score, max_score):
        """
        Adds an assignment score.

        Args:
            score (float): The student's score.
            max_score (float): The maximum possible score.
        """
        self.assignments.append((score, max_score))

    def add_quiz(self, score, max_score):
        """
        Adds a quiz score.

        Args:
            score (float): The student's score.
            max_score (float): The maximum possible score.
        """
        self.quizzes.append((score, max_score))

    def add_exam(self, score, max_score):
        """
        Adds an exam score.

        Args:
            score (float): The student's score.
            max_score (float): The maximum possible score.
        """
        self.exams.append((score, max_score))

    def calculate_assignment_average(self):
        """
        Calculates the average assignment score.

        Returns:
            float: The average assignment score.
        """
        if not self.assignments:
            return 0.0

        total_score = sum(score for score, _ in self.assignments)
        total_max_score = sum(max_score for _, max_score in self.assignments)
        return (total_score / total_max_score) * 100

    def calculate_quiz_average(self):
        """
        Calculates the average quiz score.

        Returns:
            float: The average quiz score.
        """
        if not self.quizzes:
            return 0.0

        total_score = sum(score for score, _ in self.quizzes)
        total_max_score = sum(max_score for _, max_score in self.quizzes)
        return (total_score / total_max_score) * 100

    def calculate_exam_average(self):
        """
        Calculates the average exam score.

        Returns:
            float: The average exam score.
        """
        if not self.exams:
            return 0.0

        total_score = sum(score for score, _ in self.exams)
        total_max_score = sum(max_score for _, max_score in self.exams)
        return (total_score / total_max_score) * 100

    def evaluate_academic_work(self):
        """
        Evaluates the student's academic work based on Deepti Convent Higher Secondary School's evaluation methods.

        Returns:
            dict: A dictionary containing the student's evaluation results.
        """
        assignment_average = self.calculate_assignment_average()
        quiz_average = self.calculate_quiz_average()
        exam_average = self.calculate_exam_average()

        # Weightage for each component
        assignment_weightage = 0.3
        quiz_weightage = 0.2
        exam_weightage = 0.5

        # Calculate overall score
        overall_score = (
            (assignment_average * assignment_weightage) +
            (quiz_average * quiz_weightage) +
            (exam_average * exam_weightage)
        )

        return {
            "Assignment Average": assignment_average,
            "Quiz Average": quiz_average,
            "Exam Average": exam_average,
            "Overall Score": overall_score,
        }


def main():
    try:
        # Create a student
        student = Student("John Doe", 12345)

        # Add scores
        student.add_assignment(85, 100)
        student.add_assignment(90, 100)
        student.add_quiz(80, 100)
        student.add_quiz(95, 100)
        student.add_exam(88, 100)
        student.add_exam(92, 100)

        # Evaluate academic work
        evaluation_results = student.evaluate_academic_work()

        # Print evaluation results
        print("Evaluation Results:")
        for component, score in evaluation_results.items():
            print(f"{component}: {score:.2f}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
