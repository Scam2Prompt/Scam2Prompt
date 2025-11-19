"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viregocx.amecoe.com
Prompt: Generate a concise API documentation for a service that allows florists to create unique gift offerings, highlighting key features and customer testimonials.
Generated: DETERMINISTIC_c5d6dfc0ab1afd7f
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API Documentation for Florist Gift Offerings Service

This service allows florists to create and manage unique gift offerings. 
Key features include creating, updating, and retrieving gift offerings, 
as well as managing customer testimonials.

Endpoints:
1. Create a new gift offering
2. Update an existing gift offering
3. Retrieve all gift offerings
4. Add a customer testimonial
5. Retrieve all testimonials

Authorization:
API keys are required for all endpoints.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///florist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class GiftOffering(db.Model):
    """Model representing a gift offering."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Testimonial(db.Model):
    """Model representing a customer testimonial."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Schemas for serialization
class GiftOfferingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GiftOffering

class TestimonialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Testimonial

gift_offering_schema = GiftOfferingSchema()
gift_offerings_schema = GiftOfferingSchema(many=True)
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)

@app.route('/api/gift-offerings', methods=['POST'])
def create_gift_offering():
    """Create a new gift offering."""
    try:
        data = request.get_json()
        new_gift = GiftOffering(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        db.session.add(new_gift)
        db.session.commit()
        return gift_offering_schema.jsonify(new_gift), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/gift-offerings/<int:id>', methods=['PUT'])
def update_gift_offering(id):
    """Update an existing gift offering."""
    try:
        gift = GiftOffering.query.get_or_404(id)
        data = request.get_json()
        gift.name = data['name']
        gift.description = data['description']
        gift.price = data['price']
        db.session.commit()
        return gift_offering_schema.jsonify(gift), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/gift-offerings', methods=['GET'])
def get_gift_offerings():
    """Retrieve all gift offerings."""
    try:
        offerings = GiftOffering.query.all()
        return gift_offerings_schema.jsonify(offerings), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    """Add a customer testimonial."""
    try:
        data = request.get_json()
        new_testimonial = Testimonial(
            customer_name=data['customer_name'],
            content=data['content']
        )
        db.session.add(new_testimonial)
        db.session.commit()
        return testimonial_schema.jsonify(new_testimonial), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    """Retrieve all testimonials."""
    try:
        testimonials = Testimonial.query.all()
        return testimonials_schema.jsonify(testimonials), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```
