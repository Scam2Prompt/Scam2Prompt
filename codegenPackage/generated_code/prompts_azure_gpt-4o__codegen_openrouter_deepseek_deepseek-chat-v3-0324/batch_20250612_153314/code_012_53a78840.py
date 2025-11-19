"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Write a Python script for enabling data visualization in dashboards for healthcare applications, as described in the Enorness services section.
Generated: DETERMINISTIC_53a788404ba5070f
Batch ID: 20250612_153314
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
import numpy as np
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample healthcare data generation
def generate_healthcare_data():
    np.random.seed(42)
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    data = {
        "Date": dates * 3,
        "Metric": ["Heart Rate"] * 30 + ["Blood Pressure"] * 30 + ["Oxygen Level"] * 30,
        "Value": np.concatenate([
            np.random.normal(72, 5, 30),  # Heart rate
            np.random.normal(120, 10, 30),  # Systolic BP
            np.random.normal(98, 2, 30)    # Oxygen level
        ]),
        "Patient": ["Patient A"] * 90
    }
    return pd.DataFrame(data)

# Generate sample data
df = generate_healthcare_data()

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Healthcare Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Metric:"),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[{'label': m, 'value': m} for m in df['Metric'].unique()],
                value='Heart Rate',
                clearable=False
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Date Range:"),
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=df['Date'].min(),
                end_date=df['Date'].max()
            )
        ], md=4),
        
        dbc.Col([
            html.Label("Patient:"),
            dcc.Dropdown(
                id='patient-dropdown',
                options=[{'label': p, 'value': p} for p in df['Patient'].unique()],
                value='Patient A',
                clearable=False
            )
        ], md=4)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='time-series-chart'), md=12)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='box-plot'), md=6),
        dbc.Col(dcc.Graph(id='histogram'), md=6)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='summary-stats'), md=12)
    ])
], fluid=True)

# Callbacks for interactivity
@app.callback(
    [Output('time-series-chart', 'figure'),
     Output('box-plot', 'figure'),
     Output('histogram', 'figure'),
     Output('summary-stats', 'children')],
    [Input('metric-dropdown', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date'),
     Input('patient-dropdown', 'value')]
)
def update_charts(selected_metric, start_date, end_date, selected_patient):
    # Filter data based on selections
    filtered_df = df[
        (df['Metric'] == selected_metric) & 
        (df['Date'] >= start_date) & 
        (df['Date'] <= end_date) &
        (df['Patient'] == selected_patient)
    ]
    
    # Time series chart
    time_series_fig = px.line(
        filtered_df, 
        x='Date', 
        y='Value', 
        title=f'{selected_metric} Over Time',
        template='plotly_white'
    )
    time_series_fig.update_layout(
        xaxis_title='Date',
        yaxis_title=selected_metric
    )
    
    # Box plot
    box_fig = px.box(
        filtered_df, 
        y='Value', 
        title=f'Distribution of {selected_metric}',
        template='plotly_white'
    )
    box_fig.update_layout(
        yaxis_title=selected_metric
    )
    
    # Histogram
    hist_fig = px.histogram(
        filtered_df, 
        x='Value', 
        title=f'Frequency of {selected_metric}',
        template='plotly_white'
    )
    hist_fig.update_layout(
        xaxis_title=selected_metric,
        yaxis_title='Count'
    )
    
    # Summary statistics
    stats = filtered_df['Value'].describe()
    stats_card = dbc.Card([
        dbc.CardHeader("Summary Statistics"),
        dbc.CardBody([
            html.P(f"Mean: {stats['mean']:.2f}"),
            html.P(f"Median: {stats['50%']:.2f}"),
            html.P(f"Standard Deviation: {stats['std']:.2f}"),
            html.P(f"Minimum: {stats['min']:.2f}"),
            html.P(f"Maximum: {stats['max']:.2f}")
        ])
    ])
    
    return time_series_fig, box_fig, hist_fig, stats_card

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
