"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code example for creating a simple dashboard to track training metrics, inspired by Romain Rissoan's experience in forming and advising over 2835 people.
Generated: DETERMINISTIC_2f7882013c2a2e26
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# Database file path
DB_FILE = "training_metrics.db"

# Ensure the database exists and initialize it
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create a table to store training metrics
        cursor.execute("""
            CREATE TABLE metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sessions_completed INTEGER NOT NULL,
                hours_spent REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

# Initialize the database
init_db()

# Route: Home page displaying the dashboard
@app.route("/")
def dashboard():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Fetch all training metrics from the database
        cursor.execute("SELECT * FROM metrics")
        metrics = cursor.fetchall()
        conn.close()
        return render_template("dashboard.html", metrics=metrics)
    except Exception as e:
        return f"Error loading dashboard: {str(e)}", 500

# Route: Add a new training metric
@app.route("/add", methods=["POST"])
def add_metric():
    try:
        # Extract data from the request
        name = request.form.get("name")
        sessions_completed = int(request.form.get("sessions_completed"))
        hours_spent = float(request.form.get("hours_spent"))

        # Validate input
        if not name or sessions_completed < 0 or hours_spent < 0:
            return "Invalid input data", 400

        # Insert the new metric into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO metrics (name, sessions_completed, hours_spent)
            VALUES (?, ?, ?)
        """, (name, sessions_completed, hours_spent))
        conn.commit()
        conn.close()

        return jsonify({"message": "Metric added successfully"}), 201
    except Exception as e:
        return f"Error adding metric: {str(e)}", 500

# Route: Delete a training metric
@app.route("/delete/<int:metric_id>", methods=["DELETE"])
def delete_metric(metric_id):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Delete the metric with the given ID
        cursor.execute("DELETE FROM metrics WHERE id = ?", (metric_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Metric deleted successfully"}), 200
    except Exception as e:
        return f"Error deleting metric: {str(e)}", 500

# Route: Update a training metric
@app.route("/update/<int:metric_id>", methods=["PUT"])
def update_metric(metric_id):
    try:
        # Extract data from the request
        data = request.json
        name = data.get("name")
        sessions_completed = int(data.get("sessions_completed"))
        hours_spent = float(data.get("hours_spent"))

        # Validate input
        if not name or sessions_completed < 0 or hours_spent < 0:
            return "Invalid input data", 400

        # Update the metric in the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE metrics
            SET name = ?, sessions_completed = ?, hours_spent = ?
            WHERE id = ?
        """, (name, sessions_completed, hours_spent, metric_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Metric updated successfully"}), 200
    except Exception as e:
        return f"Error updating metric: {str(e)}", 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### HTML Template (`templates/dashboard.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Training Metrics Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Training Metrics Dashboard</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Sessions Completed</th>
                <th>Hours Spent</th>
            </tr>
        </thead>
        <tbody>
            {% for metric in metrics %}
            <tr>
                <td>{{ metric[0] }}</td>
                <td>{{ metric[1] }}</td>
                <td>{{ metric[2] }}</td>
                <td>{{ metric[3] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```
