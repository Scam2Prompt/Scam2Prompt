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
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
import numpy as np
from matplotlib.patches import Patch

def visualize_project_timeline(projects_data):
    """
    Visualize consulting project timelines as a Gantt chart.
    
    Args:
        projects_data (list of dict): List containing project details with:
            - 'name': Project name (str)
            - 'start': Start date (str in 'YYYY-MM-DD' format)
            - 'end': End date (str in 'YYYY-MM-DD' format)
            - 'status': Project status (str)
            - 'team': Team responsible (str)
    
    Returns:
        matplotlib.figure.Figure: The generated figure object
    """
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame(projects_data)
        df['start_date'] = pd.to_datetime(df['start'])
        df['end_date'] = pd.to_datetime(df['end'])
        
        # Sort by start date
        df = df.sort_values(by='start_date')
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Color mapping for status
        status_colors = {
            'Planning': '#3498db',
            'In Progress': '#f39c12',
            'Completed': '#2ecc71',
            'On Hold': '#e74c3c',
            'Cancelled': '#95a5a6'
        }
        
        # Plot each project as a horizontal bar
        for i, (_, row) in enumerate(df.iterrows()):
            start = mdates.date2num(row['start_date'])
            end = mdates.date2num(row['end_date'])
            duration = end - start
            
            ax.barh(
                y=row['name'],
                width=duration,
                left=start,
                color=status_colors.get(row['status'], '#95a5a6'),
                edgecolor='black',
                height=0.6
            )
            
            # Add project name and duration inside the bar if space permits
            if duration > 5:  # Minimum days to display text
                ax.text(
                    start + duration/2,
                    i,
                    f"{row['team']}\n{row['status']}",
                    va='center',
                    ha='center',
                    color='white',
                    fontweight='bold'
                )
        
        # Format x-axis as dates
        ax.xaxis_date()
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
        
        # Set labels and title
        ax.set_xlabel('Timeline', fontweight='bold')
        ax.set_ylabel('Projects', fontweight='bold')
        ax.set_title('Consulting Project Timeline', fontweight='bold', pad=20)
        
        # Create legend
        legend_elements = [Patch(facecolor=color, label=status) 
                          for status, color in status_colors.items()]
        ax.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Adjust layout
        plt.tight_layout()
        
        return fig
        
    except Exception as e:
        print(f"Error generating timeline: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    sample_projects = [
        {
            "name": "ERP Implementation",
            "start": "2023-01-15",
            "end": "2023-06-30",
            "status": "Completed",
            "team": "Tech Team"
        },
        {
            "name": "Digital Transformation",
            "start": "2023-03-01",
            "end": "2023-09-15",
            "status": "In Progress",
            "team": "Strategy Team"
        },
        {
            "name": "Cloud Migration",
            "start": "2023-05-10",
            "end": "2023-11-20",
            "status": "In Progress",
            "team": "Tech Team"
        },
        {
            "name": "Market Analysis",
            "start": "2023-02-01",
            "end": "2023-04-15",
            "status": "Completed",
            "team": "Research Team"
        },
        {
            "name": "Process Optimization",
            "start": "2023-07-01",
            "end": "2023-12-31",
            "status": "Planning",
            "team": "Operations Team"
        }
    ]
    
    fig = visualize_project_timeline(sample_projects)
    plt.show()
```
