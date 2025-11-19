"""
Generated Code Metadata:
========================
Original URL: https://haitwik.com
Prompt: Develop a RESTful API endpoint that responds with a custom message, mimicking the repetitive nature of the haitwik website.
Generated: DETERMINISTIC_1680d32a948f2661
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_custom_message():
    """
    Endpoint to return a custom repetitive message similar to haitwik website.
    
    Query Parameters:
        repeat (int): Number of times to repeat the message (default: 3).
        
    Returns:
        JSON response containing the repeated message.
        
    Raises:
        BadRequest: If repeat parameter is not a positive integer.
        InternalServerError: If an unexpected error occurs.
    """
    try:
        # Get repeat count from query parameters
        repeat = request.args.get('repeat', default=3, type=int)
        
        # Validate repeat count
        if repeat <= 0:
            raise BadRequest("Repeat count must be a positive integer")
            
        # Create the repetitive message
        base_message = "This is a custom message. "
        message = base_message * repeat
        
        # Prepare response
        response = {
            'message': message.strip(),
            'repeat_count': repeat,
            'status': 'success'
        }
        
        return jsonify(response)
    
    except BadRequest as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400
        
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
