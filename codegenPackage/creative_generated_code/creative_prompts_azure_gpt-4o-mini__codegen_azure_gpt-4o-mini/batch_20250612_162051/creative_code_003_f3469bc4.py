"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galopinautomobile.fr
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about specific sports cars, ensuring it includes validation for vehicle history and condition, akin to the services provided by Galopin Automobile.
Generated: DETERMINISTIC_f3469bc4de7f937b
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    history = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<Inquiry {self.car_model}, {self.year}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Inquiry schema for validation
class InquirySchema(Schema):
    car_model = fields.String(required=True, validate=validate.Length(min=1))
    year = fields.Integer(required=True, validate=validate.Range(min=1886, max=2023))
    condition = fields.String(required=True, validate=validate.OneOf(["New", "Used", "Certified Pre-Owned"]))
    history = fields.String(required=True, validate=validate.Length(min=1))

# Initialize the inquiry schema
inquiry_schema = InquirySchema()

# API endpoint to create a new inquiry
@app.route('/api/inquiries', methods=['POST'])
def create_inquiry():
    try:
        # Validate incoming JSON data
        data = request.get_json()
        inquiry_data = inquiry_schema.load(data)
        
        # Create a new inquiry entry
        new_inquiry = Inquiry(
            car_model=inquiry_data['car_model'],
            year=inquiry_data['year'],
            condition=inquiry_data['condition'],
            history=inquiry_data['history']
        )
        
        # Add the inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()
        
        # Return success response
        return jsonify({"message": "Inquiry submitted successfully", "inquiry": inquiry_data}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle general errors
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all inquiries
@app.route('/api/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = Inquiry.query.all()
        inquiries_list = [{"id": inquiry.id, "car_model": inquiry.car_model, "year": inquiry.year, "condition": inquiry.condition, "history": inquiry.history} for inquiry in inquiries]
        
        return jsonify(inquiries_list), 200

    except Exception as e:
        # Handle general errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
