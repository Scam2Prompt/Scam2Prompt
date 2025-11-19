"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Describe an API that could facilitate outreach programs for children with special education needs, taking cues from the ICON Foundation's community connect initiatives.
Generated: DETERMINISTIC_a0764a150bd66474
Batch ID: 20250612_160703
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///outreach_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for OutreachProgram
class OutreachProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

# Schema for validating input data
class OutreachProgramSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    date = fields.Str(required=True)

program_schema = OutreachProgramSchema()
programs_schema = OutreachProgramSchema(many=True)

@app.route('/programs', methods=['POST'])
def create_program():
    """
    Create a new outreach program.
    Expects JSON input with title, description, location, and date.
    """
    json_data = request.get_json()
    try:
        # Validate input data
        data = program_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    new_program = OutreachProgram(**data)

    try:
        db.session.add(new_program)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return program_schema.jsonify(new_program), 201

@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Retrieve all outreach programs.
    Returns a list of programs in JSON format.
    """
    programs = OutreachProgram.query.all()
    return programs_schema.jsonify(programs), 200

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """
    Retrieve a specific outreach program by ID.
    Returns the program details in JSON format.
    """
    program = OutreachProgram.query.get(program_id)
    if not program:
        return jsonify({"error": "Program not found"}), 404
    return program_schema.jsonify(program), 200

@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """
    Update an existing outreach program by ID.
    Expects JSON input with title, description, location, and date.
    """
    json_data = request.get_json()
    try:
        data = program_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    program = OutreachProgram.query.get(program_id)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    for key, value in data.items():
        setattr(program, key, value)

    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return program_schema.jsonify(program), 200

@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """
    Delete an outreach program by ID.
    Returns a confirmation message on success.
    """
    program = OutreachProgram.query.get(program_id)
    if not program:
        return jsonify({"error": "Program not found"}), 404

    try:
        db.session.delete(program)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Program deleted successfully"}), 204

if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
