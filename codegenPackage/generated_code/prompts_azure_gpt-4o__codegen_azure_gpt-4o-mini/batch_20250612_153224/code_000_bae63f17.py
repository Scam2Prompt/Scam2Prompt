"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Write Python code to simulate a financial investment analysis tool for infrastructure projects, incorporating metrics mentioned by Lao Tai Trading - Investment Group, such as environmental and social impact assessments.
Generated: DETERMINISTIC_bae63f17783e1bca
Batch ID: 20250612_153224
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

class InvestmentAnalysisTool:
    """
    A class to simulate financial investment analysis for infrastructure projects.
    
    Attributes:
        projects (pd.DataFrame): A DataFrame containing project data.
    """

    def __init__(self):
        """Initializes the InvestmentAnalysisTool with an empty DataFrame."""
        self.projects = pd.DataFrame(columns=['Project Name', 'Investment', 'Return', 'Environmental Impact', 'Social Impact'])

    def add_project(self, name: str, investment: float, return_on_investment: float, environmental_impact: float, social_impact: float):
        """
        Adds a new project to the analysis tool.
        
        Args:
            name (str): The name of the project.
            investment (float): The amount invested in the project.
            return_on_investment (float): The expected return from the investment.
            environmental_impact (float): The environmental impact score of the project.
            social_impact (float): The social impact score of the project.
        """
        if investment < 0 or return_on_investment < 0:
            raise ValueError("Investment and return on investment must be non-negative.")
        
        new_project = {
            'Project Name': name,
            'Investment': investment,
            'Return': return_on_investment,
            'Environmental Impact': environmental_impact,
            'Social Impact': social_impact
        }
        
        self.projects = self.projects.append(new_project, ignore_index=True)

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each project.
        
        Returns:
            pd.Series: A Series containing the ROI for each project.
        """
        if self.projects.empty:
            raise ValueError("No projects available for ROI calculation.")
        
        roi = (self.projects['Return'] - self.projects['Investment']) / self.projects['Investment']
        return roi

    def evaluate_projects(self):
        """
        Evaluates projects based on their ROI, environmental impact, and social impact.
        
        Returns:
            pd.DataFrame: A DataFrame containing the evaluation results.
        """
        if self.projects.empty:
            raise ValueError("No projects available for evaluation.")
        
        self.projects['ROI'] = self.calculate_roi()
        self.projects['Overall Impact'] = self.projects['Environmental Impact'] + self.projects['Social Impact']
        
        # Sort projects by ROI and Overall Impact
        evaluation = self.projects.sort_values(by=['ROI', 'Overall Impact'], ascending=False)
        return evaluation

    def display_projects(self):
        """
        Displays the current projects in the analysis tool.
        """
        if self.projects.empty:
            print("No projects to display.")
        else:
            print(self.projects)

# Example usage
if __name__ == "__main__":
    try:
        analysis_tool = InvestmentAnalysisTool()
        analysis_tool.add_project("Solar Farm", 1000000, 1500000, 8, 7)
        analysis_tool.add_project("Wind Turbine", 500000, 800000, 6, 9)
        analysis_tool.add_project("Highway Expansion", 2000000, 2500000, 5, 6)

        analysis_tool.display_projects()
        evaluation_results = analysis_tool.evaluate_projects()
        print("\nEvaluation Results:")
        print(evaluation_results)
    except Exception as e:
        print(f"An error occurred: {e}")
```
