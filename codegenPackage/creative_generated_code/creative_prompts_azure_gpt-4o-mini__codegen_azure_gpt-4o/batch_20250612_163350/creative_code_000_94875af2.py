"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Generate a simple API that returns a greeting message, similar to the repetitive structure found on the haitwik website.
Generated: DETERMINISTIC_94875af260b916b4
Batch ID: 20250612_163350
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

# Route to handle greeting messages
@app.route('/greet', methods=['GET'])
def greet():
    """
    Endpoint to return a greeting message.

    Query Parameters:
    - name (optional): Name of the person to greet. Defaults to 'Guest'.
    """
    try:
        # Get the 'name' parameter from the query string, default to 'Guest' if not provided
        name = request.args.get('name', 'Guest')
        # Generate a greeting message
        greeting_message = f"Hello, {name}! Welcome to our API."
        # Return JSON response with the greeting message
        return jsonify({"message": greeting_message}), 200
    except Exception as e:
        # Handle unexpected errors and return an error response
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Error handler for 404 - Not Found
@app.errorhandler(404)
def resource_not_found(error):
    """
    Custom error handler for 404 responses.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 405 - Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Custom error handler for 405 responses.
    """
    return jsonify({"error": "Method not allowed."}), 405

# Entry point to run the application
if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(debug=True)
```
