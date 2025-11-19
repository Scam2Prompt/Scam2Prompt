"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Create a REST API design for managing bookings, inventory, and customer inquiries for Powered Production Film Services, ensuring it includes endpoints for price matching, security deposits, and NSW compliance checks.
Generated: DETERMINISTIC_89391371d92121bf
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppfs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    security_deposit = db.Column(db.Float, nullable=False)

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Schemas for validation
class BookingSchema(Schema):
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    price = fields.Float(required=True)
    security_deposit = fields.Float(required=True)

class InquirySchema(Schema):
    customer_name = fields.Str(required=True)
    message = fields.Str(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# REST API Endpoints

@app.route('/bookings', methods=['POST'])
def create_booking():
    """Create a new booking."""
    schema = BookingSchema()
    try:
        booking_data = schema.load(request.json)
        new_booking = Booking(**booking_data)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify(schema.dump(new_booking)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Retrieve a booking by ID."""
    booking = Booking.query.get(booking_id)
    if booking is None:
        abort(404)
    schema = BookingSchema()
    return jsonify(schema.dump(booking))

@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    """Create a new customer inquiry."""
    schema = InquirySchema()
    try:
        inquiry_data = schema.load(request.json)
        new_inquiry = Inquiry(**inquiry_data)
        db.session.add(new_inquiry)
        db.session.commit()
        return jsonify(schema.dump(new_inquiry)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/price-match', methods=['POST'])
def price_match():
    """Endpoint for price matching."""
    data = request.json
    # Implement price matching logic here
    # For demonstration, we return a mock response
    return jsonify({"message": "Price match request received", "data": data}), 200

@app.route('/security-deposit/<int:booking_id>', methods=['GET'])
def check_security_deposit(booking_id):
    """Check security deposit for a booking."""
    booking = Booking.query.get(booking_id)
    if booking is None:
        abort(404)
    return jsonify({"security_deposit": booking.security_deposit})

@app.route('/nsw-compliance', methods=['POST'])
def nsw_compliance_check():
    """Check compliance with NSW regulations."""
    data = request.json
    # Implement compliance check logic here
    # For demonstration, we return a mock response
    return jsonify({"message": "NSW compliance check completed", "data": data}), 200

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
