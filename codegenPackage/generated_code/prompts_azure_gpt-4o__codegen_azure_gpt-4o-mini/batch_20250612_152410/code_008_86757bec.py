"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write a program to generate reports on housing development progress, incorporating productivity and quality metrics similar to those highlighted by Westpoint Construction.
Generated: DETERMINISTIC_86757bec4c78b90f
Batch ID: 20250612_152410
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

class HousingDevelopmentReport:
    """
    A class to generate reports on housing development progress, incorporating productivity and quality metrics.
    """

    def __init__(self, data):
        """
        Initializes the report with the provided data.

        :param data: A pandas DataFrame containing housing development data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.

        :raises ValueError: If required columns are missing.
        """
        required_columns = ['date', 'units_completed', 'units_started', 'quality_score']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_productivity_metrics(self):
        """
        Calculates productivity metrics such as completion rate and start rate.

        :return: A DataFrame with productivity metrics.
        """
        self.data['completion_rate'] = self.data['units_completed'] / self.data['units_started'].replace(0, np.nan)
        return self.data[['date', 'completion_rate']]

    def calculate_quality_metrics(self):
        """
        Calculates average quality score over the reporting period.

        :return: A float representing the average quality score.
        """
        return self.data['quality_score'].mean()

    def generate_report(self):
        """
        Generates a comprehensive report including productivity and quality metrics.

        :return: A summary report as a dictionary.
        """
        self.validate_data()
        productivity_metrics = self.calculate_productivity_metrics()
        average_quality = self.calculate_quality_metrics()

        report = {
            'productivity_metrics': productivity_metrics,
            'average_quality_score': average_quality
        }
        return report

    def plot_productivity(self):
        """
        Plots the productivity metrics over time.

        :raises ValueError: If the data has not been validated or is empty.
        """
        self.validate_data()
        if self.data.empty:
            raise ValueError("Data is empty. Cannot plot productivity metrics.")

        plt.figure(figsize=(10, 5))
        plt.plot(self.data['date'], self.data['completion_rate'], marker='o', linestyle='-')
        plt.title('Housing Development Productivity Over Time')
        plt.xlabel('Date')
        plt.ylabel('Completion Rate')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'date': pd.date_range(start='2023-01-01', periods=5, freq='M'),
        'units_completed': [10, 20, 15, 30, 25],
        'units_started': [15, 25, 20, 35, 30],
        'quality_score': [80, 85, 90, 75, 88]
    }

    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    # Generate the report
    report_generator = HousingDevelopmentReport(df)
    report = report_generator.generate_report()

    # Print the report
    print("Productivity Metrics:")
    print(report['productivity_metrics'])
    print(f"Average Quality Score: {report['average_quality_score']}")

    # Plot the productivity metrics
    report_generator.plot_productivity()
```
