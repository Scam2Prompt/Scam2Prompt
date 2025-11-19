"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Create a RESTful API endpoint that allows users to add and retrieve tools from a collection, referencing specific tools like "caixa de ferramentas" and "ferramentas plumo."
Generated: DETERMINISTIC_0050a03139bf828b
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

# Initialize the database
db = SQLAlchemy(app)

# Define the Tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Tool object to a dictionary."""
        return {'id': self.id, 'name': self.name}

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tools', methods=['POST'])
def add_tool():
    """Add a new tool to the collection."""
    data = request.get_json()
    
    if not data or 'name' not in data:
        abort(400, description="Invalid input: 'name' is required.")
    
    new_tool = Tool(name=data['name'])
    
    try:
        db.session.add(new_tool)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"Error adding tool: {str(e)}")
    
    return jsonify(new_tool.to_dict()), 201

@app.route('/tools', methods=['GET'])
def get_tools():
    """Retrieve all tools from the collection."""
    tools = Tool.query.all()
    return jsonify([tool.to_dict() for tool in tools]), 200

@app.route('/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """Retrieve a specific tool by its ID."""
    tool = Tool.query.get(tool_id)
    
    if tool is None:
        abort(404, description="Tool not found.")
    
    return jsonify(tool.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)
```
