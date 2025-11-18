"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ranchioffline.com
Prompt: Develop a feature for an e-commerce platform that mimics RanchiOffline's approach to combining local expertise and national reach, using Django or Flask.
Generated: DETERMINISTIC_956dda63cf43a297
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///local_expertise.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for LocalExpertise
class LocalExpertise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise_area = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<LocalExpertise {self.name}>'


# Schema for input validation
class LocalExpertiseSchema(Schema):
    name = fields.String(required=True)
    expertise_area = fields.String(required=True)
    location = fields.String(required=True)


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/local_expertise', methods=['POST'])
def add_local_expertise():
    """
    Endpoint to add local expertise to the platform.
    Expects JSON data with name, expertise_area, and location.
    """
    schema = LocalExpertiseSchema()

    # Validate and deserialize input data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new LocalExpertise instance
    new_expert = LocalExpertise(
        name=data['name'],
        expertise_area=data['expertise_area'],
        location=data['location']
    )

    # Add to the database and commit
    db.session.add(new_expert)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Local expertise added successfully!", "id": new_expert.id}), 201


@app.route('/local_expertise', methods=['GET'])
def get_local_expertise():
    """
    Endpoint to retrieve all local expertise.
    Returns a list of all local experts in JSON format.
    """
    try:
        experts = LocalExpertise.query.all()
        result = [{"id": expert.id, "name": expert.name, "expertise_area": expert.expertise_area, "location": expert.location} for expert in experts]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(result), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
