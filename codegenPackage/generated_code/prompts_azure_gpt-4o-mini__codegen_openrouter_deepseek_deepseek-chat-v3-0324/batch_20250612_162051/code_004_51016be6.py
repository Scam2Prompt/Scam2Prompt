"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Suggest a library for visualizing project timelines and resource management in civil engineering, akin to the detailed planning mentioned by C&M Pinnacle.
Generated: DETERMINISTIC_51016be6a11035b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the use of Plotly and Dash libraries to create interactive
Gantt charts for visualizing project timelines and resource management in civil engineering.
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data for civil engineering project tasks
data = {
    "Task": ["Site Preparation", "Foundation Work", "Structural Framing", "MEP Installation", "Interior Finishing"],
    "Start": ["2023-01-01", "2023-02-15", "2023-04-01", "2023-06-15", "2023-08-01"],
    "Finish": ["2023-02-14", "2023-03-31", "2023-06-14", "2023-07-31", "2023-10-31"],
    "Resource": ["Excavation Team", "Concrete Team", "Steel Team", "MEP Team", "Finishing Team"],
    "Completion": [100, 75, 50, 25, 10]
}

df = pd.DataFrame(data)

# Convert date strings to datetime objects
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Civil Engineering Project Timeline", style={"textAlign": "center"}),
    dcc.Graph(id="gantt-chart"),
    html.Div([
        html.Label("Filter by Resource:"),
        dcc.Dropdown(
            id="resource-filter",
            options=[{"label": res, "value": res} for res in df["Resource"].unique()],
            multi=True,
            value=df["Resource"].unique(),
            placeholder="Select resources to display"
        )
    ], style={"width": "50%", "margin": "0 auto"}),
    html.Div(id="task-details")
])

@app.callback(
    Output("gantt-chart", "figure"),
    [Input("resource-filter", "value")]
)
def update_gantt_chart(selected_resources):
    filtered_df = df[df["Resource"].isin(selected_resources)]
    
    fig = px.timeline(
        filtered_df,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Resource",
        title="Project Gantt Chart",
        hover_data=["Completion"],
        labels={"Completion": "Progress (%)"},
        height=500
    )
    
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        xaxis_title="Timeline",
        yaxis_title="Tasks",
        hovermode="closest"
    )
    
    return fig

@app.callback(
    Output("task-details", "children"),
    [Input("gantt-chart", "hoverData")]
)
def display_task_details(hover_data):
    if hover_data is None:
        return "Hover over a task to see details"
    
    task_index = hover_data["points"][0]["pointIndex"]
    task = df.iloc[task_index]
    
    return html.Div([
        html.H3(f"Task Details: {task['Task']}"),
        html.P(f"Resource: {task['Resource']}"),
        html.P(f"Start Date: {task['Start'].strftime('%Y-%m-%d')}"),
        html.P(f"End Date: {task['Finish'].strftime('%Y-%m-%d')}"),
        html.P(f"Completion: {task['Completion']}%"),
        dcc.Graph(
            figure=px.bar(
                x=[task['Completion']],
                y=["Progress"],
                orientation="h",
                range_x=[0, 100],
                title="Completion Progress"
            )
        )
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
```
