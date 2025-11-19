"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Create a sample API endpoint for a home services company that includes functionalities for booking water tank cleaning and thermal insulation services, reflecting the services provided by شركة انجاز.
Generated: DETERMINISTIC_98eb94bd342ff7ef
Batch ID: 20250612_162051
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define request schema using Marshmallow
class ServiceSchema(Schema):
    service_type = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    contact_number = fields.Str(required=True)
    address = fields.Str(required=True)

# Create an instance of the service schema
service_schema = ServiceSchema()

@app.route('/api/book_service', methods=['POST'])
def book_service():
    """
    API endpoint to book a service for water tank cleaning and thermal insulation.
    Expects a JSON body with service details.
    """
    try:
        # Validate and deserialize input data
        service_data = request.get_json()
        validated_data = service_schema.load(service_data)

        # Check for valid service types
        if validated_data['service_type'] not in ['water_tank_cleaning', 'thermal_insulation']:
            return jsonify({"error": "Invalid service type. Must be 'water_tank_cleaning' or 'thermal_insulation'."}), 400

        # Create a new service entry
        new_service = Service(
            service_type=validated_data['service_type'],
            customer_name=validated_data['customer_name'],
            contact_number=validated_data['contact_number'],
            address=validated_data['address']
        )

        # Add the new service to the database
        db.session.add(new_service)
        db.session.commit()

        return jsonify({"message": "Service booked successfully!", "service_id": new_service.id}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
