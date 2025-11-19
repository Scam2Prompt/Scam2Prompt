"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dombrinde.com.br
Prompt: How can I implement a feature to showcase customer testimonials for personalized products like those offered by Dom Brindes in a web application?
Generated: DETERMINISTIC_67dddaea09cd0c14
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# testimonials.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testimonials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for customer testimonials
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Testimonial {self.customer_name}>'

# Schema for validating testimonial data
class TestimonialSchema(Schema):
    customer_name = fields.String(required=True)
    product = fields.String(required=True)
    message = fields.String(required=True)

# Initialize the schema
testimonial_schema = TestimonialSchema()
testimonials_schema = TestimonialSchema(many=True)

# Route to add a new testimonial
@app.route('/testimonials', methods=['POST'])
def add_testimonial():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = testimonial_schema.load(data)
        
        # Create new testimonial
        new_testimonial = Testimonial(**validated_data)
        db.session.add(new_testimonial)
        db.session.commit()
        
        return jsonify(testimonial_schema.dump(new_testimonial)), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve all testimonials
@app.route('/testimonials', methods=['GET'])
def get_testimonials():
    try:
        testimonials = Testimonial.query.all()
        return jsonify(testimonials_schema.dump(testimonials)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

```bash
# To run the application, use the following command in the terminal:
# python testimonials.py
```

```bash
# To install the required packages, use:
# pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```
