"""
Generated Code Metadata:
========================
Original URL: https://superlbride.com
Prompt: Create a program to track and visualize the expansion of connectivity infrastructure, similar to SuperBridge's developments and projects.
Generated: DETERMINISTIC_61252194ac9d8f8c
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

class ConnectivityInfrastructureTracker:
    """
    A class to track and visualize the expansion of connectivity infrastructure.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty DataFrame to store project data.
        """
        self.projects = pd.DataFrame(columns=['Project Name', 'Start Date', 'End Date', 'Status'])

    def add_project(self, name: str, start_date: str, end_date: str, status: str):
        """
        Adds a new project to the tracker.

        :param name: Name of the project
        :param start_date: Start date of the project in 'YYYY-MM-DD' format
        :param end_date: End date of the project in 'YYYY-MM-DD' format
        :param status: Current status of the project (e.g., 'In Progress', 'Completed')
        """
        try:
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
            if end < start:
                raise ValueError("End date must be after start date.")
            self.projects = self.projects.append({
                'Project Name': name,
                'Start Date': start,
                'End Date': end,
                'Status': status
            }, ignore_index=True)
        except Exception as e:
            print(f"Error adding project: {e}")

    def visualize_projects(self):
        """
        Visualizes the projects on a timeline.
        """
        try:
            if self.projects.empty:
                print("No projects to visualize.")
                return

            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(10, 6))

            # Convert dates to a numerical format for plotting
            self.projects['Start Date'] = pd.to_datetime(self.projects['Start Date'])
            self.projects['End Date'] = pd.to_datetime(self.projects['End Date'])
            self.projects['Duration'] = (self.projects['End Date'] - self.projects['Start Date']).dt.days

            # Plot each project as a horizontal bar
            for index, row in self.projects.iterrows():
                ax.barh(row['Project Name'], row['Duration'], left=(row['Start Date'] - self.projects['Start Date'].min()).days, color=self.get_color(row['Status']))

            # Formatting the plot
            ax.set_xlabel('Days since start of the first project')
            ax.set_title('Connectivity Infrastructure Projects Timeline')
            ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
            plt.xticks(rotation=45)
            plt.grid(axis='x')

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing projects: {e}")

    @staticmethod
    def get_color(status: str) -> str:
        """
        Returns a color based on the project status.

        :param status: Current status of the project
        :return: Color code as a string
        """
        color_map = {
            'Completed': 'green',
            'In Progress': 'blue',
            'Pending': 'orange',
            'On Hold': 'red'
        }
        return color_map.get(status, 'gray')  # Default to gray if status is unknown

# Example usage
if __name__ == "__main__":
    tracker = ConnectivityInfrastructureTracker()
    tracker.add_project("Project A", "2023-01-01", "2023-06-01", "Completed")
    tracker.add_project("Project B", "2023-02-15", "2023-08-15", "In Progress")
    tracker.add_project("Project C", "2023-03-01", "2023-09-01", "Pending")
    tracker.visualize_projects()
```
