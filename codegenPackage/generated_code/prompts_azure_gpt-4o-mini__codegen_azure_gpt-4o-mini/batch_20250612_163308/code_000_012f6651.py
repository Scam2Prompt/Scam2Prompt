"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate a code snippet for a tool management API that includes functionalities for tracking inventory of tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_012f6651a8204dcb
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Tool object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/tools', methods=['GET'])
def get_tools():
    """Retrieve all tools in the inventory."""
    tools = Tool.query.all()
    return jsonify([tool.to_dict() for tool in tools]), 200

@app.route('/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """Retrieve a specific tool by its ID."""
    tool = Tool.query.get(tool_id)
    if tool is None:
        abort(404, description="Tool not found")
    return jsonify(tool.to_dict()), 200

@app.route('/tools', methods=['POST'])
def add_tool():
    """Add a new tool to the inventory."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid input data")
    
    new_tool = Tool(name=data['name'], quantity=data['quantity'])
    db.session.add(new_tool)
    db.session.commit()
    return jsonify(new_tool.to_dict()), 201

@app.route('/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    """Update the details of an existing tool."""
    tool = Tool.query.get(tool_id)
    if tool is None:
        abort(404, description="Tool not found")
    
    data = request.get_json()
    if 'name' in data:
        tool.name = data['name']
    if 'quantity' in data:
        tool.quantity = data['quantity']
    
    db.session.commit()
    return jsonify(tool.to_dict()), 200

@app.route('/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    """Delete a tool from the inventory."""
    tool = Tool.query.get(tool_id)
    if tool is None:
        abort(404, description="Tool not found")
    
    db.session.delete(tool)
    db.session.commit()
    return jsonify({'message': 'Tool deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
