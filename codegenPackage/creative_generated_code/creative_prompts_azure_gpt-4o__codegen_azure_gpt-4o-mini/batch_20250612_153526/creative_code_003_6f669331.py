"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Create a web application that supports international vocational education programs, including features for micro-credentials and joint education programs, as detailed on the AVEA website.
Generated: DETERMINISTIC_6f66933131f8f472
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web application
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Education Program model
class EducationProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'micro-credential', 'joint program'
    description = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(50), nullable=True)

    def __init__(self, name, type, description, country):
        self.name = name
        self.type = type
        self.description = description
        self.country = country

# Define the schema for serialization
class EducationProgramSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EducationProgram

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new education program
@app.route('/programs', methods=['POST'])
def add_program():
    try:
        data = request.get_json()
        name = data.get('name')
        program_type = data.get('type')
        description = data.get('description')
        country = data.get('country')

        # Validate input
        if not name or not program_type:
            raise BadRequest("Name and type are required fields.")

        # Create a new education program
        new_program = EducationProgram(name=name, type=program_type, description=description, country=country)
        db.session.add(new_program)
        db.session.commit()

        return EducationProgramSchema().jsonify(new_program), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all education programs
@app.route('/programs', methods=['GET'])
def get_programs():
    try:
        programs = EducationProgram.query.all()
        return EducationProgramSchema(many=True).jsonify(programs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a specific education program by ID
@app.route('/programs/<int:id>', methods=['GET'])
def get_program(id):
    try:
        program = EducationProgram.query.get_or_404(id)
        return EducationProgramSchema().jsonify(program), 200
    except NotFound:
        return jsonify({"error": "Program not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an education program
@app.route('/programs/<int:id>', methods=['PUT'])
def update_program(id):
    try:
        program = EducationProgram.query.get_or_404(id)
        data = request.get_json()

        # Update the program's fields
        program.name = data.get('name', program.name)
        program.type = data.get('type', program.type)
        program.description = data.get('description', program.description)
        program.country = data.get('country', program.country)

        db.session.commit()
        return EducationProgramSchema().jsonify(program), 200

    except NotFound:
        return jsonify({"error": "Program not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete an education program
@app.route('/programs/<int:id>', methods=['DELETE'])
def delete_program(id):
    try:
        program = EducationProgram.query.get_or_404(id)
        db.session.delete(program)
        db.session.commit()
        return jsonify({"message": "Program deleted successfully."}), 204

    except NotFound:
        return jsonify({"error": "Program not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
