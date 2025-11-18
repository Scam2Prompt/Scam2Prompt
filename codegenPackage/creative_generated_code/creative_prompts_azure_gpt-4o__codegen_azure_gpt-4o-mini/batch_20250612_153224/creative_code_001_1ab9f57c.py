"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Develop an API endpoint that allows users to query details about community treatment programs, including methodologies like ECO 2, as described on Fundación Munasim Kullakita's platform.
Generated: DETERMINISTIC_1ab9f57cfd3bb7c8
Batch ID: 20250612_153224
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

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model representing a community treatment program
class TreatmentProgram(db.Model):
    __tablename__ = 'treatment_programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    methodology = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        """Convert the TreatmentProgram object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'methodology': self.methodology,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/treatment-programs', methods=['GET'])
def get_treatment_programs():
    """API endpoint to retrieve treatment programs based on query parameters."""
    methodology = request.args.get('methodology')

    try:
        # Query the database for treatment programs
        if methodology:
            programs = TreatmentProgram.query.filter_by(methodology=methodology).all()
        else:
            programs = TreatmentProgram.query.all()

        # Convert the programs to a list of dictionaries
        programs_list = [program.to_dict() for program in programs]

        return jsonify(programs_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database query failed', 'message': str(e)}), 500

@app.route('/api/treatment-programs/<int:program_id>', methods=['GET'])
def get_treatment_program(program_id):
    """API endpoint to retrieve a specific treatment program by its ID."""
    try:
        program = TreatmentProgram.query.get(program_id)

        if not program:
            return jsonify({'error': 'Program not found'}), 404

        return jsonify(program.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database query failed', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
