"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: Suggest an API for integrating vocational guidance tools into an HR platform, similar to the "Orientación Vocacional-Ocupacional" services offered by Search HR.
Generated: DETERMINISTIC_6ed133004e8faefa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vocational_guidance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for vocational guidance tools
class VocationalTool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Create a schema for input validation
class VocationalToolSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    category = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# API endpoint to create a new vocational guidance tool
@app.route('/api/tools', methods=['POST'])
def create_tool():
    """Create a new vocational guidance tool."""
    schema = VocationalToolSchema()
    try:
        # Validate and deserialize input data
        tool_data = schema.load(request.json)
        new_tool = VocationalTool(**tool_data)
        db.session.add(new_tool)
        db.session.commit()
        return jsonify({"message": "Tool created successfully", "tool": tool_data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all vocational guidance tools
@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Retrieve all vocational guidance tools."""
    try:
        tools = VocationalTool.query.all()
        tool_schema = VocationalToolSchema(many=True)
        return jsonify(tool_schema.dump(tools)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific vocational guidance tool by ID
@app.route('/api/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """Retrieve a specific vocational guidance tool by ID."""
    try:
        tool = VocationalTool.query.get_or_404(tool_id)
        tool_schema = VocationalToolSchema()
        return jsonify(tool_schema.dump(tool)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a vocational guidance tool
@app.route('/api/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    """Update an existing vocational guidance tool."""
    schema = VocationalToolSchema()
    try:
        tool = VocationalTool.query.get_or_404(tool_id)
        tool_data = schema.load(request.json)
        for key, value in tool_data.items():
            setattr(tool, key, value)
        db.session.commit()
        return jsonify({"message": "Tool updated successfully", "tool": tool_data}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a vocational guidance tool
@app.route('/api/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    """Delete a vocational guidance tool."""
    try:
        tool = VocationalTool.query.get_or_404(tool_id)
        db.session.delete(tool)
        db.session.commit()
        return jsonify({"message": "Tool deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
