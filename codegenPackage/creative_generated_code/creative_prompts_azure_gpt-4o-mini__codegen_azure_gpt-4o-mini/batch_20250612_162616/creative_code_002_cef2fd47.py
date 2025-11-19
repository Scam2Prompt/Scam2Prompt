"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paramgaminglabs.app
Prompt: Write a code snippet that demonstrates how to validate user input to prevent phishing attempts in a web application.
Generated: DETERMINISTIC_cef2fd477b8b90f9
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to validate user input
def is_valid_input(user_input):
    """
    Validate user input to prevent phishing attempts.

    Args:
        user_input (str): The input string to validate.

    Returns:
        bool: True if input is valid, False otherwise.
    """
    # Regular expression to allow only alphanumeric characters and specific safe symbols
    pattern = re.compile(r'^[a-zA-Z0-9_.-]*$')
    
    # Check if the input matches the allowed pattern
    if pattern.match(user_input):
        return True
    else:
        return False

@app.route('/submit', methods=['POST'])
def submit():
    """
    Endpoint to handle user input submission.

    Returns:
        JSON response indicating success or error.
    """
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        
        # Check if 'user_input' is in the request data
        if 'user_input' not in data:
            return jsonify({'error': 'Missing user_input field.'}), 400
        
        user_input = data['user_input']
        
        # Validate the user input
        if is_valid_input(user_input):
            return jsonify({'message': 'Input is valid.'}), 200
        else:
            return jsonify({'error': 'Invalid input detected.'}), 400

    except Exception as e:
        # Log the error and return a server error response
        app.logger.error(f"Error processing request: {e}")
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
