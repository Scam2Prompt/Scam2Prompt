"""
Generated Code Metadata:
========================
Original URL: https://bitbama-14n.pages.dev
Prompt: Create a roadmap visualization tool for a cryptocurrency project, inspired by the roadmap section on Bitbama.
Generated: DETERMINISTIC_35afd2c6f017f858
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roadmap_visualizer.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import json

class RoadmapVisualizer:
    def __init__(self, roadmap_data):
        """
        Initialize the RoadmapVisualizer with roadmap data.

        :param roadmap_data: A list of dictionaries containing milestone information.
            Each dictionary should have the following keys:
                - 'title': The title of the milestone.
                - 'description': A brief description of the milestone.
                - 'start_date': The start date of the milestone in YYYY-MM-DD format.
                - 'end_date': The end date of the milestone in YYYY-MM-DD format.
        """
        self.roadmap_data = roadmap_data

    def visualize(self):
        """
        Visualize the roadmap using a Gantt chart.
        """
        # Create a new figure
        fig, ax = plt.subplots()

        # Iterate over each milestone
        for i, milestone in enumerate(self.roadmap_data):
            start_date = datetime.strptime(milestone['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(milestone['end_date'], '%Y-%m-%d')

            # Plot the milestone as a bar
            ax.barh(i, (end_date - start_date).days, left=start_date, height=0.8)

            # Add milestone title and description as annotations
            ax.text(start_date, i, milestone['title'], ha='left', va='center')
            ax.text(end_date, i, milestone['description'], ha='left', va='center')

        # Set the y-axis ticks and limits
        ax.set_yticks(range(len(self.roadmap_data)))
        ax.set_yticklabels([milestone['title'] for milestone in self.roadmap_data])

        # Set the x-axis to display dates
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        # Show the plot
        plt.show()

def load_roadmap_data(file_path):
    """
    Load roadmap data from a JSON file.

    :param file_path: The path to the JSON file.
    :return: A list of dictionaries containing milestone information.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return []

def main():
    # Example usage
    roadmap_data_file = 'roadmap_data.json'
    roadmap_data = load_roadmap_data(roadmap_data_file)

    if roadmap_data:
        visualizer = RoadmapVisualizer(roadmap_data)
        visualizer.visualize()

if __name__ == '__main__':
    main()
```

```json
// roadmap_data.json

[
    {
        "title": "Milestone 1",
        "description": "This is the first milestone",
        "start_date": "2024-01-01",
        "end_date": "2024-06-30"
    },
    {
        "title": "Milestone 2",
        "description": "This is the second milestone",
        "start_date": "2024-07-01",
        "end_date": "2024-12-31"
    }
]
```
