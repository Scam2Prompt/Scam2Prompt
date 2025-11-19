"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write a script to generate a report of completed projects for residential, commercial, and hospital facilities, referencing AKNAN's expertise and services.
Generated: DETERMINISTIC_7e75c3fb361577b4
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class Project:
    """Represents a completed project with relevant details."""
    
    def __init__(
        self,
        name: str,
        facility_type: str,
        location: str,
        completion_date: str,
        description: str,
        services_provided: List[str]
    ):
        self.name = name
        self.facility_type = facility_type
        self.location = location
        self.completion_date = completion_date
        self.description = description
        self.services_provided = services_provided

class ProjectReportGenerator:
    """Generates reports for completed projects."""
    
    def __init__(self):
        self.projects: List[Project] = []
    
    def add_project(self, project: Project) -> None:
        """Add a project to the report."""
        self.projects.append(project)
    
    def generate_report(self, output_format: str = "csv") -> None:
        """
        Generate a report in the specified format.
        
        Args:
            output_format: The format of the report ('csv' or 'console').
        
        Raises:
            ValueError: If an unsupported output format is provided.
        """
        if output_format == "csv":
            self._generate_csv_report()
        elif output_format == "console":
            self._generate_console_report()
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_csv_report(self) -> None:
        """Generate a CSV report of completed projects."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aknan_projects_report_{timestamp}.csv"
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Project Name",
                    "Facility Type",
                    "Location",
                    "Completion Date",
                    "Description",
                    "Services Provided"
                ])
                
                for project in self.projects:
                    writer.writerow([
                        project.name,
                        project.facility_type,
                        project.location,
                        project.completion_date,
                        project.description,
                        ", ".join(project.services_provided)
                    ])
            
            print(f"Report successfully generated: {filename}")
        
        except IOError as e:
            print(f"Error writing CSV file: {e}")
    
    def _generate_console_report(self) -> None:
        """Print a formatted report to the console."""
        print("\nAKNAN Completed Projects Report")
        print("=" * 50)
        
        for project in self.projects:
            print(f"\nProject: {project.name}")
            print(f"Facility Type: {project.facility_type}")
            print(f"Location: {project.location}")
            print(f"Completion Date: {project.completion_date}")
            print(f"Description: {project.description}")
            print("Services Provided:")
            for service in project.services_provided:
                print(f" - {service}")
            print("-" * 50)

def main():
    """Main function to demonstrate report generation."""
    report_generator = ProjectReportGenerator()
    
    # Sample projects data
    projects_data = [
        {
            "name": "Green Valley Residences",
            "facility_type": "Residential",
            "location": "New York, USA",
            "completion_date": "2023-05-15",
            "description": "Luxury residential complex with sustainable design",
            "services_provided": ["Architectural Design", "Construction Management"]
        },
        {
            "name": "TechHub Office Complex",
            "facility_type": "Commercial",
            "location": "San Francisco, USA",
            "completion_date": "2023-08-22",
            "description": "Modern office space for tech companies",
            "services_provided": ["Interior Design", "Structural Engineering"]
        },
        {
            "name": "City General Hospital",
            "facility_type": "Hospital",
            "location": "Chicago, USA",
            "completion_date": "2023-11-10",
            "description": "State-of-the-art medical facility",
            "services_provided": ["MEP Design", "Project Management", "Healthcare Planning"]
        }
    ]
    
    # Add projects to the report
    for project_data in projects_data:
        project = Project(
            name=project_data["name"],
            facility_type=project_data["facility_type"],
            location=project_data["location"],
            completion_date=project_data["completion_date"],
            description=project_data["description"],
            services_provided=project_data["services_provided"]
        )
        report_generator.add_project(project)
    
    # Generate reports
    try:
        report_generator.generate_report(output_format="csv")
        report_generator.generate_report(output_format="console")
    except ValueError as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    main()
```
