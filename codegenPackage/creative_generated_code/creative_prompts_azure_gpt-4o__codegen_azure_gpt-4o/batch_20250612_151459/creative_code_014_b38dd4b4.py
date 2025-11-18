"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Write code to create a visualization comparing the nutritional profile of Relivo with other supplements, highlighting its unique combination of ingredients.
Generated: DETERMINISTIC_b38dd4b4b62f601f
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the nutritional profile for Relivo and other supplements
# Example data: Each supplement has values for Protein, Vitamin A, Vitamin C, Iron, and Calcium
data = {
    'Supplement': ['Relivo', 'Supplement A', 'Supplement B', 'Supplement C'],
    'Protein (g)': [12, 8, 10, 7],
    'Vitamin A (mg)': [900, 800, 700, 850],
    'Vitamin C (mg)': [80, 75, 60, 65],
    'Iron (mg)': [18, 12, 15, 10],
    'Calcium (mg)': [1000, 900, 950, 850]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Normalize the nutritional data for better visual comparison
# Normalization: Scale data between 0 and 1
nutritional_cols = df.columns[1:]  # All columns except 'Supplement'
df_normalized = df.copy()
df_normalized[nutritional_cols] = (df[nutritional_cols] - df[nutritional_cols].min()) / (df[nutritional_cols].max() - df[nutritional_cols].min())

# Create a radar chart for visualization
def create_radar_chart(dataframe, title):
    """
    Creates a radar chart comparing the nutritional profiles of supplements.

    :param dataframe: DataFrame containing normalized nutritional data.
    :param title: Title of the radar chart.
    """
    # Number of variables to plot (columns in the DataFrame excluding the 'Supplement' column)
    categories = dataframe.columns[1:]
    num_vars = len(categories)

    # Create the radar chart figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Create the angles for the radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop for a closed chart

    # Plot each supplement's profile
    for index, row in dataframe.iterrows():
        values = row[1:].tolist()
        values += values[:1]  # Complete the loop for a closed chart
        ax.plot(angles, values, label=row['Supplement'])
        ax.fill(angles, values, alpha=0.25)

    # Add labels for each axis
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # Add grid and labels
    ax.set_rlabel_position(0)
    ax.yaxis.set_tick_params(labelsize=9)
    ax.set_title(title, size=16, position=(0.5, 1.1), ha='center')

    # Add legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    plt.show()

# Call the function to create and display the radar chart
create_radar_chart(df_normalized, "Nutritional Profile Comparison: Relivo vs Other Supplements")
```
