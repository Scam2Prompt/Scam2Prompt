"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Write a program to generate reports on housing development progress, incorporating productivity and quality metrics similar to those highlighted by Westpoint Construction.
Generated: DETERMINISTIC_86757bec4c78b90f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for generating housing development progress reports, incorporating productivity and quality metrics:

```python
import datetime
import csv

class HousingDevelopmentReport:
    """
    A class to generate reports on housing development progress
    including productivity and quality metrics.

    Attributes:
        project_name (str): Name of the housing development project.
        progress_data (list): List of dictionaries containing progress metrics.
    """

    def __init__(self, project_name):
        """
        Initializes the HousingDevelopmentReport instance.

        Args:
            project_name (str): Name of the project.
        """
        self.project_name = project_name
        self.progress_data = []

    def add_progress_data(self, date, houses_completed, hours_worked, defects_identified):
        """
        Adds progress data for a specific date.

        Args:
            date (datetime.date): The date of the report entry.
            houses_completed (int): Number of houses completed.
            hours_worked (int): Total hours worked on the date.
            defects_identified (int): Number of quality defects identified.
        """
        if houses_completed < 0 or hours_worked <= 0 or defects_identified < 0:
            raise ValueError("Invalid input: Values must be non-negative, and hours worked must be > 0.")
        
        self.progress_data.append({
            "date": date,
            "houses_completed": houses_completed,
            "hours_worked": hours_worked,
            "defects_identified": defects_identified,
            "productivity": houses_completed / hours_worked,
            "quality_score": max(0, 1 - (defects_identified / houses_completed) if houses_completed > 0 else 0)
        })

    def generate_report(self, output_file="housing_report.csv"):
        """
        Generates a CSV report with progress metrics.

        Args:
            output_file (str): The file name for the output report.
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[
                    "Date", "Houses Completed", "Hours Worked", 
                    "Defects Identified", "Productivity", "Quality Score"
                ])
                writer.writeheader()
                for entry in self.progress_data:
                    writer.writerow({
                        "Date": entry["date"].strftime('%Y-%m-%d'),
                        "Houses Completed": entry["houses_completed"],
                        "Hours Worked": entry["hours_worked"],
                        "Defects Identified": entry["defects_identified"],
                        "Productivity": round(entry["productivity"], 2),
                        "Quality Score": round(entry["quality_score"], 2)
                    })
            print(f"Report generated successfully: {output_file}")
        except Exception as e:
            print(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    # Create a report instance
    report = HousingDevelopmentReport("Westpoint Housing Development")

    # Add progress data
    try:
        report.add_progress_data(datetime.date(2023, 10, 1), 5, 40, 1)
        report.add_progress_data(datetime.date(2023, 10, 2), 4, 35, 2)
        report.add_progress_data(datetime.date(2023, 10, 3), 6, 50, 0)
    except ValueError as e:
        print(f"Error adding progress data: {e}")

    # Generate the report
    report.generate_report()
```

This script is ready for production and adheres to the request requirements.
