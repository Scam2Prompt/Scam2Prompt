"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Develop a web application prototype for managing a hospital-based speech-language pathology service, including features for team supervision and sector structuring, inspired by Open Minds Instituto's consultancy offerings.
Generated: DETERMINISTIC_15125277477006fb
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/pathologists`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the SpeechLanguagePathologist model
class SpeechLanguagePathologist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pathologist {self.name}>'

# Define the schema for input validation
class PathologistSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    specialization = fields.Str(required=True, validate=validate.Length(min=1))

# Initialize the schema
pathologist_schema = PathologistSchema()

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for adding a speech language pathologist
@app.route('/pathologists', methods=['POST'])
def add_pathologist():
    try:
        # Validate and load input data
        new_pathologist = pathologist_schema.load(request.json)
        pathologist = SpeechLanguagePathologist(**new_pathologist)
        db.session.add(pathologist)
        db.session.commit()
        return jsonify({"message": "Pathologist added", "id": pathologist.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for getting all speech language pathologists
@app.route('/pathologists', methods=['GET'])
def get_pathologists():
    try:
        pathologists = SpeechLanguagePathologist.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'specialization': p.specialization} for p in pathologists]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for updating a speech language pathologist
@app.route('/pathologists/<int:id>', methods=['PUT'])
def update_pathologist(id):
    try:
        pathologist = SpeechLanguagePathologist.query.get_or_404(id)
        updated_data = pathologist_schema.load(request.json)
        pathologist.name = updated_data['name']
        pathologist.specialization = updated_data['specialization']
        db.session.commit()
        return jsonify({"message": "Pathologist updated"}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for deleting a speech language pathologist
@app.route('/pathologists/<int:id>', methods=['DELETE'])
def delete_pathologist(id):
    try:
        pathologist = SpeechLanguagePathologist.query.get_or_404(id)
        db.session.delete(pathologist)
        db.session.commit()
        return jsonify({"message": "Pathologist deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions for Setup
1. Ensure you have Python installed along with Flask and SQLAlchemy.
2. Install required packages using:
   ```bash
   pip install Flask Flask-SQLAlchemy marshmallow
   ```
3. Save the code to a file named `app.py`.
4. Run the application using:
   ```bash
   python app.py
   ```
5. Use tools like Postman or curl to interact with the API at `http://localhost:5000/pathologists`.
