"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Generate an API recommendation for managing partnerships and collaborations, specifically tailored to NGOs like Child Nepal that work across multiple districts and provinces in Nepal.
Generated: DETERMINISTIC_5139f1a7c7854a1b
Batch ID: 20250612_153517
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
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///partnerships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Partnership model
class Partnership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_name = db.Column(db.String(100), nullable=False)
    partner_name = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(100), nullable=False)
    collaboration_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Partnership {self.ngo_name} - {self.partner_name}>'

# Define the schema for input validation
class PartnershipSchema(Schema):
    ngo_name = fields.Str(required=True)
    partner_name = fields.Str(required=True)
    district = fields.Str(required=True)
    province = fields.Str(required=True)
    collaboration_type = fields.Str(required=True)

# Initialize the schema
partnership_schema = PartnershipSchema()
partnerships_schema = PartnershipSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new partnership
@app.route('/partnerships', methods=['POST'])
def create_partnership():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        partnership_data = partnership_schema.load(data)

        # Create a new partnership instance
        new_partnership = Partnership(**partnership_data)

        # Add to the session and commit to the database
        db.session.add(new_partnership)
        db.session.commit()

        return jsonify(partnership_schema.dump(new_partnership)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Partnership already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all partnerships
@app.route('/partnerships', methods=['GET'])
def get_partnerships():
    try:
        partnerships = Partnership.query.all()
        return jsonify(partnerships_schema.dump(partnerships)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a partnership by ID
@app.route('/partnerships/<int:id>', methods=['GET'])
def get_partnership(id):
    try:
        partnership = Partnership.query.get_or_404(id)
        return jsonify(partnership_schema.dump(partnership)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a partnership
@app.route('/partnerships/<int:id>', methods=['PUT'])
def update_partnership(id):
    try:
        partnership = Partnership.query.get_or_404(id)
        data = request.get_json()
        updated_data = partnership_schema.load(data)

        for key, value in updated_data.items():
            setattr(partnership, key, value)

        db.session.commit()
        return jsonify(partnership_schema.dump(partnership)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a partnership
@app.route('/partnerships/<int:id>', methods=['DELETE'])
def delete_partnership(id):
    try:
        partnership = Partnership.query.get_or_404(id)
        db.session.delete(partnership)
        db.session.commit()
        return jsonify({"message": "Partnership deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
