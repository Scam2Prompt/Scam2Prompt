"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tallhills.com
Prompt: Generate a sample API that integrates design thinking methodologies into a product development workflow, based on insights from TallHills.
Generated: DETERMINISTIC_85eb3f2cb23898e8
Batch ID: 20250612_162050
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

# Sample data storage for simplicity; In production, use a database.
product_workflows = {}

# Error messages
ERROR_MISSING_FIELDS = "Required fields are missing."
ERROR_WORKFLOW_NOT_FOUND = "Workflow not found."

# Endpoints

@app.route('/workflow', methods=['POST'])
def create_workflow():
    """
    Endpoint to create a new product development workflow.
    Request JSON format:
    {
        "workflow_id": "unique_id",
        "name": "Workflow Name",
        "design_thinking_phases": ["Empathize", "Define", "Ideate", "Prototype", "Test"],
        "insights": "Key insights from TallHills"
    }
    """
    try:
        data = request.json
        # Validate input
        if not all(field in data for field in ["workflow_id", "name", "design_thinking_phases", "insights"]):
            return jsonify({"error": ERROR_MISSING_FIELDS}), 400
        
        workflow_id = data["workflow_id"]
        if workflow_id in product_workflows:
            return jsonify({"error": "Workflow ID already exists."}), 400
        
        product_workflows[workflow_id] = {
            "name": data["name"],
            "design_thinking_phases": data["design_thinking_phases"],
            "insights": data["insights"]
        }
        
        return jsonify({"message": "Workflow created successfully.", "workflow": product_workflows[workflow_id]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/workflow/<workflow_id>', methods=['GET'])
def get_workflow(workflow_id):
    """
    Endpoint to retrieve a specific workflow by ID.
    """
    try:
        workflow = product_workflows.get(workflow_id)
        if not workflow:
            return jsonify({"error": ERROR_WORKFLOW_NOT_FOUND}), 404
        
        return jsonify({"workflow": workflow}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/workflow', methods=['GET'])
def list_workflows():
    """
    Endpoint to list all product development workflows.
    """
    try:
        return jsonify({"workflows": product_workflows}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/workflow/<workflow_id>', methods=['PUT'])
def update_workflow(workflow_id):
    """
    Endpoint to update an existing workflow.
    Request JSON format:
    {
        "name": "Updated Workflow Name",
        "design_thinking_phases": ["Updated Phase List"],
        "insights": "Updated insights from TallHills"
    }
    """
    try:
        data = request.json
        workflow = product_workflows.get(workflow_id)
        if not workflow:
            return jsonify({"error": ERROR_WORKFLOW_NOT_FOUND}), 404
        
        # Update fields, if provided
        if "name" in data:
            workflow["name"] = data["name"]
        if "design_thinking_phases" in data:
            workflow["design_thinking_phases"] = data["design_thinking_phases"]
        if "insights" in data:
            workflow["insights"] = data["insights"]
        
        return jsonify({"message": "Workflow updated successfully.", "workflow": workflow}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/workflow/<workflow_id>', methods=['DELETE'])
def delete_workflow(workflow_id):
    """
    Endpoint to delete a workflow by ID.
    """
    try:
        if workflow_id not in product_workflows:
            return jsonify({"error": ERROR_WORKFLOW_NOT_FOUND}), 404
        
        del product_workflows[workflow_id]
        return jsonify({"message": "Workflow deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Application entry point
if __name__ == "__main__":
    """
    Run the Flask application.
    """
    app.run(debug=True)
```
