"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Suggest an API for tracking and managing tool inventory, including features for handling tool categories like pliers, drills, and toolboxes.
Generated: DETERMINISTIC_248ed3b72287c804
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Tool Category
class ToolCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    tools = db.relationship('Tool', backref='category', lazy=True)

# Model for Tool
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('tool_category.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new tool category
@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = ToolCategory(name=data['name'])
    try:
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created', 'category': new_category.name}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating category', 'error': str(e)}), 400

# API endpoint to list all tool categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = ToolCategory.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories]), 200

# API endpoint to add a new tool
@app.route('/tools', methods=['POST'])
def add_tool():
    data = request.get_json()
    new_tool = Tool(name=data['name'], quantity=data['quantity'], category_id=data['category_id'])
    try:
        db.session.add(new_tool)
        db.session.commit()
        return jsonify({'message': 'Tool added', 'tool': new_tool.name}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Error adding tool', 'error': str(e)}), 400

# API endpoint to list all tools
@app.route('/tools', methods=['GET'])
def get_tools():
    tools = Tool.query.all()
    return jsonify([{'id': tool.id, 'name': tool.name, 'quantity': tool.quantity, 'category_id': tool.category_id} for tool in tools]), 200

# API endpoint to update tool quantity
@app.route('/tools/<int:tool_id>', methods=['PUT'])
def update_tool(tool_id):
    data = request.get_json()
    tool = Tool.query.get_or_404(tool_id)
    tool.quantity = data['quantity']
    try:
        db.session.commit()
        return jsonify({'message': 'Tool quantity updated', 'tool': tool.name, 'quantity': tool.quantity}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating tool', 'error': str(e)}), 400

# API endpoint to delete a tool
@app.route('/tools/<int:tool_id>', methods=['DELETE'])
def delete_tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    try:
        db.session.delete(tool)
        db.session.commit()
        return jsonify({'message': 'Tool deleted'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'message': 'Error deleting tool', 'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
