"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Develop a Python script to analyze patient appointment data for a gastroenterology clinic, including metrics for exams like elastografia hepática and supercrescimento bacteriano.
Generated: DETERMINISTIC_0b98735fe75bc673
Batch ID: 20250612_151301
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
from datetime import datetime

# Define a class for Gastroenterology Clinic Analysis
class GastroenterologyClinicAnalysis:
    def __init__(self, data):
        """
        Initialize the GastroenterologyClinicAnalysis class.

        Args:
            data (pd.DataFrame): A pandas DataFrame containing patient appointment data.
        """
        self.data = data

    def calculate_exam_metrics(self, exam_name):
        """
        Calculate metrics for a specific exam.

        Args:
            exam_name (str): The name of the exam.

        Returns:
            dict: A dictionary containing the exam metrics.
        """
        # Filter data for the specific exam
        exam_data = self.data[self.data['exam'] == exam_name]

        # Calculate metrics
        total_exams = len(exam_data)
        completed_exams = len(exam_data[exam_data['status'] == 'completed'])
        cancellation_rate = len(exam_data[exam_data['status'] == 'cancelled']) / total_exams if total_exams > 0 else 0

        # Return exam metrics
        return {
            'total_exams': total_exams,
            'completed_exams': completed_exams,
            'cancellation_rate': cancellation_rate
        }

    def analyze_elastografia_hepática(self):
        """
        Analyze elastografia hepática exam metrics.

        Returns:
            dict: A dictionary containing the elastografia hepática exam metrics.
        """
        return self.calculate_exam_metrics('elastografia hepática')

    def analyze_supercrescimento_bacteriano(self):
        """
        Analyze supercrescimento bacteriano exam metrics.

        Returns:
            dict: A dictionary containing the supercrescimento bacteriano exam metrics.
        """
        return self.calculate_exam_metrics('supercrescimento bacteriano')

    def generate_report(self):
        """
        Generate a report containing metrics for all exams.

        Returns:
            dict: A dictionary containing the report data.
        """
        # Define exams to analyze
        exams = ['elastografia hepática', 'supercrescimento bacteriano']

        # Initialize report data
        report_data = {}

        # Analyze each exam and add to report data
        for exam in exams:
            if exam == 'elastografia hepática':
                report_data[exam] = self.analyze_elastografia_hepática()
            elif exam == 'supercrescimento bacteriano':
                report_data[exam] = self.analyze_supercrescimento_bacteriano()

        # Return report data
        return report_data


def load_data(file_path):
    """
    Load patient appointment data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the patient appointment data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ['exam', 'status', 'appointment_date']
        if not all(column in data.columns for column in required_columns):
            raise ValueError("The CSV file is missing required columns.")

        # Return loaded data
        return data

    except FileNotFoundError:
        print("The specified file was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("The specified file is empty.")
        return None
    except pd.errors.ParserError:
        print("An error occurred while parsing the specified file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    # Specify the file path to the patient appointment data
    file_path = 'patient_appointment_data.csv'

    # Load patient appointment data
    data = load_data(file_path)

    if data is not None:
        # Create an instance of the GastroenterologyClinicAnalysis class
        analysis = GastroenterologyClinicAnalysis(data)

        # Generate a report containing metrics for all exams
        report = analysis.generate_report()

        # Print the report
        for exam, metrics in report.items():
            print(f"Exam: {exam}")
            print(f"Total Exams: {metrics['total_exams']}")
            print(f"Completed Exams: {metrics['completed_exams']}")
            print(f"Cancellation Rate: {metrics['cancellation_rate']:.2%}")
            print("------------------------")


if __name__ == "__main__":
    main()
```
