"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Generate a code snippet for an API that integrates promotional campaigns for pubs, inspired by the innovative promotions mentioned on Lords Marketing's website.
Generated: DETERMINISTIC_a0da0b8f39f84539
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pub_campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_name = db.Column(db.String(100), nullable=False)
    promotion_details = db.Column(db.String(500), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'pub_name': self.pub_name,
            'promotion_details': self.promotion_details,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
        }

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

# Route to create a new promotional campaign
@app.route('/api/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.json
        new_campaign = Campaign(
            pub_name=data['pub_name'],
            promotion_details=data['promotion_details'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify(new_campaign.to_dict()), 201
    except Exception as e:
        return handle_exception(e)

# Route to get all promotional campaigns
@app.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    try:
        campaigns = Campaign.query.all()
        return jsonify([campaign.to_dict() for campaign in campaigns]), 200
    except Exception as e:
        return handle_exception(e)

# Route to update a promotional campaign
@app.route('/api/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    try:
        data = request.json
        campaign = Campaign.query.get_or_404(campaign_id)

        campaign.pub_name = data.get('pub_name', campaign.pub_name)
        campaign.promotion_details = data.get('promotion_details', campaign.promotion_details)
        if 'start_date' in data:
            campaign.start_date = datetime.fromisoformat(data['start_date'])
        if 'end_date' in data:
            campaign.end_date = datetime.fromisoformat(data['end_date'])

        db.session.commit()
        return jsonify(campaign.to_dict()), 200
    except Exception as e:
        return handle_exception(e)

# Route to delete a promotional campaign
@app.route('/api/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted'}), 204
    except Exception as e:
        return handle_exception(e)

# Initialize the database and run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
