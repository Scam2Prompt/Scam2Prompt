"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Recommend a library or API for visualizing COVID-19 data trends, including features like hover tooltips, zooming, and dynamic updates, similar to the graph described on the website.
Generated: DETERMINISTIC_401963de2cb7dc39
Batch ID: 20250612_151018
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
import numpy as np
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import layout
from bokeh.models.widgets import Select
from bokeh.io import output_notebook

# Sample Data Generation (Replace with actual COVID-19 data)
def generate_sample_data():
    dates = pd.date_range(start='2022-01-01', end='2022-12-31')
    cases = np.random.randint(0, 1000, size=len(dates))
    deaths = np.random.randint(0, 100, size=len(dates))
    return pd.DataFrame({'date': dates, 'cases': cases, 'deaths': deaths})

# Load COVID-19 data (replace with actual data source/API call)
data = generate_sample_data()

# Convert date column to string for Bokeh compatibility
data['date'] = data['date'].dt.strftime('%Y-%m-%d')

# Create a ColumnDataSource (dynamic data container for Bokeh)
source = ColumnDataSource(data={
    'date': data['date'],
    'cases': data['cases'],
    'deaths': data['deaths'],
    'x': pd.to_datetime(data['date']),  # Convert back to datetime for x-axis
})

# Initialize plot
plot = figure(
    title="COVID-19 Data Trends",
    x_axis_label="Date",
    y_axis_label="Count",
    x_axis_type="datetime",
    plot_width=800,
    plot_height=400,
)

# Add line for cases and deaths
case_line = plot.line(
    x='x', y='cases', source=source, legend_label="Cases",
    line_width=2, color="blue", alpha=0.7
)
death_line = plot.line(
    x='x', y='deaths', source=source, legend_label="Deaths",
    line_width=2, color="red", alpha=0.7
)

# Add hover tool for tooltip display
hover_tool = HoverTool(
    tooltips=[
        ("Date", "@date"),
        ("Cases", "@cases"),
        ("Deaths", "@deaths"),
    ],
    mode='vline'  # Display tooltip vertically along the hovered line
)
plot.add_tools(hover_tool)

# Enable zooming and panning tools
plot.add_tools(
    "pan", "wheel_zoom", "box_zoom", "reset"
)

# Add interactive filtering (dropdown)
def update_plot(attr, old, new):
    """Callback function to dynamically update plot based on dropdown selection."""
    if new == "Cases":
        source.data = {
            'date': data['date'],
            'cases': data['cases'],
            'deaths': data['deaths'],
            'x': pd.to_datetime(data['date']),
        }
    elif new == "Deaths":
        source.data = {
            'date': data['date'],
            'cases': data['deaths'],  # Switch to 'deaths' for the y-axis
            'deaths': data['deaths'],  # Keep original data untouched
            'x': pd.to_datetime(data['date']),
        }

dropdown = Select(
    title="Data Type:",
    value="Cases",
    options=["Cases", "Deaths"]
)
dropdown.on_change("value", update_plot)

# Layout arrangement
app_layout = layout([
    dropdown,
    plot,
])

# Show the Bokeh application
curdoc().add_root(app_layout)
```
