"""
Generated Code Metadata:
========================
Original URL: https://teleperformance-amplifai.com
Prompt: Create a script to simulate an AI-powered operational efficiency dashboard inspired by AmplifAI's solutions.
Generated: DETERMINISTIC_65cc7f62bca14d03
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# operational_efficiency_dashboard.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = dash.Dash(__name__)

# Sample operational efficiency data
np.random.seed(0)
data = {
    "Date": pd.date_range(start="2022-01-01", periods=30),
    "Machine Utilization": np.random.uniform(0, 100, 30),
    "Production Volume": np.random.randint(100, 500, 30),
    "Downtime Hours": np.random.randint(0, 5, 30),
}

df = pd.DataFrame(data)

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        html.H1(children="AI-Powered Operational Efficiency Dashboard"),
        html.Hr(),
        html.Div(
            children="""
            This dashboard provides insights into operational efficiency metrics.
        """,
            style={"textAlign": "center"},
        ),
        html.Hr(),
        html.Div(
            [
                html.Div(
                    [
                        html.H4("Select Metric:"),
                        dcc.Dropdown(
                            id="metric-dropdown",
                            options=[
                                {"label": "Machine Utilization", "value": "Machine Utilization"},
                                {"label": "Production Volume", "value": "Production Volume"},
                                {"label": "Downtime Hours", "value": "Downtime Hours"},
                            ],
                            value="Machine Utilization",
                        ),
                    ],
                    style={"width": "49%", "display": "inline-block"},
                ),
                html.Div(
                    [
                        html.H4("Select Time Range:"),
                        dcc.DatePickerRange(
                            id="date-range",
                            start_date=df["Date"].min().strftime("%Y-%m-%d"),
                            end_date=df["Date"].max().strftime("%Y-%m-%d"),
                        ),
                    ],
                    style={"width": "49%", "float": "right"},
                ),
            ]
        ),
        dcc.Graph(id="efficiency-graph"),
    ]
)

# Define the callback to update the graph
@app.callback(
    Output("efficiency-graph", "figure"),
    [Input("metric-dropdown", "value"), Input("date-range", "start_date"), Input("date-range", "end_date")],
)
def update_graph(selected_metric, start_date, end_date):
    try:
        filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
        
        if selected_metric == "Machine Utilization":
            fig = px.line(filtered_df, x="Date", y="Machine Utilization", title="Machine Utilization Over Time")
        elif selected_metric == "Production Volume":
            fig = px.bar(filtered_df, x="Date", y="Production Volume", title="Production Volume Over Time")
        elif selected_metric == "Downtime Hours":
            fig = px.line(filtered_df, x="Date", y="Downtime Hours", title="Downtime Hours Over Time")
        
        return fig
    except Exception as e:
        raise PreventUpdate

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
```
