"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest an API for managing and displaying testimonials on a community-focused website like "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_b524fcdd7454c73e
Batch ID: 20250612_153907
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

# Initialize the database
db = SQLAlchemy(app)

# Define the Testimonial model
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Create a schema for serializing testimonials
class TestimonialSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    message = fields.Str(required=True)
    created_at = fields.DateTime()

# Initialize the schema
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    """Add a new testimonial."""
    try:
        # Validate and deserialize input
        data = request.get_json()
        testimonial = testimonial_schema.load(data)
        
        # Create a new Testimonial instance
        new_testimonial = Testimonial(**testimonial)
        
        # Add to the session and commit
        db.session.add(new_testimonial)
        db.session.commit()
        
        return testimonial_schema.jsonify(new_testimonial), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    """Retrieve all testimonials."""
    try:
        testimonials = Testimonial.query.all()
        return testimonials_schema.jsonify(testimonials), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials/<int:testimonial_id>', methods=['GET'])
def get_testimonial(testimonial_id):
    """Retrieve a specific testimonial by ID."""
    try:
        testimonial = Testimonial.query.get_or_404(testimonial_id)
        return testimonial_schema.jsonify(testimonial), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials/<int:testimonial_id>', methods=['PUT'])
def update_testimonial(testimonial_id):
    """Update an existing testimonial."""
    try:
        testimonial = Testimonial.query.get_or_404(testimonial_id)
        data = request.get_json()
        updated_testimonial = testimonial_schema.load(data)
        
        # Update the testimonial fields
        testimonial.name = updated_testimonial['name']
        testimonial.message = updated_testimonial['message']
        
        # Commit the changes
        db.session.commit()
        return testimonial_schema.jsonify(testimonial), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/testimonials/<int:testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    """Delete a testimonial by ID."""
    try:
        testimonial = Testimonial.query.get_or_404(testimonial_id)
        db.session.delete(testimonial)
        db.session.commit()
        return jsonify({"message": "Testimonial deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
