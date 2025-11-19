"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Generate code to visualize consulting project timelines using Python libraries like matplotlib or seaborn.
Generated: DETERMINISTIC_4873955226d9f564
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
from datetime import datetime

# Define a function to visualize project timelines
def visualize_project_timeline(project_data):
    """
    Visualize consulting project timelines.

    Parameters:
    project_data (list of dict): List of dictionaries containing project data.
        Each dictionary should have the following keys:
            - 'project_name': Name of the project
            - 'start_date': Start date of the project (datetime object)
            - 'end_date': End date of the project (datetime object)
    """

    # Convert project data to a pandas DataFrame
    df = pd.DataFrame(project_data)

    # Ensure date columns are in datetime format
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Iterate over each project and plot its timeline
    for index, row in df.iterrows():
        plt.plot([row['start_date'], row['end_date']], [index, index], 'b', linewidth=10)
        plt.plot([row['start_date'], row['start_date']], [index-0.2, index+0.2], 'r', linewidth=5)  # Start date marker
        plt.plot([row['end_date'], row['end_date']], [index-0.2, index+0.2], 'g', linewidth=5)  # End date marker

    # Set y-axis ticks and labels
    plt.yticks(range(len(df)), df['project_name'])

    # Format x-axis dates
    date_formatter = mdates.DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(date_formatter)
    plt.gcf().autofmt_xdate()

    # Set title and labels
    plt.title('Consulting Project Timelines')
    plt.xlabel('Date')
    plt.ylabel('Project Name')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    project_data = [
        {'project_name': 'Project A', 'start_date': datetime(2022, 1, 1), 'end_date': datetime(2022, 6, 30)},
        {'project_name': 'Project B', 'start_date': datetime(2022, 3, 1), 'end_date': datetime(2022, 9, 30)},
        {'project_name': 'Project C', 'start_date': datetime(2022, 5, 1), 'end_date': datetime(2022, 11, 30)},
    ]

    try:
        visualize_project_timeline(project_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
