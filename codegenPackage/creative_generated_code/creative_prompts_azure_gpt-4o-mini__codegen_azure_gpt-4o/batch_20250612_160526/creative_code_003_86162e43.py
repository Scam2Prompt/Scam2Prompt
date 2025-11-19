"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://screciclados.mx
Prompt: Create a RESTful API endpoint that allows users to submit electronic waste for recycling, referencing the environmental responsibility highlighted by SCR Reciclados.
Generated: DETERMINISTIC_86162e4333b04654
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py
# Description: RESTful API to allow users to submit electronic waste for recycling.

from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample storage for submitted data (in production, use a database)
electronic_waste_submissions = []

@app.route('/submit-ewaste', methods=['POST'])
def submit_ewaste():
    """
    Endpoint to submit electronic waste for recycling.
    Accepts JSON payload with the following format:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "item_type": "Laptop",
        "quantity": 1
    }
    Returns a success message if input is valid and submission is stored.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate input fields
        required_fields = ['name', 'email', 'item_type', 'quantity']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Validate quantity (must be a positive integer)
        if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
            return jsonify({"error": "Quantity must be a positive integer"}), 400

        # Store submission (in-memory storage for this example)
        submission = {
            "name": data['name'],
            "email": data['email'],
            "item_type": data['item_type'],
            "quantity": data['quantity']
        }
        electronic_waste_submissions.append(submission)

        # Log the submission
        logging.info(f"Electronic waste submission received: {submission}")

        # Return success response
        return jsonify({"message": "Electronic waste submitted successfully!", "submission": submission}), 201

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


@app.route('/submissions', methods=['GET'])
def get_submissions():
    """
    Endpoint to retrieve all electronic waste submissions.
    Returns a list of all submissions stored in memory.
    """
    try:
        return jsonify({"submissions": electronic_waste_submissions}), 200
    except Exception as e:
        logging.error(f"An error occurred while retrieving submissions: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
