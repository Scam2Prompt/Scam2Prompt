"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write a program to generate reports on housing development progress, incorporating productivity and quality metrics similar to those highlighted by Westpoint Construction.
Generated: DETERMINISTIC_86757bec4c78b90f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional, Any

class HousingDevelopmentReportGenerator:
    """
    A class to generate reports on housing development progress with productivity and quality metrics.
    """

    def __init__(self, projects_data: List[Dict[str, Any]]):
        """
        Initialize the report generator with project data.

        Args:
            projects_data: List of dictionaries containing project information.
        """
        self.projects_data = projects_data
        self.report_data = []

    def calculate_productivity_metrics(self, project: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate productivity metrics for a given project.

        Args:
            project: Dictionary containing project data.

        Returns:
            Dictionary with calculated productivity metrics.
        """
        planned_days = project.get('planned_duration_days', 1)
        actual_days = project.get('actual_duration_days', 1)
        planned_units = project.get('planned_units', 1)
        completed_units = project.get('completed_units', 0)

        schedule_variance = (planned_days - actual_days) / planned_days * 100
        units_per_day = completed_units / actual_days if actual_days > 0 else 0
        planned_units_per_day = planned_units / planned_days if planned_days > 0 else 0
        productivity_ratio = units_per_day / planned_units_per_day if planned_units_per_day > 0 else 0

        return {
            'schedule_variance_percent': schedule_variance,
            'units_per_day': units_per_day,
            'productivity_ratio': productivity_ratio
        }

    def calculate_quality_metrics(self, project: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate quality metrics for a given project.

        Args:
            project: Dictionary containing project data.

        Returns:
            Dictionary with calculated quality metrics.
        """
        inspections_passed = project.get('inspections_passed', 0)
        total_inspections = project.get('total_inspections', 1)
        defects_found = project.get('defects_found', 0)
        total_units = project.get('completed_units', 1)

        inspection_pass_rate = (inspections_passed / total_inspections) * 100
        defects_per_unit = defects_found / total_units if total_units > 0 else 0

        return {
            'inspection_pass_rate_percent': inspection_pass_rate,
            'defects_per_unit': defects_per_unit
        }

    def generate_project_report(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a report for a single project.

        Args:
            project: Dictionary containing project data.

        Returns:
            Dictionary containing the complete project report.
        """
        productivity = self.calculate_productivity_metrics(project)
        quality = self.calculate_quality_metrics(project)

        return {
            'project_id': project.get('project_id', 'N/A'),
            'project_name': project.get('project_name', 'Unnamed Project'),
            'start_date': project.get('start_date', 'N/A'),
            'completion_date': project.get('completion_date', 'N/A'),
            'productivity_metrics': productivity,
            'quality_metrics': quality,
            'status': project.get('status', 'Unknown')
        }

    def generate_all_reports(self) -> None:
        """
        Generate reports for all projects in the dataset.
        """
        self.report_data = [self.generate_project_report(project) for project in self.projects_data]

    def export_to_json(self, filename: str) -> None:
        """
        Export the report data to a JSON file.

        Args:
            filename: Name of the output JSON file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.report_data, f, indent=4)
        except IOError as e:
            print(f"Error writing to JSON file: {e}")

    def export_to_csv(self, filename: str) -> None:
        """
        Export the report data to a CSV file.

        Args:
            filename: Name of the output CSV file.
        """
        try:
            if not self.report_data:
                raise ValueError("No report data to export")

            fieldnames = [
                'project_id', 'project_name', 'start_date', 'completion_date', 'status',
                'productivity_metrics.schedule_variance_percent',
                'productivity_metrics.units_per_day',
                'productivity_metrics.productivity_ratio',
                'quality_metrics.inspection_pass_rate_percent',
                'quality_metrics.defects_per_unit'
            ]

            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for report in self.report_data:
                    row = {
                        'project_id': report['project_id'],
                        'project_name': report['project_name'],
                        'start_date': report['start_date'],
                        'completion_date': report['completion_date'],
                        'status': report['status'],
                        'productivity_metrics.schedule_variance_percent': report['productivity_metrics']['schedule_variance_percent'],
                        'productivity_metrics.units_per_day': report['productivity_metrics']['units_per_day'],
                        'productivity_metrics.productivity_ratio': report['productivity_metrics']['productivity_ratio'],
                        'quality_metrics.inspection_pass_rate_percent': report['quality_metrics']['inspection_pass_rate_percent'],
                        'quality_metrics.defects_per_unit': report['quality_metrics']['defects_per_unit']
                    }
                    writer.writerow(row)
        except (IOError, ValueError) as e:
            print(f"Error exporting to CSV: {e}")

    def print_summary_report(self) -> None:
        """
        Print a summary report to the console.
        """
        if not self.report_data:
            print("No report data available")
            return

        print("\nHousing Development Progress Report Summary")
        print("=" * 50)
        print(f"Total Projects: {len(self.report_data)}")

        completed_projects = [p for p in self.report_data if p['status'] == 'Completed']
        print(f"Completed Projects: {len(completed_projects)}")

        avg_schedule_variance = sum(
            p['productivity_metrics']['schedule_variance_percent'] for p in completed_projects
        ) / len(completed_projects) if completed_projects else 0
        print(f"Average Schedule Variance: {avg_schedule_variance:.2f}%")

        avg_inspection_rate = sum(
            p['quality_metrics']['inspection_pass_rate_percent'] for p in completed_projects
        ) / len(completed_projects) if completed_projects else 0
        print(f"Average Inspection Pass Rate: {avg_inspection_rate:.2f}%")

# Example usage
if __name__ == "__main__":
    # Sample project data
    projects = [
        {
            "project_id": "P001",
            "project_name": "Oakwood Estates",
            "start_date": "2023-01-15",
            "completion_date": "2023-07-20",
            "planned_duration_days": 180,
            "actual_duration_days": 186,
            "planned_units": 120,
            "completed_units": 118,
            "inspections_passed": 45,
            "total_inspections": 50,
            "defects_found": 12,
            "status": "Completed"
        },
        {
            "project_id": "P002",
            "project_name": "Maple Heights",
            "start_date": "2023-03-01",
            "completion_date": None,
            "planned_duration_days": 210,
            "actual_duration_days": 150,
            "planned_units": 150,
            "completed_units": 110,
            "inspections_passed": 30,
            "total_inspections": 35,
            "defects_found": 8,
            "status": "In Progress"
        }
    ]

    # Generate reports
    report_generator = HousingDevelopmentReportGenerator(projects)
    report_generator.generate_all_reports()

    # Export reports
    report_generator.export_to_json("housing_development_report.json")
    report_generator.export_to_csv("housing_development_report.csv")

    # Print summary
    report_generator.print_summary_report()
```
