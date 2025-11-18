"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthcareventure.nl
Prompt: Create a dashboard using Python and Flask to track the progress of a buy-and-build strategy for youth mental healthcare firms, including metrics for client growth and revenue generation.
Generated: DETERMINISTIC_31a524439156b464
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css": {
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
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

# Flask application setup
app = Flask(__name__)

# Database configuration
DB_FILE = "dashboard.db"

def init_db():
    """Initialize the database if it doesn't already exist."""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            client_growth INTEGER NOT NULL,
            revenue REAL NOT NULL
        )
        """)
        conn.commit()
        conn.close()

# Initialize the database
init_db()

@app.route('/')
def dashboard():
    """
    Dashboard route that displays metrics for client growth and revenue generation.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM metrics ORDER BY date DESC")
    metrics = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', metrics=metrics)

@app.route('/add_metrics', methods=['POST'])
def add_metrics():
    """
    API endpoint to add new metrics to the dashboard.
    Expected JSON payload:
    {
        "date": "YYYY-MM-DD",
        "client_growth": <int>,
        "revenue": <float>
    }
    """
    try:
        data = request.json
        date = data['date']
        client_growth = data['client_growth']
        revenue = data['revenue']

        # Validate input data
        if not date or not isinstance(client_growth, int) or not isinstance(revenue, float):
            return jsonify({"error": "Invalid input"}), 400

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO metrics (date, client_growth, revenue) 
        VALUES (?, ?, ?)
        """, (date, client_growth, revenue))
        conn.commit()
        conn.close()

        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Template for the dashboard
# Save this HTML file as 'templates/dashboard.html' in the project directory.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buy-and-Build Strategy Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Buy-and-Build Strategy Dashboard</h1>
        <table class="table table-striped mt-4">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Client Growth</th>
                    <th>Revenue ($)</th>
                </tr>
            </thead>
            <tbody>
                {% for metric in metrics %}
                <tr>
                    <td>{{ metric[1] }}</td>
                    <td>{{ metric[2] }}</td>
                    <td>{{ metric[3] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
