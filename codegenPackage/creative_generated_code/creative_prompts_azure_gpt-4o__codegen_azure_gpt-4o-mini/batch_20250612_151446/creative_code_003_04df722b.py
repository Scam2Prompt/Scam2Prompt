"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Suggest a library for creating interactive dashboards that visualize statistics, such as the number of students enrolled in vocational schools or the distribution of technical courses across regions.
Generated: DETERMINISTIC_04df722b1b5557a0
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample data creation function
def create_sample_data():
    """Creates a sample DataFrame representing student enrollment statistics."""
    data = {
        'Region': ['North', 'South', 'East', 'West'],
        'Vocational_School_Enrollment': [150, 200, 100, 250],
        'Technical_Courses': [10, 15, 5, 20]
    }
    return pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Load sample data
df = create_sample_data()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Vocational Schools Enrollment Dashboard'),

    html.Div(children='''
        Interactive dashboard to visualize student enrollment statistics.
    '''),

    # Dropdown to select the metric to visualize
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Vocational School Enrollment', 'value': 'Vocational_School_Enrollment'},
            {'label': 'Technical Courses', 'value': 'Technical_Courses'}
        ],
        value='Vocational_School_Enrollment'  # Default value
    ),

    # Graph to display the data
    dcc.Graph(id='bar-chart')
])

# Callback to update the bar chart based on the selected metric
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_bar_chart(selected_metric):
    """Updates the bar chart based on the selected metric from the dropdown."""
    try:
        # Create bar chart using Plotly Express
        fig = px.bar(df, x='Region', y=selected_metric,
                     title=f'Distribution of {selected_metric.replace("_", " ").title()}',
                     labels={'Region': 'Region', selected_metric: selected_metric.replace("_", " ").title()})

        return fig
    except Exception as e:
        # Handle any exceptions and return an error message
        return px.bar(title="Error occurred while generating the chart", 
                       labels={"x": "Error", "y": str(e)})

# Run the Dash app
if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```
