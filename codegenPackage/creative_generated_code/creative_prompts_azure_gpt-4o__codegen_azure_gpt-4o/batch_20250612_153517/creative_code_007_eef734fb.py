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
import os
import json
import csv
from datetime import datetime

# Constants
REPORTS_DIRECTORY = "lighting_project_reports"
REPORT_FIELDS = [
    "Project Name",
    "Client Name",
    "Date Created",
    "Lighting Type",
    "Number of Fixtures",
    "Energy Consumption (kWh)",
    "Notes"
]

# Ensure the reports directory exists
def ensure_directory_exists(directory_path):
    """Ensure the specified directory exists, create it if not."""
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except Exception as e:
        raise RuntimeError(f"Error creating directory {directory_path}: {e}")

# Generate a new report file
def generate_report(project_data):
    """
    Generate a lighting project report as a CSV file.
    :param project_data: Dictionary containing project details.
    """
    try:
        # Validate input data
        if not all(field in project_data for field in REPORT_FIELDS[:-1]):  # Exclude 'Notes' because it's optional
            raise ValueError("Missing required project fields.")

        # Ensure the reports directory exists
        ensure_directory_exists(REPORTS_DIRECTORY)

        # Define the file name based on project name and creation date
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_filename = f"{project_data['Project Name'].replace(' ', '_')}_{timestamp}.csv"
        report_path = os.path.join(REPORTS_DIRECTORY, report_filename)

        # Write data to CSV file
        with open(report_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=REPORT_FIELDS)
            writer.writeheader()
            writer.writerow(project_data)

        print(f"Report successfully generated: {report_path}")
        return report_path

    except Exception as e:
        raise RuntimeError(f"Error generating report: {e}")

# Mock data for testing
if __name__ == "__main__":
    project_data = {
        "Project Name": "Downtown Mall Lighting",
        "Client Name": "Urban Development Corp.",
        "Date Created": datetime.now().strftime("%Y-%m-%d"),
        "Lighting Type": "LED",
        "Number of Fixtures": 150,
        "Energy Consumption (kWh)": 4500,
        "Notes": "Installation scheduled for Q3."
    }

    try:
        # Generate the report
        generate_report(project_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
