"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Create a script to analyze construction project data and generate reports on social and environmental responsibility, inspired by MGEL's management system.
Generated: DETERMINISTIC_71c732366cadaec4
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_analyzer.py

import pandas as pd
import numpy as np

class ConstructionProjectAnalyzer:
    """
    Analyzes construction project data and generates reports on social and environmental responsibility.
    """

    def __init__(self, project_data):
        """
        Initializes the analyzer with project data.

        Args:
            project_data (pd.DataFrame): Construction project data.
        """
        self.project_data = project_data

    def calculate_social_responsibility_score(self):
        """
        Calculates the social responsibility score for each project.

        Returns:
            pd.Series: Social responsibility scores.
        """
        # Define social responsibility indicators
        social_indicators = [
            'community_engagement',
            'worker_safety',
            'local_employment'
        ]

        # Calculate social responsibility score
        social_scores = self.project_data[social_indicators].mean(axis=1)

        return social_scores

    def calculate_environmental_responsibility_score(self):
        """
        Calculates the environmental responsibility score for each project.

        Returns:
            pd.Series: Environmental responsibility scores.
        """
        # Define environmental responsibility indicators
        environmental_indicators = [
            'carbon_footprint',
            'waste_management',
            'water_conservation'
        ]

        # Calculate environmental responsibility score
        environmental_scores = self.project_data[environmental_indicators].mean(axis=1)

        return environmental_scores

    def generate_report(self):
        """
        Generates a report on social and environmental responsibility.

        Returns:
            dict: Report data.
        """
        try:
            social_scores = self.calculate_social_responsibility_score()
            environmental_scores = self.calculate_environmental_responsibility_score()

            report_data = {
                'social_responsibility': social_scores,
                'environmental_responsibility': environmental_scores
            }

            return report_data

        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return None

    def save_report_to_csv(self, report_data, output_file):
        """
        Saves the report data to a CSV file.

        Args:
            report_data (dict): Report data.
            output_file (str): Output file path.
        """
        try:
            # Create a DataFrame from report data
            report_df = pd.DataFrame(report_data)

            # Save to CSV
            report_df.to_csv(output_file, index=True)

            print(f"Report saved to {output_file}")

        except Exception as e:
            print(f"Error saving report to CSV: {str(e)}")


def main():
    # Example usage
    project_data = pd.DataFrame({
        'community_engagement': [8, 9, 7, 6],
        'worker_safety': [9, 8, 9, 7],
        'local_employment': [7, 8, 6, 9],
        'carbon_footprint': [6, 7, 8, 9],
        'waste_management': [8, 9, 7, 6],
        'water_conservation': [9, 8, 9, 7]
    })

    analyzer = ConstructionProjectAnalyzer(project_data)
    report_data = analyzer.generate_report()

    if report_data:
        analyzer.save_report_to_csv(report_data, 'construction_project_report.csv')


if __name__ == "__main__":
    main()
```
