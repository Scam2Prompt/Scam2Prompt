"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Create a RESTful API endpoint that allows users to add and retrieve tools from a collection, referencing specific tools like "caixa de ferramentas" and "ferramentas plumo."
Generated: DETERMINISTIC_0050a03139bf828b
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
        return {"id": self.id, "name": self.name}

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tools', methods=['POST'])
def add_tool():
    """Endpoint to add a new tool."""
    data = request.json
    if not data or 'name' not in data:
        abort(400, description="Bad Request: 'name' is required.")
    
    new_tool = Tool(name=data['name'])
    
    try:
        db.session.add(new_tool)
        db.session.commit()
        return jsonify(new_tool.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"Internal Server Error: {str(e)}")

@app.route('/tools', methods=['GET'])
def get_tools():
    """Endpoint to retrieve all tools."""
    try:
        tools = Tool.query.all()
        return jsonify([tool.to_dict() for tool in tools]), 200
    except Exception as e:
        abort(500, description=f"Internal Server Error: {str(e)}")

@app.route('/tools/<int:tool_id>', methods=['GET'])
def get_tool(tool_id):
    """Endpoint to retrieve a specific tool by ID."""
    tool = Tool.query.get(tool_id)
    if not tool:
        abort(404, description="Not Found: Tool does not exist.")
    
    return jsonify(tool.to_dict()), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
