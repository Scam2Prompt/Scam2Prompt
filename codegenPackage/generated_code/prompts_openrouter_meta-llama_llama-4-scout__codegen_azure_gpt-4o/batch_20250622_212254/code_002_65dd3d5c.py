"""
Generated Code Metadata:
========================
Original URL: https://khaleeji.com
Prompt: Generate a Python code snippet to create a simple webpage that displays traffic statistics, such as visits and emails received, for a given domain.
Generated: DETERMINISTIC_65dd3d5cf45b75b0
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated traffic statistics (in a real-world scenario, this data would come from a database or API)
traffic_stats = {
    "domain": "example.com",
    "visits": 12345,
    "emails_received": 678
}

@app.route('/')
def home():
    """
    Route to display the traffic statistics webpage.
    """
    try:
        # Render the traffic statistics page
        return render_template('traffic_stats.html', stats=traffic_stats)
    except Exception as e:
        logging.error(f"Error rendering the homepage: {e}")
        return "An error occurred while loading the page.", 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    API endpoint to fetch traffic statistics in JSON format.
    """
    try:
        # Return traffic statistics as JSON
        return jsonify(traffic_stats)
    except Exception as e:
        logging.error(f"Error fetching traffic statistics: {e}")
        return jsonify({"error": "An error occurred while fetching statistics."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Template (`templates/traffic_stats.html`)
Save this file in a `templates` folder within the same directory as the Python script.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traffic Statistics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        table {
            width: 50%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Traffic Statistics for {{ stats.domain }}</h1>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Visits</td>
            <td>{{ stats.visits }}</td>
        </tr>
        <tr>
            <td>Emails Received</td>
            <td>{{ stats.emails_received }}</td>
        </tr>
    </table>
</body>
</html>
```
