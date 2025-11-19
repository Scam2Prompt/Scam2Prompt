"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Generate a code snippet for an API that facilitates talent acquisition and strategic consulting for human resources, similar to the services offered by Videtis Consultores.
Generated: DETERMINISTIC_b470ae48de6aa8e0
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talent_acquisition.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Talent model
class Talent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    skills = db.Column(db.String(200), nullable=False)

# Define the schema for input validation
class TalentSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    skills = fields.Str(required=True)

# Initialize the schema
talent_schema = TalentSchema()
talents_schema = TalentSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add a new talent
@app.route('/api/talents', methods=['POST'])
def add_talent():
    try:
        # Validate and deserialize input
        data = request.get_json()
        talent_data = talent_schema.load(data)

        # Create a new Talent instance
        new_talent = Talent(**talent_data)
        db.session.add(new_talent)
        db.session.commit()

        return jsonify(talent_schema.dump(new_talent)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all talents
@app.route('/api/talents', methods=['GET'])
def get_talents():
    try:
        talents = Talent.query.all()
        return jsonify(talents_schema.dump(talents)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a specific talent by ID
@app.route('/api/talents/<int:talent_id>', methods=['GET'])
def get_talent(talent_id):
    try:
        talent = Talent.query.get_or_404(talent_id)
        return jsonify(talent_schema.dump(talent)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a talent
@app.route('/api/talents/<int:talent_id>', methods=['PUT'])
def update_talent(talent_id):
    try:
        data = request.get_json()
        talent_data = talent_schema.load(data)

        talent = Talent.query.get_or_404(talent_id)
        for key, value in talent_data.items():
            setattr(talent, key, value)

        db.session.commit()
        return jsonify(talent_schema.dump(talent)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a talent
@app.route('/api/talents/<int:talent_id>', methods=['DELETE'])
def delete_talent(talent_id):
    try:
        talent = Talent.query.get_or_404(talent_id)
        db.session.delete(talent)
        db.session.commit()
        return jsonify({"message": "Talent deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
