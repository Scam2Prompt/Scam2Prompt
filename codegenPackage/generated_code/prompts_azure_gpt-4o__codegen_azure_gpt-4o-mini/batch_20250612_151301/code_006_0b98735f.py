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
import pandas as pd
import numpy as np

class AppointmentAnalyzer:
    """
    A class to analyze patient appointment data for a gastroenterology clinic.
    """

    def __init__(self, data_file):
        """
        Initializes the AppointmentAnalyzer with the provided data file.

        :param data_file: str, path to the CSV file containing appointment data
        """
        self.data_file = data_file
        self.appointments = self.load_data()

    def load_data(self):
        """
        Loads appointment data from a CSV file.

        :return: DataFrame containing appointment data
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_exams(self):
        """
        Analyzes the appointment data for specific exams and returns metrics.

        :return: dict containing metrics for elastografia hepática and supercrescimento bacteriano
        """
        try:
            # Filter for specific exams
            elastografia_count = self.appointments[self.appointments['exam'] == 'elastografia hepática'].shape[0]
            supercrescimento_count = self.appointments[self.appointments['exam'] == 'supercrescimento bacteriano'].shape[0]

            # Calculate total appointments
            total_appointments = self.appointments.shape[0]

            # Calculate percentages
            elastografia_percentage = (elastografia_count / total_appointments) * 100 if total_appointments > 0 else 0
            supercrescimento_percentage = (supercrescimento_count / total_appointments) * 100 if total_appointments > 0 else 0

            # Prepare metrics
            metrics = {
                'total_appointments': total_appointments,
                'elastografia_count': elastografia_count,
                'elastografia_percentage': elastografia_percentage,
                'supercrescimento_count': supercrescimento_count,
                'supercrescimento_percentage': supercrescimento_percentage
            }

            return metrics
        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            raise

    def display_metrics(self, metrics):
        """
        Displays the calculated metrics in a readable format.

        :param metrics: dict, metrics to display
        """
        print("\nAppointment Analysis Metrics:")
        print(f"Total Appointments: {metrics['total_appointments']}")
        print(f"Elastografia Hepática Count: {metrics['elastografia_count']} ({metrics['elastografia_percentage']:.2f}%)")
        print(f"Supercrescimento Bacteriano Count: {metrics['supercrescimento_count']} ({metrics['supercrescimento_percentage']:.2f}%)")

if __name__ == "__main__":
    # Path to the appointment data CSV file
    data_file_path = 'appointments.csv'

    # Create an instance of AppointmentAnalyzer
    analyzer = AppointmentAnalyzer(data_file_path)

    # Analyze the exams and get metrics
    metrics = analyzer.analyze_exams()

    # Display the metrics
    analyzer.display_metrics(metrics)
```
