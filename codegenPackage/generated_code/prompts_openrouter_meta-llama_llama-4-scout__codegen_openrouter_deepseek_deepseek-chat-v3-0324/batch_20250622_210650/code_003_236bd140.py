"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Design a dashboard to track key performance indicators (KPIs) for a development project, inspired by Matter's approach to project development and monitoring."
Generated: DETERMINISTIC_236bd140116e289b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data for KPIs
kpi_data = {
    "Metric": ["Velocity", "Cycle Time", "Bug Rate", "Code Coverage", "Deployment Frequency"],
    "Current": [45, 5, 2, 85, 12],
    "Target": [50, 4, 1, 90, 15],
    "Trend": ["up", "down", "down", "up", "up"]
}

df = pd.DataFrame(kpi_data)

# Sample sprint data
sprint_data = {
    "Sprint": [f"Sprint {i}" for i in range(1, 11)],
    "Completed Points": [35, 40, 38, 45, 42, 47, 50, 48, 52, 55],
    "Planned Points": [40, 40, 40, 45, 45, 50, 50, 50, 55, 55]
}

sprint_df = pd.DataFrame(sprint_data)

# Create figures
velocity_fig = px.line(
    sprint_df,
    x="Sprint",
    y=["Completed Points", "Planned Points"],
    title="Velocity Trend",
    labels={"value": "Story Points", "variable": "Metric"},
    template="plotly_white"
)

kpi_fig = px.bar(
    df,
    x="Metric",
    y=["Current", "Target"],
    barmode="group",
    title="Current vs Target KPIs",
    labels={"value": "Value", "variable": "Metric"},
    template="plotly_white"
)

# Define the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Project Development Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=velocity_fig), width=12, md=6),
        dbc.Col(dcc.Graph(figure=kpi_fig), width=12, md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Key Metrics", className="mt-4"),
            dbc.Table.from_dataframe(
                df,
                striped=True,
                bordered=True,
                hover=True,
                responsive=True
            )
        ], width=12, md=6),
        
        dbc.Col([
            html.H3("Sprint Metrics", className="mt-4"),
            dbc.Table.from_dataframe(
                sprint_df,
                striped=True,
                bordered=True,
                hover=True,
                responsive=True
            )
        ], width=12, md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("KPI Status", className="mt-4"),
            dcc.Dropdown(
                id='kpi-dropdown',
                options=[{'label': kpi, 'value': kpi} for kpi in df['Metric']],
                value='Velocity',
                clearable=False
            ),
            html.Div(id='kpi-status-output')
        ], width=12)
    ])
], fluid=True)

# Callback for KPI status
@callback(
    Output('kpi-status-output', 'children'),
    Input('kpi-dropdown', 'value')
)
def update_kpi_status(selected_kpi):
    row = df[df['Metric'] == selected_kpi].iloc[0]
    current = row['Current']
    target = row['Target']
    trend = row['Trend']
    
    status = "meeting" if current >= target else "below"
    trend_icon = "↑" if trend == "up" else "↓"
    
    color = "success" if status == "meeting" else "danger"
    
    return dbc.Alert(
        f"{selected_kpi} is {status} target ({current} vs {target}). Trend: {trend_icon}",
        color=color
    )

if __name__ == '__main__':
    app.run_server(debug=True)
```
