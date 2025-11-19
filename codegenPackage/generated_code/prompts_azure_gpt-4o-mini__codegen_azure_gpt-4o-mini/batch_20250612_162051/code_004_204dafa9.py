"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Create a REST API that facilitates communication between different public sector departments, leveraging Licitare's solutions in T.I and system development.
Generated: DETERMINISTIC_204dafa95adb8881
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///departments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Department model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new department
@app.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_department = Department(name=data['name'], description=data.get('description'))
    try:
        db.session.add(new_department)
        db.session.commit()
        return jsonify(new_department.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error creating department: {e}")
        return jsonify({'error': 'Database error'}), 500

# Route to get all departments
@app.route('/departments', methods=['GET'])
def get_departments():
    try:
        departments = Department.query.all()
        return jsonify([dept.to_dict() for dept in departments]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error fetching departments: {e}")
        return jsonify({'error': 'Database error'}), 500

# Route to get a specific department by ID
@app.route('/departments/<int:dept_id>', methods=['GET'])
def get_department(dept_id):
    try:
        department = Department.query.get_or_404(dept_id)
        return jsonify(department.to_dict()), 200
    except SQLAlchemyError as e:
        logging.error(f"Error fetching department {dept_id}: {e}")
        return jsonify({'error': 'Database error'}), 500

# Route to update a department
@app.route('/departments/<int:dept_id>', methods=['PUT'])
def update_department(dept_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        department = Department.query.get_or_404(dept_id)
        department.name = data.get('name', department.name)
        department.description = data.get('description', department.description)
        db.session.commit()
        return jsonify(department.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error updating department {dept_id}: {e}")
        return jsonify({'error': 'Database error'}), 500

# Route to delete a department
@app.route('/departments/<int:dept_id>', methods=['DELETE'])
def delete_department(dept_id):
    try:
        department = Department.query.get_or_404(dept_id)
        db.session.delete(department)
        db.session.commit()
        return jsonify({'message': 'Department deleted'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Error deleting department {dept_id}: {e}")
        return jsonify({'error': 'Database error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
