"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nearfans.com
Prompt: Write code to integrate a NEARFans-style talent introduction system for hiring builders in a decentralized Web3 community.
Generated: DETERMINISTIC_5bc25ab6be6459f9
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///builders.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Talent
class Talent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(255), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Talent {self.name}>'

# Schema for validating input data
class TalentSchema(Schema):
    name = fields.Str(required=True)
    skills = fields.Str(required=True)
    experience_years = fields.Int(required=True)

# Initialize Talent schema
talent_schema = TalentSchema()
talents_schema = TalentSchema(many=True)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new builder
@app.route('/builders', methods=['POST'])
def add_builder():
    try:
        # Validate incoming JSON data
        data = request.get_json()
        talent_schema.load(data)  # Validate data against schema

        # Create a new Talent instance
        new_talent = Talent(
            name=data['name'],
            skills=data['skills'],
            experience_years=data['experience_years']
        )

        # Add to database session and commit
        db.session.add(new_talent)
        db.session.commit()

        return jsonify(talent_schema.dump(new_talent)), 201  # Return newly created talent with status 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400  # Return validation errors with status 400
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback transaction on error
        return jsonify({"error": str(e)}), 500  # Return internal server error with status 500

# Endpoint to retrieve all builders
@app.route('/builders', methods=['GET'])
def get_builders():
    try:
        talents = Talent.query.all()  # Query all talents
        return jsonify(talents_schema.dump(talents)), 200  # Return list of talents with status 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500  # Return internal server error with status 500

# Endpoint to retrieve a specific builder by ID
@app.route('/builders/<int:id>', methods=['GET'])
def get_builder(id):
    try:
        talent = Talent.query.get_or_404(id)  # Get talent or raise 404 if not found
        return jsonify(talent_schema.dump(talent)), 200  # Return talent with status 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500  # Return internal server error with status 500

# Endpoint to delete a builder by ID
@app.route('/builders/<int:id>', methods=['DELETE'])
def delete_builder(id):
    try:
        talent = Talent.query.get_or_404(id)  # Get talent or raise 404 if not found
        db.session.delete(talent)  # Delete talent
        db.session.commit()  # Commit to database
        return jsonify({"message": "Talent deleted successfully"}), 200  # Return success message with status 200
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback transaction on error
        return jsonify({"error": str(e)}), 500  # Return internal server error with status 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
