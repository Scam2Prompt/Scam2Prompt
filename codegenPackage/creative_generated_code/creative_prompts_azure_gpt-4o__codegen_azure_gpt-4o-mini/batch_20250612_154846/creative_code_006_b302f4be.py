"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Write a program to model risk assessment in engineering maintenance tasks, adhering to the safety and responsibility standards highlighted by SET Ingeniería.
Generated: DETERMINISTIC_b302f4be20d1fcd8
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class RiskAssessment:
    def __init__(self, tasks):
        """
        Initializes the RiskAssessment class with a list of tasks.

        :param tasks: List of dictionaries where each dictionary contains information about a maintenance task.
        """
        self.tasks = pd.DataFrame(tasks)
        self.validate_tasks()

    def validate_tasks(self):
        """
        Validates the structure of the tasks DataFrame to ensure it contains the required columns.
        
        Raises:
            ValueError: If any required column is missing.
        """
        required_columns = ['task_id', 'description', 'likelihood', 'consequence', 'controls']
        for column in required_columns:
            if column not in self.tasks.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_risk(self):
        """
        Calculates the risk score for each task based on the likelihood and consequence.
        
        The risk score is computed as:
        Risk Score = Likelihood * Consequence

        :return: DataFrame with risk scores added.
        """
        self.tasks['risk_score'] = self.tasks['likelihood'] * self.tasks['consequence']
        return self.tasks

    def prioritize_tasks(self):
        """
        Prioritizes tasks based on their risk scores in descending order.

        :return: DataFrame sorted by risk scores.
        """
        return self.tasks.sort_values(by='risk_score', ascending=False)

    def apply_controls(self):
        """
        Applies the safety controls to reduce risk scores based on the effectiveness of controls.

        :return: DataFrame with adjusted risk scores.
        """
        # Assuming controls are a multiplicative factor to reduce risk
        self.tasks['effective_reduction'] = self.tasks['controls'].apply(lambda x: 1 - (x / 100))
        self.tasks['adjusted_risk'] = self.tasks['risk_score'] * self.tasks['effective_reduction']
        return self.tasks

    def display_results(self):
        """
        Displays the final DataFrame with risk assessments, including original and adjusted risk scores.
        """
        print(self.tasks[['task_id', 'description', 'risk_score', 'adjusted_risk']])

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for maintenance tasks
        maintenance_tasks = [
            {'task_id': 1, 'description': 'Check hydraulic system', 'likelihood': 4, 'consequence': 5, 'controls': 20},
            {'task_id': 2, 'description': 'Inspect electrical wiring', 'likelihood': 3, 'consequence': 4, 'controls': 30},
            {'task_id': 3, 'description': 'Replace worn bearings', 'likelihood': 2, 'consequence': 3, 'controls': 10},
            {'task_id': 4, 'description': 'Test safety systems', 'likelihood': 5, 'consequence': 5, 'controls': 50}
        ]

        # Create a RiskAssessment object
        risk_assessment = RiskAssessment(maintenance_tasks)

        # Calculate risk scores
        risk_assessment.calculate_risk()

        # Prioritize tasks based on risk
        prioritized_tasks = risk_assessment.prioritize_tasks()

        # Apply controls to adjust risk scores
        adjusted_tasks = risk_assessment.apply_controls()

        # Display the results
        risk_assessment.display_results()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
