"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Develop a script for analyzing the feasibility of electrical and civil engineering projects, inspired by Jau Consulting's services.
Generated: DETERMINISTIC_86ed5a2723bb3618
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class ProjectFeasibilityAnalyzer:
    """
    A class to analyze the feasibility of electrical and civil engineering projects.
    """

    def __init__(self, project_data):
        """
        Initializes the ProjectFeasibilityAnalyzer with project data.

        :param project_data: A pandas DataFrame containing project details.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the project data to ensure it contains the necessary columns.

        :raises ValueError: If required columns are missing.
        """
        required_columns = ['Project_Name', 'Cost_Estimate', 'Expected_Profit', 'Duration', 'Risk_Factor']
        for column in required_columns:
            if column not in self.project_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each project.

        :return: A pandas Series containing the ROI for each project.
        """
        roi = (self.project_data['Expected_Profit'] - self.project_data['Cost_Estimate']) / self.project_data['Cost_Estimate']
        return roi

    def assess_risk(self):
        """
        Assesses the risk level of each project based on the Risk Factor.

        :return: A pandas Series indicating the risk level ('Low', 'Medium', 'High').
        """
        risk_levels = pd.cut(self.project_data['Risk_Factor'], bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])
        return risk_levels

    def analyze_projects(self):
        """
        Analyzes the projects and returns a summary DataFrame with ROI and Risk Level.

        :return: A pandas DataFrame summarizing the analysis.
        """
        self.validate_data()
        
        # Calculate ROI
        self.project_data['ROI'] = self.calculate_roi()
        
        # Assess Risk
        self.project_data['Risk_Level'] = self.assess_risk()
        
        # Create summary DataFrame
        summary = self.project_data[['Project_Name', 'Cost_Estimate', 'Expected_Profit', 'Duration', 'ROI', 'Risk_Level']]
        return summary

def main():
    """
    Main function to execute the project feasibility analysis.
    """
    # Sample project data
    data = {
        'Project_Name': ['Project A', 'Project B', 'Project C'],
        'Cost_Estimate': [100000, 150000, 200000],
        'Expected_Profit': [120000, 180000, 250000],
        'Duration': [12, 18, 24],
        'Risk_Factor': [2, 5, 8]
    }

    # Create a DataFrame
    project_data = pd.DataFrame(data)

    try:
        # Initialize the analyzer
        analyzer = ProjectFeasibilityAnalyzer(project_data)
        
        # Analyze projects
        analysis_summary = analyzer.analyze_projects()
        
        # Display the analysis summary
        print(analysis_summary)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
