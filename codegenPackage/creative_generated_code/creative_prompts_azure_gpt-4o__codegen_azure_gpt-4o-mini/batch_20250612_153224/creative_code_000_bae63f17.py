"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Write Python code to simulate a financial investment analysis tool for infrastructure projects, incorporating metrics mentioned by Lao Tai Trading - Investment Group, such as environmental and social impact assessments.
Generated: DETERMINISTIC_bae63f17783e1bca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class InvestmentAnalysisTool:
    """
    A class to analyze financial investments in infrastructure projects.
    
    Attributes:
        projects (pd.DataFrame): DataFrame containing project data.
    """

    def __init__(self, projects_data):
        """
        Initializes the InvestmentAnalysisTool with project data.

        Args:
            projects_data (dict): A dictionary where keys are project names and values are dictionaries of project metrics.
        """
        self.projects = pd.DataFrame(projects_data)
        self.validate_data()

    def validate_data(self):
        """
        Validates the input project data to ensure required metrics are present.
        
        Raises:
            ValueError: If any required metrics are missing from the DataFrame.
        """
        required_columns = ['Project Name', 'Investment Cost', 'Expected Returns', 
                            'Environmental Impact', 'Social Impact']
        
        missing_columns = [col for col in required_columns if col not in self.projects.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each project.
        
        Returns:
            pd.Series: A series containing ROI for each project.
        """
        roi = (self.projects['Expected Returns'] - self.projects['Investment Cost']) / self.projects['Investment Cost'] * 100
        return roi

    def assess_environmental_impact(self):
        """
        Analyzes the overall environmental impact across all projects.
        
        Returns:
            float: Average environmental impact score.
        """
        return self.projects['Environmental Impact'].mean()

    def assess_social_impact(self):
        """
        Analyzes the overall social impact across all projects.
        
        Returns:
            float: Average social impact score.
        """
        return self.projects['Social Impact'].mean()

    def project_summary(self):
        """
        Summarizes the projects by computing ROI, environmental, and social impact assessments.

        Returns:
            pd.DataFrame: A summary DataFrame with project names, ROI, environmental impact, and social impact.
        """
        self.projects['ROI (%)'] = self.calculate_roi()
        summary = self.projects[['Project Name', 'ROI (%)', 'Environmental Impact', 'Social Impact']]
        return summary

# Example usage:
if __name__ == "__main__":
    # Sample project data
    project_data = {
        'Project Name': ['Project A', 'Project B', 'Project C'],
        'Investment Cost': [100000, 150000, 200000],
        'Expected Returns': [120000, 180000, 250000],
        'Environmental Impact': [7.5, 6.0, 8.0],
        'Social Impact': [8.0, 9.0, 7.5]
    }

    try:
        investment_tool = InvestmentAnalysisTool(project_data)
        summary = investment_tool.project_summary()
        
        print("Project Summary:")
        print(summary)
        print(f"Average Environmental Impact: {investment_tool.assess_environmental_impact()}")
        print(f"Average Social Impact: {investment_tool.assess_social_impact()}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
