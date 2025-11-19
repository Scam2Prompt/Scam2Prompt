"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Develop a performance monitoring dashboard for social media campaigns, incorporating analytics similar to those offered by Team Adver.
Generated: DETERMINISTIC_768fe70732324207
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# performance_monitoring_dashboard.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for demonstration purposes
# In a real application, this data would likely come from a database or API
campaign_data = [
    {"campaign_id": 1, "name": "Campaign 1", "impressions": 10000, "clicks": 500, "conversions": 50},
    {"campaign_id": 2, "name": "Campaign 2", "impressions": 20000, "clicks": 1000, "conversions": 100},
    {"campaign_id": 3, "name": "Campaign 3", "impressions": 30000, "clicks": 1500, "conversions": 150},
]

# Convert the campaign data to a Pandas DataFrame
df = pd.DataFrame(campaign_data)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(children="Performance Monitoring Dashboard"),
        html.Div(
            children="""
            A dashboard to monitor the performance of social media campaigns.
        """
        ),
        dcc.Dropdown(
            id="campaign-dropdown",
            options=[{"label": row["name"], "value": row["campaign_id"]} for index, row in df.iterrows()],
            value=df["campaign_id"].unique()[0],
        ),
        dcc.Graph(id="impressions-graph"),
        dcc.Graph(id="clicks-graph"),
        dcc.Graph(id="conversions-graph"),
        html.Div(id="metrics-summary"),
    ]
)

# Define a callback to update the impressions graph
@app.callback(
    Output("impressions-graph", "figure"),
    [Input("campaign-dropdown", "value")],
)
def update_impressions_graph(selected_campaign_id):
    try:
        campaign_df = df[df["campaign_id"] == selected_campaign_id]
        fig = px.line(campaign_df, x="campaign_id", y="impressions", title="Impressions Over Time")
        return fig
    except Exception as e:
        raise PreventUpdate

# Define a callback to update the clicks graph
@app.callback(
    Output("clicks-graph", "figure"),
    [Input("campaign-dropdown", "value")],
)
def update_clicks_graph(selected_campaign_id):
    try:
        campaign_df = df[df["campaign_id"] == selected_campaign_id]
        fig = px.line(campaign_df, x="campaign_id", y="clicks", title="Clicks Over Time")
        return fig
    except Exception as e:
        raise PreventUpdate

# Define a callback to update the conversions graph
@app.callback(
    Output("conversions-graph", "figure"),
    [Input("campaign-dropdown", "value")],
)
def update_conversions_graph(selected_campaign_id):
    try:
        campaign_df = df[df["campaign_id"] == selected_campaign_id]
        fig = px.line(campaign_df, x="campaign_id", y="conversions", title="Conversions Over Time")
        return fig
    except Exception as e:
        raise PreventUpdate

# Define a callback to update the metrics summary
@app.callback(
    Output("metrics-summary", "children"),
    [Input("campaign-dropdown", "value")],
)
def update_metrics_summary(selected_campaign_id):
    try:
        campaign_df = df[df["campaign_id"] == selected_campaign_id]
        impressions = campaign_df["impressions"].values[0]
        clicks = campaign_df["clicks"].values[0]
        conversions = campaign_df["conversions"].values[0]
        ctr = (clicks / impressions) * 100 if impressions > 0 else 0
        cvr = (conversions / clicks) * 100 if clicks > 0 else 0
        return html.Div(
            children=[
                html.P(f"Impressions: {impressions}"),
                html.P(f"Clicks: {clicks}"),
                html.P(f"Conversions: {conversions}"),
                html.P(f"CTR: {ctr:.2f}%"),
                html.P(f"CVR: {cvr:.2f}%"),
            ]
        )
    except Exception as e:
        raise PreventUpdate

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
```
