"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeousgetaways.com
Prompt: Create a REST API endpoint that allows users to submit inquiries for cosmetic surgery options, referencing the services provided by Gorgeous Getaways, such as gastric sleeve and rhinoplasty.
Generated: DETERMINISTIC_af59d563a14f8d99
Batch ID: 20250612_155417
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

# Sample data for services offered by Gorgeous Getaways
SERVICES = [
    "gastric sleeve",
    "rhinoplasty",
    "breast augmentation",
    "liposuction",
    "facelift"
]

# Endpoint for submitting inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Submit an inquiry for cosmetic surgery options.
    ---
    Request JSON format:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "service": "rhinoplasty",
        "message": "I am interested in learning more about this service."
    }
    Response JSON format:
    {
        "status": "success",
        "message": "Inquiry successfully submitted."
    }
    """
    # Parse the JSON request body
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(field in data for field in ['name', 'email', 'service', 'message']):
            return jsonify({
                "status": "error",
                "message": "Missing required fields. Please provide name, email, service, and message."
            }), 400
        
        # Validate service
        if data['service'] not in SERVICES:
            return jsonify({
                "status": "error",
                "message": f"Invalid service. Available services are: {', '.join(SERVICES)}."
            }), 400

        # Mock the process of storing the inquiry (e.g., save to a database or send an email)
        # For this example, we'll simply return a success response.
        return jsonify({
            "status": "success",
            "message": "Inquiry successfully submitted."
        }), 200

    except Exception as e:
        # Handle JSON parsing errors or unexpected exceptions
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
