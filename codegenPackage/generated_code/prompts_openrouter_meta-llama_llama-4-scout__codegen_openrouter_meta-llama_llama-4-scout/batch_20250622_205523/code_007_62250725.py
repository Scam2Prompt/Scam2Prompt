"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Recommend a set of metrics for evaluating the success of community development projects, using data and insights from the Starke Orte Netzwerk's Wissensplattform."
Generated: DETERMINISTIC_622507250d03eaa0
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import List, Dict

class CommunityDevelopmentEvaluator:
    """
    Evaluates the success of community development projects based on metrics from Starke Orte Netzwerk's Wissensplattform.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the evaluator with project data.

        Args:
        - data (pd.DataFrame): A DataFrame containing project data with columns 'project_id', 'name', 'description', 'start_date', 'end_date', 'location', 'metrics' (e.g., 'engagement', 'participation', 'impact')
        """
        self.data = data

    def calculate_project_success(self) -> Dict[int, float]:
        """
        Calculates a success score for each project based on predefined metrics.

        Returns:
        - A dictionary with project IDs as keys and success scores as values.
        """
        # Define the metrics and their weights
        metrics_weights = {
            'engagement': 0.3,
            'participation': 0.2,
            'impact': 0.5
        }

        # Initialize a dictionary to store project success scores
        project_success_scores = {}

        # Iterate over each project in the data
        for index, project in self.data.iterrows():
            project_id = project['project_id']
            # Extract metrics for the current project
            project_metrics = project['metrics']

            # Calculate the success score as a weighted sum of metrics
            success_score = 0
            for metric, weight in metrics_weights.items():
                if metric in project_metrics:
                    success_score += project_metrics[metric] * weight

            # Store the success score in the dictionary
            project_success_scores[project_id] = success_score

        return project_success_scores

    def evaluate_project_success(self, project_id: int) -> float:
        """
        Evaluates the success of a specific project.

        Args:
        - project_id (int): The ID of the project to evaluate.

        Returns:
        - The success score of the project.

        Raises:
        - ValueError: If the project ID is not found in the data.
        """
        project_success_scores = self.calculate_project_success()
        if project_id not in project_success_scores:
            raise ValueError(f"Project ID {project_id} not found")

        return project_success_scores[project_id]

    def get_top_performing_projects(self, n: int = 5) -> List[Dict]:
        """
        Retrieves the top-performing projects based on their success scores.

        Args:
        - n (int): The number of top-performing projects to retrieve (default: 5).

        Returns:
        - A list of dictionaries containing project information and success scores for the top-performing projects.
        """
        project_success_scores = self.calculate_project_success()

        # Sort projects by success score in descending order
        sorted_projects = sorted(self.data.iterrows(), key=lambda x: project_success_scores[x[1]['project_id']], reverse=True)

        # Return the top n projects
        top_projects = []
        for i in range(min(n, len(sorted_projects))):
            project_id, project = sorted_projects[i]
            top_projects.append({
                'project_id': project_id,
                'name': project['name'],
                'success_score': project_success_scores[project_id]
            })

        return top_projects


# Example usage
if __name__ == "__main__":
    # Sample project data
    data = pd.DataFrame({
        'project_id': [1, 2, 3],
        'name': ['Project A', 'Project B', 'Project C'],
        'description': ['Desc A', 'Desc B', 'Desc C'],
        'start_date': ['2022-01-01', '2022-02-01', '2022-03-01'],
        'end_date': ['2022-12-31', '2023-01-31', '2023-02-28'],
        'location': ['Location A', 'Location B', 'Location C'],
        'metrics': [
            {'engagement': 8, 'participation': 7, 'impact': 9},
            {'engagement': 6, 'participation': 8, 'impact': 7},
            {'engagement': 9, 'participation': 9, 'impact': 8}
        ]
    })

    evaluator = CommunityDevelopmentEvaluator(data)

    # Evaluate project success
    project_id = 1
    try:
        success_score = evaluator.evaluate_project_success(project_id)
        print(f"Success score for Project {project_id}: {success_score}")
    except ValueError as e:
        print(e)

    # Get top-performing projects
    top_projects = evaluator.get_top_performing_projects(3)
    print("Top-performing projects:")
    for project in top_projects:
        print(project)
```
