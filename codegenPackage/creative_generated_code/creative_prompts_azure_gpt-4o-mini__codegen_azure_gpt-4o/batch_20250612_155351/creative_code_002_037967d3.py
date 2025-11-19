"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-metamesklogin.uteach.io
Prompt: Create an API response in Python that returns a 404 status code with a custom message, inspired by the content of the Uteach error page.
Generated: DETERMINISTIC_037967d3f1971624
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/custom-404', methods=['GET'])
def custom_404():
    """
    A route that simulates a 404 error with a custom message.
    """
    response = {
        "status": 404,
        "message": "Oops! The page you're looking for doesn't exist.",
        "suggestion": "Check the URL or return to the homepage."
    }
    return jsonify(response), 404

@app.errorhandler(404)
def handle_404(e):
    """
    Global error handler for 404 errors.
    Returns a consistent custom message for all 404 errors.
    """
    response = {
        "status": 404,
        "message": "Oops! The page you're looking for doesn't exist.",
        "suggestion": "Check the URL or return to the homepage."
    }
    return jsonify(response), 404

if __name__ == '__main__':
    # Start the Flask development server.
    app.run(debug=True)
```
