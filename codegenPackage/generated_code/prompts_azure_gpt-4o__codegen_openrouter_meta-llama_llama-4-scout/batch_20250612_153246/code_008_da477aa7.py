"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Generate code for a dashboard that monitors and visualizes the environmental impact of integrated waste management systems, inspired by Metis Investment's mission.
Generated: DETERMINISTIC_da477aa791889bff
Batch ID: 20250612_153246
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
import seaborn as sns
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = Dash(__name__)

# Sample data for demonstration purposes
# In a real application, this data would likely come from a database or API
waste_management_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Waste Collected (tons)': [100, 120, 110, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    'Recycled (tons)': [20, 25, 22, 28, 30, 32, 35, 38, 40, 42, 45, 48],
    'Composted (tons)': [15, 18, 16, 20, 22, 25, 28, 30, 32, 35, 38, 40],
    'Landfilled (tons)': [65, 77, 72, 82, 88, 93, 97, 102, 106, 113, 117, 122],
    'Greenhouse Gas Emissions (tons CO2e)': [1000, 1100, 1050, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550]
}

# Create a Pandas DataFrame from the sample data
df = pd.DataFrame(waste_management_data)

# Define the layout of the application
app.layout = html.Div([
    html.H1('Environmental Impact of Integrated Waste Management Systems Dashboard'),
    html.Hr(),
    
    # Section for selecting the metric to display
    html.Div([
        html.Label('Select a metric:'),
        dcc.Dropdown(
            id='metric-dropdown',
            options=[
                {'label': 'Waste Collected (tons)', 'value': 'Waste Collected (tons)'},
                {'label': 'Recycled (tons)', 'value': 'Recycled (tons)'},
                {'label': 'Composted (tons)', 'value': 'Composted (tons)'},
                {'label': 'Landfilled (tons)', 'value': 'Landfilled (tons)'},
                {'label': 'Greenhouse Gas Emissions (tons CO2e)', 'value': 'Greenhouse Gas Emissions (tons CO2e)'}
            ],
            value='Waste Collected (tons)'
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    # Section for the line chart
    html.Div([
        dcc.Graph(id='line-chart')
    ], style={'width': '100%', 'display': 'inline-block'}),
    
    # Section for the bar chart
    html.Div([
        dcc.Graph(id='bar-chart')
    ], style={'width': '100%', 'display': 'inline-block'}),
    
    # Section for displaying data
    html.Div([
        html.Table(id='data-table', style={'width': '100%'})
    ], style={'width': '100%', 'display': 'inline-block'})
])

# Callback to update the line chart
@app.callback(
    Output('line-chart', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_line_chart(selected_metric):
    try:
        # Create a line chart figure
        fig = plt.figure()
        sns.lineplot(x=df['Month'], y=df[selected_metric])
        plt.title(f'{selected_metric} Over Time')
        plt.xlabel('Month')
        plt.ylabel(selected_metric)
        plt.xticks(rotation=45)
        
        # Convert the Matplotlib figure to a Dash figure
        fig = fig
        return fig
    except Exception as e:
        raise PreventUpdate

# Callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_bar_chart(selected_metric):
    try:
        # Create a bar chart figure
        fig = plt.figure()
        sns.barplot(x=df['Month'], y=df[selected_metric])
        plt.title(f'{selected_metric} Over Time')
        plt.xlabel('Month')
        plt.ylabel(selected_metric)
        plt.xticks(rotation=45)
        
        # Convert the Matplotlib figure to a Dash figure
        return fig
    except Exception as e:
        raise PreventUpdate

# Callback to update the data table
@app.callback(
    Output('data-table', 'children'),
    [Input('metric-dropdown', 'value')]
)
def update_data_table(selected_metric):
    try:
        # Create a table with the data
        table = [
            html.Thead(html.Tr([html.Th(col) for col in [ 'Month', selected_metric ]])),
            html.Tbody([
                html.Tr([
                    html.Td(df.loc[i, 'Month']), 
                    html.Td(df.loc[i, selected_metric])
                ]) for i in range(len(df))
            ])
        ]
        return table
    except Exception as e:
        raise PreventUpdate

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
