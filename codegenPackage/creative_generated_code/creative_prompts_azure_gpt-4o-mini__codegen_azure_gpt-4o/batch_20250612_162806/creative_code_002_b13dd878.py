"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Generate an API endpoint for submitting customer testimonials for a paving service, inspired by the testimonials section of Bedford Paving's site.
Generated: DETERMINISTIC_b13dd878501d43c3
Batch ID: 20250612_162806
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

# In-memory storage for testimonials (in production, use a database)
testimonials = []

# Regex to validate email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


@app.route('/api/testimonials', methods=['POST'])
def submit_testimonial():
    """
    API endpoint to submit customer testimonials.

    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "testimonial": "Great service!"
    }

    Returns:
        A success message or an error response.
    """
    try:
        # Parse JSON request data
        data = request.get_json()

        # Validate input fields
        if not data:
            return jsonify({"error": "Invalid request format. JSON payload required."}), 400

        name = data.get("name")
        email = data.get("email")
        testimonial = data.get("testimonial")

        if not name or not isinstance(name, str):
            return jsonify({"error": "Name is required and must be a string."}), 400

        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({"error": "Valid email address is required."}), 400

        if not testimonial or not isinstance(testimonial, str):
            return jsonify({"error": "Testimonial is required and must be a string."}), 400

        # Save testimonial (in production, this would involve saving to a database)
        testimonials.append({
            "name": name,
            "email": email,
            "testimonial": testimonial
        })

        # Return success response
        return jsonify({"message": "Thank you! Your testimonial has been submitted."}), 201

    except Exception as e:
        # Log exception in production for debugging
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """
    API endpoint to retrieve customer testimonials.

    Returns:
        A list of all submitted testimonials.
    """
    return jsonify(testimonials), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
