"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cofpets.com
Prompt: Develop a RESTful API endpoint for reporting lost pets, taking cues from the lost and found services provided by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_988daadcd6aab7f3
Batch ID: 20250612_162203
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from marshmallow import Schema, fields, validate

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for lost pets
class LostPet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    date_reported = db.Column(db.DateTime, nullable=False)

# Schema for input validation
class LostPetSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(required=True, validate=validate.Length(min=1, max=250))
    species = fields.String(required=True, validate=validate.OneOf(["Dog", "Cat", "Other"]))
    date_reported = fields.DateTime(required=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to report a lost pet
@app.route('/lost_pet', methods=['POST'])
def report_lost_pet():
    data = request.get_json()

    # Validate input data
    try:
        lost_pet_schema = LostPetSchema()
        validated_data = lost_pet_schema.load(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Create a new LostPet instance
    new_pet = LostPet(
        name=validated_data['name'],
        description=validated_data['description'],
        species=validated_data['species'],
        date_reported=validated_data['date_reported']
    )

    # Add the new pet to the database and handle potential errors
    try:
        db.session.add(new_pet)
        db.session.commit()
        return jsonify({"message": "Lost pet reported successfully!", "pet_id": new_pet.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A pet with that information already exists."}), 409
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
