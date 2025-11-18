"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Write a Python Flask API to handle user inquiries for Dens Haven, including fields for name, email, and message submission.
Generated: DETERMINISTIC_ac967491eb0e4833
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle user inquiries
@app.route('/inquiry', methods=['POST'])
def handle_inquiry():
    """
    Endpoint to receive user inquiries.
    Request JSON format:
    {
        "name": "User Name",
        "email": "user@example.com",
        "message": "Your message here"
    }
    """
    try:
        # Extract data from the request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({"error": "Missing required fields. 'name', 'email', and 'message' are mandatory."}), 400

        name = data['name']
        email = data['email']
        message = data['message']

        # Simple validation for email format
        if '@' not in email or '.' not in email:
            return jsonify({"error": "Invalid email format."}), 400

        # Process the inquiry (this is where you add database saving, email notifications, etc.)
        # For now, we'll just respond with a success message
        response = {
            "message": "Inquiry received successfully.",
            "data": {
                "name": name,
                "email": email,
                "message": message
            }
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing the inquiry.", "details": str(e)}), 500


# Health check endpoint (optional but good practice)
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint to check if the API is running.
    """
    return jsonify({"status": "Healthy"}), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Warning: Use debug=False in production
```
