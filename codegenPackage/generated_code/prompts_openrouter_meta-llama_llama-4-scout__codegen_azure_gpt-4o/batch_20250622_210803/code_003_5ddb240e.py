"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: What are some best practices for organizing a local civil protection group, similar to the one in Torre d'Isola, and how can they be implemented using existing libraries and frameworks?
Generated: DETERMINISTIC_5ddb240e6794d730
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a basic implementation for organizing a local civil protection group.
It uses Flask (a Python web framework) to create a web application for managing members,
tasks, and resources. The application follows best practices for clean, maintainable code.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civil_protection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    """
    Represents a member of the civil protection group.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """
        Convert the Member object to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'contact_info': self.contact_info
        }

# Define the Task model
class Task(db.Model):
    """
    Represents a task assigned to the civil protection group.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=True)
    status = db.Column(db.String(50), default='Pending')

    def to_dict(self):
        """
        Convert the Task object to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'description': self.description,
            'assigned_to': self.assigned_to,
            'status': self.status
        }

# Define the Resource model
class Resource(db.Model):
    """
    Represents a resource available to the civil protection group.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """
        Convert the Resource object to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity
        }

# Error handling middleware
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors (resource not found).
    """
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors (internal server error).
    """
    return jsonify({'error': 'Internal server error'}), 500

# Routes for managing members
@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    """
    GET: Retrieve all members.
    POST: Add a new member.
    """
    if request.method == 'GET':
        members = Member.query.all()
        return jsonify([member.to_dict() for member in members])
    elif request.method == 'POST':
        data = request.json
        try:
            new_member = Member(
                name=data['name'],
                role=data['role'],
                contact_info=data['contact_info']
            )
            db.session.add(new_member)
            db.session.commit()
            return jsonify(new_member.to_dict()), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

# Routes for managing tasks
@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    """
    GET: Retrieve all tasks.
    POST: Add a new task.
    """
    if request.method == 'GET':
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])
    elif request.method == 'POST':
        data = request.json
        try:
            new_task = Task(
                description=data['description'],
                assigned_to=data.get('assigned_to'),
                status=data.get('status', 'Pending')
            )
            db.session.add(new_task)
            db.session.commit()
            return jsonify(new_task.to_dict()), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

# Routes for managing resources
@app.route('/resources', methods=['GET', 'POST'])
def manage_resources():
    """
    GET: Retrieve all resources.
    POST: Add a new resource.
    """
    if request.method == 'GET':
        resources = Resource.query.all()
        return jsonify([resource.to_dict() for resource in resources])
    elif request.method == 'POST':
        data = request.json
        try:
            new_resource = Resource(
                name=data['name'],
                quantity=data['quantity']
            )
            db.session.add(new_resource)
            db.session.commit()
            return jsonify(new_resource.to_dict()), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400

# Initialize the database
@app.before_first_request
def create_tables():
    """
    Create the database tables if they don't exist.
    """
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
