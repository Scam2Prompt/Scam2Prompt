"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Provide code to design a dashboard for tracking energy production and savings for residential, business, and agricultural solar systems, inspired by Nexe Energetic's offerings.
Generated: DETERMINISTIC_2a98100c53a1eab3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, render_template, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database file path
DB_FILE = "energy_dashboard.db"

# Define database schema
def initialize_database():
    """Set up the database schema if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Table for energy data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS energy_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            system_type TEXT NOT NULL,
            energy_production REAL NOT NULL,
            energy_savings REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Helper function to interact with the database
def query_database(query, params=()):
    """Execute a query and return results."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

# Initialize the database
initialize_database()

# Routes
@app.route("/")
def index():
    """
    Render the dashboard homepage.
    """
    return render_template("index.html")

@app.route("/api/data", methods=["GET", "POST"])
def manage_data():
    """
    API endpoint to retrieve or update energy data.
    - GET: Retrieve all data.
    - POST: Insert new data.
    """
    try:
        if request.method == "GET":
            # Retrieve all energy data
            data = query_database("SELECT * FROM energy_data")
            return jsonify(data)
        
        elif request.method == "POST":
            # Insert new energy data
            content = request.json
            system_type = content.get("system_type")
            energy_production = content.get("energy_production")
            energy_savings = content.get("energy_savings")

            # Input validation
            if not system_type or not energy_production or not energy_savings:
                return jsonify({"error": "Invalid input"}), 400

            query_database(
                "INSERT INTO energy_data (system_type, energy_production, energy_savings) VALUES (?, ?, ?)",
                (system_type, energy_production, energy_savings)
            )
            return jsonify({"message": "Data inserted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/summary", methods=["GET"])
def summary():
    """
    API endpoint to get a summary of energy production and savings grouped by system type.
    """
    try:
        data = query_database("""
            SELECT 
                system_type, 
                SUM(energy_production) AS total_production, 
                SUM(energy_savings) AS total_savings 
            FROM energy_data 
            GROUP BY system_type
        """)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run development server
if __name__ == "__main__":
    app.run(debug=True)
```

**File Structure**:
- `app.py`: The main Flask application code (provided above).
- `templates/index.html`: A basic HTML file for the dashboard interface.

**Sample `index.html`**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Energy Dashboard</title>
    <script>
        async function fetchSummary() {
            const response = await fetch('/api/summary');
            const data = await response.json();
            const container = document.getElementById('summary');
            container.innerHTML = JSON.stringify(data, null, 2);
        }
        window.onload = fetchSummary;
    </script>
</head>
<body>
    <h1>Solar Energy Dashboard</h1>
    <h2>Summary of Energy Production and Savings</h2>
    <pre id="summary">Loading...</pre>
</body>
</html>
```

This code provides a complete web-based solar energy dashboard with data storage, an API for interaction, and error handling.
