"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Provide an API integration example for a doodle drawing tool that enhances user engagement on a website.
Generated: DETERMINISTIC_a3a85a58e8de570a
Batch ID: 20250612_135804
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
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging for debugging and production readiness
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for doodles (could be replaced with a database for production)
doodle_storage = {}

# Define a route to save a doodle
@app.route('/api/doodle', methods=['POST'])
def save_doodle():
    """
    Endpoint to save a doodle.
    Expects JSON payload: {"user_id": <str>, "doodle_data": <str>}
    Saves the doodle with a unique ID and associates it with the user.
    """
    try:
        data = request.json

        # Validate request data
        if not data or 'user_id' not in data or 'doodle_data' not in data:
            return jsonify({"error": "Invalid input"}), 400

        user_id = data['user_id']
        doodle_data = data['doodle_data']

        # Generate a unique doodle ID (could use UUID for more robust uniqueness)
        doodle_id = f"doodle_{len(doodle_storage) + 1}"

        # Save the doodle in memory (could be stored in a database in production)
        doodle_storage[doodle_id] = {
            "user_id": user_id,
            "doodle_data": doodle_data
        }

        logging.info(f"Doodle saved: {doodle_id}")
        
        return jsonify({"message": "Doodle saved successfully", "doodle_id": doodle_id}), 201

    except Exception as e:
        logging.error(f"Error saving doodle: {str(e)}")
        return jsonify({"error": "An error occurred while saving the doodle"}), 500


# Define a route to retrieve a doodle
@app.route('/api/doodle/<doodle_id>', methods=['GET'])
def get_doodle(doodle_id):
    """
    Endpoint to retrieve a doodle by ID.
    """
    try:
        doodle = doodle_storage.get(doodle_id)

        if not doodle:
            return jsonify({"error": "Doodle not found"}), 404

        logging.info(f"Doodle retrieved: {doodle_id}")
        
        return jsonify(doodle), 200

    except Exception as e:
        logging.error(f"Error retrieving doodle: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving the doodle"}), 500


# Define a route to list all doodles
@app.route('/api/doodles', methods=['GET'])
def list_doodles():
    """
    Endpoint to list all doodles.
    Returns all saved doodles.
    """
    try:
        logging.info("Listing all doodles")
        return jsonify(list(doodle_storage.values())), 200

    except Exception as e:
        logging.error(f"Error listing doodles: {str(e)}")
        return jsonify({"error": "An error occurred while listing doodles"}), 500


# Start the Flask application
if __name__ == '__main__':
    # Run the server on localhost at port 5000
    app.run(host='127.0.0.1', port=5000)
```
