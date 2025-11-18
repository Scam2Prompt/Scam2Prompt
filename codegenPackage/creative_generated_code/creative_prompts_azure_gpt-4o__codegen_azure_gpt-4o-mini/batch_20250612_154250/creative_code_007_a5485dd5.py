"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tari.ee
Prompt: Recommend a software framework for managing architectural consulting workflows, inspired by the services offered on Tari.ee.
Generated: DETERMINISTIC_a5485dd55e3e6238
Batch ID: 20250612_154250
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
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_workflows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Workflow model
class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Workflow {self.name}>'

# Define a schema for serializing Workflow
class WorkflowSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True)

workflow_schema = WorkflowSchema()
workflows_schema = WorkflowSchema(many=True)

# Endpoint to create a new workflow
@app.route('/workflows', methods=['POST'])
def create_workflow():
    try:
        # Validate and deserialize request data
        data = workflow_schema.load(request.json)
        
        # Create and save a new workflow instance
        new_workflow = Workflow(**data)
        db.session.add(new_workflow)
        db.session.commit()
        
        return workflow_schema.jsonify(new_workflow), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all workflows
@app.route('/workflows', methods=['GET'])
def get_workflows():
    try:
        workflows = Workflow.query.all()
        return workflows_schema.jsonify(workflows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a specific workflow
@app.route('/workflows/<int:workflow_id>', methods=['PUT'])
def update_workflow(workflow_id):
    try:
        # Validate and deserialize request data
        data = workflow_schema.load(request.json)
        
        # Find the workflow to update
        workflow = Workflow.query.get_or_404(workflow_id)
        
        # Update the workflow's attributes
        for key, value in data.items():
            setattr(workflow, key, value)
        
        db.session.commit()
        return workflow_schema.jsonify(workflow), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a specific workflow
@app.route('/workflows/<int:workflow_id>', methods=['DELETE'])
def delete_workflow(workflow_id):
    try:
        # Find the workflow to delete
        workflow = Workflow.query.get_or_404(workflow_id)
        db.session.delete(workflow)
        db.session.commit()
        return jsonify({"message": "Workflow deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables before the first request
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
