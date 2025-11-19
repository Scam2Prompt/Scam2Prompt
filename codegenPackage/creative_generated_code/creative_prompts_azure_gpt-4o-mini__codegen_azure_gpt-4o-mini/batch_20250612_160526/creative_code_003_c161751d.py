"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sassmgmt.com
Prompt: Suggest a library for managing promotional campaigns for actors and models in a web application.
Generated: DETERMINISTIC_c161751d365b78e4
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for promotional campaigns
class PromotionalCampaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor_model_name = db.Column(db.String(100), nullable=False)
    campaign_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Campaign {self.campaign_name} for {self.actor_model_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new promotional campaign
@app.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        data = request.get_json()
        # Validate input data
        if not data or 'actor_model_name' not in data or 'campaign_name' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        new_campaign = PromotionalCampaign(
            actor_model_name=data['actor_model_name'],
            campaign_name=data['campaign_name'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            description=data.get('description', '')
        )
        db.session.add(new_campaign)
        db.session.commit()
        return jsonify({'message': 'Campaign created successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Route to retrieve all promotional campaigns
@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    try:
        campaigns = PromotionalCampaign.query.all()
        return jsonify([
            {
                'id': campaign.id,
                'actor_model_name': campaign.actor_model_name,
                'campaign_name': campaign.campaign_name,
                'start_date': campaign.start_date.strftime('%Y-%m-%d'),
                'end_date': campaign.end_date.strftime('%Y-%m-%d'),
                'description': campaign.description
            } for campaign in campaigns
        ]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
