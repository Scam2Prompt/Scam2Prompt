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
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Initialize a dictionary to store performance metrics
performance_metrics = {
    'page_load_times': [],
    'api_response_times': []
}


def track_cookie(user_id, cookie_name, value):
    """
    Set a cookie in the user's browser to track performance metrics.

    Args:
        user_id (str): Unique identifier for the user.
        cookie_name (str): Name of the cookie to set.
        value (str): Value to store in the cookie.
    """
    response = make_response()
    response.set_cookie(cookie_name, value, httponly=True, secure=True, samesite='Lax')
    return response


@app.route('/track_performance', methods=['POST'])
def track_performance():
    """
    Endpoint to track page load and API response times.

    Expects JSON payload with a user ID, page load time, and API response time.
    Example payload:
    {
        "user_id": "user123",
        "page_load_time": 1.23,
        "api_response_time": 0.45
    }

    Returns HTTP status 200 on success, or error message if input is invalid.
    """
    try:
        data = request.json
        user_id = data['user_id']
        page_load_time = data['page_load_time']
        api_response_time = data['api_response_time']
        
        # Validate input data
        if not isinstance(user_id, str) or not isinstance(page_load_time, (int, float)) or not isinstance(api_response_time, (int, float)):
            return jsonify({"error": "Invalid input format"}), 400

        # Track performance metrics
        performance_metrics['page_load_times'].append(page_load_time)
        performance_metrics['api_response_times'].append(api_response_time)

        # Track cookie for user
        response = track_cookie(user_id, 'performance_cookie', json.dumps(performance_metrics))
        return response

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500


@app.route('/get_metrics', methods=['GET'])
def get_metrics():
    """
    Endpoint to retrieve tracked performance metrics.

    Returns a JSON object containing the tracked performance metrics.
    """
    return jsonify(performance_metrics)


if __name__ == '__main__':
    # Run the Flask app in production-ready mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```

This Python code creates a simple performance monitoring tool using Flask. It allows clients to send page load and API response times, tracks them using cookies, and retrieves the metrics upon request. Proper error handling and input validation are implemented, ensuring the application is robust and production-ready.
