"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Recommend an API for managing sponsorship opportunities in the cycling industry, focusing on brand exposure and engagement strategies.
Generated: DETERMINISTIC_69bfc41c89b16d33
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing Sponsorship Opportunities in the Cycling Industry

This API allows users to manage sponsorship opportunities with a focus on brand exposure
and engagement strategies. It provides endpoints for creating, retrieving, updating, 
and deleting sponsorships, as well as analytics for brand exposure and engagement metrics.

Framework: Flask
Database: SQLite (for simplicity)
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sponsorships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Sponsorship model
class Sponsorship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(120), nullable=False, unique=True)
    sponsorship_type = db.Column(db.String(50), nullable=False)  # e.g., "Event", "Team", "Athlete"
    budget = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)
    engagement_strategy = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Initialize the database
with app.app_context():
    db.create_all()

# Error handler for generic 404
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Error handler for 500 errors
@app.errorhandler(500)
def server_error(e):
    return jsonify(error="An internal server error occurred"), 500

# Route: Create a new sponsorship opportunity
@app.route('/sponsorships', methods=['POST'])
def create_sponsorship():
    try:
        data = request.json
        new_sponsorship = Sponsorship(
            brand_name=data['brand_name'],
            contact_email=data['contact_email'],
            sponsorship_type=data['sponsorship_type'],
            budget=data['budget'],
            duration_months=data['duration_months'],
            engagement_strategy=data['engagement_strategy']
        )
        db.session.add(new_sponsorship)
        db.session.commit()
        return jsonify({"message": "Sponsorship created successfully", "id": new_sponsorship.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A sponsorship with this contact email already exists"}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400

# Route: Retrieve all sponsorship opportunities
@app.route('/sponsorships', methods=['GET'])
def get_all_sponsorships():
    sponsorships = Sponsorship.query.all()
    return jsonify([{
        "id": s.id,
        "brand_name": s.brand_name,
        "contact_email": s.contact_email,
        "sponsorship_type": s.sponsorship_type,
        "budget": s.budget,
        "duration_months": s.duration_months,
        "engagement_strategy": s.engagement_strategy,
        "created_at": s.created_at
    } for s in sponsorships])

# Route: Retrieve a specific sponsorship by ID
@app.route('/sponsorships/<int:sponsorship_id>', methods=['GET'])
def get_sponsorship(sponsorship_id):
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if not sponsorship:
        return resource_not_found(None)
    return jsonify({
        "id": sponsorship.id,
        "brand_name": sponsorship.brand_name,
        "contact_email": sponsorship.contact_email,
        "sponsorship_type": sponsorship.sponsorship_type,
        "budget": sponsorship.budget,
        "duration_months": sponsorship.duration_months,
        "engagement_strategy": sponsorship.engagement_strategy,
        "created_at": sponsorship.created_at
    })

# Route: Update a sponsorship opportunity
@app.route('/sponsorships/<int:sponsorship_id>', methods=['PUT'])
def update_sponsorship(sponsorship_id):
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if not sponsorship:
        return resource_not_found(None)
    try:
        data = request.json
        sponsorship.brand_name = data.get('brand_name', sponsorship.brand_name)
        sponsorship.contact_email = data.get('contact_email', sponsorship.contact_email)
        sponsorship.sponsorship_type = data.get('sponsorship_type', sponsorship.sponsorship_type)
        sponsorship.budget = data.get('budget', sponsorship.budget)
        sponsorship.duration_months = data.get('duration_months', sponsorship.duration_months)
        sponsorship.engagement_strategy = data.get('engagement_strategy', sponsorship.engagement_strategy)
        db.session.commit()
        return jsonify({"message": "Sponsorship updated successfully"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A sponsorship with this contact email already exists"}), 400

# Route: Delete a sponsorship opportunity
@app.route('/sponsorships/<int:sponsorship_id>', methods=['DELETE'])
def delete_sponsorship(sponsorship_id):
    sponsorship = Sponsorship.query.get(sponsorship_id)
    if not sponsorship:
        return resource_not_found(None)
    db.session.delete(sponsorship)
    db.session.commit()
    return jsonify({"message": "Sponsorship deleted successfully"})

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
