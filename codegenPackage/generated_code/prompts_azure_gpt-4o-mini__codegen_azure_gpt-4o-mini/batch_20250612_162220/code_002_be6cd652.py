"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Create a REST API endpoint that provides information about the academic and cultural training programs offered by the Escuela de Suboficiales de la Fuerza Aérea del Perú.
Generated: DETERMINISTIC_be6cd65202c0f67a
Batch ID: 20250612_162220
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Program model
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'Academic', 'Cultural'

    def to_dict(self):
        """Convert the Program object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/programs', methods=['GET'])
def get_programs():
    """Retrieve all training programs."""
    try:
        programs = Program.query.all()
        return jsonify([program.to_dict() for program in programs]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific training program by ID."""
    try:
        program = Program.query.get_or_404(program_id)
        return jsonify(program.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/programs', methods=['POST'])
def create_program():
    """Create a new training program."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'type')):
        return jsonify({'error': 'Invalid input'}), 400

    new_program = Program(name=data['name'], description=data['description'], type=data['type'])
    
    try:
        db.session.add(new_program)
        db.session.commit()
        return jsonify(new_program.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """Update an existing training program."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    program = Program.query.get_or_404(program_id)
    
    program.name = data.get('name', program.name)
    program.description = data.get('description', program.description)
    program.type = data.get('type', program.type)

    try:
        db.session.commit()
        return jsonify(program.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """Delete a training program."""
    program = Program.query.get_or_404(program_id)

    try:
        db.session.delete(program)
        db.session.commit()
        return jsonify({'message': 'Program deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
