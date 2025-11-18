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
# Import necessary modules
from flask import Flask, render_template, jsonify, request
import pandas as pd
import plotly.express as px
import logging

# Initialize a Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample IoT data (can be replaced with data from a database or API)
iot_data = pd.DataFrame({
    'Timestamp': ['2023-10-01 12:00:00', '2023-10-01 12:01:00', '2023-10-01 12:02:00'],
    'DeviceID': ['Sensor_1', 'Sensor_2', 'Sensor_1'],
    'Temperature': [23.5, 26.7, 24.0],
    'Humidity': [60, 55, 58]
})

# Route for the dashboard homepage
@app.route('/')
def dashboard():
    """
    Renders the dashboard HTML page.
    """
    try:
        return render_template('dashboard.html')
    except Exception as e:
        logging.error(f"Error rendering dashboard: {e}")
        return "An error occurred while loading the dashboard.", 500

# API endpoint to fetch data for visualization
@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Provides IoT data in JSON format for frontend visualization purposes.
    """
    try:
        data_json = iot_data.to_dict(orient='records')
        return jsonify(data_json)
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return jsonify({'error': 'An error occurred while fetching data.'}), 500

# API endpoint for generating plots
@app.route('/api/plot', methods=['POST'])
def generate_plot():
    """
    Creates a Plotly graph based on the given parameters and returns it as JSON.
    """
    try:
        # Extract parameters from the request
        payload = request.json
        x_axis = payload.get('x_axis', 'Timestamp')
        y_axis = payload.get('y_axis', 'Temperature')

        # Validate requested axes
        if x_axis not in iot_data.columns or y_axis not in iot_data.columns:
            return jsonify({'error': 'Invalid axis specified.'}), 400

        # Generate the plot using Plotly
        fig = px.line(iot_data, x=x_axis, y=y_axis, title=f'{y_axis} vs {x_axis}')
        return jsonify(fig.to_json())
    except Exception as e:
        logging.error(f"Error generating plot: {e}")
        return jsonify({'error': 'An error occurred while generating the plot.'}), 500

# Main entry point for running the app
if __name__ == '__main__':
    # Ensure the app runs in debug mode for local development
    app.run(debug=True)
```

### Notes:
- Create a `templates/dashboard.html` file for the frontend of the dashboard. Use JavaScript libraries like Plotly or D3.js for visualization.
- Replace the sample IoT data with your actual data source (e.g., database query or IoT API).
- Deploy Flask using a production-ready server like Gunicorn or uWSGI for production environments.
