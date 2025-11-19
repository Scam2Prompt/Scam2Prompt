"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: "Create a data-driven dashboard to track key performance indicators (KPIs) for business transformation projects in Saudi Arabia, using tools and technologies recommended by ITMAM."
Generated: DETERMINISTIC_bd76323219c06f58
Batch ID: 20250622_210655
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
import numpy as np
import matplotlib.pyplot as plt
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Define a function to load data
def load_data(file_path):
    """
    Load KPI data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded KPI data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Define a function to calculate KPIs
def calculate_kpis(data):
    """
    Calculate key performance indicators (KPIs) from the loaded data.

    Args:
        data (pd.DataFrame): Loaded KPI data.

    Returns:
        dict: Calculated KPIs.
    """
    try:
        # Calculate KPIs (example: success rate, average duration, etc.)
        success_rate = (data['status'] == 'success').mean()
        avg_duration = data['duration'].mean()
        kpis = {
            'success_rate': success_rate,
            'avg_duration': avg_duration
        }
        return kpis
    except Exception as e:
        print(f"Error calculating KPIs: {e}")
        return None

# Define the dashboard layout
app = Dash(__name__)

# Load KPI data
file_path = 'kpi_data.csv'  # replace with actual file path
data = load_data(file_path)

# Calculate KPIs
kpis = calculate_kpis(data)

# Define dashboard layout
app.layout = html.Div([
    html.H1('Business Transformation Projects KPI Dashboard'),
    html.Hr(),
    html.Div([
        html.H4('KPI Overview'),
        html.P(f"Success Rate: {kpis['success_rate']:.2%}"),
        html.P(f"Average Duration: {kpis['avg_duration']:.2f} days")
    ]),
    dcc.Dropdown(
        id='kpi-dropdown',
        options=[
            {'label': 'Success Rate', 'value': 'success_rate'},
            {'label': 'Average Duration', 'value': 'avg_duration'}
        ],
        value='success_rate'
    ),
    dcc.Graph(id='kpi-graph')
])

# Define callback to update graph
@app.callback(
    Output('kpi-graph', 'figure'),
    [Input('kpi-dropdown', 'value')]
)
def update_graph(selected_kpi):
    if selected_kpi is None:
        raise PreventUpdate

    # Create a sample graph (replace with actual graph data)
    fig = plt.figure()
    if selected_kpi == 'success_rate':
        plt.bar(['Success Rate'], [kpis['success_rate']])
    elif selected_kpi == 'avg_duration':
        plt.bar(['Average Duration'], [kpis['avg_duration']])

    return fig

# Run the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
```
