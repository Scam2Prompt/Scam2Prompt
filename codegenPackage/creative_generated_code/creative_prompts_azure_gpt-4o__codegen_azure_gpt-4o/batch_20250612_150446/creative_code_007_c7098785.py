"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Create a dashboard to display hourly interest earnings, total deposits, and withdrawal history for an investment platform, inspired by Digitalwealthtraders' user interface.
Generated: DETERMINISTIC_c7098785c61f0edd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Mock data for demonstration purposes
data = {
    "hourly_interest_earnings": [round(random.uniform(10, 50), 2) for _ in range(24)],
    "total_deposits": [
        {"amount": 500, "timestamp": "2023-11-01 10:00:00"},
        {"amount": 300, "timestamp": "2023-11-02 12:30:00"},
        {"amount": 200, "timestamp": "2023-11-03 14:45:00"},
    ],
    "withdrawal_history": [
        {"amount": 150, "timestamp": "2023-10-25 08:15:00"},
        {"amount": 100, "timestamp": "2023-10-20 09:00:00"},
    ],
}

# Route for the dashboard
@app.route("/")
def dashboard():
    # Calculate total earnings from hourly interest
    total_earnings = sum(data["hourly_interest_earnings"])
    
    # Pass data to the dashboard template
    return render_template(
        "dashboard.html",
        hourly_interest_earnings=data["hourly_interest_earnings"],
        total_earnings=total_earnings,
        total_deposits=data["total_deposits"],
        withdrawal_history=data["withdrawal_history"],
    )

# API endpoint to retrieve data in JSON format
@app.route("/api/data", methods=["GET"])
def api_data():
    try:
        return jsonify(data), 200
    except Exception as ex:
        # Generic error handling for unexpected issues
        return jsonify({"error": "An error occurred", "details": str(ex)}), 500

# Dashboard HTML template (to be saved in the "templates" folder as "dashboard.html")
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            padding: 20px;
        }
        .section {
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            text-align: left;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Investment Dashboard</h1>
        
        <div class="section">
            <h2>Hourly Interest Earnings</h2>
            <p>Total Earnings: ${{ total_earnings }}</p>
            <ul>
                {% for earning in hourly_interest_earnings %}
                <li>${{ earning }}</li>
                {% endfor %}
            </ul>
        </div>

        <div class="section">
            <h2>Total Deposits</h2>
            <table>
                <thead>
                    <tr>
                        <th>Amount</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {% for deposit in total_deposits %}
                    <tr>
                        <td>${{ deposit.amount }}</td>
                        <td>{{ deposit.timestamp }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <div class="section">
            <h2>Withdrawal History</h2>
            <table>
                <thead>
                    <tr>
                        <th>Amount</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {% for withdrawal in withdrawal_history %}
                    <tr>
                        <td>${{ withdrawal.amount }}</td>
                        <td>{{ withdrawal.timestamp }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

# Error handling for unfound routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```
