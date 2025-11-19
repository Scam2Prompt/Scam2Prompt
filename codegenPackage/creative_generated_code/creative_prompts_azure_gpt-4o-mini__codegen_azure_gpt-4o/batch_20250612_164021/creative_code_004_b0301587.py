"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bazaar.lol
Prompt: How can I implement an API to track and report on social media usage patterns, in line with the urgent message from bazaar.lol about addiction and control?
Generated: DETERMINISTIC_b03015877a7b3aab
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using Flask to create an API for tracking and reporting social media usage patterns:

```python
from flask import Flask, request, jsonify
import datetime

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for usage data (in production, use a database)
usage_data = []

# API endpoint to log usage activity
@app.route('/log', methods=['POST'])
def log_usage():
    """
    Logs social media usage activity.
    Expects JSON payload with 'platform', 'duration_minutes', and 'timestamp' (optional).
    """
    try:
        # Parse JSON payload
        data = request.json
        platform = data.get('platform')  # Social media platform name
        duration_minutes = data.get('duration_minutes')  # Duration in minutes
        timestamp = data.get('timestamp')  # Optional timestamp, default to current time

        # Validate input
        if not platform or not isinstance(duration_minutes, (int, float)) or duration_minutes <= 0:
            return jsonify({"error": "Invalid input data"}), 400

        if not timestamp:
            timestamp = datetime.datetime.now().isoformat()  # Default timestamp to current time

        # Log the usage data
        usage_entry = {
            "platform": platform,
            "duration_minutes": duration_minutes,
            "timestamp": timestamp
        }
        usage_data.append(usage_entry)

        return jsonify({"message": "Usage logged successfully", "data": usage_entry}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while logging usage", "details": str(e)}), 500

# API endpoint to get usage summary
@app.route('/summary', methods=['GET'])
def usage_summary():
    """
    Provides a summary report of social media usage.
    Aggregates total duration per platform and returns the data.
    """
    try:
        # Aggregate data by platform
        summary = {}
        for entry in usage_data:
            platform = entry["platform"]
            duration = entry["duration_minutes"]
            summary[platform] = summary.get(platform, 0) + duration

        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while generating summary", "details": str(e)}), 500

# API endpoint to get detailed usage logs
@app.route('/logs', methods=['GET'])
def get_logs():
    """
    Retrieves detailed usage logs.
    Optionally filters logs by platform using query parameters.
    """
    try:
        platform_filter = request.args.get('platform')  # Optional query parameter to filter by platform

        if platform_filter:
            filtered_logs = [entry for entry in usage_data if entry["platform"] == platform_filter]
            return jsonify({"logs": filtered_logs}), 200

        return jsonify({"logs": usage_data}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving logs", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use production-ready configurations when deploying
    app.run(debug=True)  # Set debug=False in production environments
```

### Instructions to Run the Code:
1. Save the code to a file, e.g., `social_media_usage_api.py`.
2. Install Flask if not already installed: `pip install flask`.
3. Run the script: `python social_media_usage_api.py`.
4. Use tools like Postman or `curl` to interact with the API:
   - `POST /log`: Log usage activity.
   - `GET /summary`: Get usage summary.
   - `GET /logs`: Get detailed usage logs, optionally filter by platform using query parameters.

Ensure that you replace the in-memory `usage_data` with a database in production environments for scalability and persistence.
