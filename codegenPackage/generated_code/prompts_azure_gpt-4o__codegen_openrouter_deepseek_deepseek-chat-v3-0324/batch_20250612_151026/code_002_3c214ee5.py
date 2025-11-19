"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Generate Python code for a dashboard that visualizes metrics such as the number of courses imparted, hours of consultancy, and executives trained, similar to the statistics provided by Virtual5.
Generated: DETERMINISTIC_3c214ee528f27f6f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Sample data
data = {
    "Metric": ["Courses Imparted", "Hours of Consultancy", "Executives Trained"],
    "Count": [150, 500, 200],
    "Target": [200, 600, 250]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Virtual5 Metrics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='metrics-bar-chart',
                figure=px.bar(
                    df,
                    x='Metric',
                    y='Count',
                    title='Current Metrics',
                    color='Metric',
                    text='Count'
                ).update_layout(
                    showlegend=False,
                    yaxis_title="Count",
                    xaxis_title=""
                )
            )
        ], width=6),
        
        dbc.Col([
            dcc.Graph(
                id='metrics-pie-chart',
                figure=px.pie(
                    df,
                    names='Metric',
                    values='Count',
                    title='Metrics Distribution',
                    hole=0.3
                )
            )
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='progress-chart',
                figure=px.bar(
                    df,
                    x='Metric',
                    y=['Count', 'Target'],
                    title='Progress Towards Targets',
                    barmode='group',
                    labels={'value': 'Count', 'variable': 'Type'}
                )
            )
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Summary Statistics", className="mt-4"),
                html.P(f"Total Courses Imparted: {df[df['Metric'] == 'Courses Imparted']['Count'].values[0]}"),
                html.P(f"Total Hours of Consultancy: {df[df['Metric'] == 'Hours of Consultancy']['Count'].values[0]}"),
                html.P(f"Total Executives Trained: {df[df['Metric'] == 'Executives Trained']['Count'].values[0]}"),
            ], className="p-3 border rounded")
        ], width=12)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
```
