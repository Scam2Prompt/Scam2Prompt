"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Create a REST API endpoint that provides information about the academic and cultural training programs offered by the Escuela de Suboficiales de la Fuerza Aérea del Perú.
Generated: DETERMINISTIC_be6cd65202c0f67a
Batch ID: 20250612_162220
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
from werkzeug.exceptions import NotFound, InternalServerError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (ensure to set your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Program model
class Program(db.Model):
    __tablename__ = 'programs'
    
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
@app.before_first_request
def create_tables():
    db.create_all()

# REST API endpoint to get all programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    """Retrieve all training programs."""
    try:
        programs = Program.query.all()
        return jsonify([program.to_dict() for program in programs]), 200
    except Exception as e:
        # Log the error here if needed
        raise InternalServerError("An error occurred while retrieving programs.") from e

# REST API endpoint to get a program by id
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific training program by ID."""
    try:
        program = Program.query.get(program_id)
        if program is None:
            raise NotFound("Program not found.")
        return jsonify(program.to_dict()), 200
    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # Log the error here if needed
        raise InternalServerError("An error occurred while retrieving the program.") from e

# Error handler for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

# Error handler for InternalServerError
@app.errorhandler(InternalServerError)
def handle_internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to install the required libraries (`Flask` and `Flask-SQLAlchemy`) before running the application:

```bash
pip install Flask Flask-SQLAlchemy
```
