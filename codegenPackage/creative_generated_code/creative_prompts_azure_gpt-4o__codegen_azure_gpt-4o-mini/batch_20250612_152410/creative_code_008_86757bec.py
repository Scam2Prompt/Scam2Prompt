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

```python
import json
import datetime
from typing import List, Dict, Any

class HousingDevelopmentReport:
    """Class to generate reports on housing development progress."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.metrics = []  # List to store productivity and quality metrics

    def add_metric(self, date: str, productivity: float, quality: float) -> None:
        """Add a metric for a specific date.
        
        Args:
            date (str): The date of the metric in 'YYYY-MM-DD' format.
            productivity (float): The productivity metric for the day.
            quality (float): The quality metric for the day.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, '%Y-%m-%d')
            self.metrics.append({
                'date': date,
                'productivity': productivity,
                'quality': quality
            })
        except ValueError as e:
            print(f"Error: {e}. Please provide the date in 'YYYY-MM-DD' format.")

    def generate_report(self) -> Dict[str, Any]:
        """Generate a report with average productivity and quality metrics.

        Returns:
            Dict[str, Any]: A dictionary containing the report data.
        """
        if not self.metrics:
            return {
                'project': self.project_name,
                'average_productivity': 0,
                'average_quality': 0,
                'total_entries': 0
            }

        total_productivity = sum(metric['productivity'] for metric in self.metrics)
        total_quality = sum(metric['quality'] for metric in self.metrics)
        total_entries = len(self.metrics)

        return {
            'project': self.project_name,
            'average_productivity': total_productivity / total_entries,
            'average_quality': total_quality / total_entries,
            'total_entries': total_entries
        }

    def save_report(self, file_path: str) -> None:
        """Save the report to a JSON file.

        Args:
            file_path (str): The file path to save the report.
        """
        report = self.generate_report()
        try:
            with open(file_path, 'w') as f:
                json.dump(report, f, indent=4)
            print(f"Report saved successfully to {file_path}.")
        except IOError as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == '__main__':
    report = HousingDevelopmentReport("Westpoint Construction Project")
    
    # Adding sample metrics
    report.add_metric("2023-10-01", 85.5, 90.0)
    report.add_metric("2023-10-02", 90.0, 88.5)
    report.add_metric("2023-10-03", 89.0, 85.0)

    # Generating and saving the report
    report.save_report("housing_development_report.json")
```
