"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Describe the common reasons for seeing a server error page and how to resolve them in a web application.
Generated: DETERMINISTIC_c33c8816eecaf117
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates common reasons for seeing a server error (HTTP 5xx errors) in a web application
and provides resolutions for these errors. It simulates error handling and logs diagnostic information.

Language: Python
Framework: Flask (a lightweight web framework)
"""

from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.DEBUG, filename="app_errors.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")


@app.route("/")
def home():
    """
    Root endpoint to verify that the server is running.
    Returns a simple JSON response.
    """
    return jsonify({"message": "Server is running"})


@app.route("/simulate_error/<error_type>")
def simulate_error(error_type):
    """
    Endpoint that simulates server errors based on the `error_type` parameter.
    :param error_type: Type of error to simulate (e.g., 'database', 'timeout', 'syntax', 'exception')
    :return: JSON response indicating the simulated error.
    """
    try:
        if error_type == "database":
            # Simulate a database connection error
            raise ConnectionError("Database connection failed")

        elif error_type == "timeout":
            # Simulate a timeout error
            raise TimeoutError("Request timed out")

        elif error_type == "syntax":
            # Simulate a programming error (syntax or runtime error)
            eval("invalid syntax")  # This will raise a SyntaxError

        elif error_type == "exception":
            # Simulate a general server exception
            raise Exception("General server exception occurred")

        else:
            return jsonify({"error": "Unknown error type specified. Use 'database', 'timeout', 'syntax', or 'exception'."}), 400

    except ConnectionError as e:
        logging.error(f"Database error: {e}")
        return jsonify({"error": "Database error occurred. Please check your database connection."}), 500

    except TimeoutError as e:
        logging.error(f"Timeout error: {e}")
        return jsonify({"error": "Request timed out. Please try again later."}), 504

    except SyntaxError as e:
        logging.error(f"Syntax error: {e}")
        return jsonify({"error": "Code contains a syntax error. Please review application code."}), 500

    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        return jsonify({"error": "An unexpected error occurred. Please contact support."}), 500


@app.errorhandler(404)
def handle_404_error(e):
    """
    Custom handler for 404 errors (Page Not Found).
    """
    logging.warning(f"404 Error: {request.path} not found")
    return jsonify({"error": "Endpoint not found. Check your URL."}), 404


@app.errorhandler(500)
def handle_500_error(e):
    """
    Custom handler for 500 errors (Internal Server Error).
    """
    logging.error(f"500 Error: {e}")
    return jsonify({"error": "Internal server error. Please try again later."}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
