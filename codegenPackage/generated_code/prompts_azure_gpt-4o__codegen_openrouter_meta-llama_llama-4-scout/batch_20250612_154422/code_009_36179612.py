"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write code to implement a leaderboard system for tracking student performance in IAS test series, including Prelims FLTs and CSAT FLTs, as described on Shield IAS.
Generated: DETERMINISTIC_36179612037f8d9d
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class Student:
    """Represents a student with a name and scores."""

    def __init__(self, name):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
        """
        self.name = name
        self.scores = {
            'prelims': {},
            'csat': {}
        }

    def add_score(self, test_type, test_name, score):
        """
        Adds a score for a test.

        Args:
            test_type (str): The type of test (prelims or csat).
            test_name (str): The name of the test.
            score (int): The student's score.

        Raises:
            ValueError: If test_type is not 'prelims' or 'csat'.
        """
        if test_type not in ['prelims', 'csat']:
            raise ValueError("Invalid test type. Must be 'prelims' or 'csat'.")

        self.scores[test_type][test_name] = score


class Leaderboard:
    """Represents a leaderboard for tracking student performance."""

    def __init__(self):
        """Initializes a Leaderboard object."""
        self.students = {}

    def add_student(self, name):
        """
        Adds a student to the leaderboard.

        Args:
            name (str): The student's name.
        """
        self.students[name] = Student(name)

    def add_score(self, name, test_type, test_name, score):
        """
        Adds a score for a student.

        Args:
            name (str): The student's name.
            test_type (str): The type of test (prelims or csat).
            test_name (str): The name of the test.
            score (int): The student's score.

        Raises:
            ValueError: If the student does not exist.
        """
        if name not in self.students:
            raise ValueError("Student does not exist.")

        self.students[name].add_score(test_type, test_name, score)

    def get_leaderboard(self, test_type=None):
        """
        Gets the leaderboard for a test type.

        Args:
            test_type (str, optional): The type of test (prelims or csat). Defaults to None.

        Returns:
            list: A list of tuples containing the student's name and score.
        """
        leaderboard = []

        for student in self.students.values():
            if test_type:
                scores = student.scores[test_type]
                for test_name, score in scores.items():
                    leaderboard.append((student.name, test_name, score))
            else:
                for test_type, scores in student.scores.items():
                    for test_name, score in scores.items():
                        leaderboard.append((student.name, f"{test_type.capitalize()} - {test_name}", score))

        leaderboard.sort(key=lambda x: x[2], reverse=True)

        return leaderboard


def main():
    leaderboard = Leaderboard()

    while True:
        print("\n1. Add Student")
        print("2. Add Score")
        print("3. Get Leaderboard")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student's name: ")
            leaderboard.add_student(name)
        elif choice == '2':
            name = input("Enter student's name: ")
            test_type = input("Enter test type (prelims or csat): ")
            test_name = input("Enter test name: ")
            score = int(input("Enter score: "))

            try:
                leaderboard.add_score(name, test_type, test_name, score)
            except ValueError as e:
                print(e)
        elif choice == '3':
            test_type = input("Enter test type (prelims, csat, or leave blank for all): ")

            if test_type:
                leaderboard_data = [(name, score) for name, test_name, score in leaderboard.get_leaderboard(test_type)]
            else:
                leaderboard_data = [(name, test_name, score) for name, test_name, score in leaderboard.get_leaderboard()]

            for data in leaderboard_data:
                if len(data) == 2:
                    print(f"{data[0]} - {data[1]}")
                else:
                    print(f"{data[0]} - {data[1]}: {data[2]}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
