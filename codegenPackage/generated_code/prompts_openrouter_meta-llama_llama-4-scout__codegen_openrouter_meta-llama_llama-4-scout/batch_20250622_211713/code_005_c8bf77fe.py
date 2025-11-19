"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Write a code snippet in a programming language to analyze student performance in CBSE Physics exams and provide recommendations for improvement.
Generated: DETERMINISTIC_c8bf77fe24b92dba
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class StudentPerformanceAnalyzer:
    """
    Analyzes student performance in CBSE Physics exams and provides recommendations for improvement.
    """

    def __init__(self, student_data):
        """
        Initializes the analyzer with student data.

        Args:
            student_data (pd.DataFrame): A DataFrame containing student data.
                It should have the following columns:
                    - 'Student ID'
                    - 'Name'
                    - 'Marks Obtained'
                    - 'Total Marks'
        """
        self.student_data = student_data

    def calculate_performance(self):
        """
        Calculates the performance of each student.

        Returns:
            pd.DataFrame: A DataFrame containing student performance data.
                It has the following columns:
                    - 'Student ID'
                    - 'Name'
                    - 'Percentage'
                    - 'Grade'
        """
        # Calculate percentage
        self.student_data['Percentage'] = (self.student_data['Marks Obtained'] / self.student_data['Total Marks']) * 100

        # Assign grades based on percentage
        self.student_data['Grade'] = self.student_data['Percentage'].apply(self.assign_grade)

        return self.student_data

    def assign_grade(self, percentage):
        """
        Assigns a grade based on the percentage.

        Args:
            percentage (float): The percentage of marks obtained.

        Returns:
            str: The grade.
        """
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        else:
            return 'F'

    def provide_recommendations(self):
        """
        Provides recommendations for improvement.

        Returns:
            dict: A dictionary containing recommendations for each student.
        """
        recommendations = {}

        # Iterate over each student
        for index, row in self.student_data.iterrows():
            if row['Grade'] != 'A+':
                # Provide recommendations based on grade
                if row['Grade'] == 'A':
                    recommendations[row['Student ID']] = 'Focus on weak areas to improve to A+.'
                elif row['Grade'] == 'B+':
                    recommendations[row['Student ID']] = 'Work hard to improve to A or A+.'
                elif row['Grade'] == 'B':
                    recommendations[row['Student ID']] = 'Put in more effort to improve to B+ or A.'
                elif row['Grade'] == 'C':
                    recommendations[row['Student ID']] = 'Significantly improve to pass with good grades.'
                elif row['Grade'] == 'F':
                    recommendations[row['Student ID']] = 'Work hard to pass the exam.'

        return recommendations


def main():
    try:
        # Sample student data
        data = {
            'Student ID': [1, 2, 3, 4, 5],
            'Name': ['John', 'Emma', 'Michael', 'Sophia', 'William'],
            'Marks Obtained': [85, 90, 78, 92, 45],
            'Total Marks': [100, 100, 100, 100, 100]
        }

        # Create a DataFrame
        student_data = pd.DataFrame(data)

        # Create an instance of the analyzer
        analyzer = StudentPerformanceAnalyzer(student_data)

        # Calculate performance
        performance_data = analyzer.calculate_performance()

        # Print performance data
        print("Performance Data:")
        print(performance_data)

        # Provide recommendations
        recommendations = analyzer.provide_recommendations()

        # Print recommendations
        print("\nRecommendations:")
        for student_id, recommendation in recommendations.items():
            print(f"Student ID: {student_id}, Recommendation: {recommendation}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
