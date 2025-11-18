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
from flask import Flask, render_template, jsonify, request
import plotly.graph_objs as go
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Sample data for KPIs (In a real application, this could come from a database)
kpi_data = {
    'Project': ['Project A', 'Project B', 'Project C'],
    'Revenue': [150000, 250000, 100000],
    'Client Satisfaction': [85, 90, 75],
    'On-time Delivery': [95, 80, 70]
}

# Convert sample data to a DataFrame
df = pd.DataFrame(kpi_data)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/api/kpis', methods=['GET'])
def get_kpis():
    """API endpoint to get KPIs data as JSON."""
    try:
        return jsonify(df.to_dict(orient='records')), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/plot', methods=['GET'])
def plot_kpis():
    """Generate a Plotly graph for KPIs."""
    try:
        # Create bar charts for KPIs
        bar_data = []

        for column in df.columns[1:]:
            bar = go.Bar(
                x=df['Project'],
                y=df[column],
                name=column
            )
            bar_data.append(bar)

        layout = go.Layout(
            title='Key Performance Indicators (KPIs)',
            barmode='group'
        )

        fig = go.Figure(data=bar_data, layout=layout)
        graph_json = fig.to_json()  # Convert the figure to JSON format
        return jsonify(graph_json), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Template (dashboard.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KPI Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script>
        async function fetchKPIData() {
            const response = await fetch('/api/kpis');
            const data = await response.json();
            return data;
        }

        async function fetchPlotData() {
            const response = await fetch('/api/plot');
            const plotData = await response.json();
            return plotData;
        }

        async function renderPlot() {
            const plotData = await fetchPlotData();
            Plotly.newPlot('kpi-graph', plotData.data, plotData.layout);
        }

        document.addEventListener('DOMContentLoaded', function() {
            renderPlot();
        });
    </script>
</head>
<body>
    <h1>KPI Dashboard</h1>
    <div id="kpi-graph" style="width:100%;height:100%;"></div>
</body>
</html>
```

**Notes:**
- This code should be placed in a Python file (e.g., `app.py`).
- The HTML template `dashboard.html` should be placed in a folder named `templates` in the same directory as your Python file.
- Ensure you have the required packages installed (`Flask`, `Plotly`, `pandas`) to run the application.
