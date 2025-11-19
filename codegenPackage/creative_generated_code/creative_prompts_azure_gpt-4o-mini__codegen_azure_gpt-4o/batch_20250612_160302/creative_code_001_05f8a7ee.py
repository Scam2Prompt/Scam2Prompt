"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.xyz
Prompt: What are the best practices for setting up a domain inquiry form similar to the one on Idex.xyz?
Generated: DETERMINISTIC_05f8a7ee421f41e2
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re  # For validating email and domain formats
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Regex pattern for validating domain names
DOMAIN_REGEX = r"^(?!-)[A-Za-z0-9-]+(?<!-)\.[A-Za-z]{2,}$"

# Regex pattern for validating email addresses
EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

# Route for handling domain inquiry form submissions
@app.route('/inquire', methods=['POST'])
def domain_inquiry():
    """
    Handles domain inquiry form submissions.
    Validates user input and returns appropriate responses.
    """
    try:
        # Extract JSON data from the request
        data = request.get_json()

        # Ensure required fields exist in the request
        if not data or 'email' not in data or 'domain' not in data:
            return jsonify({"error": "Missing 'email' or 'domain' field."}), 400
        
        email = data['email']
        domain = data['domain']

        # Validate email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate domain format
        if not re.match(DOMAIN_REGEX, domain):
            return jsonify({"error": "Invalid domain format."}), 400

        # Simulate storing or processing the inquiry
        # In a production environment, you might save this data to a database or send it to an API
        inquiry_result = {
            "message": "Inquiry submitted successfully!",
            "submitted_data": {
                "email": email,
                "domain": domain
            }
        }

        return jsonify(inquiry_result), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Main application entry point
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)  # Production-ready setup
```

### Notes:
- To run this code, you will need to install Flask (`pip install flask`).
- Set `debug=False` for production to avoid exposing sensitive information.
- Use a reverse proxy (e.g., Nginx) or a WSGI server (e.g., Gunicorn) for deploying this app to production.
- Ensure the API endpoint `/inquire` is protected against common security vulnerabilities (e.g., rate limiting, request validation).
