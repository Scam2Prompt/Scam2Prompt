"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysolana.info
Prompt: Generate an example of a web application that includes performance and security features similar to those provided by Cloudflare.
Generated: DETERMINISTIC_458511b6eee50477
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a structured response."""
    return jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle general exceptions and return a structured response."""
    logging.error(f"Unhandled exception: {str(e)}")
    return jsonify({
        "error": {
            "code": 500,
            "name": "Internal Server Error",
            "description": "An unexpected error occurred."
        }
    }), 500

@app.route('/api/data', methods=['GET'])
@limiter.limit("10 per minute")
def get_data():
    """API endpoint to retrieve data with rate limiting."""
    # Simulating data retrieval (mock example)
    data = {"message": "Hello, secure world!"}
    logging.info("Data retrieved successfully.")
    return jsonify(data)

@app.route('/api/submit', methods=['POST'])
@limiter.limit("5 per minute")
def submit_data():
    """API endpoint to submit data with validation and rate limiting."""
    data = request.get_json()
    
    # Simple validation
    if not data or 'content' not in data:
        logging.warning("Invalid data submitted.")
        return jsonify({"error": "Invalid data."}), 400
    
    logging.info(f"Data submitted: {data['content']}")
    return jsonify({"message": "Data received!", "content": data['content']}), 201

if __name__ == '__main__':
    # Run the application securely
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
```

### Requirements
To run the above code, make sure you have the following packages installed:

```bash
pip install Flask Flask-Cors Flask-Limiter
```

### Note
This Flask application features:
- Rate limiting to prevent abuse.
- Error handling for HTTP exceptions and general exceptions.
- Structured JSON responses for errors.
- CORS support for cross-origin requests.
- SSL context for secure communication (temporary self-signed certificate).

Make sure to replace the SSL context with a proper certificate for production environments.
