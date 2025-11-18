"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Create a Python script to generate a report summarizing participation in Egatur events, such as "Feliz Día del Frappe" and "Marcha por la Salud Mental."
Generated: DETERMINISTIC_cdb7248316e44138
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

class EventParticipationReport:
    def __init__(self, events_file, output_file):
        """
        Initialize the EventParticipationReport class.

        Args:
            events_file (str): Path to the CSV file containing event participation data.
            output_file (str): Path to the output file where the summary report will be saved.
        """
        self.events_file = events_file
        self.output_file = output_file

    def generate_report(self):
        """
        Generate a summary report for event participation.

        Reads the events participation data from the input CSV file, aggregates the
        data, and saves a summary report to the output file.
        """
        try:
            # Read event data
            event_data = self._read_events()

            # Aggregate participation data
            summary = self._aggregate_data(event_data)

            # Write summary report
            self._write_report(summary)

            print(f"Report generated successfully: {self.output_file}")

        except Exception as e:
            print(f"An error occurred while generating the report: {e}")

    def _read_events(self):
        """
        Read event participation data from the CSV file.

        Returns:
            list: A list of dictionaries containing event participation data.
        """
        if not os.path.exists(self.events_file):
            raise FileNotFoundError(f"Events file not found: {self.events_file}")

        event_data = []
        try:
            with open(self.events_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    event_data.append(row)
        except Exception as e:
            raise Exception(f"Error reading events file: {e}")

        return event_data

    def _aggregate_data(self, event_data):
        """
        Aggregate participation data for events.

        Args:
            event_data (list): A list of dictionaries containing event participation data.

        Returns:
            dict: A dictionary summarizing participation counts for each event.
        """
        summary = {}
        for entry in event_data:
            event_name = entry.get('Event Name', 'Unknown Event')
            participants = int(entry.get('Participants', 0))

            if event_name in summary:
                summary[event_name] += participants
            else:
                summary[event_name] = participants

        return summary

    def _write_report(self, summary):
        """
        Write the summary report to the output file.

        Args:
            summary (dict): A dictionary summarizing participation counts for each event.
        """
        try:
            with open(self.output_file, mode='w', encoding='utf-8') as file:
                file.write("Event Participation Summary Report\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                file.write("Event Name,Participants\n")

                for event_name, participants in summary.items():
                    file.write(f"{event_name},{participants}\n")

        except Exception as e:
            raise Exception(f"Error writing report file: {e}")


# Example usage (replace 'events.csv' with your input file and 'report.csv' with your desired output file):
if __name__ == "__main__":
    events_file = 'events.csv'  # Input CSV file containing event participation data
    output_file = 'report.csv'  # Output file for the summary report

    report_generator = EventParticipationReport(events_file, output_file)
    report_generator.generate_report()
```
