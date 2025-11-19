"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitaprojects.co.za
Prompt: Write a Python script that automates daily site visit reports for high-end construction projects, ensuring quality control and project management efficiency.
Generated: DETERMINISTIC_a7aac997c69f2dd4
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import os
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SiteVisitReport:
    """Class to represent a site visit report for construction projects."""
    
    def __init__(self, project_name: str, visit_date: str, observations: List[str], issues: List[str]):
        """
        Initialize a SiteVisitReport instance.

        :param project_name: Name of the construction project
        :param visit_date: Date of the site visit in YYYY-MM-DD format
        :param observations: List of observations made during the site visit
        :param issues: List of issues encountered during the site visit
        """
        self.project_name = project_name
        self.visit_date = visit_date
        self.observations = observations
        self.issues = issues

    def to_dict(self) -> Dict:
        """Convert the report to a dictionary format for JSON serialization."""
        return {
            "project_name": self.project_name,
            "visit_date": self.visit_date,
            "observations": self.observations,
            "issues": self.issues,
        }

    def save_report(self, directory: str) -> None:
        """
        Save the report to a JSON file in the specified directory.

        :param directory: The directory where the report should be saved
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)  # Create directory if it doesn't exist
            
            filename = f"{self.project_name.replace(' ', '_')}_{self.visit_date}.json"
            filepath = os.path.join(directory, filename)

            with open(filepath, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            logging.info(f"Report saved to {filepath}")
        except Exception as e:
            logging.error(f"Failed to save report: {e}")

def get_today_date() -> str:
    """Get today's date in YYYY-MM-DD format."""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def main():
    """Main function to automate the site visit report generation."""
    # Example project details; these would typically be gathered from user input or a database
    project_name = "High-End Construction Project"
    visit_date = get_today_date()
    observations = [
        "Site is clean and well-organized.",
        "Workers are following safety protocols.",
        "Materials are delivered on time."
    ]
    issues = [
        "Delay in concrete delivery.",
        "Need to address scaffolding safety."
    ]

    # Create a site visit report
    report = SiteVisitReport(project_name, visit_date, observations, issues)

    # Specify the directory to save the report
    report_directory = "./site_visit_reports"

    # Save the report
    report.save_report(report_directory)

if __name__ == "__main__":
    main()
```
