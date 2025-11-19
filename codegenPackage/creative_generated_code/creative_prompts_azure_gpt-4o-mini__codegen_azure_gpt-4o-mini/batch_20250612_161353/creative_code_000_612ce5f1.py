"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iedeoccidente.edu.co
Prompt: Generate a Python script that uses the educational resources from the Institución Educativa de Occidente to create a student performance tracking system.
Generated: DETERMINISTIC_612ce5f13fbef66e
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class StudentPerformanceTracker:
    """
    A class to track and manage student performance data.
    """

    def __init__(self, data_file: str):
        """
        Initializes the StudentPerformanceTracker with a data file.
        
        Args:
            data_file (str): The path to the JSON file that stores student data.
        """
        self.data_file = data_file
        self.students = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Loads student performance data from a JSON file.
        
        Returns:
            List[Dict[str, Any]]: A list of students with their performance data.
        """
        if not os.path.exists(self.data_file):
            return []
        
        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: The data file is not a valid JSON.")
                return []

    def save_data(self) -> None:
        """
        Saves the current student performance data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_name: str, grades: List[int]) -> None:
        """
        Adds a new student to the tracking system.

        Args:
            student_name (str): The name of the student.
            grades (List[int]): A list of grades for the student.
        """
        self.students.append({
            'name': student_name,
            'grades': grades,
            'average': self.calculate_average(grades)
        })
        self.save_data()

    def calculate_average(self, grades: List[int]) -> float:
        """
        Calculates the average of a list of grades.

        Args:
            grades (List[int]): A list of grades.

        Returns:
            float: The average of the grades.
        """
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def get_student_performance(self, student_name: str) -> Dict[str, Any]:
        """
        Retrieves the performance data for a specific student.

        Args:
            student_name (str): The name of the student.

        Returns:
            Dict[str, Any]: The performance data of the student or an error message if not found.
        """
        for student in self.students:
            if student['name'] == student_name:
                return student
        return {'error': 'Student not found.'}

    def main_menu(self) -> None:
        """
        Displays the main menu for user interaction and processes user input.
        """
        while True:
            print("\nStudent Performance Tracker")
            print("1. Add Student")
            print("2. Get Student Performance")
            print("3. Exit")
            
            choice = input("Select an option: ")
            if choice == '1':
                name = input("Enter student name: ")
                grades_input = input("Enter grades separated by commas: ")
                grades = [int(grade.strip()) for grade in grades_input.split(',')]
                self.add_student(name, grades)
                print(f"Added student {name} with grades {grades}.")
            elif choice == '2':
                name = input("Enter student name to view performance: ")
                performance = self.get_student_performance(name)
                print(performance)
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = StudentPerformanceTracker('students_performance.json')
    tracker.main_menu()
```
