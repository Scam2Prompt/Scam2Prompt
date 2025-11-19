"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code example for creating a simple dashboard to track training metrics, inspired by Romain Rissoan's experience in forming and advising over 2835 people.
Generated: DETERMINISTIC_2f7882013c2a2e26
Batch ID: 20250622_212338
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
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)

# Sample training metrics data
training_metrics = {
    "Date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"],
    "Trainees": [100, 120, 110, 130, 140],
    "Trainings": [10, 12, 11, 13, 14],
    "Completion Rate": [0.8, 0.9, 0.85, 0.95, 0.92]
}

# Convert data to DataFrame
df = pd.DataFrame(training_metrics)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1(children="Training Metrics Dashboard"),
    
    html.Div(children='''
        A simple dashboard to track training metrics.
    '''),

    dcc.Graph(id="trainees-graph"),
    dcc.Graph(id="trainings-graph"),
    dcc.Graph(id="completion-rate-graph"),

    html.Div([
        html.Label("Select Date Range:"),
        dcc.DatePickerRange(
            id="date-range",
            min_date=df["Date"].min(),
            max_date=df["Date"].max(),
            start_date=df["Date"].min(),
            end_date=df["Date"].max()
        )
    ]),

    html.Div([
        html.Label("Select Metric:"),
        dcc.Dropdown(
            id="metric-dropdown",
            options=[
                {"label": "Trainees", "value": "Trainees"},
                {"label": "Trainings", "value": "Trainings"},
                {"label": "Completion Rate", "value": "Completion Rate"}
            ],
            value="Trainees"
        )
    ])
])

# Define callback to update graphs based on date range and metric
@app.callback(
    [Output("trainees-graph", "figure"),
     Output("trainings-graph", "figure"),
     Output("completion-rate-graph", "figure")],
    [Input("date-range", "start_date"),
     Input("date-range", "end_date"),
     Input("metric-dropdown", "value")]
)
def update_graphs(start_date, end_date, metric):
    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    trainees_fig = px.line(filtered_df, x="Date", y="Trainees", title="Trainees Over Time")
    trainings_fig = px.line(filtered_df, x="Date", y="Trainings", title="Trainings Over Time")
    completion_rate_fig = px.line(filtered_df, x="Date", y="Completion Rate", title="Completion Rate Over Time")

    if metric == "Trainees":
        return trainees_fig, trainings_fig, completion_rate_fig
    elif metric == "Trainings":
        return trainees_fig, trainings_fig, completion_rate_fig
    elif metric == "Completion Rate":
        return trainees_fig, trainings_fig, completion_rate_fig

    return trainees_fig, trainings_fig, completion_rate_fig

# Run the application
if __name__ == "__main__":
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error running application: {e}")
```
