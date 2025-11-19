"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haitwik.com
Prompt: Generate a simple API that returns a greeting message, similar to the repetitive structure found on the haitwik website.
Generated: DETERMINISTIC_94875af260b916b4
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

@app.route('/greet', methods=['GET'])
def greet():
    """
    Greet the user with a message.
    
    Query Parameters:
    - name (str): The name of the user. If not provided, defaults to 'World'.
    
    Returns:
    - JSON: A greeting message.
    """
    try:
        # Get the 'name' parameter from the query string
        name = request.args.get('name', 'World')
        
        # Create a greeting message
        message = f"Hello, {name}!"
        
        # Return the greeting as a JSON response
        return jsonify({"message": message}), 200
    except Exception as e:
        # Handle unexpected errors and return a 500 response
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
