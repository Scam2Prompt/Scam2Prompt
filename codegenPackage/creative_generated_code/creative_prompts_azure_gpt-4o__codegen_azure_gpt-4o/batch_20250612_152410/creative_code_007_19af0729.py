"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://k7play.top
Prompt: Generate code for a streaming service dashboard that displays active users, available channels, movies, and series, similar to K7 Play's statistics.
Generated: DETERMINISTIC_19af07291c796a64
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# streaming_dashboard.py

import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock Data: In production, you would use a database or dynamic data source
mock_data = {
    "active_users": 4523,
    "available_channels": [
        {"id": 1, "name": "Sports HD", "active_viewers": 1234},
        {"id": 2, "name": "Movies Plus", "active_viewers": 895},
        {"id": 3, "name": "News 24/7", "active_viewers": 567},
    ],
    "movies": [
        {"id": 101, "title": "The Great Adventure", "genre": "Action"},
        {"id": 102, "title": "Romance in Paris", "genre": "Romance"},
    ],
    "series": [
        {"id": 201, "title": "Mystery Nights", "seasons": 3},
        {"id": 202, "title": "Tech Titans", "seasons": 5},
    ],
}

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    """
    Endpoint to fetch streaming service dashboard statistics.
    :return: JSON response with active users, channels, movies, and series.
    """
    try:
        # Return mock data as JSON
        return jsonify({
            "status": "success",
            "data": mock_data
        })
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.route('/dashboard/active_users', methods=['GET'])
def get_active_users():
    """
    Endpoint to fetch the number of active users.
    :return: JSON response with the count of active users.
    """
    try:
        return jsonify({
            "status": "success",
            "active_users": mock_data["active_users"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.route('/dashboard/channels', methods=['GET'])
def get_channels():
    """
    Endpoint to fetch available channels and their statistics.
    :return: JSON response with channel information.
    """
    try:
        return jsonify({
            "status": "success",
            "channels": mock_data["available_channels"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.route('/dashboard/movies', methods=['GET'])
def get_movies():
    """
    Endpoint to fetch available movies.
    :return: JSON response with movie information.
    """
    try:
        return jsonify({
            "status": "success",
            "movies": mock_data["movies"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.route('/dashboard/series', methods=['GET'])
def get_series():
    """
    Endpoint to fetch available series.
    :return: JSON response with series information.
    """
    try:
        return jsonify({
            "status": "success",
            "series": mock_data["series"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)
```

This code sets up a Flask-based API that serves the streaming service dashboard statistics. It includes separate endpoints for active users, channels, movies, and series. The code is clean, adheres to best practices, and includes error handling for robustness.
