"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://free-eth.paperplane.io
Prompt: How can I implement a redirect mechanism in my API to manage changes in endpoint URLs effectively?
Generated: DETERMINISTIC_d7f4b9f25d0f38d6
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, redirect, jsonify

app = Flask(__name__)

# A dictionary to hold the mapping of old endpoints to new endpoints
redirects = {
    '/old-endpoint-1': '/new-endpoint-1',
    '/old-endpoint-2': '/new-endpoint-2',
}

@app.route('/old-endpoint-1')
def old_endpoint_1():
    """
    Redirects to the new endpoint for old-endpoint-1.
    """
    return redirect(redirects['/old-endpoint-1'], code=301)

@app.route('/old-endpoint-2')
def old_endpoint_2():
    """
    Redirects to the new endpoint for old-endpoint-2.
    """
    return redirect(redirects['/old-endpoint-2'], code=301)

@app.route('/new-endpoint-1')
def new_endpoint_1():
    """
    A new endpoint that replaces old-endpoint-1.
    """
    return jsonify(message="This is the new endpoint 1.")

@app.route('/new-endpoint-2')
def new_endpoint_2():
    """
    A new endpoint that replaces old-endpoint-2.
    """
    return jsonify(message="This is the new endpoint 2.")

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found.
    Returns a JSON response indicating the error.
    """
    return jsonify(error="Not found", status=404), 404

if __name__ == '__main__':
    # Running the Flask application
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
