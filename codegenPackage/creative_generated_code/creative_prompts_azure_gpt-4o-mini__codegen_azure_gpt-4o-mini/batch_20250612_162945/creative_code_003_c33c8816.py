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
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle internal server errors (HTTP 500).
    This function logs the error and returns a JSON response with the error message.
    """
    # Log the error for debugging purposes (could log to a file or monitoring service)
    app.logger.error(f'Internal Server Error: {str(e)}')
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."}), 500

@app.errorhandler(404)
def not_found_error(e):
    """
    Handle not found errors (HTTP 404).
    Returns a JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Not Found", "message": "The requested resource was not found."}), 404

@app.route('/example', methods=['GET'])
def example_endpoint():
    """
    An example endpoint to demonstrate error handling.
    Returns a simple message, but could raise an exception to trigger the error handler.
    """
    # Simulate a potential error for demonstration (uncomment to see error handling)
    # raise Exception("Simulated error for testing purposes.")

    return jsonify({"message": "This is an example endpoint."}), 200

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=True)  # Set debug=True for development; replace with False for production
    except Exception as e:
        app.logger.error(f'Failed to start the application: {str(e)}')
```
