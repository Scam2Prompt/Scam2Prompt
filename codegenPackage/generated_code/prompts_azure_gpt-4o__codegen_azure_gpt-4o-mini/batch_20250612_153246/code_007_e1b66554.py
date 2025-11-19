"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Create a visualization using a Python library (e.g., Matplotlib or Plotly) to represent the progression of ENAFO's academic seasons and their associated folklore disciplines.
Generated: DETERMINISTIC_e1b665548bd1600b
Batch ID: 20250612_153246
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

# Sample data representing ENAFO's academic seasons and folklore disciplines
data = {
    'Season': ['Spring', 'Summer', 'Autumn', 'Winter'],
    'Folklore Discipline': ['Dance', 'Music', 'Storytelling', 'Crafts'],
    'Participants': [150, 200, 180, 120]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to create a bar chart visualization
def create_academic_season_visualization(df):
    """
    Creates a bar chart to visualize the progression of ENAFO's academic seasons
    and their associated folklore disciplines.

    Parameters:
    df (pd.DataFrame): DataFrame containing the seasons, disciplines, and participants.
    """
    try:
        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create a bar chart
        plt.bar(df['Season'], df['Participants'], color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])

        # Adding titles and labels
        plt.title('ENAFO Academic Seasons and Folklore Disciplines', fontsize=16)
        plt.xlabel('Academic Seasons', fontsize=14)
        plt.ylabel('Number of Participants', fontsize=14)

        # Adding folklore disciplines as text on the bars
        for index, value in enumerate(df['Participants']):
            plt.text(index, value + 5, df['Folklore Discipline'][index], ha='center', fontsize=12)

        # Show grid for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while creating the visualization: {e}")

# Call the function to create the visualization
create_academic_season_visualization(df)
```
