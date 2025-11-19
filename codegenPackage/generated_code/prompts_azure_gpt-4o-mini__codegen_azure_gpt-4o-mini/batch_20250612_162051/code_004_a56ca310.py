"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TrainingProgram model
class TrainingProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    objectives = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<TrainingProgram {self.name}>'

# Define the schema for input validation
class TrainingProgramSchema(Schema):
    name = fields.Str(required=True)
    duration = fields.Str(required=True)
    objectives = fields.Str(required=True)

# Initialize the schema
training_program_schema = TrainingProgramSchema()
training_programs_schema = TrainingProgramSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new training program
@app.route('/training_programs', methods=['POST'])
def create_training_program():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        training_program = training_program_schema.load(data)

        # Create a new TrainingProgram instance
        new_program = TrainingProgram(**training_program)
        db.session.add(new_program)
        db.session.commit()

        return jsonify(training_program_schema.dump(new_program)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all training programs
@app.route('/training_programs', methods=['GET'])
def get_training_programs():
    try:
        programs = TrainingProgram.query.all()
        return jsonify(training_programs_schema.dump(programs)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific training program by ID
@app.route('/training_programs/<int:id>', methods=['GET'])
def get_training_program(id):
    try:
        program = TrainingProgram.query.get_or_404(id)
        return jsonify(training_program_schema.dump(program)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a training program
@app.route('/training_programs/<int:id>', methods=['PUT'])
def update_training_program(id):
    try:
        program = TrainingProgram.query.get_or_404(id)
        data = request.get_json()
        updated_program = training_program_schema.load(data)

        # Update the program's attributes
        for key, value in updated_program.items():
            setattr(program, key, value)

        db.session.commit()
        return jsonify(training_program_schema.dump(program)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a training program
@app.route('/training_programs/<int:id>', methods=['DELETE'])
def delete_training_program(id):
    try:
        program = TrainingProgram.query.get_or_404(id)
        db.session.delete(program)
        db.session.commit()
        return jsonify({"message": "Training program deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
