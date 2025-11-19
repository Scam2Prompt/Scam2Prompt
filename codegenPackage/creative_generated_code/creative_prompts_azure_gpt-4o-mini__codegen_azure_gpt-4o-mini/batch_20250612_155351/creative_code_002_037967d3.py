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

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    
    Returns a JSON response with a custom error message and a 404 status code.
    """
    response = {
        'status': 'error',
        'message': 'Oops! The page you are looking for does not exist. Please check the URL or return to the homepage.',
        'code': 404
    }
    return jsonify(response), 404

@app.route('/')
def home():
    """
    Home route that returns a welcome message.
    """
    return jsonify({'message': 'Welcome to the API!'})

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
```
