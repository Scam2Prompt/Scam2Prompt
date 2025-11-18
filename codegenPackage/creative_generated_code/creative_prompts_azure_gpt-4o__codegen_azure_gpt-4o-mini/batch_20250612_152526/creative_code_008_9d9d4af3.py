"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a REST API in Flask for managing institutional data, including endpoints for retrieving information about academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_9d9d4af3c02c7453
Batch ID: 20250612_152526
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

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database (for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///institution_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define model for Academic Programs
class AcademicProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

# Define model for Administrative Services
class AdministrativeService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "details": self.details}

# Define model for Institutional Recognitions
class InstitutionalRecognition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "year": self.year}

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve all academic programs
@app.route('/api/programs', methods=['GET'])
def get_programs():
    try:
        programs = AcademicProgram.query.all()
        return jsonify([program.to_dict() for program in programs]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific academic program by ID
@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    program = AcademicProgram.query.get(program_id)
    if program:
        return jsonify(program.to_dict()), 200
    else:
        return jsonify({"error": "Program not found"}), 404

# Endpoint to retrieve all administrative services
@app.route('/api/services', methods=['GET'])
def get_services():
    try:
        services = AdministrativeService.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all institutional recognitions
@app.route('/api/recognitions', methods=['GET'])
def get_recognitions():
    try:
        recognitions = InstitutionalRecognition.query.all()
        return jsonify([recognition.to_dict() for recognition in recognitions]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- The code sets up a simple REST API using Flask and SQLAlchemy.
- It includes models for academic programs, administrative services, and institutional recognitions.
- Each model has a corresponding endpoint to retrieve data.
- Error handling is implemented for database operations.
- The database is initialized with SQLite for demonstration purposes.
