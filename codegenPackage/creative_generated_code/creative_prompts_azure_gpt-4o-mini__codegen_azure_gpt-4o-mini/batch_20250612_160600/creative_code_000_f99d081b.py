"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://20000.paperplane.io
Prompt: What are the implications of a website being permanently moved, and how can I handle redirects in my web application?
Generated: DETERMINISTIC_f99d081bffad5fde
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

# Error handling for bad requests
class CustomError(Exception):
    pass

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify({'message': str(error)})
    response.status_code = 400
    return response

@app.route('/old-url')
def old_url():
    """
    Redirects permanently from /old-url to /new-url.
    This should be used when a resource has been permanently moved.
    """
    return redirect(url_for('new_url'), code=301)

@app.route('/new-url')
def new_url():
    """
    The new location of the resource. This endpoint should provide
    the content or functionality that was previously available at /old-url.
    """
    return "You have been redirected to the new URL!"

@app.route('/move-url', methods=['POST'])
def move_url():
    """
    Endpoint to handle a request for moving a URL permanently.
    Accepts JSON with 'old_url' and 'new_url'.
    """
    data = request.get_json()
    
    if not data or 'old_url' not in data or 'new_url' not in data:
        raise CustomError("Invalid input. Please provide 'old_url' and 'new_url'.")
    
    old_url = data['old_url']
    new_url = data['new_url']
    
    # Here you would typically update your routing configuration or database
    # For demonstration purposes, this will just return a success message
    return jsonify({
        'message': f"URL moved from {old_url} to {new_url} permanently.",
        'status': 'success'
    }), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
