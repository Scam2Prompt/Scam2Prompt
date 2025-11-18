"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Develop a Python script to analyze patient appointment data for a gastroenterology clinic, including metrics for exams like elastografia hepática and supercrescimento bacteriano.
Generated: DETERMINISTIC_0b98735fe75bc673
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class AppointmentAnalyzer:
    """
    A class to analyze patient appointment data for a gastroenterology clinic.
    """

    def __init__(self, data_file):
        """
        Initializes the AppointmentAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing appointment data
        """
        self.data_file = data_file
        self.appointments_df = self.load_data()

    def load_data(self):
        """
        Loads appointment data from a CSV file into a DataFrame.

        :return: pd.DataFrame containing appointment data
        """
        try:
            df = pd.read_csv(self.data_file)
            # Ensure the necessary columns are present
            required_columns = ['patient_id', 'appointment_date', 'exam_type', 'status']
            if not all(column in df.columns for column in required_columns):
                raise ValueError("Missing required columns in the input data.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {str(e)}")

    def analyze_exams(self):
        """
        Analyzes metrics for specific exams: elastografia hepática and supercrescimento bacteriano.

        :return: dict, containing counts and percentages for the exams
        """
        analysis_results = {}
        exam_types = ['elastografia hepática', 'supercrescimento bacteriano']

        for exam in exam_types:
            # Filter data for the specific exam type
            exam_data = self.appointments_df[self.appointments_df['exam_type'] == exam]
            total_appointments = len(exam_data)
            completed_appointments = len(exam_data[exam_data['status'] == 'completed'])
            cancelled_appointments = len(exam_data[exam_data['status'] == 'cancelled'])

            if total_appointments > 0:
                analysis_results[exam] = {
                    'total': total_appointments,
                    'completed': completed_appointments,
                    'cancelled': cancelled_appointments,
                    'completion_rate': completed_appointments / total_appointments * 100
                }
            else:
                analysis_results[exam] = {
                    'total': 0,
                    'completed': 0,
                    'cancelled': 0,
                    'completion_rate': 0.0
                }

        return analysis_results

    def generate_report(self):
        """
        Generates a report of the appointment analysis.

        :return: str, formatted report of the analysis
        """
        results = self.analyze_exams()
        report_lines = []

        for exam, metrics in results.items():
            report_lines.append(
                f"Exam: {exam}\n"
                f"Total Appointments: {metrics['total']}\n"
                f"Completed Appointments: {metrics['completed']}\n"
                f"Cancelled Appointments: {metrics['cancelled']}\n"
                f"Completion Rate: {metrics['completion_rate']:.2f}%\n"
            )

        return "\n".join(report_lines)

if __name__ == "__main__":
    # Path to the patient appointment data CSV file
    data_file_path = 'patient_appointments.csv'

    try:
        analyzer = AppointmentAnalyzer(data_file_path)
        report = analyzer.generate_report()
        print(report)
    except Exception as e:
        print(f"Error: {str(e)}")
```
