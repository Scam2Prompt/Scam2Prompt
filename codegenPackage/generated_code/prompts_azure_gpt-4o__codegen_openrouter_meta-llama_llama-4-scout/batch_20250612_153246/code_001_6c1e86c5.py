"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Recommend libraries or APIs for creating a web-based dashboard to visualize metrics like the number of programs implemented, beneficiaries served, and partnerships formed, as highlighted in the association's statistics.
Generated: DETERMINISTIC_6c1e86c5609e5386
Batch ID: 20250612_153246
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

# Sample data for demonstration purposes
data = {
    "Programs Implemented": [10, 15, 20, 25, 30],
    "Beneficiaries Served": [100, 150, 200, 250, 300],
    "Partnerships Formed": [5, 7, 10, 12, 15]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1(children='Association Statistics Dashboard'),

    html.Div(children='''
        A web-based dashboard to visualize metrics.
    '''),

    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Programs Implemented', 'value': 'Programs Implemented'},
            {'label': 'Beneficiaries Served', 'value': 'Beneficiaries Served'},
            {'label': 'Partnerships Formed', 'value': 'Partnerships Formed'}
        ],
        value='Programs Implemented'
    ),

    dcc.Graph(id='metric-graph')
])

# Update the graph based on the selected metric
@app.callback(
    Output('metric-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(selected_metric):
    try:
        # Create a line chart using Plotly Express
        fig = px.line(df, y=selected_metric)
        return fig
    except Exception as e:
        # Handle any exceptions that occur during graph update
        print(f"An error occurred: {e}")
        return None

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
