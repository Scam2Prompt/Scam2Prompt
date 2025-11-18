"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://com-eligibility-checker.live
Prompt: Develop a performance monitoring tool for a website that uses cookies to track key performance indexes and improve user experience.
Generated: DETERMINISTIC_d1452c69f37c8c0d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
from http.cookies import SimpleCookie
from flask import Flask, request, jsonify, make_response

# Flask web application
app = Flask(__name__)

# Helper function to get current timestamp
def get_timestamp():
    return time.time()


@app.route("/start_monitoring", methods=["GET"])
def start_monitoring():
    """
    Endpoint to start performance monitoring for a user session.
    Creates cookies to track initial page load time.
    """
    try:
        # Create cookies to store initial load timestamp and session ID
        response = make_response(
            jsonify({"message": "Performance monitoring started."})
        )
        start_time = get_timestamp()
        response.set_cookie("session_id", str(start_time), httponly=True, secure=True)
        response.set_cookie("load_start_time", str(start_time), httponly=True, secure=True)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/log_performance", methods=["POST"])
def log_performance():
    """
    Endpoint to log performance metrics.
    Accepts JSON payload with user metrics and enhances it with cookie data.
    """
    try:
        # Extract cookies
        session_id = request.cookies.get("session_id")
        start_time = request.cookies.get("load_start_time")

        if not session_id or not start_time:
            return jsonify({"error": "Session not initialized properly."}), 400

        # Extract payload from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload."}), 400

        # Calculate page load duration
        current_timestamp = get_timestamp()
        load_duration = current_timestamp - float(start_time)

        # Add additional metadata to the payload
        metrics = {
            "session_id": session_id,
            "load_duration_seconds": load_duration,
            "user_metrics": data,
            "timestamp": current_timestamp
        }

        # Log metrics (placeholder for actual logging, e.g., database or analytics)
        print(json.dumps(metrics))  # In production, use a proper logging tool

        return jsonify({"message": "Performance metrics logged successfully.", "data": metrics})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/end_monitoring", methods=["GET"])
def end_monitoring():
    """
    Endpoint to end performance monitoring by clearing session cookies.
    """
    try:
        # Remove cookies
        response = make_response(jsonify({"message": "Performance monitoring ended."}))
        response.set_cookie("session_id", "", expires=0)
        response.set_cookie("load_start_time", "", expires=0)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
