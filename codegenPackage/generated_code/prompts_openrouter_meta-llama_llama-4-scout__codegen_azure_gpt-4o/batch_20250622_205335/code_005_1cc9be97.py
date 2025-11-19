"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Generate a Python API for integrating ComplyAML's training solutions with an existing compliance management system for accountable institutions.
Generated: DETERMINISTIC_1cc9be97f7df9c41
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for storing training data
training_data = {}

# Error handling class
class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    """Handle custom API errors."""
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response

@app.errorhandler(500)
def handle_internal_error(error):
    """Handle unexpected server errors."""
    logging.error(f"Internal server error: {error}")
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

@app.route('/api/training', methods=['POST'])
def add_training():
    """
    Endpoint to add a new training session.
    Expects JSON payload with 'training_id', 'title', 'description', and 'status'.
    """
    try:
        data = request.get_json()
        if not data:
            raise APIError("Invalid JSON payload", 400)

        # Validate required fields
        required_fields = ['training_id', 'title', 'description', 'status']
        for field in required_fields:
            if field not in data:
                raise APIError(f"Missing required field: {field}", 400)

        training_id = data['training_id']
        if training_id in training_data:
            raise APIError("Training ID already exists", 400)

        # Add training to mock database
        training_data[training_id] = {
            "title": data['title'],
            "description": data['description'],
            "status": data['status']
        }

        logging.info(f"Training added: {training_id}")
        return jsonify({"message": "Training added successfully"}), 201

    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        logging.error(f"Error adding training: {e}")
        return handle_internal_error(e)

@app.route('/api/training/<training_id>', methods=['GET'])
def get_training(training_id):
    """
    Endpoint to retrieve a training session by ID.
    """
    try:
        if training_id not in training_data:
            raise APIError("Training ID not found", 404)

        training = training_data[training_id]
        return jsonify(training), 200

    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        logging.error(f"Error retrieving training: {e}")
        return handle_internal_error(e)

@app.route('/api/training/<training_id>', methods=['PUT'])
def update_training(training_id):
    """
    Endpoint to update an existing training session.
    Expects JSON payload with 'title', 'description', and/or 'status'.
    """
    try:
        if training_id not in training_data:
            raise APIError("Training ID not found", 404)

        data = request.get_json()
        if not data:
            raise APIError("Invalid JSON payload", 400)

        # Update training fields
        training = training_data[training_id]
        for key in ['title', 'description', 'status']:
            if key in data:
                training[key] = data[key]

        logging.info(f"Training updated: {training_id}")
        return jsonify({"message": "Training updated successfully"}), 200

    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        logging.error(f"Error updating training: {e}")
        return handle_internal_error(e)

@app.route('/api/training/<training_id>', methods=['DELETE'])
def delete_training(training_id):
    """
    Endpoint to delete a training session by ID.
    """
    try:
        if training_id not in training_data:
            raise APIError("Training ID not found", 404)

        del training_data[training_id]
        logging.info(f"Training deleted: {training_id}")
        return jsonify({"message": "Training deleted successfully"}), 200

    except APIError as e:
        return handle_api_error(e)
    except Exception as e:
        logging.error(f"Error deleting training: {e}")
        return handle_internal_error(e)

@app.route('/api/training', methods=['GET'])
def list_trainings():
    """
    Endpoint to list all training sessions.
    """
    try:
        return jsonify(training_data), 200
    except Exception as e:
        logging.error(f"Error listing trainings: {e}")
        return handle_internal_error(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
