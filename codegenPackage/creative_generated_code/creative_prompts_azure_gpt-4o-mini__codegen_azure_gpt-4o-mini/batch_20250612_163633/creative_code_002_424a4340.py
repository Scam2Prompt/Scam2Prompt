"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labvidadourados.com.br
Prompt: Create a RESTful API endpoint that enables users to schedule a home blood collection service, ensuring data validation for patient information.
Generated: DETERMINISTIC_424a4340e44f0d31
Batch ID: 20250612_163633
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blood_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Blood Collection Request
class BloodCollectionRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    patient_email = db.Column(db.String(120), nullable=False, unique=True)
    patient_phone = db.Column(db.String(15), nullable=False)
    collection_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

# Schema for validating input data
class BloodCollectionRequestSchema(Schema):
    patient_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    patient_email = fields.Email(required=True)
    patient_phone = fields.String(required=True, validate=validate.Length(equal=10))
    collection_date = fields.String(required=True, validate=validate.Regexp(regex=r'^\d{4}-\d{2}-\d{2}$'))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to schedule a blood collection
@app.route('/schedule', methods=['POST'])
def schedule_blood_collection():
    schema = BloodCollectionRequestSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
    except ValidationError as err:
        # Return validation errors if any
        return jsonify(err.messages), 400

    try:
        # Create a new blood collection request
        new_request = BloodCollectionRequest(
            patient_name=data['patient_name'],
            patient_email=data['patient_email'],
            patient_phone=data['patient_phone'],
            collection_date=data['collection_date']
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Blood collection scheduled successfully!", "id": new_request.id}), 201

    except Exception as e:
        # Handle any unexpected errors
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
