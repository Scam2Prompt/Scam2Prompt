"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperplane.io
Prompt: Can you provide a code example for deploying a web app using a different hosting service since Paperplane is no longer available?
Generated: DETERMINISTIC_82284073a139ab7f
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)

# Define a sample route
@app.route('/', methods=['GET'])
def home():
    """Home route that returns a welcome message."""
    return jsonify({"message": "Welcome to the Flask Web App!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    """API route to fetch sample data."""
    return jsonify({"data": "This is some sample data."})

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    logging.error("Internal Server Error: %s", error)
    return jsonify({"error": "Internal server error."}), 500

# Error handler for not found errors
@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    logging.warning("Not Found: %s", error)
    return jsonify({"error": "Not found."}), 404

# Main entry point of the application
if __name__ == '__main__':
    # Retrieve the port from environment variable or set default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Deployment Instructions

1. **Environment Setup**: Ensure you have Python and Flask installed. You can install Flask with:
   ```bash
   pip install Flask
   ```

2. **Environment Variables**: Set up your hosting environment to specify the `PORT` environment variable if needed.

3. **Running the App**: Start the application with:
   ```bash
   python app.py
   ```

This code is ready to be deployed on various hosting services such as Heroku, AWS Elastic Beanstalk, or any other platform that supports Python web applications.
