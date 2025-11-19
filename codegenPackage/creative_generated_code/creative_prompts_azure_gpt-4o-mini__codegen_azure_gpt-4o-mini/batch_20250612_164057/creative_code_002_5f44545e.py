"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineaa.cyou
Prompt: Can you provide a code snippet to log errors in Apache when encountering a 500 Internal Server Error?
Generated: DETERMINISTIC_5f44545e8b8d1170
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = 'error.log'

# Set up rotating file handler for logging errors
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
handler.setFormatter(log_formatter)
handler.setLevel(logging.ERROR)

# Get the logger and add the handler
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(handler)

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server Error by logging the error details
    and returning a JSON response to the client.
    """
    # Log the error with traceback
    logger.error('500 Internal Server Error: %s', error)

    # Return a JSON response indicating an error occurred
    response = {
        'status': 500,
        'message': 'Internal Server Error'
    }
    return jsonify(response), 500

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=False)
    except Exception as e:
        logger.error('Application failed to start: %s', e)
```
