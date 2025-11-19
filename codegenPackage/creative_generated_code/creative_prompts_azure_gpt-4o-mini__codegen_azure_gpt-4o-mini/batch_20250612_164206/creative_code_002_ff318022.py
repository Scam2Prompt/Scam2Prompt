"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Create a REST API endpoint for managing academic programs at SMKN 1 Kadipaten, including features for adding, updating, and retrieving program details.
Generated: DETERMINISTIC_ff31802238eb700d
Batch ID: 20250612_164206
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Academic Program
class AcademicProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create the database and the tables
with app.app_context():
    db.create_all()

@app.route('/programs', methods=['GET'])
def get_programs():
    """Retrieve all academic programs."""
    programs = AcademicProgram.query.all()
    return jsonify([program.to_dict() for program in programs]), 200

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific academic program by ID."""
    program = AcademicProgram.query.get_or_404(program_id)
    return jsonify(program.to_dict()), 200

@app.route('/programs', methods=['POST'])
def add_program():
    """Add a new academic program."""
    data = request.json
    if 'name' not in data:
        abort(400, 'Name is required.')

    new_program = AcademicProgram(name=data['name'], description=data.get('description'))

    try:
        db.session.add(new_program)
        db.session.commit()
        return jsonify(new_program.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Program with this name already exists.')

@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """Update an existing academic program."""
    program = AcademicProgram.query.get_or_404(program_id)
    data = request.json

    if 'name' in data:
        program.name = data['name']
    if 'description' in data:
        program.description = data.get('description')

    db.session.commit()
    return jsonify(program.to_dict()), 200

@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """Delete an academic program by ID."""
    program = AcademicProgram.query.get_or_404(program_id)
    db.session.delete(program)
    db.session.commit()
    return jsonify({'message': 'Program deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
