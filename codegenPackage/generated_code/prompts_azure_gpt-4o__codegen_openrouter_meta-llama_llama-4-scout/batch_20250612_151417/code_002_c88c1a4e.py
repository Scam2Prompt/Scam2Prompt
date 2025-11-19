"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Generate code for a feedback mechanism that collects and analyzes student performance data during placement training, as emphasized by SMART Training Resources.
Generated: DETERMINISTIC_c88c1a4e7ca748d5
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_mechanism.py

import datetime
import json

class StudentPerformance:
    def __init__(self, student_id, name):
        """
        Initialize a StudentPerformance object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
        """
        self.student_id = student_id
        self.name = name
        self.performance_data = []

    def add_performance_data(self, topic, score, feedback):
        """
        Add performance data for a specific topic.

        Args:
            topic (str): Topic of the placement training.
            score (float): Score achieved by the student.
            feedback (str): Feedback provided by the trainer.
        """
        data = {
            "topic": topic,
            "score": score,
            "feedback": feedback,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.performance_data.append(data)

    def get_performance_data(self):
        """
        Retrieve all performance data for the student.

        Returns:
            list: List of performance data dictionaries.
        """
        return self.performance_data

    def analyze_performance(self):
        """
        Analyze the student's performance data.

        Returns:
            dict: Dictionary containing average score and feedback summary.
        """
        if not self.performance_data:
            return {"average_score": 0, "feedback_summary": "No data available"}

        total_score = sum(data["score"] for data in self.performance_data)
        average_score = total_score / len(self.performance_data)
        feedback_summary = "\n".join(data["feedback"] for data in self.performance_data)

        return {"average_score": average_score, "feedback_summary": feedback_summary}


class FeedbackMechanism:
    def __init__(self):
        """
        Initialize a FeedbackMechanism object.
        """
        self.students = {}

    def add_student(self, student_id, name):
        """
        Add a student to the feedback mechanism.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
        """
        if student_id in self.students:
            raise ValueError("Student already exists")

        self.students[student_id] = StudentPerformance(student_id, name)

    def get_student(self, student_id):
        """
        Retrieve a student object.

        Args:
            student_id (int): Unique identifier for the student.

        Returns:
            StudentPerformance: StudentPerformance object for the given student ID.
        """
        return self.students.get(student_id)

    def save_data(self, filename):
        """
        Save the feedback data to a JSON file.

        Args:
            filename (str): Name of the file to save the data to.
        """
        data = []
        for student in self.students.values():
            student_data = {
                "student_id": student.student_id,
                "name": student.name,
                "performance_data": student.get_performance_data()
            }
            data.append(student_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, filename):
        """
        Load feedback data from a JSON file.

        Args:
            filename (str): Name of the file to load the data from.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for student_data in data:
                    student_id = student_data["student_id"]
                    name = student_data["name"]
                    self.add_student(student_id, name)
                    for performance_data in student_data["performance_data"]:
                        self.students[student_id].add_performance_data(
                            performance_data["topic"],
                            performance_data["score"],
                            performance_data["feedback"]
                        )
        except FileNotFoundError:
            print("File not found")


def main():
    feedback_mechanism = FeedbackMechanism()

    while True:
        print("1. Add student")
        print("2. Add performance data")
        print("3. Get performance data")
        print("4. Analyze performance")
        print("5. Save data")
        print("6. Load data")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            feedback_mechanism.add_student(student_id, name)
        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            topic = input("Enter topic: ")
            score = float(input("Enter score: "))
            feedback = input("Enter feedback: ")
            student = feedback_mechanism.get_student(student_id)
            if student:
                student.add_performance_data(topic, score, feedback)
            else:
                print("Student not found")
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            student = feedback_mechanism.get_student(student_id)
            if student:
                print(student.get_performance_data())
            else:
                print("Student not found")
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            student = feedback_mechanism.get_student(student_id)
            if student:
                print(student.analyze_performance())
            else:
                print("Student not found")
        elif choice == "5":
            filename = input("Enter filename: ")
            feedback_mechanism.save_data(filename)
        elif choice == "6":
            filename = input("Enter filename: ")
            feedback_mechanism.load_data(filename)
        elif choice == "7":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
