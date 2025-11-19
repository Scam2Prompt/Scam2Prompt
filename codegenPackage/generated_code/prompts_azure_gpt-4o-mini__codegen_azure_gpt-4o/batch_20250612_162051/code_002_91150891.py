"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Create an API recommendation for managing mechanical installations in the oil and gas industry, referencing the expertise of C&M Pinnacle.
Generated: DETERMINISTIC_9115089170d47c96
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for mechanical installations
mechanical_installations = [
    {
        "id": 1,
        "name": "Pipeline Installation",
        "description": "Installation of pipelines for oil and gas transport.",
        "expertise": "C&M Pinnacle",
        "status": "Completed"
    },
    {
        "id": 2,
        "name": "Pump Station Setup",
        "description": "Setup of pump stations for oil extraction.",
        "expertise": "C&M Pinnacle",
        "status": "In Progress"
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to get all mechanical installations
@app.route('/api/installations', methods=['GET'])
def get_installations():
    """
    Fetch all mechanical installations.
    """
    logging.info("Fetching all mechanical installations.")
    return jsonify(mechanical_installations), 200

# Route to get a specific installation by ID
@app.route('/api/installations/<int:installation_id>', methods=['GET'])
def get_installation_by_id(installation_id):
    """
    Fetch a specific mechanical installation by ID.
    """
    logging.info(f"Fetching installation with ID: {installation_id}")
    installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
    if installation is None:
        logging.warning(f"Installation with ID {installation_id} not found.")
        return jsonify({"error": "Installation not found"}), 404
    return jsonify(installation), 200

# Route to add a new mechanical installation
@app.route('/api/installations', methods=['POST'])
def add_installation():
    """
    Add a new mechanical installation.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "description", "expertise", "status")):
            logging.error("Invalid input data for new installation.")
            return jsonify({"error": "Invalid input data"}), 400

        new_installation = {
            "id": len(mechanical_installations) + 1,
            "name": data["name"],
            "description": data["description"],
            "expertise": data["expertise"],
            "status": data["status"]
        }
        mechanical_installations.append(new_installation)
        logging.info(f"Added new installation: {new_installation}")
        return jsonify(new_installation), 201
    except Exception as e:
        logging.error(f"Error adding new installation: {str(e)}")
        return jsonify({"error": "Failed to add installation"}), 500

# Route to update an existing installation by ID
@app.route('/api/installations/<int:installation_id>', methods=['PUT'])
def update_installation(installation_id):
    """
    Update an existing mechanical installation by ID.
    """
    try:
        data = request.get_json()
        installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
        if installation is None:
            logging.warning(f"Installation with ID {installation_id} not found.")
            return jsonify({"error": "Installation not found"}), 404

        installation.update({
            "name": data.get("name", installation["name"]),
            "description": data.get("description", installation["description"]),
            "expertise": data.get("expertise", installation["expertise"]),
            "status": data.get("status", installation["status"])
        })
        logging.info(f"Updated installation with ID {installation_id}: {installation}")
        return jsonify(installation), 200
    except Exception as e:
        logging.error(f"Error updating installation: {str(e)}")
        return jsonify({"error": "Failed to update installation"}), 500

# Route to delete an installation by ID
@app.route('/api/installations/<int:installation_id>', methods=['DELETE'])
def delete_installation(installation_id):
    """
    Delete a mechanical installation by ID.
    """
    try:
        installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
        if installation is None:
            logging.warning(f"Installation with ID {installation_id} not found.")
            return jsonify({"error": "Installation not found"}), 404

        mechanical_installations.remove(installation)
        logging.info(f"Deleted installation with ID {installation_id}")
        return jsonify({"message": "Installation deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting installation: {str(e)}")
        return jsonify({"error": "Failed to delete installation"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
