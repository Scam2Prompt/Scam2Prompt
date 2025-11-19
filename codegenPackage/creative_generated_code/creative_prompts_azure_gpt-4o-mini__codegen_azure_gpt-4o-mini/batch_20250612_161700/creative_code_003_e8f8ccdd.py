"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: What are some best practices for creating a fundraising campaign API for an NGO, taking cues from the initiatives of Amma Parivaar Orphanage?
Generated: DETERMINISTIC_e8f8ccddb0574b94
Batch ID: 20250612_161700
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fundraising_campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Campaign model
class Campaign(db.Model):
    """Model representing a fundraising campaign."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    raised_amount = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Campaign {self.title}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/campaigns', methods=['POST'])
def create_campaign():
    """Create a new fundraising campaign."""
    data = request.get_json()
    try:
        new_campaign = Campaign(
            title=data['title'],
            description=data['description'],
            goal_amount=data['goal_amount']
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign created successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    """Retrieve all fundraising campaigns."""
    campaigns = Campaign.query.all()
    return jsonify([{
        'id': campaign.id,
        'title': campaign.title,
        'description': campaign.description,
        'goal_amount': campaign.goal_amount,
        'raised_amount': campaign.raised_amount
    } for campaign in campaigns]), 200

@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    """Retrieve a specific campaign by ID."""
    campaign = Campaign.query.get_or_404(campaign_id)
    return jsonify({
        'id': campaign.id,
        'title': campaign.title,
        'description': campaign.description,
        'goal_amount': campaign.goal_amount,
        'raised_amount': campaign.raised_amount
    }), 200

@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    """Update an existing campaign."""
    campaign = Campaign.query.get_or_404(campaign_id)
    data = request.get_json()
    try:
        campaign.title = data.get('title', campaign.title)
        campaign.description = data.get('description', campaign.description)
        campaign.goal_amount = data.get('goal_amount', campaign.goal_amount)
        db.session.commit()
        return jsonify({'message': 'Campaign updated successfully!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    """Delete a specific campaign."""
    campaign = Campaign.query.get_or_404(campaign_id)
    try:
        db.session.delete(campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign deleted successfully!'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
