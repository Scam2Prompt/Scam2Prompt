"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matter.com.uy
Prompt: Develop a program that evaluates the impact of social and educational projects, incorporating the monitoring and evaluation techniques outlined by Matter.
Generated: DETERMINISTIC_866b4b3299dda49a
Batch ID: 20250612_162050
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
from typing import List, Dict

class ProjectEvaluator:
    """
    A class to evaluate the impact of social and educational projects.
    """

    def __init__(self, project_data: pd.DataFrame):
        """
        Initializes the ProjectEvaluator with project data.

        Args:
            project_data (pd.DataFrame): DataFrame containing project attributes and metrics.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the project data to ensure it meets the necessary criteria.
        Raises ValueError if the data is invalid.
        """
        required_columns = ['project_id', 'impact_score', 'cost', 'duration', 'participants']
        if not all(col in self.project_data.columns for col in required_columns):
            raise ValueError("Missing required columns in project data.")

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculates the Return on Investment (ROI) for each project.

        Returns:
            pd.DataFrame: A DataFrame with projects and their calculated ROI.
        """
        self.validate_data()
        self.project_data['roi'] = (self.project_data['impact_score'] - self.project_data['cost']) / self.project_data['cost']
        return self.project_data[['project_id', 'roi']]

    def summarize_impacts(self) -> Dict[str, float]:
        """
        Summarizes the overall impacts across all projects.

        Returns:
            Dict[str, float]: A dictionary containing total impact, total cost, and average ROI.
        """
        total_impact = self.project_data['impact_score'].sum()
        total_cost = self.project_data['cost'].sum()
        average_roi = self.project_data['roi'].mean()

        return {
            'total_impact': total_impact,
            'total_cost': total_cost,
            'average_roi': average_roi
        }

    def evaluate_projects(self) -> None:
        """
        Evaluates all projects and prints the ROI and summary of impacts.
        """
        try:
            roi_data = self.calculate_roi()
            print("ROI for each project:")
            print(roi_data)

            summary = self.summarize_impacts()
            print("\nSummary of impacts:")
            print(summary)
        except Exception as e:
            print(f"Error during evaluation: {e}")


if __name__ == "__main__":
    # Sample project data
    data = {
        'project_id': [1, 2, 3],
        'impact_score': [1000, 1500, 800],
        'cost': [200, 400, 300],
        'duration': [12, 24, 18],
        'participants': [50, 100, 75]
    }

    # Convert to DataFrame
    project_data_df = pd.DataFrame(data)

    # Create an instance of ProjectEvaluator
    evaluator = ProjectEvaluator(project_data_df)

    # Run the evaluation
    evaluator.evaluate_projects()
```
