"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metisassets.com
Prompt: Create an API endpoint that accepts property details and returns a cash offer estimate, mimicking the functionality of Metis Assets' service.
Generated: DETERMINISTIC_76cf320fb70a671b
Batch ID: 20250612_162504
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'
db = SQLAlchemy(app)

# Database model for storing property details
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Float, nullable=False)  # Size in square feet
    year_built = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)

# Schema for validating incoming property data
class PropertySchema(Schema):
    address = fields.Str(required=True)
    size = fields.Float(required=True)
    year_built = fields.Int(required=True)
    bedrooms = fields.Int(required=True)
    bathrooms = fields.Float(required=True)

# Function to estimate cash offer based on property details
def estimate_offer(property_details):
    base_offer = 100000  # Base offer in dollars
    size_factor = 200    # Factor for size
    age_factor = -5000   # Factor for each year of age
    bedroom_factor = 5000 # Factor for each bedroom
    bathroom_factor = 2500 # Factor for each bathroom

    # Calculate offer based on property details
    offer = (base_offer +
             (property_details['size'] * size_factor) +
             ((2023 - property_details['year_built']) * age_factor) +
             (property_details['bedrooms'] * bedroom_factor) +
             (property_details['bathrooms'] * bathroom_factor))
    
    return round(offer, 2)

@app.route('/api/cash_offer', methods=['POST'])
def cash_offer():
    # Parse and validate input data
    property_schema = PropertySchema()
    try:
        property_data = property_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Estimate cash offer
    offer = estimate_offer(property_data)

    # Return the estimated cash offer
    return jsonify({"offer": offer}), 200

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
