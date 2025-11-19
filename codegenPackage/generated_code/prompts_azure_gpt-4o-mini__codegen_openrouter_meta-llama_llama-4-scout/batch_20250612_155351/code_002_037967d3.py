"""
Generated Code Metadata:
========================
Original URL: https://web-metamesklogin.uteach.io
Prompt: Create an API response in Python that returns a 404 status code with a custom message, inspired by the content of the Uteach error page.
Generated: DETERMINISTIC_037967d3f1971624
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Define a custom error handler for 404 status code
@app.errorhandler(404)
def not_found(error):
    """
    Returns a JSON response with a custom message for 404 status code.

    Args:
        error: The error object.

    Returns:
        A JSON response with a 404 status code and a custom message.
    """
    # Define the custom error message
    error_message = {
        "status_code": 404,
        "message": "The page you're looking for doesn't exist. Please check the URL and try again.",
        "error": "Not Found"
    }
    
    # Return the JSON response with the custom error message
    return jsonify(error_message), 404

# Define a route to test the custom error handler
@app.route('/test-404', methods=['GET'])
def test_404():
    # Simulate a 404 error
    return '', 404

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Handle any exceptions that occur during application execution
        print(f"An error occurred: {e}")
```
