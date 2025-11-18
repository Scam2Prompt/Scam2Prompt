"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Create a dashboard interface to display total users, deposits, investments, and withdrawals, similar to the statistics shown on Hyiprio.
Generated: DETERMINISTIC_1963dfcb7a060f1e
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dashboard.py
# This script creates a simple dashboard interface using Flask to display user statistics.
# Statistics include Total Users, Deposits, Investments, and Withdrawals.

from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data. In production, this would come from a database or API.
statistics = {
    "total_users": 1234,
    "total_deposits": 98765.43,
    "total_investments": 54321.67,
    "total_withdrawals": 76543.21,
    "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

@app.route('/')
def dashboard():
    """
    Renders the dashboard HTML with the current statistics.
    """
    return render_template('dashboard.html', stats=statistics)

@app.route('/api/statistics', methods=['GET'])
def api_statistics():
    """
    API endpoint to fetch the statistics in JSON format.
    """
    return jsonify(statistics)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask app. In production, use a WSGI server (e.g., Gunicorn) instead of the built-in server.
    app.run(debug=True)

# HTML Template: templates/dashboard.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .stat-box {
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 200px;
            text-align: center;
        }
        .stat-box h2 {
            margin: 0;
            font-size: 1.5em;
        }
        .stat-box p {
            margin: 5px 0 0;
            font-size: 1em;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Dashboard</h1>
    <div class="stats-container">
        <div class="stat-box">
            <h2>{{ stats.total_users }}</h2>
            <p>Total Users</p>
        </div>
        <div class="stat-box">
            <h2>${{ stats.total_deposits }}</h2>
            <p>Total Deposits</p>
        </div>
        <div class="stat-box">
            <h2>${{ stats.total_investments }}</h2>
            <p>Total Investments</p>
        </div>
        <div class="stat-box">
            <h2>${{ stats.total_withdrawals }}</h2>
            <p>Total Withdrawals</p>
        </div>
    </div>
    <p style="text-align: center; margin-top: 20px;">Last Updated: {{ stats.last_updated }}</p>
</body>
</html>
"""
```
