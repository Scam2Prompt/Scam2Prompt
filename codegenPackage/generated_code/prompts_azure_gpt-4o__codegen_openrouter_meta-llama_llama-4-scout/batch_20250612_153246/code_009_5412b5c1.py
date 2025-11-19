"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Provide an example of how to implement a feature in an ERP system similar to SOLPEN that supports rapid decision-making through real-time data visualization.
Generated: DETERMINISTIC_5412b5c102d5cb5c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**SOLPEN-like ERP System Feature: Real-time Data Visualization**
===========================================================

**System Requirements**
-----------------------

* Python 3.9+
* Dash 2.0+
* Pandas 1.4+
* NumPy 1.22+

**Implementation**
-----------------

```python
# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Sample data
np.random.seed(0)
data = {
    "Category": np.random.choice(["A", "B", "C"], size=100),
    "Subcategory": np.random.choice(["X", "Y", "Z"], size=100),
    "Value": np.random.rand(100)
}
df = pd.DataFrame(data)

# Define the layout
app.layout = dbc.Container(
    [
        html.H1("Real-time Data Visualization"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="category-dropdown",
                        options=[{"label": cat, "value": cat} for cat in df["Category"].unique()],
                        value=df["Category"].unique()[0],
                    ),
                    md=4,
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="subcategory-dropdown",
                        options=[{"label": subcat, "value": subcat} for subcat in df["Subcategory"].unique()],
                        value=df["Subcategory"].unique()[0],
                    ),
                    md=4,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="bar-chart"),
                    md=6,
                ),
                dbc.Col(
                    dcc.Graph(id="pie-chart"),
                    md=6,
                ),
            ]
        ),
    ]
)

# Define callback for bar chart
@app.callback(
    Output("bar-chart", "figure"),
    [Input("category-dropdown", "value"), Input("subcategory-dropdown", "value")],
)
def update_bar_chart(category, subcategory):
    try:
        filtered_df = df[(df["Category"] == category)]
        fig = {
            "data": [
                {
                    "x": filtered_df["Subcategory"],
                    "y": filtered_df.groupby("Subcategory")["Value"].sum(),
                    "type": "bar",
                }
            ],
            "layout": {"title": f"Bar Chart - {category}", "xaxis": {"title": "Subcategory"}, "yaxis": {"title": "Value"}},
        }
        return fig
    except Exception as e:
        raise PreventUpdate

# Define callback for pie chart
@app.callback(
    Output("pie-chart", "figure"),
    [Input("category-dropdown", "value"), Input("subcategory-dropdown", "value")],
)
def update_pie_chart(category, subcategory):
    try:
        filtered_df = df[(df["Category"] == category)]
        fig = {
            "data": [
                {
                    "labels": filtered_df["Subcategory"],
                    "values": filtered_df.groupby("Subcategory")["Value"].sum(),
                    "type": "pie",
                }
            ],
            "layout": {"title": f"Pie Chart - {category}"},
        }
        return fig
    except Exception as e:
        raise PreventUpdate

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
```
