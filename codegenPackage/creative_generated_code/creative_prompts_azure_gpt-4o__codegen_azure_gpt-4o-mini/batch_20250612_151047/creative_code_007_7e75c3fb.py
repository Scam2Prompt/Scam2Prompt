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
import logging
from datetime import datetime
from typing import List, Dict

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a Project class to represent project details
class Project:
    def __init__(self, name: str, project_type: str, completion_date: str, services: List[str]):
        self.name = name
        self.project_type = project_type
        self.completion_date = self.parse_date(completion_date)
        self.services = services

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """Parses a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date: {date_str}. {e}")
            raise

# Function to load project data from a CSV file
def load_projects_from_csv(file_path: str) -> List[Project]:
    """Loads project data from a CSV file and returns a list of Project objects."""
    projects = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                project = Project(
                    name=row['name'],
                    project_type=row['type'],
                    completion_date=row['completion_date'],
                    services=row['services'].split(';')  # Assume services are semicolon-separated
                )
                projects.append(project)
        logging.info(f"Loaded {len(projects)} projects from {file_path}.")
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading projects: {e}")
        raise
    return projects

# Function to generate a report of completed projects
def generate_project_report(projects: List[Project], report_type: str) -> Dict[str, List[Project]]:
    """Generates a report of completed projects categorized by project type."""
    report = {}
    for project in projects:
        if project.project_type not in report:
            report[project.project_type] = []
        report[project.project_type].append(project)

    logging.info(f"Generated report with {len(report)} categories.")
    return report

# Function to save the report to a text file
def save_report_to_file(report: Dict[str, List[Project]], output_file: str) -> None:
    """Saves the generated report to a text file."""
    try:
        with open(output_file, mode='w') as file:
            for project_type, projects in report.items():
                file.write(f"--- {project_type.upper()} PROJECTS ---\n")
                for project in projects:
                    file.write(f"Name: {project.name}, Completion Date: {project.completion_date.date()}, Services: {', '.join(project.services)}\n")
                file.write("\n")
        logging.info(f"Report saved to {output_file}.")
    except Exception as e:
        logging.error(f"An error occurred while writing to the file: {e}")
        raise

def main():
    """Main function to execute the report generation."""
    # Define file paths and output file
    input_file_path = 'projects.csv'
    output_file_path = 'completed_projects_report.txt'

    # Load the projects from CSV
    projects = load_projects_from_csv(input_file_path)

    # Generate the project report
    project_report = generate_project_report(projects, report_type="completed")

    # Save the report to a file
    save_report_to_file(project_report, output_file_path)

if __name__ == "__main__":
    main()
```
