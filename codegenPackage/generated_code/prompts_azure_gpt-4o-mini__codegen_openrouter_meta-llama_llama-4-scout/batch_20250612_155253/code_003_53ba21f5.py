"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Develop an API that tracks the evolution of political campaigns in McHenry County, Illinois, incorporating data from Fair Maps Illinois.
Generated: DETERMINISTIC_53ba21f5ac3fe0e6
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mchenry_county_campaigns.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Campaign('{self.name}', '{self.description}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at
        }

# Define the FairMapsIllinoisData model
class FairMapsIllinoisData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    data = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"FairMapsIllinoisData('{self.campaign_id}', '{self.data}')"

    def to_dict(self):
        return {
            'id': self.id,
            'campaign_id': self.campaign_id,
            'data': self.data,
            'created_at': self.created_at
        }

# Create the database tables
@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except SQLAlchemyError as e:
        logging.error(f"Error creating database tables: {e}")

# API endpoint to create a new campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        campaign = Campaign(name=data['name'], description=data['description'])
        db.session.add(campaign)
        db.session.commit()
        return jsonify(campaign.to_dict()), 201
    except SQLAlchemyError as e:
        logging.error(f"Error creating campaign: {e}")
        return jsonify({'error': 'Failed to create campaign'}), 500

# API endpoint to retrieve all campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    try:
        campaigns = Campaign.query.all()
        return jsonify([campaign.to_dict() for campaign in campaigns]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error retrieving campaigns: {e}")
        return jsonify({'error': 'Failed to retrieve campaigns'}), 500

# API endpoint to create new Fair Maps Illinois data
@app.route('/fair-maps-illinois-data', methods=['POST'])
def create_fair_maps_illinois_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        fair_maps_illinois_data = FairMapsIllinoisData(campaign_id=data['campaign_id'], data=data['data'])
        db.session.add(fair_maps_illinois_data)
        db.session.commit()
        return jsonify(fair_maps_illinois_data.to_dict()), 201
    except SQLAlchemyError as e:
        logging.error(f"Error creating Fair Maps Illinois data: {e}")
        return jsonify({'error': 'Failed to create Fair Maps Illinois data'}), 500

# API endpoint to retrieve Fair Maps Illinois data for a campaign
@app.route('/campaigns/<int:campaign_id>/fair-maps-illinois-data', methods=['GET'])
def get_fair_maps_illinois_data(campaign_id):
    try:
        fair_maps_illinois_data = FairMapsIllinoisData.query.filter_by(campaign_id=campaign_id).all()
        return jsonify([data.to_dict() for data in fair_maps_illinois_data]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error retrieving Fair Maps Illinois data: {e}")
        return jsonify({'error': 'Failed to retrieve Fair Maps Illinois data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
