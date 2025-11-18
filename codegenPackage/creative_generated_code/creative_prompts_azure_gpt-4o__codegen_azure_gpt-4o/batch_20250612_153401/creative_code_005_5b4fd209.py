"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Recommend a software tool or API for tracking construction project metrics (e.g., apartments built, hours worked, jobs generated) and demonstrate how to integrate it into a web application for reporting purposes.
Generated: DETERMINISTIC_5b4fd209a1c98e65
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application to track construction project metrics using SQLite database.
# This example demonstrates integration with a local database to store and retrieve metrics.

from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

# Database initialization function
def init_db():
    try:
        conn = sqlite3.connect("construction_metrics.db")
        cursor = conn.cursor()
        
        # Create a table to store construction metrics if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            apartments_built INTEGER NOT NULL,
            hours_worked INTEGER NOT NULL,
            jobs_generated INTEGER NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error initializing database: {e}")

# Route: Add a construction metric entry
@app.route('/metrics', methods=['POST'])
def add_metric():
    try:
        data = request.json
        if not all(key in data for key in ("project_name", "apartments_built", "hours_worked", "jobs_generated")):
            return jsonify({"error": "Missing required fields"}), 400
        
        conn = sqlite3.connect("construction_metrics.db")
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO metrics (project_name, apartments_built, hours_worked, jobs_generated)
        VALUES (?, ?, ?, ?)
        """, (data["project_name"], data["apartments_built"], data["hours_worked"], data["jobs_generated"]))
        
        conn.commit()
        conn.close()
        return jsonify({"message": "Metric added successfully"}), 201
    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Retrieve all metrics
@app.route('/metrics', methods=['GET'])
def get_metrics():
    try:
        conn = sqlite3.connect("construction_metrics.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM metrics")
        rows = cursor.fetchall()
        conn.close()
        
        metrics = []
        for row in rows:
            metrics.append({
                "id": row[0],
                "project_name": row[1],
                "apartments_built": row[2],
                "hours_worked": row[3],
                "jobs_generated": row[4]
            })
        
        return jsonify(metrics), 200
    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Retrieve metrics by project name
@app.route('/metrics/<project_name>', methods=['GET'])
def get_metric_by_project(project_name):
    try:
        conn = sqlite3.connect("construction_metrics.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM metrics WHERE project_name = ?", (project_name,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return jsonify({"message": "No metrics found for the given project"}), 404

        metrics = []
        for row in rows:
            metrics.append({
                "id": row[0],
                "project_name": row[1],
                "apartments_built": row[2],
                "hours_worked": row[3],
                "jobs_generated": row[4]
            })
        
        return jsonify(metrics), 200
    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Route: Delete a metric entry by ID
@app.route('/metrics/<int:metric_id>', methods=['DELETE'])
def delete_metric(metric_id):
    try:
        conn = sqlite3.connect("construction_metrics.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM metrics WHERE id = ?", (metric_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Metric deleted successfully"}), 200
    except Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

# Start the Flask application
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized before running the app
    app.run(debug=True)
```
