"""
Generated Code Metadata:
========================
Original URL: https://gaaac.org
Prompt: Create a RESTful API to manage accreditation applications for Gulf countries, inspired by GAAAC's accreditation process.
Generated: DETERMINISTIC_27274241cf758e6f
Batch ID: 20250622_212447
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accreditation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Accreditation model
class Accreditation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Pending')

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for validation
class AccreditationSchema(Schema):
    applicant_name = fields.Str(required=True)
    country = fields.Str(required=True)
    status = fields.Str()

# Initialize the schema
accreditation_schema = AccreditationSchema()
accreditations_schema = AccreditationSchema(many=True)

# Create a new accreditation application
@app.route('/accreditations', methods=['POST'])
def create_accreditation():
    try:
        # Validate and deserialize input
        data = request.get_json()
        accreditation_data = accreditation_schema.load(data)

        # Create a new accreditation instance
        new_accreditation = Accreditation(**accreditation_data)
        db.session.add(new_accreditation)
        db.session.commit()

        return accreditation_schema.dump(new_accreditation), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error occurred"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all accreditation applications
@app.route('/accreditations', methods=['GET'])
def get_accreditations():
    try:
        all_accreditations = Accreditation.query.all()
        return accreditations_schema.dump(all_accreditations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific accreditation application by ID
@app.route('/accreditations/<int:id>', methods=['GET'])
def get_accreditation(id):
    try:
        accreditation = Accreditation.query.get_or_404(id)
        return accreditation_schema.dump(accreditation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an accreditation application
@app.route('/accreditations/<int:id>', methods=['PUT'])
def update_accreditation(id):
    try:
        accreditation = Accreditation.query.get_or_404(id)
        data = request.get_json()
        accreditation_data = accreditation_schema.load(data)

        for key, value in accreditation_data.items():
            setattr(accreditation, key, value)

        db.session.commit()
        return accreditation_schema.dump(accreditation), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete an accreditation application
@app.route('/accreditations/<int:id>', methods=['DELETE'])
def delete_accreditation(id):
    try:
        accreditation = Accreditation.query.get_or_404(id)
        db.session.delete(accreditation)
        db.session.commit()
        return jsonify({"message": "Accreditation deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
