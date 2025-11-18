"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumaipce.com
Prompt: Develop a Python-based solution for fiscalization and consultancy in civil engineering projects, aligned with Puma Ipce's specialized services.
Generated: DETERMINISTIC_8b9ac4b6ad6fada2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class ProjectFiscalization:
    """
    Class to handle fiscalization and consultancy for civil engineering projects.
    """

    def __init__(self, project_name, budget, start_date, end_date):
        """
        Initialize a civil engineering project.

        :param project_name: Name of the project
        :param budget: Allocated budget for the project
        :param start_date: Start date of the project (YYYY-MM-DD format)
        :param end_date: End date of the project (YYYY-MM-DD format)
        """
        self.project_name = project_name
        self.budget = budget
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.consultancy_records = []

    def _validate_date(self, date_str):
        """
        Validate and parse date strings into datetime objects.

        :param date_str: Date in YYYY-MM-DD format
        :return: datetime object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected YYYY-MM-DD.")

    def add_consultancy(self, consultant_name, consultancy_date, notes):
        """
        Add a consultancy record to the project.

        :param consultant_name: Name of the consultant
        :param consultancy_date: Date of consultancy (YYYY-MM-DD format)
        :param notes: Notes or recommendations from the consultancy
        """
        consultancy_date = self._validate_date(consultancy_date)
        if consultancy_date < self.start_date or consultancy_date > self.end_date:
            raise ValueError("Consultancy date must be within the project's start and end dates.")
        
        self.consultancy_records.append({
            "consultant_name": consultant_name,
            "consultancy_date": consultancy_date.strftime("%Y-%m-%d"),
            "notes": notes
        })

    def generate_report(self, file_name="project_report.json"):
        """
        Generate a fiscalization report and save it as a JSON file.

        :param file_name: Name of the output file
        """
        report_data = {
            "project_name": self.project_name,
            "budget": self.budget,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "consultancy_records": self.consultancy_records
        }
        try:
            with open(file_name, "w") as file:
                json.dump(report_data, file, indent=4)
            print(f"Report successfully generated: {file_name}")
        except IOError as e:
            print(f"Error writing report to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a project
        project = ProjectFiscalization(
            project_name="Bridge Construction Project",
            budget=5000000,
            start_date="2023-01-01",
            end_date="2023-12-31"
        )

        # Add consultancy records
        project.add_consultancy(
            consultant_name="John Doe",
            consultancy_date="2023-03-15",
            notes="Recommended additional supports for bridge foundation."
        )

        project.add_consultancy(
            consultant_name="Jane Smith",
            consultancy_date="2023-06-10",
            notes="Suggested changes to material specifications for durability."
        )

        # Generate fiscalization report
        project.generate_report("bridge_project_report.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
