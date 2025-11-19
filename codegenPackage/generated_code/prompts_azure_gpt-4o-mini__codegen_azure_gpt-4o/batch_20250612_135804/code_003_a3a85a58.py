"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Provide an API integration example for a doodle drawing tool that enhances user engagement on a website.
Generated: DETERMINISTIC_a3a85a58e8de570a
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# In-memory storage for doodles (for demonstration purposes)
# In production, consider using a database for persistent storage
doodles = {}

# Route to fetch all doodles
@app.route('/api/doodles', methods=['GET'])
def get_doodles():
    """
    Endpoint to retrieve all doodles.
    Returns:
        JSON response containing all doodles.
    """
    return jsonify({"status": "success", "data": doodles}), 200

# Route to save a new doodle
@app.route('/api/doodles', methods=['POST'])
def save_doodle():
    """
    Endpoint to save a new doodle.
    Expects:
        JSON payload with 'id' (string) and 'data' (string).
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse the incoming JSON payload
        payload = request.get_json()
        doodle_id = payload.get('id')
        doodle_data = payload.get('data')

        # Validate the payload
        if not doodle_id or not doodle_data:
            return jsonify({"status": "error", "message": "Invalid payload. 'id' and 'data' are required."}), 400

        # Save the doodle in the in-memory storage
        doodles[doodle_id] = doodle_data
        logging.info(f"Doodle saved: {doodle_id}")

        return jsonify({"status": "success", "message": "Doodle saved successfully."}), 201
    except Exception as e:
        logging.error(f"Error saving doodle: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while saving the doodle."}), 500

# Route to delete a doodle
@app.route('/api/doodles/<doodle_id>', methods=['DELETE'])
def delete_doodle(doodle_id):
    """
    Endpoint to delete a doodle by its ID.
    Args:
        doodle_id (string): ID of the doodle to delete.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Check if the doodle exists
        if doodle_id not in doodles:
            return jsonify({"status": "error", "message": "Doodle not found."}), 404

        # Delete the doodle
        del doodles[doodle_id]
        logging.info(f"Doodle deleted: {doodle_id}")

        return jsonify({"status": "success", "message": "Doodle deleted successfully."}), 200
    except Exception as e:
        logging.error(f"Error deleting doodle: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while deleting the doodle."}), 500

# Route to update an existing doodle
@app.route('/api/doodles/<doodle_id>', methods=['PUT'])
def update_doodle(doodle_id):
    """
    Endpoint to update an existing doodle.
    Args:
        doodle_id (string): ID of the doodle to update.
    Expects:
        JSON payload with 'data' (string).
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse the incoming JSON payload
        payload = request.get_json()
        doodle_data = payload.get('data')

        # Validate the payload
        if not doodle_data:
            return jsonify({"status": "error", "message": "Invalid payload. 'data' is required."}), 400

        # Check if the doodle exists
        if doodle_id not in doodles:
            return jsonify({"status": "error", "message": "Doodle not found."}), 404

        # Update the doodle
        doodles[doodle_id] = doodle_data
        logging.info(f"Doodle updated: {doodle_id}")

        return jsonify({"status": "success", "message": "Doodle updated successfully."}), 200
    except Exception as e:
        logging.error(f"Error updating doodle: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while updating the doodle."}), 500

# Run the Flask application
if __name__ == '__main__':
    # Start the server on localhost, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```

This code provides a simple API for managing doodles, including endpoints for retrieving, saving, updating, and deleting doodles. It uses Flask for the web framework and includes error handling, logging, and comments for clarity.
