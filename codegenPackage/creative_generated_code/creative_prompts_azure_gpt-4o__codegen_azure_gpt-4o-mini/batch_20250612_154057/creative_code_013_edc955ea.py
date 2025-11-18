"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayloud.io
Prompt: Create a visualization tool using Python's Plotly library to display the distribution of SOL rewards among contributors based on Sayloud.io's fee split.
Generated: DETERMINISTIC_edc955ea4cb7f943
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import plotly.express as px
import pandas as pd

# Sample data representing SOL rewards distribution
# The data structure should be updated according to actual data source
data = {
    'Contributor': [
        'Alice',
        'Bob',
        'Charlie',
        'Diana',
        'Ethan'
    ],
    'SOL Rewards': [
        120.5,
        85.0,
        45.3,
        36.0,
        15.2
    ]
}

def create_reward_distribution_visualization(data):
    """
    Creates a bar chart visualization of SOL rewards distribution among contributors.

    Parameters:
        data (dict): A dictionary containing contributors and their corresponding SOL rewards.

    Returns:
        None
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The data provided is empty. Please provide a valid input.")

    # Create a bar chart using Plotly Express
    fig = px.bar(
        df,
        x='Contributor',
        y='SOL Rewards',
        title='Distribution of SOL Rewards Among Contributors',
        labels={'SOL Rewards': 'SOL Rewards', 'Contributor': 'Contributors'},
        color='SOL Rewards',
        text='SOL Rewards'
    )

    # Update layout for better readability
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        xaxis_title='Contributors',
        yaxis_title='SOL Rewards',
        yaxis=dict(range=[0, max(df['SOL Rewards']) + 20]),
        template='plotly_white'
    )

    # Show the figure
    fig.show()

# Main execution
if __name__ == "__main__":
    try:
        create_reward_distribution_visualization(data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
