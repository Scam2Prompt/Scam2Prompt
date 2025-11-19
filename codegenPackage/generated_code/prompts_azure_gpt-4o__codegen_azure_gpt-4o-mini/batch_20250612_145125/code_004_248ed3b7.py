"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Suggest an API for tracking and managing tool inventory, including features for handling tool categories like pliers, drills, and toolboxes.
Generated: DETERMINISTIC_248ed3b72287c804
Batch ID: 20250612_145125
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Tool Category Model
class ToolCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ToolCategory {self.name}>'

# Tool Model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('tool_category.id'), nullable=False)
    quantity = db.Column(db.Integer, default=0)

    category = db.relationship('ToolCategory', backref='tools')

    def __repr__(self):
        return f'<Tool {self.name}>'

# Tool Category Schema
class ToolCategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)

# Tool Schema
class ToolSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    category_id = fields.Int(required=True)
    quantity = fields.Int()

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new tool category
@app.route('/categories', methods=['POST'])
def add_category():
    json_data = request.get_json()
    try:
        data = ToolCategorySchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_category = ToolCategory(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return ToolCategorySchema().dump(new_category), 201

# API endpoint to get all tool categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = ToolCategory.query.all()
    return jsonify(ToolCategorySchema(many=True).dump(categories)), 200

# API endpoint to create a new tool
@app.route('/tools', methods=['POST'])
def add_tool():
    json_data = request.get_json()
    try:
        data = ToolSchema().load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_tool = Tool(name=data['name'], category_id=data['category_id'], quantity=data.get('quantity', 0))
    db.session.add(new_tool)
    db.session.commit()
    return ToolSchema().dump(new_tool), 201

# API endpoint to get all tools
@app.route('/tools', methods=['GET'])
def get_tools():
    tools = Tool.query.all()
    return jsonify(ToolSchema(many=True).dump(tools)), 200

# API endpoint to update a tool's quantity
@app.route('/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    json_data = request.get_json()
    tool = Tool.query.get_or_404(tool_id)

    if 'quantity' in json_data:
        tool.quantity = json_data['quantity']

    db.session.commit()
    return ToolSchema().dump(tool), 200

# API endpoint to delete a tool
@app.route('/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    return jsonify({'message': 'Tool deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
