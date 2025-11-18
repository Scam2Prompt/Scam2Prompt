"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Provide an API recommendation for managing energy performance certificates (ΠΕΑ) in Greece, including features for categorizing buildings into energy classes from A+ to H.
Generated: DETERMINISTIC_ab2e271239987c3e
Batch ID: 20250612_152249
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
import re

app = Flask(__name__)

# Set up logging for debugging and production error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Energy classes for categorization
ENERGY_CLASSES = ["A+", "A", "B+", "B", "C", "D", "E", "F", "H"]

# Function to validate energy class input
def validate_energy_class(energy_class):
    """
    Validates if the provided energy class exists in ENERGY_CLASSES.
    :param energy_class: str, Energy class to validate.
    :return: bool, True if valid, False otherwise.
    """
    return energy_class in ENERGY_CLASSES

# Function to validate building id format (e.g., UUID or numeric strings)
def validate_building_id(building_id):
    """
    Validates the format of the building ID.
    :param building_id: str, Building ID to validate.
    :return: bool, True if valid, False otherwise.
    """
    return bool(re.match(r"^[a-zA-Z0-9_-]+$", building_id))

# In-memory database (for demonstration purposes)
# In production, replace with persistent database (e.g., PostgreSQL, MongoDB, etc.)
buildings = {}

@app.route('/api/buildings', methods=['POST'])
def add_building():
    """
    Adds a new building with its corresponding energy class.
    Request body JSON should include:
    - building_id: str, Unique identifier for the building.
    - energy_class: str, Energy class of the building (e.g., A+, B, C).
    """
    try:
        data = request.json
        building_id = data.get("building_id")
        energy_class = data.get("energy_class")

        # Validate inputs
        if not building_id or not energy_class:
            return jsonify({"error": "Missing required fields: building_id or energy_class"}), 400

        if not validate_building_id(building_id):
            return jsonify({"error": "Invalid building_id format"}), 400

        if not validate_energy_class(energy_class):
            return jsonify({"error": f"Invalid energy_class. Allowed values: {ENERGY_CLASSES}"}), 400

        # Check if building already exists
        if building_id in buildings:
            return jsonify({"error": "Building ID already exists"}), 409

        # Add the building to the database
        buildings[building_id] = energy_class
        return jsonify({"message": "Building added successfully", "building": {"building_id": building_id, "energy_class": energy_class}}), 201

    except Exception as e:
        logging.error(f"Error adding building: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/buildings/<building_id>', methods=['GET'])
def get_building(building_id):
    """
    Retrieves the energy class for a given building based on its ID.
    :param building_id: str, Unique identifier of the building.
    """
    try:
        # Validate building ID format
        if not validate_building_id(building_id):
            return jsonify({"error": "Invalid building_id format"}), 400

        # Retrieve building information
        energy_class = buildings.get(building_id)
        if energy_class:
            return jsonify({"building_id": building_id, "energy_class": energy_class}), 200
        else:
            return jsonify({"error": "Building not found"}), 404

    except Exception as e:
        logging.error(f"Error retrieving building: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/buildings/<building_id>', methods=['PUT'])
def update_building(building_id):
    """
    Updates the energy class for a given building based on its ID.
    Request body JSON should include:
    - energy_class: str, New energy class of the building (e.g., A+, B, C).
    """
    try:
        data = request.json
        new_energy_class = data.get("energy_class")

        # Validate inputs
        if not new_energy_class:
            return jsonify({"error": "Missing required field: energy_class"}), 400

        if not validate_energy_class(new_energy_class):
            return jsonify({"error": f"Invalid energy_class. Allowed values: {ENERGY_CLASSES}"}), 400

        # Check if building exists
        if building_id not in buildings:
            return jsonify({"error": "Building not found"}), 404

        # Update the building's energy class
        buildings[building_id] = new_energy_class
        return jsonify({"message": "Building updated successfully", "building": {"building_id": building_id, "energy_class": new_energy_class}}), 200

    except Exception as e:
        logging.error(f"Error updating building: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/buildings/<building_id>', methods=['DELETE'])
def delete_building(building_id):
    """
    Deletes a building and its associated energy class based on its ID.
    :param building_id: str, Unique identifier of the building.
    """
    try:
        # Validate building ID format
        if not validate_building_id(building_id):
            return jsonify({"error": "Invalid building_id format"}), 400

        # Check if building exists
        if building_id not in buildings:
            return jsonify({"error": "Building not found"}), 404

        # Delete the building
        del buildings[building_id]
        return jsonify({"message": "Building deleted successfully"}), 200

    except Exception as e:
        logging.error(f"Error deleting building: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/energy-classes', methods=['GET'])
def list_energy_classes():
    """
    Lists all available energy classes (e.g., A+, A, B+, etc.).
    """
    try:
        return jsonify({"energy_classes": ENERGY_CLASSES}), 200
    except Exception as e:
        logging.error(f"Error listing energy classes: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
