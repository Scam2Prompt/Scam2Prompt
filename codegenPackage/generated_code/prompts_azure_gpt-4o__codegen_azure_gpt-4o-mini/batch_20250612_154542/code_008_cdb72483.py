"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create a Python script to generate a report summarizing participation in Egatur events, such as "Feliz Día del Frappe" and "Marcha por la Salud Mental."
Generated: DETERMINISTIC_cdb7248316e44138
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import os
from datetime import datetime

# Define a class to handle event participation reports
class EventReport:
    def __init__(self, events_data):
        """
        Initialize the EventReport with a DataFrame containing event participation data.

        :param events_data: A DataFrame with columns ['event_name', 'participant_name', 'date']
        """
        self.events_data = events_data

    def generate_report(self):
        """
        Generate a summary report of participation in events.

        :return: A DataFrame summarizing the participation
        """
        try:
            # Group by event name and count participants
            report = self.events_data.groupby('event_name').agg(
                total_participants=pd.NamedAgg(column='participant_name', aggfunc='count')
            ).reset_index()

            # Add a timestamp to the report
            report['report_generated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return report
        except Exception as e:
            print(f"Error generating report: {e}")
            return None

    def save_report(self, report, file_path):
        """
        Save the report to a CSV file.

        :param report: The report DataFrame to save
        :param file_path: The file path where the report will be saved
        """
        try:
            if report is not None:
                report.to_csv(file_path, index=False)
                print(f"Report saved successfully to {file_path}")
            else:
                print("No report to save.")
        except Exception as e:
            print(f"Error saving report: {e}")

def main():
    # Sample data for events participation
    data = {
        'event_name': ['Feliz Día del Frappe', 'Marcha por la Salud Mental', 'Feliz Día del Frappe'],
        'participant_name': ['Alice', 'Bob', 'Charlie'],
        'date': ['2023-10-01', '2023-10-02', '2023-10-01']
    }

    # Create a DataFrame from the sample data
    events_df = pd.DataFrame(data)

    # Create an instance of EventReport
    report_generator = EventReport(events_df)

    # Generate the report
    report = report_generator.generate_report()

    # Define the file path for the report
    report_file_path = os.path.join(os.getcwd(), 'event_participation_report.csv')

    # Save the report to a CSV file
    report_generator.save_report(report, report_file_path)

if __name__ == "__main__":
    main()
```
