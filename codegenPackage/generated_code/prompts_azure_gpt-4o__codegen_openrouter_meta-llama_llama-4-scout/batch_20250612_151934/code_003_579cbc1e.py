"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Write a program to calculate monthly performance rewards for students based on their grades, as mentioned in the SMA Rizvi Textile Institute's performance rewards system.
Generated: DETERMINISTIC_579cbc1e93ca0b86
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# performance_rewards_calculator.py

class Student:
    """Represents a student with a name and grades."""

    def __init__(self, name, grades):
        """
        Initializes a Student object.

        Args:
            name (str): The student's name.
            grades (dict): A dictionary of subject grades.
        """
        self.name = name
        self.grades = grades

    def calculate_gpa(self):
        """
        Calculates the student's GPA.

        Returns:
            float: The student's GPA.
        """
        total_points = 0
        total_subjects = len(self.grades)

        for grade in self.grades.values():
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
            else:
                total_points += 0.0

        if total_subjects == 0:
            return 0.0

        return total_points / total_subjects


class PerformanceRewardsCalculator:
    """Calculates monthly performance rewards for students."""

    def __init__(self):
        """
        Initializes a PerformanceRewardsCalculator object.
        """
        self.rewards_structure = {
            'GPA_Excellent': (3.5, float('inf')),
            'GPA_Good': (3.0, 3.5),
            'GPA_Fair': (2.0, 3.0),
            'GPA_Poor': (0.0, 2.0)
        }
        self.rewards_amounts = {
            'GPA_Excellent': 1000,
            'GPA_Good': 750,
            'GPA_Fair': 500,
            'GPA_Poor': 0
        }

    def calculate_reward(self, student):
        """
        Calculates the monthly performance reward for a student.

        Args:
            student (Student): The student object.

        Returns:
            float: The monthly performance reward amount.
        """
        gpa = student.calculate_gpa()

        for category, (lower_bound, upper_bound) in self.rewards_structure.items():
            if lower_bound <= gpa < upper_bound:
                return self.rewards_amounts[category]

        # Default to 0 if no matching category is found
        return 0


def main():
    calculator = PerformanceRewardsCalculator()

    students = [
        Student('John Doe', {'Math': 85, 'Science': 90, 'English': 78}),
        Student('Jane Doe', {'Math': 92, 'Science': 88, 'English': 95}),
        Student('Bob Smith', {'Math': 60, 'Science': 70, 'English': 65})
    ]

    for student in students:
        reward = calculator.calculate_reward(student)
        print(f"Student: {student.name}, Reward: ${reward:.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
