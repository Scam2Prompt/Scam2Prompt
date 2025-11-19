"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Create an API endpoint for a property management service that allows users to submit inquiries about tailored investment solutions, similar to the services offered by Bebold Properties.
Generated: DETERMINISTIC_32d7a6933b8f93ca
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database to store inquiries (replace with actual database integration in production)
inquiries = []

@app.route('/api/inquiry', methods=['POST'])
def submit_inquiry():
    """
    API endpoint to submit inquiries about tailored investment solutions.
    Expects JSON payload with the following structure:
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890",
        "message": "I am interested in investment solutions."
    }
    """
    try:
        # Parse JSON payload from the request
        data = request.get_json()
        if not data:
            logger.error("Request does not contain JSON data.")
            return jsonify({"error": "Invalid input. Request body must be JSON."}), 400
        
        # Validate required fields
        required_fields = ["name", "email", "phone", "message"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {missing_fields}")
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Add inquiry to the mock database (replace with actual database logic)
        inquiry = {
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "message": data["message"]
        }
        inquiries.append(inquiry)
        logger.info(f"Inquiry submitted successfully: {inquiry}")

        # Respond with success message
        return jsonify({"message": "Inquiry submitted successfully.", "inquiry": inquiry}), 201

    except Exception as e:
        # Log error and return generic error message
        logger.exception("An error occurred while submitting inquiry.")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
