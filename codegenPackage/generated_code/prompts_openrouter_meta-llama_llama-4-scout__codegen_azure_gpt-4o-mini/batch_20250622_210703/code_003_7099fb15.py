"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Develop a code snippet to track and analyze construction project metrics, such as project completion rates, client satisfaction, and team performance, for a turnkey construction service provider."
Generated: DETERMINISTIC_7099fb15919ba67f
Batch ID: 20250622_210703
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
import matplotlib.pyplot as plt

class ConstructionProjectMetrics:
    def __init__(self):
        """Initialize the metrics tracker with empty data."""
        self.data = pd.DataFrame(columns=['ProjectID', 'CompletionRate', 'ClientSatisfaction', 'TeamPerformance'])

    def add_project(self, project_id, completion_rate, client_satisfaction, team_performance):
        """
        Add a new project to the metrics tracker.

        Args:
            project_id (str): Unique identifier for the project.
            completion_rate (float): Completion rate of the project (0 to 100).
            client_satisfaction (float): Client satisfaction score (0 to 10).
            team_performance (float): Team performance score (0 to 10).
        """
        if not (0 <= completion_rate <= 100):
            raise ValueError("Completion rate must be between 0 and 100.")
        if not (0 <= client_satisfaction <= 10):
            raise ValueError("Client satisfaction must be between 0 and 10.")
        if not (0 <= team_performance <= 10):
            raise ValueError("Team performance must be between 0 and 10.")

        new_project = {
            'ProjectID': project_id,
            'CompletionRate': completion_rate,
            'ClientSatisfaction': client_satisfaction,
            'TeamPerformance': team_performance
        }
        self.data = self.data.append(new_project, ignore_index=True)

    def analyze_metrics(self):
        """Analyze and return summary statistics of the project metrics."""
        if self.data.empty:
            raise ValueError("No project data available for analysis.")

        summary = {
            'AverageCompletionRate': self.data['CompletionRate'].mean(),
            'AverageClientSatisfaction': self.data['ClientSatisfaction'].mean(),
            'AverageTeamPerformance': self.data['TeamPerformance'].mean(),
            'TotalProjects': len(self.data)
        }
        return summary

    def plot_metrics(self):
        """Plot the project metrics for visual analysis."""
        if self.data.empty:
            raise ValueError("No project data available for plotting.")

        plt.figure(figsize=(10, 6))
        plt.subplot(3, 1, 1)
        plt.plot(self.data['ProjectID'], self.data['CompletionRate'], marker='o', label='Completion Rate')
        plt.title('Project Completion Rates')
        plt.xlabel('Project ID')
        plt.ylabel('Completion Rate (%)')
        plt.ylim(0, 100)
        plt.grid()
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.data['ProjectID'], self.data['ClientSatisfaction'], marker='o', color='orange', label='Client Satisfaction')
        plt.title('Client Satisfaction Scores')
        plt.xlabel('Project ID')
        plt.ylabel('Satisfaction Score (0-10)')
        plt.ylim(0, 10)
        plt.grid()
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.data['ProjectID'], self.data['TeamPerformance'], marker='o', color='green', label='Team Performance')
        plt.title('Team Performance Scores')
        plt.xlabel('Project ID')
        plt.ylabel('Performance Score (0-10)')
        plt.ylim(0, 10)
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    metrics_tracker = ConstructionProjectMetrics()
    
    # Adding sample projects
    try:
        metrics_tracker.add_project('Project1', 85, 9, 8)
        metrics_tracker.add_project('Project2', 90, 10, 9)
        metrics_tracker.add_project('Project3', 75, 7, 6)

        # Analyzing metrics
        summary = metrics_tracker.analyze_metrics()
        print("Project Metrics Summary:", summary)

        # Plotting metrics
        metrics_tracker.plot_metrics()
    except ValueError as e:
        print(f"Error: {e}")
```
