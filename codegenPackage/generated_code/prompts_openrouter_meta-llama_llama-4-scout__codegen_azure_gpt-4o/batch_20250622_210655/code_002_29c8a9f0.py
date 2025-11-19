"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Generate a report on the impact of humanitarian projects, including metrics on beneficiaries and project outcomes, for an organization focused on sustainable development like "هيئة الخليج وعدن للتنمية والخدمات الإنسانية".
Generated: DETERMINISTIC_29c8a9f0817ed7cc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime

# Define a class to handle the report generation
class HumanitarianProjectReport:
    def __init__(self, project_data_file):
        """
        Initialize the report generator with the path to the project data file.

        :param project_data_file: Path to the CSV file containing project data.
        """
        self.project_data_file = project_data_file
        self.projects = []

    def load_project_data(self):
        """
        Load project data from a CSV file into memory.

        :raises FileNotFoundError: If the CSV file is not found.
        :raises ValueError: If the CSV file contains invalid data.
        """
        try:
            with open(self.project_data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Validate and parse data
                    project = {
                        "name": row["Project Name"],
                        "start_date": datetime.strptime(row["Start Date"], "%Y-%m-%d"),
                        "end_date": datetime.strptime(row["End Date"], "%Y-%m-%d"),
                        "beneficiaries": int(row["Beneficiaries"]),
                        "outcome": row["Outcome"]
                    }
                    self.projects.append(project)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.project_data_file}' not found.")
        except ValueError as e:
            raise ValueError(f"Invalid data in file '{self.project_data_file}': {e}")

    def generate_report(self):
        """
        Generate a report summarizing the impact of humanitarian projects.

        :return: A dictionary containing the report data.
        """
        report = {
            "total_projects": len(self.projects),
            "total_beneficiaries": sum(project["beneficiaries"] for project in self.projects),
            "projects": []
        }

        for project in self.projects:
            report["projects"].append({
                "name": project["name"],
                "duration_days": (project["end_date"] - project["start_date"]).days,
                "beneficiaries": project["beneficiaries"],
                "outcome": project["outcome"]
            })

        return report

    def save_report_to_file(self, output_file):
        """
        Save the generated report to a JSON file.

        :param output_file: Path to the output JSON file.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            report = self.generate_report()
            with open(output_file, mode='w', encoding='utf-8') as file:
                json.dump(report, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file '{output_file}': {e}")


# Main function to execute the report generation
def main():
    """
    Main function to load project data, generate a report, and save it to a file.
    """
    # Path to the input CSV file containing project data
    input_file = "project_data.csv"
    # Path to the output JSON file for the report
    output_file = "humanitarian_project_report.json"

    try:
        # Create an instance of the report generator
        report_generator = HumanitarianProjectReport(input_file)
        # Load project data
        report_generator.load_project_data()
        # Save the report to a file
        report_generator.save_report_to_file(output_file)
        print(f"Report successfully saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
- The code assumes the input CSV file (`project_data.csv`) has the following columns: `Project Name`, `Start Date`, `End Date`, `Beneficiaries`, and `Outcome`.
- The output is saved as a JSON file (`humanitarian_project_report.json`) with detailed metrics.
- Proper error handling is included for file operations and data validation.
