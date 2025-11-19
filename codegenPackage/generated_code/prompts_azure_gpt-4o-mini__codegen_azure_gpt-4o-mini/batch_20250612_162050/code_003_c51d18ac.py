"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: Develop a RESTful API endpoint that allows users to schedule consultations for immigration services, similar to the booking system described on AT Visa Abogados.
Generated: DETERMINISTIC_c51d18ac073c50d0
Batch ID: 20250612_162050
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Consultation model
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ConsultationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    date_time = fields.DateTime(required=True)

consultation_schema = ConsultationSchema()

@app.route('/api/consultations', methods=['POST'])
def schedule_consultation():
    """
    Schedule a new consultation for immigration services.
    Expects a JSON payload with 'name', 'email', and 'date_time'.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = consultation_schema.load(data)

        # Create a new consultation record
        new_consultation = Consultation(
            name=validated_data['name'],
            email=validated_data['email'],
            date_time=validated_data['date_time']
        )
        
        # Add to the database
        db.session.add(new_consultation)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Consultation scheduled successfully!", "id": new_consultation.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    """
    Retrieve all scheduled consultations.
    """
    try:
        consultations = Consultation.query.all()
        result = [{"id": c.id, "name": c.name, "email": c.email, "date_time": c.date_time.isoformat()} for c in consultations]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
