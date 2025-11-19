"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a Python script to analyze student performance in CBSE exams, specifically for classes X and XII.
Generated: DETERMINISTIC_ec5292af8e12bbc9
Batch ID: 20250622_210650
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

class StudentPerformanceAnalyzer:
    """
    Analyzes student performance in CBSE exams for classes X and XII.
    """

    def __init__(self, data):
        """
        Initializes the analyzer with student data.

        Args:
            data (pd.DataFrame): A DataFrame containing student data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the student data.

        Raises:
            ValueError: If the data is invalid.
        """
        required_columns = ['class', 'roll_number', 'name', 'english', 'hindi', 'maths', 'science', 'social_science']
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError("Invalid data: missing required columns")

    def calculate_percentage(self, row):
        """
        Calculates the percentage for a given student.

        Args:
            row (pd.Series): A Series containing student marks.

        Returns:
            float: The calculated percentage.
        """
        subjects = ['english', 'hindi', 'maths', 'science', 'social_science']
        total_marks = len(subjects) * 100
        marks_obtained = row[subjects].sum()
        return (marks_obtained / total_marks) * 100

    def analyze_performance(self):
        """
        Analyzes student performance.

        Returns:
            pd.DataFrame: A DataFrame containing analysis results.
        """
        self.validate_data()

        # Calculate percentage for each student
        self.data['percentage'] = self.data.apply(self.calculate_percentage, axis=1)

        # Categorize students based on performance
        self.data['performance_category'] = pd.cut(self.data['percentage'], 
                                                   bins=[0, 33, 66, 100], 
                                                   labels=['Fail', 'Pass', 'Distinction'])

        return self.data

    def get_class_performance(self, class_number):
        """
        Gets the performance analysis for a specific class.

        Args:
            class_number (int): The class number (X or XII).

        Returns:
            pd.DataFrame: A DataFrame containing class performance analysis.
        """
        class_data = self.data[self.data['class'] == class_number]
        return class_data

def main():
    # Sample data
    data = pd.DataFrame({
        'class': [10, 10, 10, 12, 12, 12],
        'roll_number': [1, 2, 3, 1, 2, 3],
        'name': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'english': [80, 90, 70, 85, 95, 75],
        'hindi': [70, 80, 90, 75, 85, 95],
        'maths': [90, 85, 95, 80, 75, 70],
        'science': [85, 95, 80, 90, 70, 75],
        'social_science': [95, 80, 75, 70, 90, 85]
    })

    analyzer = StudentPerformanceAnalyzer(data)
    analysis_results = analyzer.analyze_performance()

    print("Overall Analysis:")
    print(analysis_results)

    print("\nClass X Performance:")
    print(analyzer.get_class_performance(10))

    print("\nClass XII Performance:")
    print(analyzer.get_class_performance(12))

if __name__ == "__main__":
    main()
```
