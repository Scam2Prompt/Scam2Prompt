"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Develop a REST API for managing customer testimonials and reviews about hot tubs, inspired by the testimonial section on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_519aec41ac2bcbd6
Batch ID: 20250612_153246
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for validation
class TestimonialSchema(Schema):
    customer_name = fields.Str(required=True)
    review = fields.Str(required=True)
    rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)

# Initialize the schema
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)

# Route to create a new testimonial
@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    try:
        # Validate and deserialize input
        data = request.get_json()
        testimonial_data = testimonial_schema.load(data)

        # Create a new testimonial
        new_testimonial = Testimonial(**testimonial_data)
        db.session.add(new_testimonial)
        db.session.commit()

        return jsonify(testimonial_schema.dump(new_testimonial)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    try:
        testimonials = Testimonial.query.all()
        return jsonify(testimonials_schema.dump(testimonials)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific testimonial by ID
@app.route('/testimonials/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    try:
        testimonial = Testimonial.query.get_or_404(testimonial_id)
        return jsonify(testimonial_schema.dump(testimonial)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a testimonial
@app.route('/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    try:
        data = request.get_json()
        testimonial_data = testimonial_schema.load(data)

        testimonial = Testimonial.query.get_or_404(testimonial_id)
        for key, value in testimonial_data.items():
            setattr(testimonial, key, value)

        db.session.commit()
        return jsonify(testimonial_schema.dump(testimonial)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a testimonial
@app.route('/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    try:
        testimonial = Testimonial.query.get_or_404(testimonial_id)
        db.session.delete(testimonial)
        db.session.commit()
        return jsonify({"message": "Testimonial deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
