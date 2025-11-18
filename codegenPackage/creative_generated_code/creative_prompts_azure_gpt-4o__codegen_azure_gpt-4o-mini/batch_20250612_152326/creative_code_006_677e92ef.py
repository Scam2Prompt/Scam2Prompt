"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Suggest a library or tool for visualizing construction project progress, tailored for a company like Sadad Engineering that operates in the fields of building construction, facilities, and infrastructure.
Generated: DETERMINISTIC_677e92efef535598
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ConstructionProjectVisualizer:
    """
    A class to visualize construction project progress using Gantt charts.

    Attributes:
        project_data (DataFrame): A pandas DataFrame containing project tasks, start dates, end dates, and progress.
    """

    def __init__(self, data):
        """
        Initializes the visualizer with project data.

        Args:
            data (DataFrame): A pandas DataFrame containing the project data.
        """
        self.project_data = data

    def validate_data(self):
        """
        Validates the input project data to ensure it has the necessary columns.
        
        Raises:
            ValueError: If the required columns are not present in the DataFrame.
        """
        required_columns = ['Task', 'Start', 'End', 'Progress']
        for column in required_columns:
            if column not in self.project_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def create_gantt_chart(self):
        """
        Creates a Gantt chart to visualize project progress.

        Returns:
            None
        """
        self.validate_data()

        # Convert dates to datetime objects
        self.project_data['Start'] = pd.to_datetime(self.project_data['Start'])
        self.project_data['End'] = pd.to_datetime(self.project_data['End'])
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))

        # Create a color map for the progress
        colors = self.project_data['Progress'].apply(lambda x: 'green' if x >= 100 else 'orange' if x > 0 else 'red')

        # Plot each task
        for idx, row in self.project_data.iterrows():
            ax.barh(row['Task'], (row['End'] - row['Start']).days, left=row['Start'].timestamp(), color=colors[idx], edgecolor='black')

        # Formatting the chart
        ax.set_xlabel('Date')
        ax.set_ylabel('Tasks')
        ax.set_title('Construction Project Progress')
        ax.xaxis_date()  # Set the x-axis to display dates
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show the plot
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data_dict = {
        'Task': ['Foundation', 'Framing', 'Roofing', 'Electrical', 'Finishing'],
        'Start': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'End': ['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-06-30'],
        'Progress': [100, 50, 0, 0, 0]
    }

    try:
        # Create a DataFrame
        project_df = pd.DataFrame(data_dict)

        # Initialize the visualizer
        visualizer = ConstructionProjectVisualizer(project_df)

        # Create the Gantt chart
        visualizer.create_gantt_chart()
    except Exception as e:
        print(f"An error occurred: {e}")
```
