"""
Generated Code Metadata:
========================
Original URL: https://celestai.xyz
Prompt: Implement a real-time performance analytics dashboard for a Celest AI agent using the provided API endpoints and data metrics.
Generated: DETERMINISTIC_3c72c40c224796dd
Batch ID: 20250622_210203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.celest.ai/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import time
import logging
from flask import Flask, jsonify, render_template

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# API endpoint configuration
API_BASE_URL = "https://api.celest.ai/v1"
AGENT_ID = "your_agent_id"  # Replace with your actual agent ID

# Function to fetch performance metrics from the Celest AI API
def fetch_performance_metrics():
    try:
        response = requests.get(f"{API_BASE_URL}/agents/{AGENT_ID}/performance")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching performance metrics: {e}")
        return None  # Return None in case of an error

# Route to serve the dashboard
@app.route('/')
def dashboard():
    metrics = fetch_performance_metrics()
    if metrics is None:
        return render_template('error.html', message="Failed to fetch performance metrics."), 500
    return render_template('dashboard.html', metrics=metrics)

# Function to periodically update metrics (for real-time updates)
def update_metrics():
    while True:
        metrics = fetch_performance_metrics()
        if metrics:
            logging.info(f"Updated metrics: {metrics}")
        time.sleep(60)  # Update every 60 seconds

# Start the metrics update in a separate thread
import threading
metrics_thread = threading.Thread(target=update_metrics, daemon=True)
metrics_thread.start()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

**HTML Templates (for completeness)**

1. `templates/dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Performance Analytics Dashboard</title>
</head>
<body>
    <h1>Performance Analytics Dashboard</h1>
    <div>
        <h2>Metrics</h2>
        <pre>{{ metrics | tojson(indent=2) }}</pre>
    </div>
</body>
</html>
```

2. `templates/error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
</body>
</html>
```

**Note:** Ensure you have Flask installed in your environment. You can install it using `pip install Flask`. Also, replace `your_agent_id` with the actual agent ID you are using.
