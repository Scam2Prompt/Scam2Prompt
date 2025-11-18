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
# Import necessary libraries
import flask
from flask import Flask, render_template, jsonify
import random

# Initialize Flask app
app = Flask(__name__)

# Function to simulate metric calculation
def calculate_metrics():
    """
    Simulates the calculation of healthcare metrics.
    Returns a dictionary with calculated metrics.
    """
    metrics = {
        "clean_claim_ratio": round(random.uniform(0.8, 1.0) * 100, 2),  # Clean Claim Ratio in %
        "net_collection_rate": round(random.uniform(0.7, 0.95) * 100, 2),  # Net Collection Rate in %
        "days_in_ar": round(random.uniform(30, 90), 1)  # Days in Accounts Receivable
    }
    return metrics

@app.route("/")
def dashboard():
    """
    Renders the dashboard HTML page.
    """
    return render_template("dashboard.html")

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    API endpoint to get healthcare metrics.
    Returns metrics as JSON data.
    """
    try:
        metrics = calculate_metrics()
        return jsonify({"success": True, "data": metrics})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    try:
        # Start the Flask server
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")
```

**HTML File: `templates/dashboard.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Healthcare Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .chart-container {
            width: 80%;
            margin: auto;
        }
    </style>
</head>
<body>
    <h1>Healthcare Metrics Dashboard</h1>
    <div class="chart-container">
        <canvas id="metricsChart"></canvas>
    </div>

    <script>
        async function fetchMetrics() {
            try {
                const response = await fetch("/metrics");
                const data = await response.json();
                if (data.success) {
                    return data.data;
                } else {
                    console.error("Error fetching metrics:", data.error);
                }
            } catch (error) {
                console.error("Network error:", error);
            }
        }

        async function renderChart() {
            const metrics = await fetchMetrics();
            if (!metrics) return;

            const ctx = document.getElementById('metricsChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Clean Claim Ratio (%)', 'Net Collection Rate (%)', 'Days in AR'],
                    datasets: [{
                        label: 'Healthcare Metrics',
                        data: [metrics.clean_claim_ratio, metrics.net_collection_rate, metrics.days_in_ar],
                        backgroundColor: ['#4caf50', '#2196f3', '#f44336'],
                        borderColor: ['#388e3c', '#1e88e5', '#d32f2f'],
                        borderWidth: 1
                    }]
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
        }

        // Render the chart on page load
        renderChart();
    </script>
</body>
</html>
```
