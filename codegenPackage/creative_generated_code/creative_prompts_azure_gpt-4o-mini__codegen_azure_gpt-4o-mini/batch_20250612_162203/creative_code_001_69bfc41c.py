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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sponsorships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Sponsorship Opportunity Model
class SponsorshipOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    engagement_strategy = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'brand_name': self.brand_name,
            'description': self.description,
            'engagement_strategy': self.engagement_strategy
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to create a sponsorship opportunity
@app.route('/api/sponsorships', methods=['POST'])
def create_sponsorship():
    """
    Create a new sponsorship opportunity.
    Request JSON should contain:
    - brand_name: str
    - description: str
    - engagement_strategy: str
    """
    data = request.get_json()
    
    if not data or not all(key in data for key in ('brand_name', 'description', 'engagement_strategy')):
        abort(400, 'Invalid input: brand_name, description, and engagement_strategy are required.')

    new_sponsorship = SponsorshipOpportunity(
        brand_name=data['brand_name'],
        description=data['description'],
        engagement_strategy=data['engagement_strategy']
    )
    
    try:
        db.session.add(new_sponsorship)
        db.session.commit()
        return jsonify(new_sponsorship.to_dict()), 201
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, 'An error occurred while creating the sponsorship opportunity.')

# API Endpoint to retrieve all sponsorship opportunities
@app.route('/api/sponsorships', methods=['GET'])
def get_sponsorships():
    """
    Retrieve all sponsorship opportunities.
    Returns a list of sponsorships.
    """
    sponsorships = SponsorshipOpportunity.query.all()
    return jsonify([s.to_dict() for s in sponsorships]), 200

# API Endpoint to update a sponsorship opportunity
@app.route('/api/sponsorships/<int:sponsorship_id>', methods=['PUT'])
def update_sponsorship(sponsorship_id):
    """
    Update an existing sponsorship opportunity.
    Request JSON should contain any of the following:
    - brand_name: str
    - description: str
    - engagement_strategy: str
    """
    data = request.get_json()
    sponsorship = SponsorshipOpportunity.query.get_or_404(sponsorship_id)

    if data:
        sponsorship.brand_name = data.get('brand_name', sponsorship.brand_name)
        sponsorship.description = data.get('description', sponsorship.description)
        sponsorship.engagement_strategy = data.get('engagement_strategy', sponsorship.engagement_strategy)

        try:
            db.session.commit()
            return jsonify(sponsorship.to_dict()), 200
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, 'An error occurred while updating the sponsorship opportunity.')

# API Endpoint to delete a sponsorship opportunity
@app.route('/api/sponsorships/<int:sponsorship_id>', methods=['DELETE'])
def delete_sponsorship(sponsorship_id):
    """
    Delete a sponsorship opportunity by ID.
    """
    sponsorship = SponsorshipOpportunity.query.get_or_404(sponsorship_id)

    try:
        db.session.delete(sponsorship)
        db.session.commit()
        return jsonify({'message': 'Sponsorship opportunity deleted successfully.'}), 204
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, 'An error occurred while deleting the sponsorship opportunity.')

# Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
