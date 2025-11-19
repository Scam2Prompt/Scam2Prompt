"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choruc.one
Prompt: Recommend an API for tracking and managing web page errors, specifically focusing on 404 error handling.
Generated: DETERMINISTIC_0bede267a9a25c79
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for error tracking
error_log = []

class ErrorTracker:
    """
    A class for tracking errors encountered on the web pages.
    """

    def log_error(self, url, error_code):
        """
        Logs the error details into the error_log.

        Parameters:
            url (str): The URL that resulted in an error.
            error_code (int): The HTTP error code.
        """
        error_details = {
            'url': url,
            'error_code': error_code,
            'message': self.get_error_message(error_code)
        }
        error_log.append(error_details)

    @staticmethod
    def get_error_message(error_code):
        """
        Returns a user-friendly error message based on the HTTP status code.

        Parameters:
            error_code (int): The HTTP error code.

        Returns:
            str: A descriptive error message.
        """
        messages = {
            404: "Page not found.",
            500: "Internal server error.",
            403: "Forbidden access.",
        }
        return messages.get(error_code, "An unexpected error occurred.")

@app.route('/check-url', methods=['GET'])
def check_url():
    """
    Endpoint to check the status of a given URL and log errors if any.
    Expects a 'url' parameter in the query string.

    Returns:
        JSON response with the status of the URL and any error details logged.
    """
    url = request.args.get('url')

    if not url:
        return jsonify({"error": "URL parameter is required."}), 400

    try:
        # Sending a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return jsonify({"message": "URL is accessible."}), 200

    except requests.HTTPError as http_err:
        # Log the error if it's an HTTP error
        tracker = ErrorTracker()
        tracker.log_error(url, http_err.response.status_code)
        return jsonify({
            "error": tracker.get_error_message(http_err.response.status_code),
            "error_code": http_err.response.status_code
        }), http_err.response.status_code

    except Exception as err:
        # Handle other exceptions (e.g., connection errors)
        return jsonify({"error": str(err)}), 500

@app.route('/errors', methods=['GET'])
def get_errors():
    """
    Endpoint to retrieve the logged errors.

    Returns:
        JSON response containing the list of logged errors.
    """
    return jsonify({"errors": error_log}), 200

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True)
```
