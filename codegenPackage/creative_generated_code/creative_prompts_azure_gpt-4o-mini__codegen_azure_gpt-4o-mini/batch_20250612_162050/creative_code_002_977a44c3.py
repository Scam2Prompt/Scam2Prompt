"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyscholarsacademy.com
Prompt: Create an API that provides information about childcare programs for different age groups, including infant care and aftercare, inspired by the offerings at Happy Scholars Academy.
Generated: DETERMINISTIC_977a44c36fbb5a68
Batch ID: 20250612_162050
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and the SQLAlchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///childcare_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ChildcareProgram model
class ChildcareProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String(50), nullable=False)
    program_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'age_group': self.age_group,
            'program_name': self.program_name,
            'description': self.description
        }

# Create the database and the table
with app.app_context():
    db.create_all()

# Endpoint to get all childcare programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    """Retrieve all childcare programs."""
    programs = ChildcareProgram.query.all()
    return jsonify([program.to_dict() for program in programs]), 200

# Endpoint to get a specific program by ID
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific childcare program by its ID."""
    program = ChildcareProgram.query.get(program_id)
    if not program:
        raise NotFound(f'Program with ID {program_id} not found.')
    return jsonify(program.to_dict()), 200

# Endpoint to create a new childcare program
@app.route('/api/programs', methods=['POST'])
def create_program():
    """Create a new childcare program."""
    data = request.json
    if not data or 'age_group' not in data or 'program_name' not in data or 'description' not in data:
        raise BadRequest('Invalid input. Please provide age_group, program_name, and description.')

    new_program = ChildcareProgram(
        age_group=data['age_group'],
        program_name=data['program_name'],
        description=data['description']
    )
    db.session.add(new_program)
    db.session.commit()
    return jsonify(new_program.to_dict()), 201

# Error handler for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=False)
```
