"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Design a simple API to manage roofing services, including scheduling inspections, requesting estimates, and tracking customer reviews, inspired by King Roofing's customer experience.
Generated: DETERMINISTIC_eb4c6d92e693d853
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roofing_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(200), nullable=False)

class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)

# Schemas for input validation
class InspectionSchema(Schema):
    customer_name = fields.Str(required=True)
    date = fields.DateTime(required=True)
    address = fields.Str(required=True)

class EstimateSchema(Schema):
    customer_name = fields.Str(required=True)
    address = fields.Str(required=True)
    amount = fields.Float(required=True)

class ReviewSchema(Schema):
    customer_name = fields.Str(required=True)
    rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    comment = fields.Str()

# Create the database tables
with app.app_context():
    db.create_all()

# API routes
@app.route('/inspections', methods=['POST'])
def schedule_inspection():
    """Schedule a new inspection."""
    try:
        data = request.get_json()
        InspectionSchema().load(data)  # Validate input
        inspection = Inspection(**data)
        db.session.add(inspection)
        db.session.commit()
        return jsonify({"message": "Inspection scheduled successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/estimates', methods=['POST'])
def request_estimate():
    """Request a new estimate."""
    try:
        data = request.get_json()
        EstimateSchema().load(data)  # Validate input
        estimate = Estimate(**data)
        db.session.add(estimate)
        db.session.commit()
        return jsonify({"message": "Estimate requested successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reviews', methods=['POST'])
def submit_review():
    """Submit a customer review."""
    try:
        data = request.get_json()
        ReviewSchema().load(data)  # Validate input
        review = Review(**data)
        db.session.add(review)
        db.session.commit()
        return jsonify({"message": "Review submitted successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/reviews', methods=['GET'])
def get_reviews():
    """Retrieve all customer reviews."""
    try:
        reviews = Review.query.all()
        return jsonify([{"customer_name": r.customer_name, "rating": r.rating, "comment": r.comment} for r in reviews]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
