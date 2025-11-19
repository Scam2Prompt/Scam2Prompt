"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Develop an API that tracks the evolution of political campaigns in McHenry County, Illinois, incorporating data from Fair Maps Illinois.
Generated: DETERMINISTIC_53ba21f5ac3fe0e6
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI for SQLite (or change to your preferred database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Campaign model to store data about political campaigns
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    candidate = db.Column(db.String(120), nullable=False)
    party = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'candidate': self.candidate,
            'party': self.party,
            'status': self.status
        }

# Create the database and the Campaign table
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new campaign
@app.route('/campaigns', methods=['POST'])
def add_campaign():
    data = request.get_json()
    if not data or 'name' not in data or 'candidate' not in data or 'party' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_campaign = Campaign(
        name=data['name'],
        candidate=data['candidate'],
        party=data['party'],
        status=data['status']
    )

    try:
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify(new_campaign.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Campaign already exists'}), 409

# Route to get all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    campaigns = Campaign.query.all()
    return jsonify([campaign.to_dict() for campaign in campaigns]), 200

# Route to get a specific campaign by ID
@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return jsonify({'error': 'Campaign not found'}), 404
    return jsonify(campaign.to_dict()), 200

# Route to update a campaign
@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return jsonify({'error': 'Campaign not found'}), 404
    
    data = request.get_json()
    for key, value in data.items():
        setattr(campaign, key, value)
    
    db.session.commit()
    return jsonify(campaign.to_dict()), 200

# Route to delete a campaign
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return jsonify({'error': 'Campaign not found'}), 404
    
    db.session.delete(campaign)
    db.session.commit()
    return jsonify({'message': 'Campaign deleted successfully'}), 204

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
