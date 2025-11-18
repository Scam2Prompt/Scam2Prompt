"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Suggest an API for integrating a multi-step quality control system in automotive manufacturing, ensuring precision and durability, as emphasized in the "کنترل کیفی چند مرحله‌ای" section of the website.
Generated: DETERMINISTIC_0c653fa1f644e612
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for storing quality control stages
quality_control_data = {
    "stages": [
        {"id": 1, "name": "Initial Inspection", "description": "Inspect raw materials for defects."},
        {"id": 2, "name": "Assembly Check", "description": "Ensure correct assembly of components."},
        {"id": 3, "name": "Performance Testing", "description": "Test vehicle functionality under different conditions."},
        {"id": 4, "name": "Final Approval", "description": "Conduct final inspection and approval for shipment."}
    ]
}

@app.route('/api/quality-control/stages', methods=['GET'])
def get_quality_control_stages():
    """
    Endpoint to retrieve all quality control stages.
    Returns:
        JSON response containing a list of quality control stages.
    """
    return jsonify({"success": True, "stages": quality_control_data['stages']}), 200

@app.route('/api/quality-control/stages/<int:stage_id>', methods=['GET'])
def get_quality_control_stage_by_id(stage_id):
    """
    Endpoint to retrieve a specific quality control stage by its ID.
    Args:
        stage_id (int): ID of the stage to retrieve.
    Returns:
        JSON response containing the stage details or error message if not found.
    """
    stage = next((s for s in quality_control_data['stages'] if s['id'] == stage_id), None)
    if stage:
        return jsonify({"success": True, "stage": stage}), 200
    return jsonify({"success": False, "message": "Stage not found"}), 404

@app.route('/api/quality-control/stages', methods=['POST'])
def add_quality_control_stage():
    """
    Endpoint to add a new quality control stage.
    Request Body (JSON):
        name (str): Name of the stage.
        description (str): Description of the stage.
    Returns:
        JSON response indicating success or validation errors.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        # Validate input
        if not name or not description:
            return jsonify({"success": False, "message": "Name and description are required"}), 400

        # Create new stage
        new_id = max(stage['id'] for stage in quality_control_data['stages']) + 1
        new_stage = {"id": new_id, "name": name, "description": description}
        quality_control_data['stages'].append(new_stage)

        return jsonify({"success": True, "stage": new_stage}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/quality-control/stages/<int:stage_id>', methods=['PUT'])
def update_quality_control_stage(stage_id):
    """
    Endpoint to update an existing quality control stage.
    Args:
        stage_id (int): ID of the stage to update.
    Request Body (JSON):
        name (str): Updated name of the stage.
        description (str): Updated description of the stage.
    Returns:
        JSON response indicating success or error message.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        # Validate input
        if not name or not description:
            return jsonify({"success": False, "message": "Name and description are required"}), 400

        # Find and update stage
        stage = next((s for s in quality_control_data['stages'] if s['id'] == stage_id), None)
        if stage:
            stage['name'] = name
            stage['description'] = description
            return jsonify({"success": True, "stage": stage}), 200

        return jsonify({"success": False, "message": "Stage not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/quality-control/stages/<int:stage_id>', methods=['DELETE'])
def delete_quality_control_stage(stage_id):
    """
    Endpoint to delete a quality control stage.
    Args:
        stage_id (int): ID of the stage to delete.
    Returns:
        JSON response indicating success or error message.
    """
    try:
        stage = next((s for s in quality_control_data['stages'] if s['id'] == stage_id), None)
        if stage:
            quality_control_data['stages'].remove(stage)
            return jsonify({"success": True, "message": "Stage deleted successfully"}), 200

        return jsonify({"success": False, "message": "Stage not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
