"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Write a program to calculate monthly performance rewards for students based on their grades, as mentioned in the SMA Rizvi Textile Institute's performance rewards system.
Generated: DETERMINISTIC_579cbc1e93ca0b86
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Student:
    """
    A class to represent a student and calculate monthly performance rewards
    based on their grades.
    """

    def __init__(self, name: str, grades: list):
        """
        Initialize a new Student.

        :param name: The name of the student
        :param grades: A list of grades (floats) received by the student
        """
        self.name = name
        self.grades = grades

    def calculate_average(self) -> float:
        """
        Calculate the average grade of the student.

        :return: The average grade
        :raises ValueError: If there are no grades to average
        """
        if not self.grades:
            raise ValueError("No grades available to calculate average.")

        return sum(self.grades) / len(self.grades)

    def calculate_reward(self) -> float:
        """
        Calculate the monthly performance reward based on the average grade.

        :return: The performance reward
        """
        average = self.calculate_average()

        # Reward criteria based on average grades
        if average >= 90:
            return 1000.0  # Excellent
        elif average >= 80:
            return 750.0   # Good
        elif average >= 70:
            return 500.0   # Fair
        elif average >= 60:
            return 250.0   # Needs Improvement
        else:
            return 0.0     # No Reward

def main():
    """
    Main function to execute the reward calculation.
    """
    try:
        # Sample student data
        students = [
            Student("Alice", [95, 90, 92]),
            Student("Bob", [85, 80, 78]),
            Student("Charlie", [70, 75, 68]),
            Student("David", [55, 60, 62]),
            Student("Eve", [])  # No grades
        ]

        # Calculate and display rewards for each student
        for student in students:
            try:
                reward = student.calculate_reward()
                print(f"Student: {student.name}, Reward: ${reward:.2f}")
            except ValueError as e:
                print(f"Student: {student.name}, Error: {e}")

    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
