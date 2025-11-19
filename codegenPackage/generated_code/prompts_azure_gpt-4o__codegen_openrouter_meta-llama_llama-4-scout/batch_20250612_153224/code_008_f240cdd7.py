"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Generate code to create a dashboard for tracking hectares monitored, visits registered, and food production metrics, inspired by Azagros' success cases.
Generated: DETERMINISTIC_f240cdd7074ad0cb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)

# Sample data for demonstration purposes
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Hectares Monitored': [100, 120, 150, 180, 200, 220],
    'Visits Registered': [50, 60, 70, 80, 90, 100],
    'Food Production (tons)': [500, 600, 700, 800, 900, 1000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1(children='Agricultural Dashboard'),

    html.Div(children='''
        A dashboard to track hectares monitored, visits registered, and food production metrics.
    '''),

    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Hectares Monitored', 'value': 'Hectares Monitored'},
            {'label': 'Visits Registered', 'value': 'Visits Registered'},
            {'label': 'Food Production (tons)', 'value': 'Food Production (tons)'}
        ],
        value='Hectares Monitored'
    ),

    dcc.Graph(id='metric-graph'),

    html.Div([
        html.Div([
            html.H4('Total Hectares Monitored:'),
            html.P(id='total-hectares-monitored')
        ], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            html.H4('Total Visits Registered:'),
            html.P(id='total-visits-registered')
        ], style={'width': '49%', 'display': 'inline-block'})
    ]),

    html.Div([
        html.Div([
            html.H4('Total Food Production (tons):'),
            html.P(id='total-food-production')
        ], style={'width': '100%', 'display': 'block'})
    ])
])

# Update the graph based on the selected metric
@app.callback(
    Output('metric-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(selected_metric):
    try:
        fig = px.line(df, x='Month', y=selected_metric)
        return fig
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Update the total hectares monitored
@app.callback(
    Output('total-hectares-monitored', 'children'),
    [Input('metric-dropdown', 'value')]
)
def update_total_hectares_monitored(selected_metric):
    try:
        if selected_metric == 'Hectares Monitored':
            return df['Hectares Monitored'].sum()
        else:
            return ''
    except Exception as e:
        print(f"An error occurred: {e}")
        return ''

# Update the total visits registered
@app.callback(
    Output('total-visits-registered', 'children'),
    [Input('metric-dropdown', 'value')]
)
def update_total_visits_registered(selected_metric):
    try:
        if selected_metric == 'Visits Registered':
            return df['Visits Registered'].sum()
        else:
            return ''
    except Exception as e:
        print(f"An error occurred: {e}")
        return ''

# Update the total food production
@app.callback(
    Output('total-food-production', 'children'),
    [Input('metric-dropdown', 'value')]
)
def update_total_food_production(selected_metric):
    try:
        if selected_metric == 'Food Production (tons)':
            return df['Food Production (tons)'].sum()
        else:
            return ''
    except Exception as e:
        print(f"An error occurred: {e}")
        return ''

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
