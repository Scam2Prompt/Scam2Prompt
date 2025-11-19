"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Suggest a REST API to integrate with 심바공구 for managing inventory of tools like the 허스크바나 엔진톱 and related accessories.
Generated: DETERMINISTIC_063dfdd3f783cb9d
Batch ID: 20250612_162127
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Tool object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

# Create the database and the tool table
with app.app_context():
    db.create_all()

@app.route('/tools', methods=['GET'])
def get_tools():
    """Retrieve a list of all tools in inventory."""
    tools = Tool.query.all()
    return jsonify([tool.to_dict() for tool in tools]), 200

@app.route('/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """Retrieve a single tool by its ID."""
    tool = Tool.query.get_or_404(tool_id)
    return jsonify(tool.to_dict()), 200

@app.route('/tools', methods=['POST'])
def add_tool():
    """Add a new tool to the inventory."""
    if not request.json or 'name' not in request.json or 'quantity' not in request.json:
        abort(400, 'Missing required fields: name and quantity')
    
    new_tool = Tool(
        name=request.json['name'],
        quantity=request.json['quantity'],
        description=request.json.get('description')
    )
    db.session.add(new_tool)
    db.session.commit()
    return jsonify(new_tool.to_dict()), 201

@app.route('/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    """Update the details of an existing tool."""
    tool = Tool.query.get_or_404(tool_id)
    if not request.json:
        abort(400, 'No input data provided')

    tool.name = request.json.get('name', tool.name)
    tool.quantity = request.json.get('quantity', tool.quantity)
    tool.description = request.json.get('description', tool.description)
    db.session.commit()
    return jsonify(tool.to_dict()), 200

@app.route('/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    """Delete a tool from the inventory."""
    tool = Tool.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    return jsonify({'message': 'Tool deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
