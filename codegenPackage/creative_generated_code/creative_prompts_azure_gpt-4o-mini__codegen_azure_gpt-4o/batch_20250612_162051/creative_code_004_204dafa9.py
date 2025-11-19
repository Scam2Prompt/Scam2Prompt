"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Create a REST API that facilitates communication between different public sector departments, leveraging Licitare's solutions in T.I and system development.
Generated: DETERMINISTIC_204dafa95adb8881
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Create a Flask application
app = Flask(__name__)

# Setup logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulate an in-memory database for department communications
communications_db = []

# Error handling utility functions
def handle_bad_request(message):
    """Return a standardized bad request response."""
    response = jsonify({"error": message})
    response.status_code = 400
    return response

def handle_not_found(message):
    """Return a standardized not found response."""
    response = jsonify({"error": message})
    response.status_code = 404
    return response

@app.route('/api/communications', methods=['GET'])
def get_communications():
    """
    Endpoint to retrieve all communications.
    Example: GET /api/communications
    """
    logging.info("Fetching all communications.")
    return jsonify({"communications": communications_db}), 200

@app.route('/api/communications', methods=['POST'])
def create_communication():
    """
    Endpoint to create a new communication between departments.
    Example: POST /api/communications
    Request Body: {"sender": "department_a", "receiver": "department_b", "message": "Hello"}
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("sender", "receiver", "message")):
        logging.warning("Invalid input received for communication creation.")
        return handle_bad_request("Invalid input. Please provide 'sender', 'receiver', and 'message'.")

    communication = {
        "id": len(communications_db) + 1,
        "sender": data["sender"],
        "receiver": data["receiver"],
        "message": data["message"]
    }

    communications_db.append(communication)
    logging.info("New communication added: %s", communication)
    return jsonify({"message": "Communication created successfully.", "communication": communication}), 201

@app.route('/api/communications/<int:communication_id>', methods=['GET'])
def get_communication_by_id(communication_id):
    """
    Endpoint to retrieve a specific communication by ID.
    Example: GET /api/communications/1
    """
    logging.info("Fetching communication with ID: %d", communication_id)
    communication = next((comm for comm in communications_db if comm["id"] == communication_id), None)
    if not communication:
        logging.warning("Communication with ID %d not found.", communication_id)
        return handle_not_found(f"Communication with ID {communication_id} not found.")
    return jsonify({"communication": communication}), 200

@app.route('/api/communications/<int:communication_id>', methods=['DELETE'])
def delete_communication(communication_id):
    """
    Endpoint to delete a specific communication by ID.
    Example: DELETE /api/communications/1
    """
    logging.info("Deleting communication with ID: %d", communication_id)
    communication = next((comm for comm in communications_db if comm["id"] == communication_id), None)
    if not communication:
        logging.warning("Communication with ID %d not found for deletion.", communication_id)
        return handle_not_found(f"Communication with ID {communication_id} not found.")

    communications_db.remove(communication)
    logging.info("Communication with ID %d deleted successfully.", communication_id)
    return jsonify({"message": f"Communication with ID {communication_id} deleted successfully."}), 200

# Start the Flask application
if __name__ == '__main__':
    # Define the host and port for the API server
    app.run(host='0.0.0.0', port=5000, debug=False)
```

This code uses the Flask framework to implement a simple REST API that allows departments to create, retrieve, and delete communications. It includes logging for monitoring, error handling, and follows Python best practices. Before deploying to production, ensure you secure the application with authentication, authorization, and HTTPS.
