"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Write a code snippet that integrates mobile and web functionalities for agricultural activity monitoring, similar to Azagros.
Generated: DETERMINISTIC_1fae262499c6ff23
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

# Database file
DB_FILE = "agriculture_monitoring.db"

# Ensure database is initialized
if not os.path.exists(DB_FILE):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Create a table for activity logs
        cursor.execute("""
        CREATE TABLE activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            activity_type TEXT NOT NULL,
            location TEXT NOT NULL,
            details TEXT
        )
        """)
        conn.commit()

# Helper function to interact with the database
def execute_query(query, params=(), fetch=False):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            conn.commit()
    except sqlite3.Error as e:
        app.logger.error(f"Database error occurred: {str(e)}")
        raise

@app.route("/log_activity", methods=["POST"])
def log_activity():
    """
    Endpoint for logging an agricultural activity.
    Expecting JSON payload:
    {
        "activity_type": "Planting",
        "location": "Farm A",
        "details": "Planted 50 apple trees"
    }
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    activity_type = data.get("activity_type")
    location = data.get("location")
    details = data.get("details")

    if not activity_type or not location:
        return jsonify({"error": "Both 'activity_type' and 'location' are required"}), 400

    # Log the activity with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        execute_query("""
        INSERT INTO activity_logs (timestamp, activity_type, location, details)
        VALUES (?, ?, ?, ?)
        """, (timestamp, activity_type, location, details))
    except Exception as e:
        return jsonify({"error": "Could not log activity"}), 500

    return jsonify({"message": "Activity logged successfully"}), 201

@app.route("/get_activities", methods=["GET"])
def get_activities():
    """
    Endpoint for retrieving logged activities.
    Optional query parameters:
    - location: Filter activities by location
    - activity_type: Filter activities by activity type
    """
    location = request.args.get("location")
    activity_type = request.args.get("activity_type")

    query = "SELECT * FROM activity_logs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)

    if activity_type:
        query += " AND activity_type = ?"
        params.append(activity_type)

    try:
        activities = execute_query(query, params, fetch=True)
    except Exception as e:
        return jsonify({"error": "Could not fetch activities"}), 500

    # Structure the response
    result = []
    for activity in activities:
        result.append({
            "id": activity[0],
            "timestamp": activity[1],
            "activity_type": activity[2],
            "location": activity[3],
            "details": activity[4]
        })

    return jsonify(result), 200

@app.route("/delete_activity/<int:activity_id>", methods=["DELETE"])
def delete_activity(activity_id):
    """
    Endpoint for deleting a specific activity by its ID.
    """
    try:
        execute_query("DELETE FROM activity_logs WHERE id = ?", (activity_id,))
    except Exception as e:
        return jsonify({"error": "Could not delete activity"}), 500

    return jsonify({"message": "Activity deleted successfully"}), 200

if __name__ == "__main__":
    # Run the app on localhost with debugging enabled
    app.run(host="0.0.0.0", port=5000)
```
