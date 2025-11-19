"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: "Create a RESTful API to manage orders and projects for a company like Aluivars that specializes in metalwork, aluminum carpentry, and glasswork."
Generated: DETERMINISTIC_4ff5aa8d271da2cb
Batch ID: 20250622_210655
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

# Create a schema for validation using Marshmallow
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    project_name = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    status = fields.Str(required=True)

class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    order_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# RESTful API for Orders
@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order."""
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()
        return order_schema.dump(new_order), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders."""
    orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    return jsonify(order_schema.dump(orders)), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve a specific order by ID."""
    order = Order.query.get_or_404(order_id)
    order_schema = OrderSchema()
    return jsonify(order_schema.dump(order)), 200

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an existing order."""
    order = Order.query.get_or_404(order_id)
    order_schema = OrderSchema()
    try:
        order_data = order_schema.load(request.json)
        for key, value in order_data.items():
            setattr(order, key, value)
        db.session.commit()
        return order_schema.dump(order), 200
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order."""
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 204

# RESTful API for Projects
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    project_schema = ProjectSchema()
    try:
        project_data = project_schema.load(request.json)
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    projects = Project.query.all()
    project_schema = ProjectSchema(many=True)
    return jsonify(project_schema.dump(projects)), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    project_schema = ProjectSchema()
    return jsonify(project_schema.dump(project)), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing project."""
    project = Project.query.get_or_404(project_id)
    project_schema = ProjectSchema()
    try:
        project_data = project_schema.load(request.json)
        for key, value in project_data.items():
            setattr(project, key, value)
        db.session.commit()
        return project_schema.dump(project), 200
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
