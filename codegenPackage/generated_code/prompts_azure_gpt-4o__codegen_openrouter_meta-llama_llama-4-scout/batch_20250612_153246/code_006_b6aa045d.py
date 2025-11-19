"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python program to track student progress across multiple subjects, incorporating features like simulated exam scores and revision schedules, as used in the Maratona do ENEM course.
Generated: DETERMINISTIC_b6aa045d4a7d15be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_progress_tracker.py

class Subject:
    """Represents a subject with a name and scores."""

    def __init__(self, name):
        """
        Initializes a Subject instance.

        Args:
            name (str): The name of the subject.
        """
        self.name = name
        self.scores = []
        self.revision_schedule = []

    def add_score(self, score):
        """
        Adds a simulated exam score.

        Args:
            score (float): The score to add.

        Raises:
            ValueError: If the score is not between 0 and 100.
        """
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)

    def add_revision(self, date):
        """
        Adds a revision date to the schedule.

        Args:
            date (str): The date of revision in YYYY-MM-DD format.
        """
        self.revision_schedule.append(date)

    def get_average_score(self):
        """
        Calculates the average score.

        Returns:
            float: The average score or 0 if no scores are available.
        """
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


class Student:
    """Represents a student with a name and subjects."""

    def __init__(self, name):
        """
        Initializes a Student instance.

        Args:
            name (str): The name of the student.
        """
        self.name = name
        self.subjects = {}

    def add_subject(self, subject_name):
        """
        Adds a subject to the student's list.

        Args:
            subject_name (str): The name of the subject.

        Returns:
            Subject: The added subject instance.
        """
        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject(subject_name)
        return self.subjects[subject_name]

    def get_subject(self, subject_name):
        """
        Retrieves a subject by name.

        Args:
            subject_name (str): The name of the subject.

        Returns:
            Subject: The subject instance or None if not found.
        """
        return self.subjects.get(subject_name)

    def display_progress(self):
        """
        Displays the student's progress across all subjects.
        """
        for subject_name, subject in self.subjects.items():
            average_score = subject.get_average_score()
            print(f"Subject: {subject_name}")
            print(f"Average Score: {average_score:.2f}")
            print(f"Revision Schedule: {subject.revision_schedule}")
            print("------------------------")


def main():
    try:
        student_name = input("Enter student name: ")
        student = Student(student_name)

        while True:
            print("\n1. Add Subject")
            print("2. Add Score")
            print("3. Add Revision")
            print("4. Display Progress")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                subject_name = input("Enter subject name: ")
                student.add_subject(subject_name)
            elif choice == "2":
                subject_name = input("Enter subject name: ")
                subject = student.get_subject(subject_name)
                if subject:
                    score = float(input("Enter score: "))
                    subject.add_score(score)
                else:
                    print("Subject not found.")
            elif choice == "3":
                subject_name = input("Enter subject name: ")
                subject = student.get_subject(subject_name)
                if subject:
                    date = input("Enter revision date (YYYY-MM-DD): ")
                    subject.add_revision(date)
                else:
                    print("Subject not found.")
            elif choice == "4":
                student.display_progress()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
