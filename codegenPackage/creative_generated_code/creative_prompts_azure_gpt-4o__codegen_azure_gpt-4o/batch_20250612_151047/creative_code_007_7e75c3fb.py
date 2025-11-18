"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aknanalofiq.com
Prompt: Write a script to generate a report of completed projects for residential, commercial, and hospital facilities, referencing AKNAN's expertise and services.
Generated: DETERMINISTIC_7e75c3fb361577b4
Batch ID: 20250612_151047
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


# --- Constants ---
REPORT_FILENAME = "completed_projects_report.csv"
FACILITY_TYPES = ["Residential", "Commercial", "Hospital"]
AKNAN_SERVICES = ["Design", "Construction", "Renovation", "Consultation"]


# --- Functions ---
def generate_completed_projects():
    """
    Simulates fetching completed project data.
    Returns a list of dictionaries representing completed projects.
    """
    return [
        {"Project Name": "Sunshine Apartments", "Facility Type": "Residential", "Completion Date": "2023-05-12", "Services Provided": "Design, Construction"},
        {"Project Name": "Downtown Mall", "Facility Type": "Commercial", "Completion Date": "2022-10-18", "Services Provided": "Renovation, Consultation"},
        {"Project Name": "City Hospital", "Facility Type": "Hospital", "Completion Date": "2023-01-23", "Services Provided": "Design, Construction"},
    ]


def validate_project_data(project_data):
    """
    Validates the project data to ensure integrity.
    Args:
        project_data (dict): A dictionary containing project details.
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        # Ensure required keys exist
        required_keys = ["Project Name", "Facility Type", "Completion Date", "Services Provided"]
        for key in required_keys:
            if key not in project_data:
                raise ValueError(f"Missing key: {key}")

        # Validate Facility Type
        if project_data["Facility Type"] not in FACILITY_TYPES:
            raise ValueError(f"Invalid Facility Type: {project_data['Facility Type']}")

        # Validate Completion Date
        datetime.strptime(project_data["Completion Date"], "%Y-%m-%d")

        # Validate Services Provided
        services = project_data["Services Provided"].split(", ")
        for service in services:
            if service not in AKNAN_SERVICES:
                raise ValueError(f"Invalid Service: {service}")

        return True
    except Exception as e:
        print(f"Error validating project data: {e}")
        return False


def generate_report(projects):
    """
    Generates a CSV report of completed projects.
    Args:
        projects (list): A list of dictionaries containing project data.
    Returns:
        None
    """
    try:
        with open(REPORT_FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Project Name", "Facility Type", "Completion Date", "Services Provided"])
            writer.writeheader()
            
            for project in projects:
                if validate_project_data(project):
                    writer.writerow(project)
                else:
                    print(f"Skipping invalid project: {project}")

        print(f"Report generated successfully: {REPORT_FILENAME}")
    except Exception as e:
        print(f"Error generating report: {e}")


# --- Main Program ---
if __name__ == "__main__":
    # Fetch completed projects
    projects = generate_completed_projects()

    # Generate report
    generate_report(projects)
```
