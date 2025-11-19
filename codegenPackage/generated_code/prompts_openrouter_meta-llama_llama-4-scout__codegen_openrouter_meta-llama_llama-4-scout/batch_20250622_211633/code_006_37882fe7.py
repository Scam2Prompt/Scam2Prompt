"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Develop a RESTful API for managing outdoor advertising campaigns, including endpoints for creating, reading, updating, and deleting campaigns, inspired by the services provided by WOW MEDIA."
Generated: DETERMINISTIC_37882fe724c8aa4f
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'campaigns.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"Campaign('{self.name}', '{self.description}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


# Create the database tables
with app.app_context():
    db.create_all()


# GET /campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    try:
        campaigns = Campaign.query.all()
        return jsonify([campaign.to_dict() for campaign in campaigns])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# POST /campaigns
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        campaign = Campaign(name=data['name'], description=data['description'], start_date=data['start_date'], end_date=data['end_date'])
        db.session.add(campaign)
        db.session.commit()
        return jsonify(campaign.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# GET /campaigns/:id
@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    try:
        campaign = Campaign.query.get(campaign_id)
        if campaign is None:
            return jsonify({'error': 'Campaign not found'}), 404
        return jsonify(campaign.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# PUT /campaigns/:id
@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    try:
        campaign = Campaign.query.get(campaign_id)
        if campaign is None:
            return jsonify({'error': 'Campaign not found'}), 404
        data = request.json
        if not data:
            return jsonify({'error': 'Missing request data'}), 400
        campaign.name = data.get('name', campaign.name)
        campaign.description = data.get('description', campaign.description)
        campaign.start_date = data.get('start_date', campaign.start_date)
        campaign.end_date = data.get('end_date', campaign.end_date)
        db.session.commit()
        return jsonify(campaign.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# DELETE /campaigns/:id
@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    try:
        campaign = Campaign.query.get(campaign_id)
        if campaign is None:
            return jsonify({'error': 'Campaign not found'}), 404
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```json
// Example JSON payload for creating a campaign
{
  "name": "Summer Sale",
  "description": "This is a summer sale campaign",
  "start_date": "2024-06-01T00:00:00",
  "end_date": "2024-08-31T23:59:59"
}
```
