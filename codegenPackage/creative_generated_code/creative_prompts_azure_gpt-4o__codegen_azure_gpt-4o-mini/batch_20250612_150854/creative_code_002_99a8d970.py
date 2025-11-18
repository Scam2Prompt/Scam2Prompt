"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-elevate.com
Prompt: Recommend APIs or libraries that can be used to develop a user-friendly interface similar to Immediate Elevate's registration process, focusing on real-time input validation.
Generated: DETERMINISTIC_99a8d970e2da372b
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to validate email format
def validate_email(email):
    # Simple regex for validating an email address
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

# Function to validate password strength
def validate_password(password):
    # Password must be at least 8 characters long, include upper/lowercase letters and numbers
    return (len(password) >= 8 and
            re.search(r'[A-Za-z]', password) and
            re.search(r'[0-9]', password))

# API endpoint to validate user registration input
@app.route('/validate_registration', methods=['POST'])
def validate_registration():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Check if data is provided
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extract email and password from data
        email = data.get('email')
        password = data.get('password')

        # Validate email and password
        if not email or not validate_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        
        if not password or not validate_password(password):
            return jsonify({"error": "Password must be at least 8 characters long and include letters and numbers"}), 400

        # Return success response if validation passes
        return jsonify({"message": "Validation successful"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Main function to run the Flask application
if __name__ == '__main__':
    # Running the app in debug mode for development purposes
    app.run(debug=True)
```

### Dependencies
Make sure to install the required libraries before running the above code:
```bash
pip install Flask Flask-CORS
``` 

### Usage
Run the script, and you can send a POST request to `/validate_registration` with JSON containing `email` and `password` to validate user registration input.
