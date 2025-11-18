"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Create a visualization using a Python library (e.g., Matplotlib or Plotly) to represent the progression of ENAFO's academic seasons and their associated folklore disciplines.
Generated: DETERMINISTIC_e1b665548bd1600b
Batch ID: 20250612_153246
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

# Sample data representing ENAFO's academic seasons and folklore disciplines
data = {
    'Season': ['Spring 2021', 'Fall 2021', 'Spring 2022', 'Fall 2022', 'Spring 2023'],
    'Folklore Discipline': ['Dance', 'Music', 'Storytelling', 'Crafting', 'Theater'],
    'Participants': [30, 45, 25, 50, 40]
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)

# Function to create a bar chart visualization of academic seasons and folklore disciplines
def visualize_academic_seasons(dataframe):
    """
    Generates a bar chart to represent the progression of ENAFO's academic seasons
    and their associated folklore disciplines.

    :param dataframe: Pandas DataFrame containing seasons, disciplines, and participant counts
    """
    try:
        # Setting the size of the figure
        plt.figure(figsize=(10, 6))

        # Create a bar chart with Seasons on the x-axis and Participants on the y-axis
        plt.bar(dataframe['Season'], dataframe['Participants'], color='royalblue')

        # Adding titles and labels
        plt.title('ENAFO Academic Seasons and Participation in Folklore Disciplines')
        plt.xlabel('Academic Seasons')
        plt.ylabel('Number of Participants')
        
        # Adding folklore discipline labels above the bars
        for index, value in enumerate(dataframe['Participants']):
            plt.text(index, value + 1, dataframe['Folklore Discipline'][index], ha='center')

        # Displaying the grid and the plot
        plt.grid(axis='y')
        plt.xticks(rotation=45)
        plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
        plt.show()  # Render the plot

    except Exception as e:
        print(f"An error occurred while generating the visualization: {e}")

# Call the visualization function
visualize_academic_seasons(df)
```
