"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate a code snippet for a tool management API that includes functionalities for tracking inventory of tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_012f6651a8204dcb
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Tool
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Tool object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/tools', methods=['GET'])
def get_tools():
    """Retrieve a list of all tools in the inventory."""
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
    if not request.json or 'name' not in request.json or 'quantity' not in request.json:
        abort(400, description="Invalid input")
    
    new_tool = Tool(name=request.json['name'], quantity=request.json['quantity'])
    db.session.add(new_tool)
    db.session.commit()
    return jsonify(new_tool.to_dict()), 201

@app.route('/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    """Update an existing tool's quantity."""
    tool = Tool.query.get(tool_id)
    if tool is None:
        abort(404, description="Tool not found")
    
    if not request.json or 'quantity' not in request.json:
        abort(400, description="Invalid input")
    
    tool.quantity = request.json['quantity']
    db.session.commit()
    return jsonify(tool.to_dict()), 200

@app.route('/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    """Remove a tool from the inventory."""
    tool = Tool.query.get(tool_id)
    if tool is None:
        abort(404, description="Tool not found")
    
    db.session.delete(tool)
    db.session.commit()
    return jsonify({'result': True}), 204

if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to install Flask and Flask-SQLAlchemy before running the application:

```bash
pip install Flask Flask-SQLAlchemy
```
