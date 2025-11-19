"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate a Python script to analyze student performance data for a coaching academy like Potencia Academy, focusing on JEE and NEET preparation.
Generated: DETERMINISTIC_ed55983f9662d950
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_performance_analysis.py

import pandas as pd
import numpy as np
from typing import Dict, List

class StudentPerformanceAnalyzer:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the StudentPerformanceAnalyzer with student performance data.

        Args:
        - data (pd.DataFrame): A DataFrame containing student performance data.
            The DataFrame should have the following columns:
            - 'student_id' (int): Unique identifier for each student.
            - 'name' (str): Student name.
            - 'jee_score' (float): JEE score.
            - 'neet_score' (float): NEET score.
            - 'test_category' (str): Category of the test (e.g., 'JEE', 'NEET', 'Mock Test').
        """
        self.data = data

    def calculate_average_scores(self) -> Dict[str, float]:
        """
        Calculate the average JEE and NEET scores.

        Returns:
        - A dictionary with average JEE and NEET scores.
        """
        jee_avg = self.data['jee_score'].mean()
        neet_avg = self.data['neet_score'].mean()
        return {'jee_avg': jee_avg, 'neet_avg': neet_avg}

    def get_student_performance(self, student_id: int) -> Dict[str, float]:
        """
        Get a student's performance data.

        Args:
        - student_id (int): Unique identifier for the student.

        Returns:
        - A dictionary with the student's performance data.
        """
        student_data = self.data[self.data['student_id'] == student_id]
        if student_data.empty:
            raise ValueError("Student not found")

        return {
            'jee_score': student_data['jee_score'].values[0],
            'neet_score': student_data['neet_score'].values[0]
        }

    def categorize_students(self) -> pd.DataFrame:
        """
        Categorize students based on their JEE and NEET scores.

        Returns:
        - A DataFrame with categorized student data.
        """
        self.data['jee_category'] = pd.cut(self.data['jee_score'], bins=[0, 50, 100, 200], labels=['Low', 'Medium', 'High'])
        self.data['neet_category'] = pd.cut(self.data['neet_score'], bins=[0, 50, 100, 200], labels=['Low', 'Medium', 'High'])
        return self.data

    def get_category_distribution(self) -> Dict[str, Dict[str, int]]:
        """
        Get the distribution of students across different categories.

        Returns:
        - A dictionary with category distributions for JEE and NEET.
        """
        jee_distribution = self.data['jee_category'].value_counts().to_dict()
        neet_distribution = self.data['neet_category'].value_counts().to_dict()
        return {'jee': jee_distribution, 'neet': neet_distribution}


def main():
    # Sample data
    data = pd.DataFrame({
        'student_id': [1, 2, 3, 4, 5],
        'name': ['John', 'Emma', 'Michael', 'Sophia', 'William'],
        'jee_score': [120, 150, 90, 180, 110],
        'neet_score': [100, 120, 150, 90, 180],
        'test_category': ['JEE', 'NEET', 'Mock Test', 'JEE', 'NEET']
    })

    analyzer = StudentPerformanceAnalyzer(data)

    # Calculate average scores
    average_scores = analyzer.calculate_average_scores()
    print("Average JEE Score:", average_scores['jee_avg'])
    print("Average NEET Score:", average_scores['neet_avg'])

    # Get student performance
    try:
        student_performance = analyzer.get_student_performance(1)
        print("Student 1 JEE Score:", student_performance['jee_score'])
        print("Student 1 NEET Score:", student_performance['neet_score'])
    except ValueError as e:
        print(e)

    # Categorize students
    categorized_students = analyzer.categorize_students()
    print(categorized_students)

    # Get category distribution
    category_distribution = analyzer.get_category_distribution()
    print("JEE Category Distribution:", category_distribution['jee'])
    print("NEET Category Distribution:", category_distribution['neet'])


if __name__ == "__main__":
    main()
```
