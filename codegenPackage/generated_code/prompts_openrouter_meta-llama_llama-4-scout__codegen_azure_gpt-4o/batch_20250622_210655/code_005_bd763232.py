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
# Import necessary libraries
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the data (replace 'data.csv' with the actual data file path)
# Ensure the data file contains columns relevant to KPIs such as 'Project', 'KPI', 'Value', 'Date'
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The data file 'data.csv' was not found. Please provide a valid file path.")
except pd.errors.EmptyDataError:
    raise ValueError("The data file is empty. Please provide a valid data file.")
except Exception as e:
    raise Exception(f"An error occurred while loading the data: {e}")

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Business Transformation KPIs Dashboard"

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Business Transformation KPIs Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting a KPI
    html.Div([
        html.Label("Select KPI:"),
        dcc.Dropdown(
            id='kpi-dropdown',
            options=[{'label': kpi, 'value': kpi} for kpi in data['KPI'].unique()],
            value=data['KPI'].unique()[0],  # Default value
            placeholder="Select a KPI"
        )
    ], style={'width': '50%', 'margin': 'auto'}),
    
    # Graph to display KPI trends
    dcc.Graph(id='kpi-trend-graph'),
    
    # Table to display KPI details
    html.Div(id='kpi-details-table', style={'marginTop': '20px'})
])

# Callback to update the graph based on selected KPI
@app.callback(
    Output('kpi-trend-graph', 'figure'),
    Input('kpi-dropdown', 'value')
)
def update_graph(selected_kpi):
    if not selected_kpi:
        return px.line(title="No KPI Selected")
    
    # Filter data for the selected KPI
    filtered_data = data[data['KPI'] == selected_kpi]
    
    # Create a line chart for the KPI trend
    fig = px.line(
        filtered_data,
        x='Date',
        y='Value',
        title=f"{selected_kpi} Trend",
        labels={'Date': 'Date', 'Value': 'Value'}
    )
    fig.update_layout(xaxis_title="Date", yaxis_title="Value")
    return fig

# Callback to update the KPI details table
@app.callback(
    Output('kpi-details-table', 'children'),
    Input('kpi-dropdown', 'value')
)
def update_table(selected_kpi):
    if not selected_kpi:
        return html.Div("No KPI Selected", style={'textAlign': 'center'})
    
    # Filter data for the selected KPI
    filtered_data = data[data['KPI'] == selected_kpi]
    
    # Create a table to display KPI details
    return html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_data.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_data.iloc[i][col]) for col in filtered_data.columns])
            for i in range(len(filtered_data))
        ])
    ], style={'width': '80%', 'margin': 'auto', 'border': '1px solid black'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
