"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-app.com
Prompt: Can you provide a code snippet for setting up a basic web server configuration for presale-app.com?
Generated: DETERMINISTIC_ee5cb6bd56c490aa
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging
from werkzeug.exceptions import HTTPException

# Create a Flask application instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description})
    response.content_type = "application/json"
    return response

# A sample route for the presale application
@app.route('/api/v1/status', methods=['GET'])
def get_status():
    """Endpoint to check the server status."""
    return jsonify({"status": "up", "message": "Presale app is running!"}), 200

# Error handling middleware
@app.before_request
def log_request_info():
    """Log request information before processing."""
    app.logger.info(f'Handling request: {request.method} {request.url}')

# Entry point of the application
if __name__ == '__main__':
    try:
        # Start the server on host 0.0.0.0 and port 5000
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        app.logger.error(f'Failed to start the server: {e}')
```
