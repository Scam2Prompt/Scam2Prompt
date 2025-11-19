"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmonyrecycle.net
Prompt: How can I implement a recycling management system using APIs to track materials and their lifecycle?
Generated: DETERMINISTIC_42be31e8d283f4e3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# recycling_management_system.py

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store materials
materials_db = {}

# Helper function to generate a unique ID for each material
def generate_material_id():
    return str(uuid.uuid4())

# API endpoint to add a new material to the system
@app.route('/materials', methods=['POST'])
def add_material():
    try:
        # Extracting material data from request
        data = request.json
        name = data.get('name')
        category = data.get('category')
        status = data.get('status', 'New')  # Default status is 'New'

        # Validate input
        if not name or not category:
            return jsonify({"error": "Name and category are required"}), 400

        # Generate unique ID for the material
        material_id = generate_material_id()

        # Add material to the database
        materials_db[material_id] = {
            'name': name,
            'category': category,
            'status': status
        }

        return jsonify({"message": "Material added successfully", "material_id": material_id}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API endpoint to update the status of a material
@app.route('/materials/<material_id>', methods=['PUT'])
def update_material_status(material_id):
    try:
        # Extracting status update data from request
        data = request.json
        new_status = data.get('status')

        # Validate input
        if not new_status:
            return jsonify({"error": "Status is required"}), 400

        # Check if material exists
        material = materials_db.get(material_id)
        if not material:
            return jsonify({"error": "Material not found"}), 404

        # Update material status
        material['status'] = new_status
        return jsonify({"message": "Material status updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API endpoint to retrieve the details of a material
@app.route('/materials/<material_id>', methods=['GET'])
def get_material(material_id):
    try:
        # Check if material exists
        material = materials_db.get(material_id)
        if not material:
            return jsonify({"error": "Material not found"}), 404

        # Return material details
        return jsonify({"material": material}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API endpoint to list all materials in the system
@app.route('/materials', methods=['GET'])
def list_materials():
    try:
        # Return all materials
        return jsonify({"materials": materials_db}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API endpoint to delete a material from the system
@app.route('/materials/<material_id>', methods=['DELETE'])
def delete_material(material_id):
    try:
        # Check if material exists
        material = materials_db.pop(material_id, None)
        if not material:
            return jsonify({"error": "Material not found"}), 404

        # Confirm deletion
        return jsonify({"message": "Material deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point for running the Flask app
if __name__ == '__main__':
    # Run the app on localhost and port 5000
    app.run(debug=True)
```

This code provides a basic implementation for a recycling management system using Flask APIs to track materials and their lifecycle. It includes endpoints for adding, updating, retrieving, listing, and deleting materials, with appropriate error handling and validation.
