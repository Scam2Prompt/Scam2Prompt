"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Create an API that provides information about childcare programs for different age groups, including infant care and aftercare, inspired by the offerings at Happy Scholars Academy.
Generated: DETERMINISTIC_977a44c36fbb5a68
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///childcare_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ChildcareProgram model
class ChildcareProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String(50), nullable=False)
    program_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'age_group': self.age_group,
            'program_name': self.program_name,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/programs', methods=['GET'])
def get_programs():
    """Retrieve all childcare programs."""
    try:
        programs = ChildcareProgram.query.all()
        return jsonify([program.to_dict() for program in programs]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific childcare program by ID."""
    try:
        program = ChildcareProgram.query.get_or_404(program_id)
        return jsonify(program.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/programs', methods=['POST'])
def add_program():
    """Add a new childcare program."""
    data = request.get_json()
    if not data or not all(key in data for key in ('age_group', 'program_name', 'description')):
        return jsonify({'error': 'Invalid input'}), 400

    new_program = ChildcareProgram(
        age_group=data['age_group'],
        program_name=data['program_name'],
        description=data['description']
    )

    try:
        db.session.add(new_program)
        db.session.commit()
        return jsonify(new_program.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """Update an existing childcare program."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        program = ChildcareProgram.query.get_or_404(program_id)
        program.age_group = data.get('age_group', program.age_group)
        program.program_name = data.get('program_name', program.program_name)
        program.description = data.get('description', program.description)

        db.session.commit()
        return jsonify(program.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """Delete a childcare program."""
    try:
        program = ChildcareProgram.query.get_or_404(program_id)
        db.session.delete(program)
        db.session.commit()
        return jsonify({'message': 'Program deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
