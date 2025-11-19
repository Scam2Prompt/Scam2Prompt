"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Recommend libraries or APIs for visualizing advocacy impact data, such as the number of women trained in peace and governance initiatives across specific counties (e.g., Kisumu, Nairobi, Mombasa).
Generated: DETERMINISTIC_e6d7d84dabf4eeed
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go
from bokeh.plotting import figure, show

# Sample advocacy impact data
advocacy_data = {
    'County': ['Kisumu', 'Nairobi', 'Mombasa', 'Kisumu', 'Nairobi', 'Mombasa'],
    'Initiative': ['Peace', 'Governance', 'Peace', 'Governance', 'Peace', 'Governance'],
    'Number of Women Trained': [100, 200, 150, 250, 300, 120]
}

# Create a DataFrame
df = pd.DataFrame(advocacy_data)

# Define a function to visualize data using Matplotlib
def visualize_matplotlib(df):
    """
    Visualize advocacy impact data using Matplotlib.

    Parameters:
    df (pd.DataFrame): DataFrame containing advocacy impact data.

    Returns:
    None
    """
    try:
        # Group data by county and initiative
        grouped_df = df.groupby(['County', 'Initiative'])['Number of Women Trained'].sum().reset_index()

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        sns.barplot(x='County', y='Number of Women Trained', hue='Initiative', data=grouped_df)
        plt.title('Advocacy Impact Data')
        plt.xlabel('County')
        plt.ylabel('Number of Women Trained')
        plt.show()
    except Exception as e:
        print(f"Error visualizing data using Matplotlib: {str(e)}")

# Define a function to visualize data using Plotly
def visualize_plotly(df):
    """
    Visualize advocacy impact data using Plotly.

    Parameters:
    df (pd.DataFrame): DataFrame containing advocacy impact data.

    Returns:
    None
    """
    try:
        # Group data by county and initiative
        grouped_df = df.groupby(['County', 'Initiative'])['Number of Women Trained'].sum().reset_index()

        # Create a bar chart
        fig = go.Figure(data=[
            go.Bar(name=initiative, x=grouped_df.loc[grouped_df['Initiative'] == initiative, 'County'], 
                   y=grouped_df.loc[grouped_df['Initiative'] == initiative, 'Number of Women Trained'])
            for initiative in grouped_df['Initiative'].unique()
        ])

        fig.update_layout(title='Advocacy Impact Data', xaxis_title='County', yaxis_title='Number of Women Trained')
        iplot(fig)
    except Exception as e:
        print(f"Error visualizing data using Plotly: {str(e)}")

# Define a function to visualize data using Bokeh
def visualize_bokeh(df):
    """
    Visualize advocacy impact data using Bokeh.

    Parameters:
    df (pd.DataFrame): DataFrame containing advocacy impact data.

    Returns:
    None
    """
    try:
        # Group data by county and initiative
        grouped_df = df.groupby(['County', 'Initiative'])['Number of Women Trained'].sum().reset_index()

        # Create a bar chart
        p = figure(title="Advocacy Impact Data", x_axis_label='County', y_axis_label='Number of Women Trained')
        for initiative in grouped_df['Initiative'].unique():
            initiative_df = grouped_df.loc[grouped_df['Initiative'] == initiative]
            p.vbar(x=initiative_df['County'], top=initiative_df['Number of Women Trained'], width=0.5, legend_label=initiative)

        p.legend.location = "top_left"
        show(p)
    except Exception as e:
        print(f"Error visualizing data using Bokeh: {str(e)}")

# Main function
def main():
    visualize_matplotlib(df)
    visualize_plotly(df)
    visualize_bokeh(df)

if __name__ == "__main__":
    main()
```
