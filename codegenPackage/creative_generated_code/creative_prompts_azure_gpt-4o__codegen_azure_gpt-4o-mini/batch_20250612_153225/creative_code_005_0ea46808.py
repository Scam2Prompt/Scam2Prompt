"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Suggest an API for implementing expatriate recruitment services, allowing organizations to find and manage international candidates, as highlighted by High Value Staffing.
Generated: DETERMINISTIC_0ea46808538d40e0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expatriates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    country = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(200), nullable=True)

# Define Candidate Schema for validation
class CandidateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    country = fields.String(required=True)
    skills = fields.String()

# Initialize database
with app.app_context():
    db.create_all()

# Create a new candidate endpoint
@app.route('/candidates', methods=['POST'])
def add_candidate():
    """Endpoint to add a new candidate."""
    schema = CandidateSchema()
    try:
        # Validate and deserialize input data
        candidate_data = schema.load(request.json)
        new_candidate = Candidate(**candidate_data)
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify(schema.dump(new_candidate)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all candidates endpoint
@app.route('/candidates', methods=['GET'])
def get_candidates():
    """Endpoint to retrieve all candidates."""
    try:
        candidates = Candidate.query.all()
        schema = CandidateSchema(many=True)
        return jsonify(schema.dump(candidates)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a candidate by ID endpoint
@app.route('/candidates/<int:id>', methods=['GET'])
def get_candidate(id):
    """Endpoint to retrieve a candidate by ID."""
    try:
        candidate = Candidate.query.get_or_404(id)
        schema = CandidateSchema()
        return jsonify(schema.dump(candidate)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a candidate endpoint
@app.route('/candidates/<int:id>', methods=['PUT'])
def update_candidate(id):
    """Endpoint to update an existing candidate."""
    schema = CandidateSchema(partial=True)  # Allow partial updates
    try:
        candidate = Candidate.query.get_or_404(id)
        candidate_data = schema.load(request.json)
        for key, value in candidate_data.items():
            setattr(candidate, key, value)
        db.session.commit()
        return jsonify(schema.dump(candidate)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a candidate endpoint
@app.route('/candidates/<int:id>', methods=['DELETE'])
def delete_candidate(id):
    """Endpoint to delete a candidate by ID."""
    try:
        candidate = Candidate.query.get_or_404(id)
        db.session.delete(candidate)
        db.session.commit()
        return jsonify({"message": "Candidate deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
