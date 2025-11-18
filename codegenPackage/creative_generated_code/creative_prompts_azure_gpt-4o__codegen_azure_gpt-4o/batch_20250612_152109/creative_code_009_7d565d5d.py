"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Write code to generate a summary report of the health extension activities conducted by MIMSR, including blood donation camps and multi-diagnostic camps.
Generated: DETERMINISTIC_7d565d5dedde0f04
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime


class HealthExtensionReport:
    """
    A class to generate a summary report of health extension activities
    conducted by MIMSR, including blood donation camps and multi-diagnostic camps.
    """

    def __init__(self, data_source):
        """
        Initializes the HealthExtensionReport object.

        Args:
        data_source (str): Path to the CSV file containing activity data.
        """
        self.data_source = data_source
        self.activities = []

    def load_data(self):
        """
        Loads activity data from the specified CSV file.

        The CSV file is expected to have the following columns:
        - activity_type: Type of activity (e.g., "Blood Donation", "Multi-Diagnostic")
        - date: Date of the activity (e.g., "YYYY-MM-DD")
        - participants: Number of participants
        """
        try:
            with open(self.data_source, mode='r') as file:
                reader = csv.DictReader(file)
                self.activities = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file '{self.data_source}' was not found.")
        except Exception as e:
            print(f"Error occurred while reading the file: {e}")

    def generate_report(self):
        """
        Generates a summary report of health extension activities.

        The report includes:
        - Total number of activities
        - Breakdown by activity type
        - Total participants for each activity type
        """
        if not self.activities:
            print("No activity data available. Please load data first.")
            return

        report = {
            "total_activities": 0,
            "activity_summary": {}
        }

        for activity in self.activities:
            activity_type = activity['activity_type']
            participants = int(activity['participants'])
            report["total_activities"] += 1

            if activity_type not in report["activity_summary"]:
                report["activity_summary"][activity_type] = {"count": 0, "participants": 0}

            report["activity_summary"][activity_type]["count"] += 1
            report["activity_summary"][activity_type]["participants"] += participants

        return report

    def display_report(self, report):
        """
        Displays the generated summary report in a readable format.

        Args:
        report (dict): The report dictionary containing summary information.
        """
        print("========== MIMSR Health Extension Summary Report ==========")
        print(f"Total Activities: {report['total_activities']}")
        print("-----------------------------------------------------------")
        print("Activity Breakdown:")
        for activity_type, details in report['activity_summary'].items():
            print(f"- {activity_type}:")
            print(f"  - Count: {details['count']}")
            print(f"  - Participants: {details['participants']}")
        print("===========================================================")


if __name__ == "__main__":
    # Path to the CSV file containing activity data
    data_source = 'activities.csv'

    # Create an instance of HealthExtensionReport
    report_generator = HealthExtensionReport(data_source)

    # Load data from file
    report_generator.load_data()

    # Generate the report
    summary_report = report_generator.generate_report()

    # Display the report (if available)
    if summary_report:
        report_generator.display_report(summary_report)
```

**Instructions for Usage:**
1. Save the code to a Python file, such as `health_extension_report.py`.
2. Provide a CSV file named `activities.csv` in the same directory with the necessary columns:
    ```
    activity_type,date,participants
    Blood Donation,2023-10-01,50
    Multi-Diagnostic,2023-10-05,100
    ```
3. Run the script using Python (`python health_extension_report.py`).
