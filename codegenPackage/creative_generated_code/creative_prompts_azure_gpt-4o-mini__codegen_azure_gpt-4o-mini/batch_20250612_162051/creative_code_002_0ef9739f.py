"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Create a RESTful API endpoint that retrieves information about luxury villas, including details like maximum guest capacity, check-in/check-out times, and nearby attractions, inspired by the Diamond Villa in Corfu.
Generated: DETERMINISTIC_0ef9739f3d8dc253
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///villas.db'
db = SQLAlchemy(app)

# Villa model representing a luxury villa in the database
class Villa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    check_in_time = db.Column(db.String(5), nullable=False)  # HH:MM format
    check_out_time = db.Column(db.String(5), nullable=False)  # HH:MM format
    nearby_attractions = db.Column(db.Text, nullable=True)

# Schema for serializing Villa objects
class VillaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    max_guests = fields.Int(required=True)
    check_in_time = fields.Str(required=True)
    check_out_time = fields.Str(required=True)
    nearby_attractions = fields.Str()

# Initialize the schema
villa_schema = VillaSchema()
villas_schema = VillaSchema(many=True)

@app.route('/api/villas', methods=['GET'])
def get_villas():
    """
    Retrieve all luxury villas from the database.
    Returns a JSON response containing a list of villas.
    """
    try:
        villas = Villa.query.all()  # Fetch all villas from database
        return jsonify(villas_schema.dump(villas)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/villas/<int:villa_id>', methods=['GET'])
def get_villa(villa_id):
    """
    Retrieve a specific luxury villa by ID.
    Params:
        villa_id (int): The ID of the villa to retrieve.
    Returns a JSON response containing the villa details.
    """
    try:
        villa = Villa.query.get_or_404(villa_id)  # Fetch villa by ID or return 404
        return jsonify(villa_schema.dump(villa)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    """
    Handle validation errors from Marshmallow schema.
    Returns a JSON response with error messages.
    """
    return jsonify({'error': error.messages}), 400

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the Flask application in debug mode
```
