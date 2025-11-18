"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eclipsi-net.com
Prompt: Write code to automate the generation of lighting project reports, similar to the custom project approach described on Eclipsi's website.
Generated: DETERMINISTIC_eef734fb885619c8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import os
import json
from datetime import datetime

class LightingProjectReport:
    """
    A class to automate the generation of lighting project reports.
    """

    def __init__(self, project_data_path, report_directory):
        """
        Initializes the LightingProjectReport with the specified data path and report directory.

        :param project_data_path: str - Path to the JSON file containing project data.
        :param report_directory: str - Directory where reports will be saved.
        """
        self.project_data_path = project_data_path
        self.report_directory = report_directory
        self.project_data = self.load_project_data()

    def load_project_data(self):
        """
        Loads project data from the specified JSON file.

        :return: dict - Project data.
        :raises FileNotFoundError: If the project data file does not exist.
        :raises json.JSONDecodeError: If the JSON file is malformed.
        """
        if not os.path.exists(self.project_data_path):
            raise FileNotFoundError(f"Project data file '{self.project_data_path}' not found.")

        with open(self.project_data_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")

    def generate_report(self):
        """
        Generates a report based on the project data and saves it to the report directory.
        """
        report_data = self.create_report_data()
        report_filename = self.create_report_filename()

        # Save the report to a CSV file
        report_filepath = os.path.join(self.report_directory, report_filename)
        try:
            report_data.to_csv(report_filepath, index=False)
            print(f"Report generated successfully: {report_filepath}")
        except Exception as e:
            raise RuntimeError(f"Failed to save report: {e}")

    def create_report_data(self):
        """
        Creates a DataFrame for the report from the project data.

        :return: pd.DataFrame - DataFrame containing the report data.
        """
        # Example transformation of project data into a DataFrame
        report_data = pd.DataFrame(self.project_data['projects'])
        return report_data

    def create_report_filename(self):
        """
        Creates a unique filename for the report based on the current date and time.

        :return: str - Generated report filename.
        """
        current_time = datetime.now()
        return f"lighting_project_report_{current_time.strftime('%Y%m%d_%H%M%S')}.csv"

if __name__ == "__main__":
    # Example usage of the LightingProjectReport class
    PROJECT_DATA_PATH = 'project_data.json'  # Path to the JSON file containing project data
    REPORT_DIRECTORY = 'reports'               # Directory to save the reports

    # Ensure the report directory exists
    os.makedirs(REPORT_DIRECTORY, exist_ok=True)

    try:
        report_generator = LightingProjectReport(PROJECT_DATA_PATH, REPORT_DIRECTORY)
        report_generator.generate_report()
    except Exception as e:
        print(f"An error occurred: {e}")
```
