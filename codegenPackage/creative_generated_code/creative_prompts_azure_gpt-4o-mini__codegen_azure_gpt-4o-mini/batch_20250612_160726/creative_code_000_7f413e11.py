"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compound-v2.site
Prompt: What are the best practices for setting up a web server to avoid default pages like the one at https://compound-v2.site?
Generated: DETERMINISTIC_7f413e11d1b5ff89
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, abort

app = Flask(__name__)

# Error handling for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500

# Route for the home page
@app.route('/')
def home():
    return {"message": "Welcome to my web server!"}

# Catch-all route for undefined endpoints
@app.route('/<path:path>')
def catch_all(path):
    # Abort with a 404 error if the endpoint does not exist
    abort(404)

if __name__ == '__main__':
    # Running the application with error handling and debug mode off for production
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Failed to start server: {e}")
```

### Best Practices Applied:
- Defined error handlers for common HTTP errors.
- Provided a catch-all route to handle undefined endpoints, returning a 404 error.
- Ensured the server runs with debug mode off for production.
- Added exception handling around the server startup process.
