"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Develop a Python script that generates a report summarizing the number of projects completed by a company like Sadad Engineering, categorized by type (e.g., metro stations, hospitals, parks).
Generated: DETERMINISTIC_63c73618cba2cfc7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from collections import defaultdict

class ProjectReportGenerator:
    def __init__(self, data_file):
        """
        Initializes the report generator with the path to the data file.

        :param data_file: Path to the JSON file containing project data
        """
        self.data_file = data_file

    def load_data(self):
        """
        Loads project data from the specified JSON file.

        :return: List of projects
        :raises FileNotFoundError: If the data file does not exist
        :raises json.JSONDecodeError: If the data file is not valid JSON
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")

        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError("Error decoding JSON data", e)

    def generate_report(self):
        """
        Generates a report summarizing the number of projects by type.

        :return: A dictionary containing the project count by type
        """
        projects = self.load_data()
        report = defaultdict(int)

        # Categorize projects by type
        for project in projects:
            project_type = project.get('type', 'Unknown')
            report[project_type] += 1

        return dict(report)

    def save_report(self, report, output_file):
        """
        Saves the generated report to a specified output file.

        :param report: Dictionary containing project summaries
        :param output_file: Path to the output file
        :raises IOError: If the output file cannot be written
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(report, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to output file '{output_file}': {e}")

def main():
    data_file = 'projects.json'  # Input data file containing project details
    output_file = 'project_report.json'  # Output report file

    try:
        report_generator = ProjectReportGenerator(data_file)
        report = report_generator.generate_report()
        report_generator.save_report(report, output_file)
        print(f"Report generated successfully: {output_file}")
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
