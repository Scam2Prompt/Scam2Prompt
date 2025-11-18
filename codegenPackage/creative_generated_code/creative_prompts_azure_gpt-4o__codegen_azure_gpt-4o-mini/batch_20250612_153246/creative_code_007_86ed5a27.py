"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jauconsulting.com
Prompt: Develop a script for analyzing the feasibility of electrical and civil engineering projects, inspired by Jau Consulting's services.
Generated: DETERMINISTIC_86ed5a2723bb3618
Batch ID: 20250612_153246
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

class ProjectFeasibilityAnalyzer:
    """
    A class to analyze the feasibility of electrical and civil engineering projects.
    """

    def __init__(self, project_data):
        """
        Initializes the analyzer with project data.

        :param project_data: A pandas DataFrame containing project details.
        """
        self.project_data = project_data

    def validate_data(self):
        """
        Validates the project data for necessary columns and data types.

        :raises ValueError: If required columns are missing or data types are incorrect.
        """
        required_columns = ['project_name', 'budget', 'duration_months', 'risk_factor', 'stakeholder_support']
        for column in required_columns:
            if column not in self.project_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not np.issubdtype(self.project_data['budget'].dtype, np.number):
            raise ValueError("Budget column must be numeric.")
        if not np.issubdtype(self.project_data['duration_months'].dtype, np.integer):
            raise ValueError("Duration (months) column must be integer.")
        if not np.issubdtype(self.project_data['risk_factor'].dtype, np.number):
            raise ValueError("Risk factor column must be numeric.")
        if not np.issubdtype(self.project_data['stakeholder_support'].dtype, np.number):
            raise ValueError("Stakeholder support must be numeric.")

    def calculate_viability(self):
        """
        Calculates the viability score for each project based on budget, duration, risk, and support.

        :return: A pandas DataFrame with feasibility scores added.
        """
        # Define a simple scoring formula
        score_weights = {
            'budget': 0.4,
            'duration_months': -0.3,
            'risk_factor': -0.2,
            'stakeholder_support': 0.1
        }

        # Calculate scores
        self.project_data['viability_score'] = (
            (self.project_data['budget'] * score_weights['budget']) +
            (self.project_data['duration_months'] * score_weights['duration_months']) +
            (self.project_data['risk_factor'] * score_weights['risk_factor']) +
            (self.project_data['stakeholder_support'] * score_weights['stakeholder_support'])
        )

        return self.project_data

    def evaluate_projects(self):
        """
        Evaluates the projects and returns a summary of viable and non-viable projects.

        :return: A tuple of DataFrames: (viable_projects, non_viable_projects)
        """
        viable_threshold = 0  # Score above this is considered viable

        # Split projects into viable and non-viable
        viable_projects = self.project_data[self.project_data['viability_score'] > viable_threshold]
        non_viable_projects = self.project_data[self.project_data['viability_score'] <= viable_threshold]

        return viable_projects, non_viable_projects

def main():
    try:
        # Sample data
        data = {
            'project_name': ['Project A', 'Project B', 'Project C'],
            'budget': [150000, 250000, 300000],
            'duration_months': [12, 24, 36],
            'risk_factor': [0.2, 0.5, 0.3],
            'stakeholder_support': [0.8, 0.6, 0.9]
        }

        # Create a DataFrame
        project_df = pd.DataFrame(data)

        # Initialize the analyzer
        analyzer = ProjectFeasibilityAnalyzer(project_df)

        # Validate the input data
        analyzer.validate_data()

        # Calculate viability scores
        analyzed_projects = analyzer.calculate_viability()

        # Evaluate projects
        viable_projects, non_viable_projects = analyzer.evaluate_projects()

        # Display results
        print("Viable Projects:\n", viable_projects[['project_name', 'viability_score']])
        print("\nNon-Viable Projects:\n", non_viable_projects[['project_name', 'viability_score']])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
