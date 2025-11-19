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
# Import required libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)

# Define sample KPI data
kpi_data = {
    "KPI": ["Velocity", "Burn-down", "Code Quality", "Deployment Frequency"],
    "Target": [50, 100, 90, 10],
    "Actual": [40, 90, 85, 8],
}

# Convert KPI data to DataFrame
kpi_df = pd.DataFrame(kpi_data)

# Define the layout of the dashboard
app.layout = html.Div(
    children=[
        html.H1(children="Development Project KPI Dashboard"),
        html.Hr(),
        html.Div(
            children="""
            This dashboard tracks key performance indicators (KPIs) for a development project.
            """
        ),
        dcc.Dropdown(
            id="kpi-dropdown",
            options=[
                {"label": "Velocity", "value": "Velocity"},
                {"label": "Burn-down", "value": "Burn-down"},
                {"label": "Code Quality", "value": "Code Quality"},
                {"label": "Deployment Frequency", "value": "Deployment Frequency"},
            ],
            value="Velocity",
        ),
        dcc.Graph(id="kpi-graph"),
        html.Div(id="kpi-table"),
    ]
)

# Define a callback to update the graph
@app.callback(
    Output("kpi-graph", "figure"),
    [Input("kpi-dropdown", "value")],
)
def update_graph(selected_kpi):
    try:
        # Filter data based on selected KPI
        filtered_df = kpi_df[kpi_df["KPI"] == selected_kpi]
        
        # Create a bar chart
        fig = px.bar(
            filtered_df,
            x="KPI",
            y=["Target", "Actual"],
            barmode="group",
            title=f"{selected_kpi} KPI",
        )
        return fig
    except Exception as e:
        # Handle any exceptions
        print(f"Error updating graph: {str(e)}")
        return None

# Define a callback to update the KPI table
@app.callback(
    Output("kpi-table", "children"),
    [Input("kpi-dropdown", "value")],
)
def update_table(selected_kpi):
    try:
        # Filter data based on selected KPI
        filtered_df = kpi_df[kpi_df["KPI"] == selected_kpi]
        
        # Display KPI data in a table
        table = html.Table(
            children=[
                html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td(filtered_df.iloc[0][col])
                                for col in filtered_df.columns
                            ]
                        )
                    ]
                ),
            ]
        )
        return table
    except Exception as e:
        # Handle any exceptions
        print(f"Error updating table: {str(e)}")
        return None

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
```
