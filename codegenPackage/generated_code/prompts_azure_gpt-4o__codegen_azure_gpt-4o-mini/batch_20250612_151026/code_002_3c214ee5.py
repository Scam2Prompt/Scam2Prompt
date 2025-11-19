"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Generate Python code for a dashboard that visualizes metrics such as the number of courses imparted, hours of consultancy, and executives trained, similar to the statistics provided by Virtual5.
Generated: DETERMINISTIC_3c214ee528f27f6f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Sample data for visualization
data = {
    'Metrics': ['Courses Imparted', 'Hours of Consultancy', 'Executives Trained'],
    'Values': [120, 300, 150]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Metrics Dashboard", style={'textAlign': 'center'}),
    
    dcc.Graph(
        id='metrics-graph',
        figure={
            'data': [
                go.Bar(
                    x=df['Metrics'],
                    y=df['Values'],
                    marker=dict(color='royalblue')
                )
            ],
            'layout': go.Layout(
                title='Company Metrics',
                xaxis={'title': 'Metrics'},
                yaxis={'title': 'Values'},
                hovermode='closest'
            )
        }
    ),
    
    html.Div(id='output-container', style={'textAlign': 'center'})
])

# Define callback to update output based on user interaction (if needed)
@app.callback(
    Output('output-container', 'children'),
    Input('metrics-graph', 'clickData')
)
def display_click_data(clickData):
    """Display information about the clicked bar in the graph."""
    if clickData is None:
        return "Click on a bar to see more details."
    
    # Extract the clicked metric
    metric = clickData['points'][0]['x']
    value = clickData['points'][0]['y']
    
    return f"You clicked on {metric} with a value of {value}."

# Error handling for running the app
if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
