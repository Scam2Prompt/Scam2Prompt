"""
Generated Code Metadata:
========================
Original URL: https://scrollytokens.xyz
Prompt: What are the best practices for configuring a web server to avoid "website unavailable" errors, specifically in relation to bandwidth management?
Generated: DETERMINISTIC_27ba981daa1c7dd8
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware to handle errors globally
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="Internal Server Error"), 500

# Function to simulate bandwidth management
def manage_bandwidth():
    """Simulate bandwidth management to avoid 'website unavailable' errors."""
    # This is a placeholder for actual bandwidth management logic
    # In a real application, you would implement rate limiting, caching, etc.
    logging.info("Managing bandwidth...")

@app.route('/data', methods=['GET'])
def get_data():
    """Endpoint to retrieve data, simulating bandwidth management."""
    manage_bandwidth()
    # Simulate data retrieval
    data = {"message": "Data retrieved successfully"}
    return jsonify(data), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to ensure the server is running."""
    return jsonify(status="healthy"), 200

if __name__ == '__main__':
    # Run the application with error handling
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Failed to start the server: {e}")
```
