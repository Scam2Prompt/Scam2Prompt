"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Generate code to create a dashboard for tracking key performance indicators (KPIs) in a consulting project using Flask and Plotly.
Generated: DETERMINISTIC_17ae6db32787a9da
Batch ID: 20250612_153710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.plot.ly/plotly-latest.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
import plotly.express as px
import pandas as pd
import json

# Initialize the Flask app
app = Flask(__name__)

# Sample data for KPIs
# In production, replace this with a database or dynamic data source
data = {
    "KPI": ["Revenue", "Expenses", "Profit Margin", "Customer Satisfaction"],
    "Value": [500000, 200000, 60, 85],
    "Target": [600000, 250000, 65, 90]
}

# Create a Pandas DataFrame from the sample data
df = pd.DataFrame(data)

@app.route('/')
def dashboard():
    """
    Renders the main dashboard page.
    """
    # Generate Plotly bar chart for KPI values vs their targets
    fig = px.bar(
        df,
        x='KPI',
        y=['Value', 'Target'],
        barmode='group',
        title="KPIs vs Targets",
        labels={"value": "Values", "KPI": "Key Performance Indicator"}
    )

    # Convert the Plotly figure to JSON for rendering
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the dashboard HTML template
    return render_template('dashboard.html', chart_json=chart_json)

@app.route('/api/kpi-data')
def get_kpi_data():
    """
    Provides the KPI data as a JSON API endpoint.
    """
    try:
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 handler.
    """
    return render_template('404.html'), 404

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 handler.
    """
    return render_template('500.html'), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulting Project Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Consulting Project KPI Dashboard</h1>
    <div id="kpiChart"></div>
    <script>
        // Render the Plotly chart using the JSON data passed from Flask
        const chartData = {{ chart_json|safe }};
        Plotly.newPlot('kpiChart', chartData);
    </script>
</body>
</html>
```

### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page could not be found.</p>
</body>
</html>
```

### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on the server.</p>
</body>
</html>
```
