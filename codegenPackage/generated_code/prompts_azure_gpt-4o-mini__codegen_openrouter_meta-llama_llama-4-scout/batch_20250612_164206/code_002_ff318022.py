"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Create a REST API endpoint for managing academic programs at SMKN 1 Kadipaten, including features for adding, updating, and retrieving program details.
Generated: DETERMINISTIC_ff31802238eb700d
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Academic Program API**
=========================

### Dependencies

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database operations
* `marshmallow`: For serialization and deserialization

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///academic_programs.db"
db = SQLAlchemy(app)


class AcademicProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class AcademicProgramSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(required=True)

    def make_object(self, data, **kwargs):
        return AcademicProgram(**data)


academic_program_schema = AcademicProgramSchema()
academic_programs_schema = AcademicProgramSchema(many=True)


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Add a new academic program
@app.route("/programs", methods=["POST"])
def add_academic_program():
    try:
        data = request.get_json()
        academic_program = academic_program_schema.make_object(data)
        db.session.add(academic_program)
        db.session.commit()
        return academic_program_schema.dump(academic_program), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": "Failed to add program"}), 500


# Get all academic programs
@app.route("/programs", methods=["GET"])
def get_academic_programs():
    try:
        programs = AcademicProgram.query.all()
        return academic_programs_schema.dump(programs), 200
    except Exception as err:
        return jsonify({"error": "Failed to retrieve programs"}), 500


# Get a single academic program by ID
@app.route("/programs/<int:program_id>", methods=["GET"])
def get_academic_program(program_id):
    try:
        program = AcademicProgram.query.get(program_id)
        if program is None:
            return jsonify({"error": "Program not found"}), 404
        return academic_program_schema.dump(program), 200
    except Exception as err:
        return jsonify({"error": "Failed to retrieve program"}), 500


# Update an academic program
@app.route("/programs/<int:program_id>", methods=["PUT"])
def update_academic_program(program_id):
    try:
        program = AcademicProgram.query.get(program_id)
        if program is None:
            return jsonify({"error": "Program not found"}), 404
        data = request.get_json()
        academic_program_schema.load(data, instance=program)
        db.session.commit()
        return academic_program_schema.dump(program), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": "Failed to update program"}), 500


# Delete an academic program
@app.route("/programs/<int:program_id>", methods=["DELETE"])
def delete_academic_program(program_id):
    try:
        program = AcademicProgram.query.get(program_id)
        if program is None:
            return jsonify({"error": "Program not found"}), 404
        db.session.delete(program)
        db.session.commit()
        return jsonify({"message": "Program deleted"}), 200
    except Exception as err:
        db.session.rollback()
        return jsonify({"error": "Failed to delete program"}), 500


if __name__ == "__main__":
    app.run(debug=True)
```
