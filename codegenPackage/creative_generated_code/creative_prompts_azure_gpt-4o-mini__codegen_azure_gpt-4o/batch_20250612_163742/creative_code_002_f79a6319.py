"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropcoin.lol
Prompt: Generate a code snippet for a web application that helps users reclaim their time from social media, inspired by the solutions proposed on Dropcoin.
Generated: DETERMINISTIC_f79a63199480280f
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code snippet for a web application that helps users reclaim their time from social media. The example is written in Python using Flask for the backend and includes basic functionality to log social media usage and set goals to reduce it.

```python
from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# In-memory data structure for simplicity (this should be replaced with a database in production)
user_data = {}

# Helper function to validate time input
def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

@app.route("/register", methods=["POST"])
def register_user():
    """
    Endpoint to register a new user.
    Request body: {"username": "string"}
    """
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in user_data:
        return jsonify({"error": "Username already exists"}), 400

    user_data[username] = {"social_media_usage": [], "goal": None}
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/log_usage", methods=["POST"])
def log_usage():
    """
    Endpoint to log social media usage.
    Request body: {"username": "string", "date": "YYYY-MM-DD", "duration": "HH:MM"}
    """
    data = request.get_json()
    username = data.get("username")
    date = data.get("date")
    duration = data.get("duration")

    if username not in user_data:
        return jsonify({"error": "User not found"}), 404

    if not date or not duration:
        return jsonify({"error": "Date and duration are required"}), 400

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    if not validate_time_format(duration):
        return jsonify({"error": "Invalid duration format"}), 400

    user_data[username]["social_media_usage"].append({"date": date, "duration": duration})
    return jsonify({"message": "Usage logged successfully"}), 201

@app.route("/set_goal", methods=["POST"])
def set_goal():
    """
    Endpoint to set a goal to limit social media usage.
    Request body: {"username": "string", "goal_duration": "HH:MM"}
    """
    data = request.get_json()
    username = data.get("username")
    goal_duration = data.get("goal_duration")

    if username not in user_data:
        return jsonify({"error": "User not found"}), 404

    if not goal_duration:
        return jsonify({"error": "Goal duration is required"}), 400

    if not validate_time_format(goal_duration):
        return jsonify({"error": "Invalid goal duration format"}), 400

    user_data[username]["goal"] = goal_duration
    return jsonify({"message": "Goal set successfully"}), 201

@app.route("/get_summary", methods=["GET"])
def get_summary():
    """
    Endpoint to retrieve a summary of social media usage.
    Query parameters: ?username=string
    """
    username = request.args.get("username")

    if username not in user_data:
        return jsonify({"error": "User not found"}), 404

    usage_data = user_data[username]["social_media_usage"]
    goal = user_data[username]["goal"]

    # Summarize total usage duration
    total_minutes = 0
    for entry in usage_data:
        hours, minutes = map(int, entry["duration"].split(":"))
        total_minutes += hours * 60 + minutes

    summary = {
        "username": username,
        "total_usage_minutes": total_minutes,
        "goal_duration": goal,
        "usage_history": usage_data
    }
    return jsonify(summary), 200

# Error handling for unexpected routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

This code provides basic functionality to register users, log social media usage, set goals, and retrieve usage summaries. Replace the in-memory `user_data` dictionary with a persistent database solution (e.g., SQL or NoSQL) for production use.
