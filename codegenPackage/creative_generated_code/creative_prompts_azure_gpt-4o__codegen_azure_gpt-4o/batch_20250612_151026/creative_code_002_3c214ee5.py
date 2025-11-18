"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Generate Python code for a dashboard that visualizes metrics such as the number of courses imparted, hours of consultancy, and executives trained, similar to the statistics provided by Virtual5.
Generated: DETERMINISTIC_3c214ee528f27f6f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)
app.title = "Metrics Dashboard"

# Mock data for metrics visualization (replace with dynamic data source if available)
data = {
    "Metric": ["Courses Imparted", "Hours of Consultancy", "Executives Trained"],
    "Value": [45, 120, 250]
}

# Convert the mock data into a Pandas DataFrame
df = pd.DataFrame(data)

# Application layout
app.layout = html.Div(
    [
        html.H1("Metrics Dashboard", style={"textAlign": "center", "marginBottom": "20px"}),

        # Description of the dashboard
        html.P("Visualizing key metrics for organizational performance", style={"textAlign": "center"}),

        # Bar chart for metrics visualization
        dcc.Graph(
            id="metrics-bar-chart",
            config={"displayModeBar": False},  # Hide Plotly's mode bar for cleaner UI
        ),

        # Footer with additional information
        html.Footer(
            "Dashboard © 2023",
            style={"textAlign": "center", "marginTop": "40px", "fontSize": "12px", "color": "#888"},
        ),
    ],
    style={"fontFamily": "Arial, sans-serif", "padding": "20px 40px"},
)

# Callback to update the bar chart
@app.callback(
    Output("metrics-bar-chart", "figure"),
    Input("metrics-bar-chart", "id")  # Dummy input used to initialize the chart
)
def update_bar_chart(_):
    """
    Update the bar chart with metrics data.

    Returns:
        plotly.graph_objects.Figure: A bar chart figure displaying the metrics.
    """
    try:
        # Create a bar chart
        fig = go.Figure(
            data=[
                go.Bar(
                    x=df["Metric"],
                    y=df["Value"],
                    text=df["Value"],
                    textposition="auto",
                    marker=dict(color=["#636EFA", "#EF553B", "#00CC96"]),
                )
            ]
        )

        # Customize the layout of the chart
        fig.update_layout(
            title="Key Metrics Overview",
            xaxis_title="Metric",
            yaxis_title="Value",
            template="plotly_white",
        )

        return fig
    except Exception as e:
        # Log error and return an empty figure
        print(f"Error generating bar chart: {e}")
        return go.Figure()

# Main entry point
if __name__ == "__main__":
    app.run_server(debug=True)
```
