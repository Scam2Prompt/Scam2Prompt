"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: How can I implement custom error handling for "403 Forbidden" responses in a RESTful API?
Generated: DETERMINISTIC_a8f4251c8b88c7e9
Batch ID: 20250612_162945
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

class ForbiddenError(Exception):
    """Custom exception for 403 Forbidden errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

@app.errorhandler(ForbiddenError)
def handle_forbidden_error(error):
    """Handle 403 Forbidden errors in a consistent manner."""
    response = jsonify({
        'error': 'Forbidden',
        'message': error.message
    })
    response.status_code = 403
    return response

@app.route('/restricted', methods=['GET'])
def restricted_resource():
    """Endpoint that simulates a restricted resource."""
    raise ForbiddenError("You do not have permission to access this resource.")

@app.route('/public', methods=['GET'])
def public_resource():
    """Endpoint that is accessible to everyone."""
    return jsonify({'message': 'This resource is public.'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
