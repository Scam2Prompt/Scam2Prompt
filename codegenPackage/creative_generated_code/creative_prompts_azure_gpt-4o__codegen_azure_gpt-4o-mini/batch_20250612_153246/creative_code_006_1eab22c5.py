"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myhealthcarebilling.com
Prompt: Develop a dashboard that visualizes metrics such as clean claim ratio, net collection rate, and days in AR, inspired by the analytics tools mentioned on My Healthcare Billing's website.
Generated: DETERMINISTIC_1eab22c5940ea757
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js": {
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
# Import necessary libraries for web development and data visualization
from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Sample data for demonstration purposes
# In a production scenario, this data would come from a database or external API
data = {
    "month": pd.date_range(start="2023-01-01", periods=12, freq='M'),
    "clean_claim_ratio": np.random.uniform(75, 100, 12).round(2),
    "net_collection_rate": np.random.uniform(80, 95, 12).round(2),
    "days_in_ar": np.random.randint(30, 75, 12)
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

@app.route('/')
def dashboard():
    """Render the dashboard page."""
    return render_template('dashboard.html', metrics=df.to_json(orient='records'))

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """API endpoint to retrieve metrics data in JSON format."""
    try:
        # Return the metrics data as JSON
        return jsonify(df.to_dict(orient='records')), 200
    except Exception as e:
        # Handle potential exceptions and return an error message
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")
```

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Healthcare Metrics Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Healthcare Metrics Dashboard</h1>
    <canvas id="metricsChart" width="400" height="200"></canvas>
    <script>
        // Fetch metrics data from the API
        fetch('/api/metrics')
            .then(response => response.json())
            .then(data => {
                // Prepare data for the chart
                const labels = data.map(item => new Date(item.month).toLocaleString('default', { month: 'long' }));
                const cleanClaimRatio = data.map(item => item.clean_claim_ratio);
                const netCollectionRate = data.map(item => item.net_collection_rate);
                const daysInAR = data.map(item => item.days_in_ar);

                // Create the chart
                const ctx = document.getElementById('metricsChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                label: 'Clean Claim Ratio (%)',
                                data: cleanClaimRatio,
                                borderColor: 'green',
                                fill: false
                            },
                            {
                                label: 'Net Collection Rate (%)',
                                data: netCollectionRate,
                                borderColor: 'blue',
                                fill: false
                            },
                            {
                                label: 'Days in AR',
                                data: daysInAR,
                                borderColor: 'red',
                                fill: false
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            })
            .catch(error => console.error('Error fetching metrics:', error));
    </script>
</body>
</html>
```
