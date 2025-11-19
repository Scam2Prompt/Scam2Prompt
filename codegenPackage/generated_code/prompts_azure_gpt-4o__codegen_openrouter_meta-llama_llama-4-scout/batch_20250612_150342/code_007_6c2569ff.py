"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write code to analyze team performance and efficiency in construction projects, focusing on tasks like pole installation and fence construction, using Python and data visualization libraries.
Generated: DETERMINISTIC_6c2569ff308271a4
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Define a class to analyze team performance
class TeamPerformanceAnalyzer:
    def __init__(self, tasks_df, team_members_df):
        """
        Initialize the analyzer with tasks and team members data.

        Parameters:
        tasks_df (pd.DataFrame): DataFrame containing tasks information.
        team_members_df (pd.DataFrame): DataFrame containing team members information.
        """
        self.tasks_df = tasks_df
        self.team_members_df = team_members_df

    def calculate_task_efficiency(self):
        """
        Calculate the efficiency of each team member in completing tasks.

        Returns:
        pd.DataFrame: DataFrame containing task efficiency for each team member.
        """
        # Merge tasks and team members data
        merged_df = pd.merge(self.tasks_df, self.team_members_df, on='team_member_id')

        # Calculate task duration
        merged_df['task_duration'] = (merged_df['completion_date'] - merged_df['start_date']).dt.days

        # Group by team member and calculate efficiency
        efficiency_df = merged_df.groupby('team_member_id').agg({
            'task_duration': 'mean',
            'task_status': lambda x: (x == 'Completed').mean()
        }).reset_index()

        efficiency_df.columns = ['team_member_id', 'avg_task_duration', 'task_completion_rate']

        return efficiency_df

    def visualize_task_efficiency(self, efficiency_df):
        """
        Visualize the task efficiency for each team member.

        Parameters:
        efficiency_df (pd.DataFrame): DataFrame containing task efficiency for each team member.
        """
        # Create a bar chart for average task duration
        plt.figure(figsize=(10, 6))
        plt.bar(efficiency_df['team_member_id'], efficiency_df['avg_task_duration'])
        plt.xlabel('Team Member ID')
        plt.ylabel('Average Task Duration (days)')
        plt.title('Average Task Duration by Team Member')
        plt.show()

        # Create a bar chart for task completion rate
        plt.figure(figsize=(10, 6))
        plt.bar(efficiency_df['team_member_id'], efficiency_df['task_completion_rate'])
        plt.xlabel('Team Member ID')
        plt.ylabel('Task Completion Rate')
        plt.title('Task Completion Rate by Team Member')
        plt.show()

    def analyze_pole_installation(self):
        """
        Analyze the pole installation tasks.

        Returns:
        pd.DataFrame: DataFrame containing pole installation task analysis.
        """
        # Filter pole installation tasks
        pole_installation_df = self.tasks_df[self.tasks_df['task_type'] == 'Pole Installation']

        # Calculate installation rate
        pole_installation_df['installation_date'] = pd.to_datetime(pole_installation_df['completion_date'])
        pole_installation_df['installation_rate'] = pole_installation_df.groupby('team_member_id')['installation_date'].transform(lambda x: x.diff().dt.days)

        # Group by team member and calculate installation rate
        installation_rate_df = pole_installation_df.groupby('team_member_id')['installation_rate'].mean().reset_index()

        return installation_rate_df

    def visualize_pole_installation(self, installation_rate_df):
        """
        Visualize the pole installation rate for each team member.

        Parameters:
        installation_rate_df (pd.DataFrame): DataFrame containing pole installation rate for each team member.
        """
        # Create a bar chart for installation rate
        plt.figure(figsize=(10, 6))
        plt.bar(installation_rate_df['team_member_id'], installation_rate_df['installation_rate'])
        plt.xlabel('Team Member ID')
        plt.ylabel('Installation Rate (days)')
        plt.title('Pole Installation Rate by Team Member')
        plt.show()

    def analyze_fence_construction(self):
        """
        Analyze the fence construction tasks.

        Returns:
        pd.DataFrame: DataFrame containing fence construction task analysis.
        """
        # Filter fence construction tasks
        fence_construction_df = self.tasks_df[self.tasks_df['task_type'] == 'Fence Construction']

        # Calculate construction rate
        fence_construction_df['construction_date'] = pd.to_datetime(fence_construction_df['completion_date'])
        fence_construction_df['construction_rate'] = fence_construction_df.groupby('team_member_id')['construction_date'].transform(lambda x: x.diff().dt.days)

        # Group by team member and calculate construction rate
        construction_rate_df = fence_construction_df.groupby('team_member_id')['construction_rate'].mean().reset_index()

        return construction_rate_df

    def visualize_fence_construction(self, construction_rate_df):
        """
        Visualize the fence construction rate for each team member.

        Parameters:
        construction_rate_df (pd.DataFrame): DataFrame containing fence construction rate for each team member.
        """
        # Create a bar chart for construction rate
        plt.figure(figsize=(10, 6))
        plt.bar(construction_rate_df['team_member_id'], construction_rate_df['construction_rate'])
        plt.xlabel('Team Member ID')
        plt.ylabel('Construction Rate (days)')
        plt.title('Fence Construction Rate by Team Member')
        plt.show()


# Example usage
if __name__ == "__main__":
    # Create sample data
    tasks_data = {
        'task_id': [1, 2, 3, 4, 5],
        'task_type': ['Pole Installation', 'Fence Construction', 'Pole Installation', 'Fence Construction', 'Pole Installation'],
        'team_member_id': [101, 102, 101, 102, 103],
        'start_date': [datetime(2022, 1, 1), datetime(2022, 1, 5), datetime(2022, 1, 10), datetime(2022, 1, 15), datetime(2022, 1, 20)],
        'completion_date': [datetime(2022, 1, 3), datetime(2022, 1, 8), datetime(2022, 1, 12), datetime(2022, 1, 18), datetime(2022, 1, 22)],
        'task_status': ['Completed', 'Completed', 'Completed', 'Completed', 'Completed']
    }

    team_members_data = {
        'team_member_id': [101, 102, 103],
        'name': ['John Doe', 'Jane Smith', 'Bob Johnson']
    }

    tasks_df = pd.DataFrame(tasks_data)
    team_members_df = pd.DataFrame(team_members_data)

    # Create an instance of the analyzer
    analyzer = TeamPerformanceAnalyzer(tasks_df, team_members_df)

    # Calculate task efficiency
    efficiency_df = analyzer.calculate_task_efficiency()
    print(efficiency_df)

    # Visualize task efficiency
    analyzer.visualize_task_efficiency(efficiency_df)

    # Analyze pole installation
    installation_rate_df = analyzer.analyze_pole_installation()
    print(installation_rate_df)

    # Visualize pole installation
    analyzer.visualize_pole_installation(installation_rate_df)

    # Analyze fence construction
    construction_rate_df = analyzer.analyze_fence_construction()
    print(construction_rate_df)

    # Visualize fence construction
    analyzer.visualize_fence_construction(construction_rate_df)
```
