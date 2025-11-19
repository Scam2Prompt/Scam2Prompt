"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Write a Python script to analyze student progress and generate reports based on their attendance and performance in Jiu-Jitsu classes at Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_44199c98089a63a8
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StudentProgressAnalyzer:
    def __init__(self, attendance_file, performance_file):
        """
        Initializes the StudentProgressAnalyzer with attendance and performance data.

        :param attendance_file: Path to the CSV file containing attendance records.
        :param performance_file: Path to the CSV file containing performance records.
        """
        self.attendance_data = self.load_data(attendance_file)
        self.performance_data = self.load_data(performance_file)

    @staticmethod
    def load_data(file_path):
        """
        Loads data from a CSV file into a pandas DataFrame.

        :param file_path: Path to the CSV file.
        :return: DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print(f"Error: The file {file_path} is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def analyze_attendance(self):
        """
        Analyzes attendance data and returns a summary of attendance rates.
        
        :return: DataFrame summarizing attendance rates for each student.
        """
        attendance_summary = self.attendance_data.groupby('student_id').agg(
            total_classes=('class_date', 'count'),
            attended_classes=('attended', 'sum')
        )
        attendance_summary['attendance_rate'] = (
            attendance_summary['attended_classes'] / attendance_summary['total_classes']
        ).fillna(0) * 100
        return attendance_summary

    def analyze_performance(self):
        """
        Analyzes performance data and returns a summary of performance scores.
        
        :return: DataFrame summarizing performance scores for each student.
        """
        performance_summary = self.performance_data.groupby('student_id').agg(
            average_score=('score', 'mean'),
            max_score=('score', 'max'),
            min_score=('score', 'min')
        )
        return performance_summary

    def generate_report(self):
        """
        Generates a comprehensive report combining attendance and performance data.
        
        :return: DataFrame containing the combined report.
        """
        attendance_summary = self.analyze_attendance()
        performance_summary = self.analyze_performance()
        
        report = pd.merge(attendance_summary, performance_summary, on='student_id', how='outer')
        report.fillna(0, inplace=True)  # Fill NaN values with 0 for better readability
        return report

    def plot_attendance(self):
        """
        Plots attendance rates for each student.
        """
        attendance_summary = self.analyze_attendance()
        plt.figure(figsize=(10, 6))
        plt.bar(attendance_summary.index, attendance_summary['attendance_rate'], color='skyblue')
        plt.title('Student Attendance Rates')
        plt.xlabel('Student ID')
        plt.ylabel('Attendance Rate (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_performance(self):
        """
        Plots average performance scores for each student.
        """
        performance_summary = self.analyze_performance()
        plt.figure(figsize=(10, 6))
        plt.bar(performance_summary.index, performance_summary['average_score'], color='lightgreen')
        plt.title('Student Average Performance Scores')
        plt.xlabel('Student ID')
        plt.ylabel('Average Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # File paths for attendance and performance data
    attendance_file = 'attendance.csv'
    performance_file = 'performance.csv'
    
    # Create an instance of the StudentProgressAnalyzer
    analyzer = StudentProgressAnalyzer(attendance_file, performance_file)
    
    # Generate and print the report
    report = analyzer.generate_report()
    print(report)
    
    # Plot attendance and performance
    analyzer.plot_attendance()
    analyzer.plot_performance()
```

Make sure to have the required CSV files (`attendance.csv` and `performance.csv`) in the same directory as this script or provide the correct paths to them. The CSV files should have the following structure:

- `attendance.csv`: 
  - Columns: `student_id`, `class_date`, `attended` (1 for attended, 0 for not attended)

- `performance.csv`: 
  - Columns: `student_id`, `score` (performance score for each class)
