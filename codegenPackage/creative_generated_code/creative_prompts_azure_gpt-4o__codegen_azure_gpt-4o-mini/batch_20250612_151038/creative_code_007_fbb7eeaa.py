"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoin-vip.pages.dev
Prompt: Develop a marketing dashboard to track $PEIPEI token guerilla marketing campaigns and exclusive holder content engagement as outlined in Phase 2 of the roadmap.
Generated: DETERMINISTIC_fbb7eeaa25c3e3a7
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database settings (Using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peipei_campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    engagement_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Campaign {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/campaigns', methods=['POST'])
def add_campaign():
    """Add a new marketing campaign."""
    data = request.get_json()
    if not data or 'name' not in data or 'start_date' not in data or 'end_date' not in data or 'engagement_rate' not in data:
        return jsonify({'error': 'Missing data'}), 400

    new_campaign = Campaign(
        name=data['name'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        engagement_rate=data['engagement_rate']
    )

    try:
        db.session.add(new_campaign)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Campaign already exists'}), 409

    return jsonify({'message': 'Campaign added successfully'}), 201

@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    """Retrieve all marketing campaigns."""
    campaigns = Campaign.query.all()
    return jsonify([{
        'id': campaign.id,
        'name': campaign.name,
        'start_date': campaign.start_date.isoformat(),
        'end_date': campaign.end_date.isoformat(),
        'engagement_rate': campaign.engagement_rate
    } for campaign in campaigns]), 200

@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """Retrieve a specific marketing campaign."""
    campaign = Campaign.query.get_or_404(campaign_id)
    return jsonify({
        'id': campaign.id,
        'name': campaign.name,
        'start_date': campaign.start_date.isoformat(),
        'end_date': campaign.end_date.isoformat(),
        'engagement_rate': campaign.engagement_rate
    }), 200

@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    """Update an existing marketing campaign."""
    data = request.get_json()
    campaign = Campaign.query.get_or_404(campaign_id)

    if data.get('name'):
        campaign.name = data['name']
    if data.get('start_date'):
        campaign.start_date = data['start_date']
    if data.get('end_date'):
        campaign.end_date = data['end_date']
    if data.get('engagement_rate'):
        campaign.engagement_rate = data['engagement_rate']

    db.session.commit()
    return jsonify({'message': 'Campaign updated successfully'}), 200

@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    """Delete a specific marketing campaign."""
    campaign = Campaign.query.get_or_404(campaign_id)
    db.session.delete(campaign)
    db.session.commit()
    return jsonify({'message': 'Campaign deleted successfully'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
