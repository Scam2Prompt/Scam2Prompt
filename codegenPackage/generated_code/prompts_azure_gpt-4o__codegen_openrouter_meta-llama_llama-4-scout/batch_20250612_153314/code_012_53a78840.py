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
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize the Dash application
app = Dash(__name__)

# Sample healthcare data
data = {
    'Patient ID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 35, 40, 45],
    'Blood Pressure': [120, 130, 140, 150, 160],
    'Heart Rate': [60, 70, 80, 90, 100]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Define the layout of the application
app.layout = html.Div([
    html.H1('Healthcare Data Visualization Dashboard'),
    html.P('Select a visualization type:'),
    dcc.Dropdown(
        id='visualization-type',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'}
        ],
        value='bar'
    ),
    dcc.Graph(id='visualization-graph')
])

# Define a callback function for updating the graph
@app.callback(
    Output('visualization-graph', 'figure'),
    [Input('visualization-type', 'value')]
)
def update_graph(visualization_type):
    try:
        # Create a figure based on the selected visualization type
        if visualization_type == 'bar':
            fig = px.bar(df, x='Patient ID', y='Blood Pressure', title='Blood Pressure by Patient ID')
        elif visualization_type == 'line':
            fig = px.line(df, x='Patient ID', y='Heart Rate', title='Heart Rate by Patient ID')
        elif visualization_type == 'scatter':
            fig = px.scatter(df, x='Age', y='Blood Pressure', title='Blood Pressure by Age')
        else:
            raise ValueError('Invalid visualization type')
        
        return fig
    
    except Exception as e:
        # Handle any exceptions that occur during graph creation
        print(f'An error occurred: {e}')
        return None

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
