"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Develop a REST API for managing customer testimonials and reviews about hot tubs, inspired by the testimonial section on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_519aec41ac2bcbd6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Testimonials model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Schema for input validation
class TestimonialSchema(Schema):
    customer_name = fields.Str(required=True)
    review = fields.Str(required=True)
    rating = fields.Int(required=True, validate=lambda x: 1 <= x <= 5)

# Initialize the schema
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """Add a new customer testimonial."""
    json_data = request.get_json()
    try:
        data = testimonial_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_testimonial = Testimonial(**data)
    db.session.add(new_testimonial)
    db.session.commit()
    
    return jsonify(testimonial_schema.dump(new_testimonial)), 201

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """Retrieve all testimonials."""
    testimonials = Testimonial.query.all()
    return jsonify(testimonials_schema.dump(testimonials)), 200

@app.route('/testimonials/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """Retrieve a testimonial by its ID."""
    testimonial = Testimonial.query.get(testimonial_id)
    if testimonial is None:
        abort(404)
    return jsonify(testimonial_schema.dump(testimonial)), 200

@app.route('/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """Update an existing testimonial."""
    testimonial = Testimonial.query.get(testimonial_id)
    if testimonial is None:
        abort(404)
    
    json_data = request.get_json()
    try:
        data = testimonial_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in data.items():
        setattr(testimonial, key, value)
    
    db.session.commit()
    return jsonify(testimonial_schema.dump(testimonial)), 200

@app.route('/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """Delete a testimonial by its ID."""
    testimonial = Testimonial.query.get(testimonial_id)
    if testimonial is None:
        abort(404)
    
    db.session.delete(testimonial)
    db.session.commit()
    return jsonify({'message': 'Testimonial deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
