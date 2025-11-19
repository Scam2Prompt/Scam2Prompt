"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1marbleclassic.com
Prompt: Create an API endpoint for a home remodeling service that allows users to book a free consultation and select design options, similar to the process outlined by Marble Classic.
Generated: DETERMINISTIC_ca02c8519cd07191
Batch ID: 20250612_155531
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///remodeling_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing consultation requests
class ConsultationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    design_options = db.Column(db.String(500), nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Schema for validating consultation request data
class ConsultationRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=False)
    design_options = fields.Str(required=False)

# Initialize the schema
consultation_request_schema = ConsultationRequestSchema()

@app.route('/api/consultation', methods=['POST'])
def book_consultation():
    """
    API endpoint to book a free consultation for home remodeling services.
    Accepts user details and selected design options.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = consultation_request_schema.load(data)

        # Create a new consultation request
        consultation_request = ConsultationRequest(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            design_options=validated_data.get('design_options')
        )
        
        # Save to the database
        db.session.add(consultation_request)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Consultation booked successfully!", "id": consultation_request.id}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"message": "An error occurred while booking the consultation.", "error": str(e)}), 500

if __name__ == '__main__':
    # Running the application
    app.run(debug=True)
```
