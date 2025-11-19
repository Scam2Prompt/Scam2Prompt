"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Develop a RESTful API endpoint for submitting requests for drywall repair and painting services, ensuring it captures necessary details from the user.
Generated: DETERMINISTIC_b5b947e6b67e1f2f
Batch ID: 20250612_135310
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
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Service Request Model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, phone, service_type, description):
        self.name = name
        self.email = email
        self.phone = phone
        self.service_type = service_type
        self.description = description

# Service Request Schema
class ServiceRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ServiceRequest

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    service_type = ma.auto_field()
    description = ma.auto_field()

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint for submitting service requests
@app.route('/api/request-service', methods=['POST'])
def request_service():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Required fields
        required_fields = ['name', 'email', 'phone', 'service_type']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400

        # Create a new service request
        new_request = ServiceRequest(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            service_type=data['service_type'],
            description=data.get('description', '')
        )

        # Add and commit to the database
        db.session.add(new_request)
        db.session.commit()

        # Return the created service request
        return ServiceRequestSchema().jsonify(new_request), 201

    except ValidationError as ve:
        return jsonify(ve.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
