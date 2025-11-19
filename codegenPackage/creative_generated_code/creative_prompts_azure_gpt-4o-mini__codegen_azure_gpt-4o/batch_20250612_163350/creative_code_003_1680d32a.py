"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Develop a RESTful API endpoint that responds with a custom message, mimicking the repetitive nature of the haitwik website.
Generated: DETERMINISTIC_1680d32a948f2661
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Custom messages to mimic repetitive nature of haitwik
DEFAULT_MESSAGE = "Welcome to Haitwik! The place where learning is infinite."
REPETITIVE_MESSAGE_TEMPLATE = "Haitwik says: {}"

@app.route('/api/haitwik-message', methods=['GET'])
def get_haitwik_message():
    """
    RESTful API endpoint to return a repetitive Haitwik-style message.
    Query parameter 'count' can be used to control the number of repetitions.
    """
    try:
        # Get the 'count' query parameter, default to 1 if not provided
        count = request.args.get('count', default=1, type=int)
        
        # Validate 'count' to ensure it is a positive integer
        if count <= 0:
            return jsonify({"error": "Count must be a positive integer"}), 400
        
        # Generate the repetitive custom message
        message = [REPETITIVE_MESSAGE_TEMPLATE.format(DEFAULT_MESSAGE) for _ in range(count)]
        
        # Return response as JSON
        return jsonify({"messages": message}), 200
    
    except Exception as e:
        # Handle unexpected exceptions and report a generic error
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000 in debug mode for development
    app.run(host='0.0.0.0', port=5000, debug=True)
```
