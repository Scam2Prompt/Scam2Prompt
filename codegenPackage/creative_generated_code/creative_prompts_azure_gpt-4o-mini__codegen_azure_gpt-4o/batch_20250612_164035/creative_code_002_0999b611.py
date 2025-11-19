"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Create an API endpoint for a legal service that allows clients to submit inquiries about "Medidas Protetivas" and "Alienação Parental."
Generated: DETERMINISTIC_0999b611aa63fded
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for the requested API endpoint using Python and Flask:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Data store for inquiries (In production, use a database)
inquiries = []

# API endpoint to submit inquiries
@app.route('/submit_inquiry', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit an inquiry related to 'Medidas Protetivas' or 'Alienação Parental'.
    Expects a JSON payload with 'client_name', 'email', 'topic', and 'message'.
    """
    try:
        # Parse and validate the request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON payload'}), 400

        client_name = data.get('client_name')
        email = data.get('email')
        topic = data.get('topic')
        message = data.get('message')

        # Ensure all required fields are present
        if not client_name or not email or not topic or not message:
            return jsonify({'error': 'Missing required fields'}), 400

        # Ensure the topic is valid
        valid_topics = ['Medidas Protetivas', 'Alienação Parental']
        if topic not in valid_topics:
            return jsonify({'error': f'Invalid topic. Must be one of {valid_topics}'}), 400

        # Store the inquiry (In production, save to a database)
        inquiry = {
            'id': len(inquiries) + 1,  # Simple auto-increment ID
            'client_name': client_name,
            'email': email,
            'topic': topic,
            'message': message
        }
        inquiries.append(inquiry)

        # Return a success response
        return jsonify({'message': 'Inquiry submitted successfully', 'inquiry': inquiry}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# API endpoint to retrieve all inquiries (Optional for debugging or admin)
@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    """
    Endpoint to retrieve all submitted inquiries.
    """
    return jsonify({'inquiries': inquiries}), 200

# Main entry point for running the Flask application
if __name__ == '__main__':
    # Use `debug=True` only in development; set it to `False` in production
    app.run(debug=True)
```

### Notes:
- Replace the in-memory `inquiries` list with a database in production for persistence.
- Ensure proper authentication and authorization for sensitive operations in production.
- Use environment variables to configure the Flask application for deployment.
