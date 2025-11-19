"""
Generated Code Metadata:
========================
Original URL: https://new-school-day-1.pages.dev
Prompt: Design a RESTful API using Flask (Python) that accepts a string input and returns a JSON response indicating whether the input string matches the specific alphanumeric pattern observed in the webpage content.
Generated: DETERMINISTIC_3a2d6ec1fe47e33c
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Define a regex pattern for alphanumeric strings
ALPHANUMERIC_PATTERN = re.compile(r'^[a-zA-Z0-9]+$')

@app.route('/validate', methods=['POST'])
def validate_string():
    """
    Validate if the input string matches the alphanumeric pattern.

    Request JSON format:
    {
        "input_string": "your_string_here"
    }

    Returns:
    JSON response indicating whether the input string is valid.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Check if the input data is valid
        if not data or 'input_string' not in data:
            return jsonify({"error": "Invalid input. Please provide 'input_string'."}), 400

        input_string = data['input_string']

        # Check if the input string matches the alphanumeric pattern
        is_valid = bool(ALPHANUMERIC_PATTERN.match(input_string))

        # Prepare the response
        response = {
            "input_string": input_string,
            "is_valid": is_valid
        }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
