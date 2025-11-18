"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Generate code to visualize consulting project timelines using Python libraries like matplotlib or seaborn.
Generated: DETERMINISTIC_4873955226d9f564
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_timeline(data):
    """
    Create a Gantt chart to visualize project timelines.

    Parameters:
        data (pd.DataFrame): DataFrame containing project tasks, start dates, and durations.

    Raises:
        ValueError: If the DataFrame does not contain required columns.
    """
    # Check if required columns are present
    required_columns = ['Task', 'Start', 'Duration']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, len(data) * 0.5))

    # Convert start dates to a numerical format
    start_dates = pd.to_datetime(data['Start'])
    durations = data['Duration']

    # Create a list of start positions for each task
    task_positions = np.arange(len(data))

    # Create a horizontal bar chart
    ax.barh(task_positions, durations, left=start_dates.astype(np.int64) // 10**9, color='skyblue')

    # Set the ticks and labels
    ax.set_yticks(task_positions)
    ax.set_yticklabels(data['Task'])
    
    # Format x-axis to show date
    ax.xaxis_date()
    plt.xticks(rotation=45)  # Rotate date labels for better readability

    # Adding labels and title
    ax.set_xlabel('Timeline')
    ax.set_ylabel('Tasks')
    ax.set_title('Consulting Project Timelines')

    # Show grid
    ax.grid(True)

    # Display the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for visualization
    project_data = {
        'Task': ['Requirement Gathering', 'Design', 'Implementation', 'Testing', 'Deployment'],
        'Start': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01'],
        'Duration': [14, 14, 14, 14, 7]  # Duration in days
    }
    
    # Create a DataFrame
    df = pd.DataFrame(project_data)

    # Create and show the timeline
    create_timeline(df)
```
