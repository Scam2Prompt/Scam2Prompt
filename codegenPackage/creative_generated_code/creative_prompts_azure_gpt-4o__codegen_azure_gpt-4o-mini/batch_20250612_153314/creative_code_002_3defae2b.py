"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Recommend a library or API for building custom dashboards that visualize data from IoT devices, based on Enorness's expertise in data analytics and dashboard development.
Generated: DETERMINISTIC_3defae2b96ef0a1f
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Custom Dashboard Builder for IoT Data Visualization

This script uses the Dash library, a productive Python framework for building web applications. 
It is particularly suited for data visualization and interactive dashboards.
"""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data generation function for IoT data
def generate_sample_data():
    """Generate sample IoT data for demonstration purposes."""
    data = {
        'Time': pd.date_range(start='2023-01-01', periods=100, freq='H'),
        'Temperature': np.random.uniform(20, 30, size=100),
        'Humidity': np.random.uniform(30, 70, size=100)
    }
    return pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Load sample data
try:
    df = generate_sample_data()
except Exception as e:
    print(f"Error generating sample data: {e}")
    df = pd.DataFrame(columns=['Time', 'Temperature', 'Humidity'])

# Layout of the dashboard
app.layout = html.Div([
    html.H1("IoT Device Data Dashboard"),
    dcc.Graph(id='temperature-graph'),
    dcc.Graph(id='humidity-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*60000,  # Refresh every minute
        n_intervals=0
    )
])

# Callback for temperature graph
@app.callback(
    Output('temperature-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_temperature_graph(n):
    """Update the temperature graph with the latest data."""
    try:
        fig = px.line(df, x='Time', y='Temperature', title='Temperature Over Time')
        return fig
    except Exception as e:
        print(f"Error updating temperature graph: {e}")
        return {}

# Callback for humidity graph
@app.callback(
    Output('humidity-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_humidity_graph(n):
    """Update the humidity graph with the latest data."""
    try:
        fig = px.line(df, x='Time', y='Humidity', title='Humidity Over Time')
        return fig
    except Exception as e:
        print(f"Error updating humidity graph: {e}")
        return {}

# Main execution
if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

**Dependencies:**
Make sure to install the required libraries before running this script:

```bash
pip install dash pandas plotly numpy
```
