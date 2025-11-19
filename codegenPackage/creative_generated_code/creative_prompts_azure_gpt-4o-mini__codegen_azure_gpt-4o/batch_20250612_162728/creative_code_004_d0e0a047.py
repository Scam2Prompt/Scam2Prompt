"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workspace-207.com
Prompt: How can I customize the CAPTCHA challenge to enhance user experience while ensuring security?
Generated: DETERMINISTIC_d0e0a0473b6d7f25
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example of a customizable CAPTCHA challenge system:

```python
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# Generate CAPTCHA text
def generate_captcha_text(length=6):
    """
    Generates a random alphanumeric CAPTCHA text.
    :param length: Length of the CAPTCHA text (default is 6).
    :return: Random alphanumeric string of the given length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Validate CAPTCHA response
def validate_captcha(user_input, actual_captcha):
    """
    Validates the user-provided CAPTCHA input against the actual CAPTCHA.
    :param user_input: User-provided CAPTCHA text.
    :param actual_captcha: Original CAPTCHA text.
    :return: Boolean indicating if the CAPTCHA is valid.
    """
    return user_input.strip().lower() == actual_captcha.strip().lower()

# Endpoint to generate a CAPTCHA
@app.route('/generate_captcha', methods=['GET'])
def generate_captcha():
    """
    API endpoint to generate a CAPTCHA challenge.
    :return: JSON response with the CAPTCHA text.
    """
    try:
        captcha_text = generate_captcha_text()
        return jsonify({
            "captcha": captcha_text,
            "message": "CAPTCHA generated successfully"
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "error": str(e),
            "message": "Failed to generate CAPTCHA"
        }), 500

# Endpoint to validate CAPTCHA
@app.route('/validate_captcha', methods=['POST'])
def captcha_validation():
    """
    API endpoint to validate the CAPTCHA response.
    :return: JSON response indicating success or failure of validation.
    """
    try:
        # Extract user input and CAPTCHA from request
        data = request.get_json()
        user_input = data.get("user_input")
        actual_captcha = data.get("actual_captcha")

        if not user_input or not actual_captcha:
            return jsonify({
                "message": "Invalid input. Both 'user_input' and 'actual_captcha' are required."
            }), 400

        # Validate CAPTCHA
        is_valid = validate_captcha(user_input, actual_captcha)
        if is_valid:
            return jsonify({
                "message": "CAPTCHA validation successful"
            }), 200
        else:
            return jsonify({
                "message": "CAPTCHA validation failed"
            }), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "error": str(e),
            "message": "Failed to validate CAPTCHA"
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code snippet provides an example of a customizable CAPTCHA challenge system using Flask. It includes endpoints for generating and validating CAPTCHA challenges, error handling, and comments for clarity. Run the code in a Python environment with Flask installed (`pip install flask`).
